"""Build the readable course pages and repeatable lesson downloads."""

from pathlib import Path
import csv
import hashlib
import html
import json
import re
import zipfile

import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
COURSE_URL = 'https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/'
PAGES = ['README', 'START-HERE', 'SETUP', 'PYTHON-BASICS', 'LEARNING-PATH', 'PRACTICE',
         'PROJECT-CHOICES', 'ELECTIVES', 'GLOSSARY', 'INDEPENDENT-PROJECT', 'TEACHING',
         'Data-Science-and-Machine-Learning']

STYLE = '''
:root{color-scheme:light dark;--bg:#f5f7fa;--panel:#fff;--text:#203346;--muted:#4e6274;--line:#cbd6df;--link:#145b91}
@media(prefers-color-scheme:dark){:root{--bg:#111c26;--panel:#192936;--text:#e6edf4;--muted:#b9c8d7;--line:#455d70;--link:#93caff}}
html[data-theme=light]{color-scheme:light;--bg:#f5f7fa;--panel:#fff;--text:#203346;--muted:#4e6274;--line:#cbd6df;--link:#145b91}
html[data-theme=dark]{color-scheme:dark;--bg:#111c26;--panel:#192936;--text:#e6edf4;--muted:#b9c8d7;--line:#455d70;--link:#93caff}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:18px/1.7 system-ui,sans-serif}header,main{max-width:1100px;margin:auto;padding:20px 28px}header{border-bottom:1px solid var(--line)}nav{display:flex;flex-wrap:wrap;gap:10px 22px}main{padding-bottom:90px}h1,h2,h3,h4,h5,h6{line-height:1.3;scroll-margin-top:20px}h1{font-size:2.2rem}h2{font-size:1.65rem;margin-top:2.7rem}h3{font-size:1.35rem}h4,h5,h6{font-size:1.15rem}p,li{max-width:86ch}li{margin:.35rem 0}a{color:var(--link);text-underline-offset:.15em}a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,summary:focus-visible{outline:3px solid #d78d13;outline-offset:3px}.skip{position:absolute;top:-100px}.skip:focus{top:0;background:var(--panel);padding:12px}table{border-collapse:collapse;width:100%;font-size:.95rem;background:var(--panel)}th,td{padding:10px 14px;text-align:left;border:1px solid var(--line);vertical-align:top}.table-frame{overflow-x:auto;margin:20px 0}code{font-size:.9em;overflow-wrap:anywhere}pre{background:var(--panel);border:1px solid var(--line);padding:18px;overflow-x:auto;line-height:1.5}pre code{overflow-wrap:normal}img{max-width:100%;height:auto;background:white}details{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:15px 20px;margin:18px 0}summary{cursor:pointer;font-weight:650}.tools{padding:18px;border:1px solid var(--line);background:var(--panel);margin:20px 0}.tools label{display:block}.tools input{width:min(100%,600px)}input,select,button{font:inherit;padding:7px 12px;border:1px solid var(--line);border-radius:5px;background:var(--panel);color:var(--text)}button{cursor:pointer}.copy{font-size:.8rem;float:right}.hint{color:var(--muted);font-size:.9rem}.toc ul{padding-left:22px}.toc{border-left:4px solid var(--line);padding-left:15px;max-height:420px;overflow:auto}.progress{height:4px;background:var(--link);position:fixed;left:0;top:0;z-index:10;width:0}.checklist-item{list-style:none}.checklist-item input{width:auto;margin-right:10px}[hidden]{display:none!important}@media(max-width:650px){body{font-size:17px}header,main{padding:16px}h1{font-size:1.8rem}th,td{padding:8px}.tools input{width:100%}}@media print{body{font-size:11pt;background:white;color:#111}header,.tools,.copy,.progress{display:none}main{padding:0;max-width:none}pre{white-space:pre-wrap}a{color:inherit}details{break-inside:avoid}h2,h3{break-after:avoid}}
'''

SCRIPT = r'''
(()=>{'use strict';
const theme=document.getElementById('theme');let saved;try{saved=localStorage.getItem('ml-course-theme')}catch{}if(saved)document.documentElement.dataset.theme=saved;
theme.addEventListener('click',()=>{const current=document.documentElement.dataset.theme|| (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');const next=current==='dark'?'light':'dark';document.documentElement.dataset.theme=next;try{localStorage.setItem('ml-course-theme',next)}catch{}});
for(const pre of document.querySelectorAll('pre')){const button=document.createElement('button');button.className='copy';button.textContent='Copy code';button.type='button';button.addEventListener('click',async()=>{const text=pre.querySelector('code')?.textContent||pre.textContent;try{if(navigator.clipboard?.writeText){await navigator.clipboard.writeText(text)}else{const area=document.createElement('textarea');area.value=text;document.body.append(area);area.select();if(!document.execCommand('copy'))throw Error();area.remove()}button.textContent='Copied'}catch{button.textContent='Select the text to copy'}setTimeout(()=>button.textContent='Copy code',1800)});pre.before(button)}
const search=document.getElementById('lesson-search'),track=document.getElementById('lesson-track');if(search){const rows=[...document.querySelectorAll('tr[data-track]')];const update=()=>{const terms=search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);let count=0;for(const row of rows){const show=(!track.value||row.dataset.track===track.value)&&terms.every(word=>row.textContent.toLowerCase().includes(word));row.hidden=!show;if(show)count++}document.getElementById('search-status').textContent=count+' matching lesson entries'};search.addEventListener('input',update);track.addEventListener('change',update);update()}
for(const [index,input] of [...document.querySelectorAll('input[data-course-check]')].entries()){const key='ml-course-check:'+location.pathname+':'+index;try{input.checked=localStorage.getItem(key)==='yes'}catch{}input.addEventListener('change',()=>{try{localStorage.setItem(key,input.checked?'yes':'no')}catch{}})}
const progress=document.querySelector('.progress');addEventListener('scroll',()=>{const size=document.documentElement.scrollHeight-innerHeight;progress.style.width=(size>0?100*scrollY/size:0)+'%'},{passive:true});
})();
'''


