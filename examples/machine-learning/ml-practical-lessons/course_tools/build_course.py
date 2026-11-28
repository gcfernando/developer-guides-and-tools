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
LIBRARY_URL = 'https://gcfernando.github.io/developer-guides-and-tools/'
PAGES = ['README', 'START-HERE', 'SETUP', 'PYTHON-BASICS', 'LEARNING-PATH', 'PRACTICE',
         'PROJECT-CHOICES', 'ELECTIVES', 'GLOSSARY', 'INDEPENDENT-PROJECT', 'TEACHING',
         'Data-Science-and-Machine-Learning']
PAGE_DESCRIPTIONS = {
    'README': 'Start a practical machine learning course with simple explanations, guided lessons and an independent project.',
    'START-HERE': 'Learn what machine learning does with small examples, plain English and basic computer steps.',
    'SETUP': 'Set up Python, open the course files and run your first machine learning lesson one step at a time.',
    'PYTHON-BASICS': 'Learn the Python basics used in this course, including values, lists, tables, functions and predictions.',
    'LEARNING-PATH': 'Follow the beginner learning path from reading a table to checking a model and finishing a project.',
    'PRACTICE': 'Practise machine learning ideas with small questions, worked examples and explained answers.',
    'PROJECT-CHOICES': 'Choose a useful machine learning question, compare a simple baseline and plan a fair check.',
    'ELECTIVES': 'Explore optional machine learning topics after learning the basic skills they need.',
    'GLOSSARY': 'Find simple English explanations of machine learning and Python words used in this course.',
    'INDEPENDENT-PROJECT': 'Use real wine measurements to plan, build and check a machine learning project independently.',
    'TEACHING': 'Build, check and teach the beginner machine learning course, and record evidence from learner practice.',
    'Data-Science-and-Machine-Learning': 'Browse practical machine learning lessons, sample data, downloadable code and simple explanations.',
    'projects/wine/README': 'Open the wine project files, data dictionary, starter code, assignment and source notes.',
    'projects/wine/SOURCE': 'Read the source, licence and limits of the wine measurements used in the independent project.',
}

STYLE = '''
:root{color-scheme:light dark;--bg:#f5f7fa;--panel:#fff;--text:#203346;--muted:#4e6274;--line:#cbd6df;--link:#145b91}
@media(prefers-color-scheme:dark){:root{--bg:#111c26;--panel:#192936;--text:#e6edf4;--muted:#b9c8d7;--line:#455d70;--link:#93caff}}
html[data-theme=light]{color-scheme:light;--bg:#f5f7fa;--panel:#fff;--text:#203346;--muted:#4e6274;--line:#cbd6df;--link:#145b91}
html[data-theme=dark]{color-scheme:dark;--bg:#111c26;--panel:#192936;--text:#e6edf4;--muted:#b9c8d7;--line:#455d70;--link:#93caff}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:18px/1.7 system-ui,sans-serif}header,main{max-width:1100px;margin:auto;padding:20px 28px}header{border-bottom:1px solid var(--line)}nav{display:flex;flex-wrap:wrap;gap:10px 22px}main{padding-bottom:90px}h1,h2,h3,h4,h5,h6{line-height:1.3;scroll-margin-top:20px}h1{font-size:2.2rem}h2{font-size:1.65rem;margin-top:2.7rem}h3{font-size:1.35rem}h4,h5,h6{font-size:1.15rem}p,li{max-width:86ch}li{margin:.35rem 0}a{color:var(--link);text-underline-offset:.15em}a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,summary:focus-visible{outline:3px solid #d78d13;outline-offset:3px}.skip{position:absolute;top:-100px}.skip:focus{top:0;background:var(--panel);padding:12px}table{border-collapse:collapse;width:100%;font-size:.95rem;background:var(--panel)}th,td{padding:10px 14px;text-align:left;border:1px solid var(--line);vertical-align:top}.table-frame{overflow-x:auto;margin:20px 0}code{font-size:.9em;overflow-wrap:anywhere}pre{background:var(--panel);border:1px solid var(--line);padding:18px;overflow-x:auto;line-height:1.5}pre code{overflow-wrap:normal}img{max-width:100%;height:auto;background:white}details{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:15px 20px;margin:18px 0}summary{cursor:pointer;font-weight:650}.tools{padding:18px;border:1px solid var(--line);background:var(--panel);margin:20px 0}.tools label{display:block}.tools input{width:min(100%,600px)}input,select,button{font:inherit;padding:7px 12px;border:1px solid var(--line);border-radius:5px;background:var(--panel);color:var(--text)}button{cursor:pointer}.copy{font-size:.8rem;float:right}.hint{color:var(--muted);font-size:.9rem}.toc ul{padding-left:22px}.toc{border-left:4px solid var(--line);padding-left:15px;max-height:420px;overflow:auto}.progress{height:4px;background:var(--link);position:fixed;left:0;top:0;z-index:10;width:0}.checklist-item{list-style:none}.checklist-item input{width:auto;margin-right:10px}[hidden]{display:none!important}@media(max-width:650px){body{font-size:17px}header,main{padding:16px}h1{font-size:1.8rem}th,td{padding:8px}.tools input{width:100%}}@media print{body{font-size:11pt;background:white;color:#111}header,.tools,.copy,.progress{display:none}main{padding:0;max-width:none}pre{white-space:pre-wrap}a{color:inherit}details{break-inside:avoid}h2,h3{break-after:avoid}}
'''

