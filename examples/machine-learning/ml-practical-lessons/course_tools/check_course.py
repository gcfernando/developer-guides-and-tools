"""Check published files and run useful learner regressions in temporary copies."""

from pathlib import Path
import argparse
import ast
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
ENV={**os.environ,'PYTHONUTF8':'1','MPLBACKEND':'Agg','OMP_NUM_THREADS':'1',
     'OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1','LOKY_MAX_CPU_COUNT':'2'}


def structure():
    problems=[]
    sources=list((ROOT/'lessons').rglob('*.py'))+list((ROOT/'projects').rglob('*.py'))
    for path in sources:
        try: ast.parse(path.read_text(encoding='utf-8'))
        except SyntaxError as error: problems.append(f'{path}: {error}')
    htmls=list(ROOT.glob('*.html'))+[ROOT/'course-review/report.html']
    parsed={p:BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser') for p in htmls}
    id_sets={p:{e['id'] for e in soup.select('[id]')} for p,soup in parsed.items()}
    for path,soup in parsed.items():
        expected='https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/'+path.relative_to(ROOT).as_posix()
        canonical=soup.select('link[rel="canonical"]')
        if len(canonical)!=1 or canonical[0].get('href')!=expected:
            problems.append(f'{path.relative_to(ROOT)}: missing or incorrect canonical URL')
        description=soup.select('meta[name="description"]')
        if len(description)!=1 or not description[0].get('content','').strip():
            problems.append(f'{path.relative_to(ROOT)}: missing description')
        ids=[e['id'] for e in soup.select('[id]')]
        if len(ids)!=len(set(ids)): problems.append(f'Duplicate IDs: {path.name}')
        for tag in soup.select('a[href],img[src]'):
            href=tag.get('href',tag.get('src',''))
            if not href or href.startswith(('https:','http:','mailto:','data:')): continue
            name,_,fragment=href.partition('#'); target=(path.parent/name).resolve() if name else path
            if not target.exists(): problems.append(f'{path.name}: missing {href}')
            elif fragment and target in parsed and fragment not in id_sets[target]:
                problems.append(f'{path.name}: missing fragment {href}')
    for archive in sorted((ROOT/'sample_code_folder').glob('*.zip')):
        with zipfile.ZipFile(archive) as z:
            if z.testzip(): problems.append(f'Archive CRC: {archive.name}')
            # Check the guide links as a learner sees them after extracting a
            # download directly into the complete course folder.
            reader=BeautifulSoup(z.read(archive.stem+'/README.html'),'html.parser')
            for link in reader.select('a[href]'):
                href=link['href']
                if href.startswith('../'):
                    target=(ROOT/archive.stem/href.split('#')[0]).resolve()
                    if not target.is_file():
                        problems.append(f'{archive.name}: missing extracted reader link {href}')
            folder=ROOT/'lessons'/archive.stem
            for path in folder.rglob('*'):
                if path.is_file() and '__pycache__' not in path.parts and path.suffix not in ('.joblib','.pyc'):
                    name=archive.stem+'/'+path.relative_to(folder).as_posix()
                    if name not in z.namelist() or z.read(name)!=path.read_bytes(): problems.append(f'Stale archive: {name}')
    rows=list(csv.DictReader((ROOT/'coverage.csv').open(encoding='utf-8-sig')))
    assert len(rows)==447
    for row in rows:
        for field in ('Python','Training or sample CSV','New input CSV'):
            value=row.get(field,'')
            # The historical manifest can contain a descriptive list of extra files.
            if value and ';' not in value and ',' not in value and not (ROOT/'lessons'/value).exists():
                problems.append(f"Manifest {row['ID']}: missing {field}: {value}")
    print(f'Checked {len(sources)} Python sources, {len(htmls)} pages, 448 archives and 447 manifest rows.')
    return problems


def run_script(folder, script='lesson.py'):
    try:
        result=subprocess.run([sys.executable,str(folder/script)],cwd=folder,env=ENV,
                              capture_output=True,text=True,encoding='utf-8',timeout=60)
        return {'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr}
    except subprocess.TimeoutExpired:
        return {'exit_code':124,'stdout':'','stderr':'Timed out after 60 seconds.'}


def fixture(name, parent):
    source=next(p for p in (ROOT/'lessons').iterdir() if p.name.startswith(name))
    target=parent/source.name
    if target.exists():
        assert target.resolve().is_relative_to(parent.resolve())
        shutil.rmtree(target)
    shutil.copytree(source,target)
    return target


def regressions():
    checks=[]
    with tempfile.TemporaryDirectory(prefix='ml-course-check-') as temp:
        parent=Path(temp)
        folder=fixture('090-',parent)
        (folder/'sample.csv').write_text('signed_up\nYes\ntrue\n1\nno\nfalse\n0\nunknown\n',encoding='utf-8')
        result=run_script(folder)
        lines=result['stdout'].splitlines()
        assert result['exit_code']==0 and re.search(r'\b1\s+1\.0',result['stdout']) and re.search(r'false\s+0\.0',result['stdout']),result
        checks.append('Boolean 1 and false stay known values; unknown stays missing.')
        folder=fixture('101-',parent)
        import pandas as pd
        data=pd.read_csv(folder/'sample.csv'); data.loc[data['day']=='2025-02-03','orders']=18; data.to_csv(folder/'sample.csv',index=False)
        result=run_script(folder); assert result['exit_code']==0 and re.search(r'2025-02-02\s+NaN\s+14\.0',result['stdout']),result
        data.loc[0,'day']='2025-02-04'; data.to_csv(folder/'sample.csv',index=False)
        result=run_script(folder); assert result['exit_code']!=0 and 'one reading per date' in result['stderr'],result
        checks.append('Documented date edit gives 14; duplicate dates give a clear recovery message.')
        folder=fixture('002-',parent)
        data=pd.read_csv(folder/'new_inputs.csv'); data.loc[0,'distance_km']=8; data.to_csv(folder/'new_inputs.csv',index=False)
        result=run_script(folder); assert result['exit_code']==0 and re.search(r'8\s+26\.0',result['stdout']),result
        checks.append('First prediction: editing 4 to 8 gives 26.0 minutes.')
        folder=fixture('069-',parent)
        for value,decision in [(90,'KEEP'),(None,'FLAG')]:
            pd.DataFrame({'parcel':[5],'verified_weight_kg':[value]}).to_csv(folder/'weighing_slip.csv',index=False)
            result=run_script(folder); assert result['exit_code']==0 and f'Decision: {decision}' in result['stdout'],result
        checks.append('Outlier task keeps a source-confirmed value and flags a missing source.')
        folder=fixture('179-',parent)
        data=pd.read_csv(folder/'sample.csv'); data.loc[1,['distance_km','weight_kg']]=data.loc[0,['distance_km','weight_kg']].to_numpy(); data.to_csv(folder/'sample.csv',index=False)
        result=run_script(folder); assert result['exit_code']==0,result
        data.loc[1,'shipment_id']=data.loc[0,'shipment_id']; data.to_csv(folder/'sample.csv',index=False)
        result=run_script(folder); assert result['exit_code']!=0 and 'same group' in result['stderr'],result
        checks.append('Equal inputs on separate shipments are accepted; copied shipment identity is rejected.')
        folder=fixture('071-',parent)
        assert run_script(folder,'train_range_model.py')['exit_code']==0
        result=run_script(folder,'test_range_model.py'); assert result['exit_code']==0 and '1.8163' in result['stdout'] and 'Outside training range' in result['stdout'],result
        checks.append('Saved scale rule handles the 90 km request without refitting.')
        folder=fixture('232-',parent)
        code="from fastapi.testclient import TestClient; from lesson import app; c=TestClient(app); assert c.get('/').status_code==200; assert c.post('/predict',json={'km':4}).json()['minutes']==18.0; assert c.post('/predict',json={'km':-4}).status_code==422"
        result=subprocess.run([sys.executable,'-c',code],cwd=folder,env=ENV,capture_output=True,text=True,encoding='utf-8'); assert result.returncode==0,result.stderr
        checks.append('The documented local web module exposes the page and validates requests.')
        folder=fixture('447-',parent)
        result=run_script(folder); assert result['exit_code']==0 and 'INVESTIGATE' in result['stdout'] and '422' in result['stdout'],result
        checks.append('The full capstone trains, serves practice requests and monitors later outcomes.')
    print('Learner regressions passed:',len(checks))
    return checks


def run_all(refresh=False):
    jobs=[]; groups={}
    for folder in sorted((ROOT/'lessons').iterdir()):
        script=folder/'lesson.py'
        if not script.exists(): script=folder/'train_delivery_model.py'
        if not script.exists(): continue
        tree=ast.parse(script.read_text(encoding='utf-8'))
        if tree.body and isinstance(tree.body[0],ast.Expr) and isinstance(tree.body[0].value,ast.Constant) and isinstance(tree.body[0].value.value,str): tree.body.pop(0)
        data=b''.join(p.name.encode()+p.read_bytes() for p in sorted(folder.glob('*.csv')))
        key=hashlib.sha256(ast.dump(tree).encode()+data).hexdigest()
        groups.setdefault(key,[]).append(folder)
        if len(groups[key])==1: jobs.append((key,folder,script.name))
    def job(item):
        key,source,name=item
        with tempfile.TemporaryDirectory(prefix='ml-course-run-') as temp:
            folder=Path(temp)/source.name; shutil.copytree(source,folder)
            result=run_script(folder,name)
        result['lesson']=source.name
        result['copies']=[p.name for p in groups[key]]
        if result['exit_code']==0 and refresh:
            for p in groups[key]:
                if (p/'expected-output.txt').exists():
                    clean='\n'.join(line.rstrip() for line in result['stdout'].splitlines()).rstrip()+'\n'
                    (p/'expected-output.txt').write_text(clean,encoding='utf-8',newline='\n')
        if result['exit_code']==0 and (source/'expected-output.txt').exists():
            result['matches_expected']=re.sub(r'\s+','',result['stdout'])==re.sub(r'\s+','',(source/'expected-output.txt').read_text(encoding='utf-8'))
        return result
    results=[]
    with ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(job,jobs):
            results.append(result)
            if result['exit_code']!=0: print('Could not run:',result['lesson'],result['stderr'].splitlines()[-1:])
    output=ROOT/'course-review/revision-checks.json'
    report=json.dumps({'python':sys.version,'results':results},indent=2,ensure_ascii=False)+'\n'
    # Keep local account names out of the shareable execution report.
    home=str(Path.home())
    for prefix in (home,home.replace('\\','/')):
        report=report.replace(json.dumps(prefix)[1:-1],'<user-home>')
    output.write_text(report,encoding='utf-8',newline='\n')
    print('Distinct source/data runs:',len(results),'passed:',sum(r['exit_code']==0 for r in results))
    return results


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--run',action='store_true'); parser.add_argument('--refresh-outputs',action='store_true'); parser.add_argument('--structure-only',action='store_true'); args=parser.parse_args()
    problems=structure()
    if problems:
        print('\n'.join(problems[:70])); raise SystemExit(f'{len(problems)} structure problems')
    if not args.structure_only:
        regressions()
        node=shutil.which('node')
        if node:
            subprocess.run([node,str(ROOT/'course_tools/check_browser.cjs')],check=True)
        else:
            print('Page control check not run: Node is not installed.')
    if args.run or args.refresh_outputs:
        results=run_all(args.refresh_outputs)
        # Missing extras are recorded, not silently called passing.
        unexpected=[r for r in results if r['exit_code']!=0 and not any(word in r['stderr'] for word in ['ModuleNotFoundError','TiffWriter.write()','Could not find a backend'])]
        if unexpected: raise SystemExit(f'{len(unexpected)} unexpected runtime failures; see revision-checks.json')
        if any(r.get('matches_expected') is False for r in results): raise SystemExit('An expected output differs.')


if __name__=='__main__': main()