def render(text, title, prefix='', workbook=False):
    text=re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)
    text=text.replace('<details>', '<details markdown="1">')
    body=markdown.markdown(text,extensions=['tables','fenced_code','toc','md_in_html','sane_lists'],extension_configs={'toc':{'permalink':False}})
    soup=BeautifulSoup(body,'html.parser')
    explicit_ids={tag['id'] for tag in soup.select('a[id]')}
    for heading in soup.find_all(re.compile(r'^h[1-6]$')):
        if heading.get('id') in explicit_ids:
            del heading['id']
    for a in soup.select('a[href]'):
        href=a['href']
        if href.startswith(COURSE_URL):
            href=prefix+href[len(COURSE_URL):]
        for page in PAGES:
            href=re.sub(r'(?<![\w-])'+re.escape(page)+r'\.md(?=#|$)',page+'.html',href)
        a['href']=href
    for table in soup.select('table'):
        wrapper=soup.new_tag('div',attrs={'class':'table-frame','role':'region','aria-label':'Scrollable table','tabindex':'0'})
        table.wrap(wrapper)
    if workbook:
        anchor=soup.find(id='lesson-downloads')
        if anchor:
            controls=BeautifulSoup('<div class="tools"><label for="lesson-search">Find a lesson by name or number</label><input id="lesson-search" type="search"><label for="lesson-track">Choose a route</label><select id="lesson-track"><option value="">All entries</option><option>Core</option><option>Practice</option><option>Reference</option></select><p id="search-status" role="status" aria-live="polite"></p></div>','html.parser')
            anchor.insert_after(controls)
            for node in anchor.find_all_next('tr'):
                if node.find_parent('table') and node.find('a',href=re.compile(r'sample_code_folder/\d{3}.*\.zip')):
                    node['data-track']=next((x for x in ('Core','Practice','Reference') if x in node.get_text()),'Practice')
    for li in soup.find_all('li'):
        if li.get_text().startswith('[ ] '):
            first=li.contents[0]
            if isinstance(first,str):
                first.replace_with(first[4:]); li['class']='checklist-item'
                box=soup.new_tag('input',attrs={'type':'checkbox','data-course-check':'','aria-label':'Mark this step complete'})
                li.insert(0,box)
    # Learning-path boxes are in table cells. Keep their labels with the controls.
    for td in soup.find_all('td'):
        if td.get_text(strip=True)=='[ ]':
            td.clear(); box=soup.new_tag('input',attrs={'type':'checkbox','data-course-check':'','aria-label':'Mark this module complete'}); td.append(box)
    return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+STYLE+'</style></head><body><a class="skip" href="#content">Skip to the lesson</a><div class="progress" aria-hidden="true"></div><header><nav aria-label="Course pages"><a href="'+prefix+'START-HERE.html">Start here</a><a href="'+prefix+'LEARNING-PATH.html">Learning path</a><a href="'+prefix+'SETUP.html">Setup</a><a href="'+prefix+'GLOSSARY.html">Word list</a><a href="'+prefix+'Data-Science-and-Machine-Learning.html#lesson-downloads">Lesson library</a><button id="theme" type="button">Change colour theme</button></nav></header><main id="content">'+str(soup)+'</main><script>'+SCRIPT+'</script></body></html>\n'


def zip_folder(folder, output):
    # A fixed timestamp and sorted paths make unchanged builds byte-for-byte equal.
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(folder.rglob('*')):
            if not p.is_file() or '__pycache__' in p.parts or p.suffix in ('.joblib','.pyc'): continue
            name=folder.name+'/'+p.relative_to(folder).as_posix()
            info=zipfile.ZipInfo(name,date_time=(2026,1,1,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o644<<16
            z.writestr(info,p.read_bytes())
        # Readable instructions travel with every download.
        info=zipfile.ZipInfo(folder.name+'/README.html',date_time=(2026,1,1,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED
        readme=(folder/'README.md').read_text(encoding='utf-8')
        # Repository lessons sit two levels below the guides. Downloaded lesson
        # folders sit directly inside the complete course folder instead.
        for guide in ('LEARNING-PATH', 'ELECTIVES'):
            readme=readme.replace('(../../'+guide+'.md)', '(../'+guide+'.md)')
        z.writestr(info,render(readme,folder.name,prefix='../'))


def main():
    hashes={}
    for name in PAGES:
        source=ROOT/(name+'.md')
        if not source.is_file(): raise SystemExit(f'Missing source: {source.name}')
        html_text=render(source.read_text(encoding='utf-8'),name.replace('-',' '),workbook=name=='Data-Science-and-Machine-Learning')
        output=ROOT/(name+'.html'); output.write_text(html_text,encoding='utf-8',newline='\n')
        hashes[output.name]=hashlib.sha256(output.read_bytes()).hexdigest()
    for folder in sorted((ROOT/'lessons').iterdir()):
        if folder.is_dir():
            output=ROOT/'sample_code_folder'/(folder.name+'.zip'); zip_folder(folder,output)
            hashes[output.relative_to(ROOT).as_posix()]=hashlib.sha256(output.read_bytes()).hexdigest()
    (ROOT/'course_tools/build-manifest.json').write_text(json.dumps(hashes,indent=2,sort_keys=True)+'\n',encoding='utf-8',newline='\n')
    print(f'Built {len(PAGES)} readable pages and {len(hashes)-len(PAGES)} lesson ZIPs.')


if __name__=='__main__': main()