VISUAL_STYLE = '''
.teaching-visual{margin:2rem 0;padding:1rem;border:1px solid var(--line);border-radius:10px;background:var(--panel)}.teaching-visual figcaption{font-weight:650;margin-bottom:.6rem}.visual-flow{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:1rem;padding:0;list-style:none;counter-reset:visual-step}.visual-flow li{padding:1rem;border:1px solid var(--line);border-radius:8px;counter-increment:visual-step}.visual-flow li::before{content:'Step ' counter(visual-step);display:block;font-size:.85em;font-weight:700}.visual-options li::before{content:"Option " counter(visual-step)}.visual-flow strong{display:block}.visual-help{font-size:.95rem}.visual-actions{display:flex;gap:1rem;flex-wrap:wrap;align-items:center}.visual-dialog{width:min(98vw,1500px);max-width:none;max-height:96vh;padding:1rem;background:var(--panel);color:var(--text);border:2px solid var(--line)}.visual-dialog::backdrop{background:#102032cc}.visual-dialog img{max-width:none;width:auto;min-width:100%;height:auto}.visual-dialog .image-scroll{overflow:auto;max-height:78vh}.visual-dialog header{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:.25rem;max-width:none}.visual-dialog button{position:sticky;right:0}.visual-caption-detail{font-weight:400}.table-frame:focus-visible{outline:3px solid #d78d13;outline-offset:3px}.table-frame table{margin:0}.visual-data{font-size:.95rem}.visual-data th{white-space:normal}.visual-source{overflow-wrap:anywhere}@media(max-width:650px){.teaching-visual{margin:1.5rem 0;padding:.7rem}.visual-flow{grid-template-columns:1fr}.visual-help{font-size:1rem}}@media print{.visual-actions,.visual-dialog{display:none}.teaching-visual{break-inside:avoid}.visual-data[open]{display:block}}
'''

SCRIPT = r'''
(()=>{'use strict';
const theme=document.getElementById('theme');let saved;try{saved=localStorage.getItem('ml-course-theme')}catch{}if(saved)document.documentElement.dataset.theme=saved;
theme.addEventListener('click',()=>{const current=document.documentElement.dataset.theme|| (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');const next=current==='dark'?'light':'dark';document.documentElement.dataset.theme=next;try{localStorage.setItem('ml-course-theme',next)}catch{}});
for(const pre of document.querySelectorAll('pre')){const code=pre.querySelector('code');const language=code?.className||'';const label=/language-(bash|powershell|bat|shell)/.test(language)?'Copy terminal command':/language-(text|plaintext)/.test(language)?'Copy example output':'Copy code example';const button=document.createElement('button');button.className='copy';button.textContent=label;button.type='button';button.addEventListener('click',async()=>{const text=code?.textContent||pre.textContent;try{if(navigator.clipboard?.writeText){await navigator.clipboard.writeText(text)}else{const area=document.createElement('textarea');area.value=text;document.body.append(area);area.select();if(!document.execCommand('copy'))throw Error();area.remove()}button.textContent='Copied'}catch{button.textContent='Select the text to copy'}setTimeout(()=>button.textContent=label,1800)});pre.before(button)}
const tableRegions=[...document.querySelectorAll('.table-frame')];
const updateTables=()=>{const widths=tableRegions.map(region=>region.scrollWidth>region.clientWidth+1);tableRegions.forEach((region,index)=>{if(widths[index]){region.tabIndex=0;region.setAttribute('role','region')}else{region.removeAttribute('tabindex');region.removeAttribute('role')}})};
let tableFrame;const scheduleTables=()=>{cancelAnimationFrame(tableFrame);tableFrame=requestAnimationFrame(updateTables)};
scheduleTables();addEventListener('resize',scheduleTables);document.addEventListener('toggle',scheduleTables,true);
for(const button of document.querySelectorAll('[data-open-visual]')){button.addEventListener('click',()=>{const dialog=document.getElementById('visual-dialog');const image=dialog.querySelector('img');image.src=button.dataset.openVisual;image.alt=button.dataset.visualAlt||'';dialog.querySelector('[data-visual-title]').textContent=button.dataset.visualTitle||'Figure';dialog.showModal();dialog.querySelector('[data-close-visual]').focus();dialog.dataset.returnTo=button.id})}
const visualDialog=document.getElementById('visual-dialog');if(visualDialog){visualDialog.querySelector('[data-close-visual]').addEventListener('click',()=>visualDialog.close());visualDialog.addEventListener('close',()=>document.getElementById(visualDialog.dataset.returnTo)?.focus())}
const search=document.getElementById('lesson-search'),track=document.getElementById('lesson-track');if(search){const rows=[...document.querySelectorAll('tr[data-track]')];const update=()=>{const terms=search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);let count=0;for(const row of rows){const show=(!track.value||row.dataset.track===track.value)&&terms.every(word=>row.textContent.toLowerCase().includes(word));row.hidden=!show;if(show)count++}document.getElementById('search-status').textContent=count+' matching lesson entries'};search.addEventListener('input',update);track.addEventListener('change',update);update()}
for(const [index,input] of [...document.querySelectorAll('input[data-course-check]')].entries()){const key='ml-course-check:'+location.pathname+':'+index;try{input.checked=localStorage.getItem(key)==='yes'}catch{}input.addEventListener('change',()=>{try{localStorage.setItem(key,input.checked?'yes':'no')}catch{}})}
const progress=document.querySelector('.progress');addEventListener('scroll',()=>{const size=document.documentElement.scrollHeight-innerHeight;progress.style.width=(size>0?100*scrollY/size:0)+'%'},{passive:true});
})();
'''


def add_visual_help(soup):
    """Keep every published figure beside its interpretation and source values."""
    manifest=ROOT/'course_tools/visuals.json'
    if not manifest.is_file():
        return
    catalog=json.loads(manifest.read_text(encoding='utf-8'))['visuals']
    for number,picture in enumerate(list(soup.select('img[src]')),1):
        name=Path(picture['src']).name
        item=catalog.get(name)
        if not item:
            continue
        if picture.parent.name=='p' and len([node for node in picture.parent.contents if str(node).strip()])==1:
            picture.parent.unwrap()
        figure=soup.new_tag('figure',attrs={'class':'teaching-visual'})
        picture.wrap(figure)
        caption=soup.new_tag('figcaption')
        caption.string=item['teaching_question']
        figure.insert(0,caption)
        if item.get('steps'):
            options=item.get('sequence_type')=='options'
            flow=soup.new_tag('ul' if options else 'ol',attrs={'class':'visual-flow'+(' visual-options' if options else '')})
            for step in item['steps']:
                row=soup.new_tag('li'); label=soup.new_tag('strong'); label.string=step['label']; row.append(label)
                row.append(step['text']); flow.append(row)
            picture.replace_with(flow)
        else:
            mobile=item.get('mobile_asset')
            if mobile:
                responsive=soup.new_tag('picture'); picture.wrap(responsive)
                source=soup.new_tag('source',attrs={'media':'(max-width: 650px)','srcset':str(Path(picture['src']).with_name(mobile)).replace('\\','/')})
                responsive.insert(0,source)
        for label,key in [('Read it','read_instructions'),('Notice','observation'),('Remember','limit')]:
            para=soup.new_tag('p',attrs={'class':'visual-help'}); strong=soup.new_tag('strong'); strong.string=label+': '; para.append(strong); para.append(item[key]); figure.append(para)
        if item.get('table_data'):
            details=soup.new_tag('details',attrs={'class':'visual-data'}); summary=soup.new_tag('summary'); summary.string='Read the figure as a table or text'; details.append(summary)
            table=soup.new_tag('table'); head=soup.new_tag('thead'); heading=soup.new_tag('tr')
            for column in item['table_data']['columns']:
                cell=soup.new_tag('th',attrs={'scope':'col'}); cell.string=str(column); heading.append(cell)
            head.append(heading); table.append(head); body=soup.new_tag('tbody')
            for values in item['table_data']['rows']:
                row=soup.new_tag('tr')
                for value in values:
                    cell=soup.new_tag('td'); cell.string=str(value); row.append(cell)
                body.append(row)
            table.append(body); details.append(table); figure.append(details)
        note=soup.new_tag('p',attrs={'class':'hint visual-source'}); note.string='Source: '+item['source_description']; figure.append(note)
        actions=soup.new_tag('p',attrs={'class':'visual-actions'})
        full=soup.new_tag('a',attrs={'href':picture['src']});full.string='Open full-size figure';actions.append(full)
        button=soup.new_tag('button',attrs={'type':'button','id':f'open-visual-{number}','data-open-visual':picture['src'],'data-visual-alt':picture.get('alt',''),'data-visual-title':item['teaching_question']});button.string='Enlarge here';actions.append(button);figure.append(actions)


def render(text, title, prefix='', workbook=False, canonical=None, description=None):
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
    add_visual_help(soup)
    for number,table in enumerate(soup.select('table'),1):
        heading=table.find_previous(re.compile(r'^h[1-6]$'))
        name=heading.get_text(' ',strip=True) if heading else title
        wrapper=soup.new_tag('div',attrs={'class':'table-frame','aria-label':f'{name}, table {number}. Scroll horizontally if needed.'})
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
                box=soup.new_tag('input',attrs={'type':'checkbox','data-course-check':'','aria-label':'Mark complete: '+li.get_text(' ',strip=True)})
                li.insert(0,box)
    # Learning-path boxes are in table cells. Keep their labels with the controls.
    for td in soup.find_all('td'):
        if td.get_text(strip=True)=='[ ]':
            row=td.find_parent('tr');cells=row.find_all('td');label=cells[1].get_text(' ',strip=True) if len(cells)>1 else 'this module'
            td.clear(); box=soup.new_tag('input',attrs={'type':'checkbox','data-course-check':'','aria-label':'Mark complete: '+label}); td.append(box)
    metadata=''
    if canonical:
        metadata+='<link rel="canonical" href="'+html.escape(canonical,quote=True)+'">'
    if description:
        metadata+='<meta name="description" content="'+html.escape(description,quote=True)+'">'
    dialog='<dialog id="visual-dialog" class="visual-dialog" aria-label="Enlarged teaching figure"><header><strong data-visual-title>Figure</strong><button type="button" data-close-visual>Close figure</button></header><p class="hint">Scroll within the image to inspect its labels. Press Escape or Close figure to return.</p><div class="image-scroll"><img alt=""></div></dialog>'
    return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+metadata+'<title>'+html.escape(title)+'</title><style>'+STYLE+VISUAL_STYLE+'</style></head><body><a class="skip" href="#content">Skip to the lesson</a><div class="progress" aria-hidden="true"></div><header><nav aria-label="Library navigation"><a href="'+LIBRARY_URL+'">Library home</a><a href="'+LIBRARY_URL+'documentation/">All resources</a></nav><nav aria-label="Course pages"><a href="'+prefix+'README.html">Course overview</a><a href="'+prefix+'START-HERE.html">Start here</a><a href="'+prefix+'LEARNING-PATH.html">Learning path</a><a href="'+prefix+'SETUP.html">Setup</a><a href="'+prefix+'GLOSSARY.html">Word list</a><a href="'+prefix+'Data-Science-and-Machine-Learning.html">Workbook</a><a href="'+prefix+'Data-Science-and-Machine-Learning.html#lesson-downloads">Lesson library</a><button id="theme" type="button">Change colour theme</button></nav><p class="hint">Course links work with the complete downloaded course. Library home and All resources need an internet connection.</p></header><main id="content">'+str(soup)+'</main>'+dialog+'<script>'+SCRIPT+'</script></body></html>\n'


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
        for guide in PAGES:
            readme=readme.replace('(../../'+guide+'.md', '(../'+guide+'.md')
        z.writestr(info,render(readme,folder.name,prefix='../'))


def main():
    hashes={}
    readable_pages = PAGES + ['projects/wine/README', 'projects/wine/SOURCE']
    for name in readable_pages:
        source=ROOT/(name+'.md')
        if not source.is_file(): raise SystemExit(f'Missing source: {source.name}')
        title = {'projects/wine/README':'Wine project files',
                 'projects/wine/SOURCE':'Wine data source and licence'}.get(name,name.replace('-',' '))
        html_text=render(source.read_text(encoding='utf-8'),title,
                         prefix='../'*len(Path(name).parts[:-1]),workbook=name=='Data-Science-and-Machine-Learning',
                         canonical=COURSE_URL+name+'.html',description=PAGE_DESCRIPTIONS[name])
        output=ROOT/(name+'.html'); output.write_text(html_text,encoding='utf-8',newline='\n')
        hashes[output.relative_to(ROOT).as_posix()]=hashlib.sha256(output.read_bytes()).hexdigest()
    for folder in sorted((ROOT/'lessons').iterdir()):
        if folder.is_dir():
            output=ROOT/'sample_code_folder'/(folder.name+'.zip'); zip_folder(folder,output)
            hashes[output.relative_to(ROOT).as_posix()]=hashlib.sha256(output.read_bytes()).hexdigest()
    (ROOT/'course_tools/build-manifest.json').write_text(json.dumps(hashes,indent=2,sort_keys=True)+'\n',encoding='utf-8',newline='\n')
    print(f'Built {len(readable_pages)} readable pages and {len(hashes)-len(readable_pages)} lesson ZIPs.')


if __name__=='__main__': main()
