
'use strict';
const DATA=JSON.parse(document.getElementById('atlas-data').textContent);
const $=(id)=>document.getElementById(id);
const field=$('site-search'),results=$('search-results');
const clean=(s)=>String(s||'').toLocaleLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
const safeText=(s)=>document.createTextNode(String(s));
let activeResult=-1;
function closeSearch(){
  results.hidden=true;
  field.setAttribute('aria-expanded','false');
  field.removeAttribute('aria-activedescendant');
  activeResult=-1;
}
function selectSearchResult(index){
  const options=Array.from(results.querySelectorAll('[role="option"]'));
  if(!options.length)return;
  activeResult=Math.max(0,Math.min(options.length-1,index));
  options.forEach((option,i)=>option.setAttribute('aria-selected',String(i===activeResult)));
  field.setAttribute('aria-activedescendant',options[activeResult].id);
  options[activeResult].scrollIntoView?.({block:'nearest'});
}
function showResults(){
  const query=clean(field.value.trim());results.replaceChildren();activeResult=-1;
  field.removeAttribute('aria-activedescendant');
  if(query.length<2){closeSearch();return;}
  const terms=query.split(/\s+/).filter(Boolean);
  let found=DATA.search.map(entry=>({entry, score:clean(entry.title).includes(query)?4:0})).filter(o=>terms.every(t=>clean(o.entry.title+' '+o.entry.context).includes(t)));
  found.sort((a,b)=>b.score-a.score||['Topic','Profession','Lesson','Subtopic','Glossary'].indexOf(a.entry.type)-['Topic','Profession','Lesson','Subtopic','Glossary'].indexOf(b.entry.type));
  const summary=document.createElement('div');summary.className='sr-summary';summary.setAttribute('role','presentation');summary.textContent=`${found.length} match${found.length===1?'':'es'} — showing up to 35. Select a result to jump to it.`;results.append(summary);
  if(!found.length){let empty=document.createElement('p');empty.className='empty';empty.textContent='No exact matches. Try fewer words (for example: RAG, Python, embeddings).';results.append(empty);}
  for(const [index,{entry}] of found.slice(0,35).entries()){
    const link=document.createElement('a');link.href=entry.href;
    link.id=`search-option-${index}`;link.setAttribute('role','option');link.setAttribute('aria-selected','false');link.tabIndex=-1;
    const heading=document.createElement('strong');heading.textContent=`${entry.type}: ${entry.title}`;
    const detail=document.createElement('small');detail.textContent=entry.context;
    link.append(heading,detail);link.addEventListener('click',closeSearch);results.append(link);
  }
  results.hidden=false;field.setAttribute('aria-expanded','true');
}
field.addEventListener('input',showResults);
field.addEventListener('keydown',e=>{
  if(e.key==='Escape'){e.preventDefault();field.value='';showResults();field.focus();}
  if(['ArrowDown','ArrowUp'].includes(e.key)&&!results.hidden){
    e.preventDefault();selectSearchResult(activeResult+(e.key==='ArrowDown'?1:-1));
  }
  if(e.key==='Enter'&&!results.hidden){
    e.preventDefault();
    const options=results.querySelectorAll('[role="option"]');
    const option=options[Math.max(0,activeResult)];
    option?.click();
  }
});
document.addEventListener('click',e=>{if(!e.target.closest('.searchbox'))closeSearch();});
function openDeepLink(){
  if(!location.hash)return;
  window.AtlasExperience?.reveal(location.hash,{scroll:false});
  let id;try{id=decodeURIComponent(location.hash.slice(1));}catch(e){return;}
  let target=document.getElementById(id);if(!target)return;
  for(let p=target.parentElement;p;p=p.parentElement){if(p.tagName==='DETAILS'){p.open=true;}}
  if(target.closest('.topic-details')){target.closest('.topic-details').open=true;}
  setTimeout(()=>target.scrollIntoView({block:'start',behavior:'instant'}),25);
}
window.addEventListener('hashchange',openDeepLink);openDeepLink();
// Open collapsed destinations BEFORE native anchor navigation, including repeated clicks to the same hash.
document.addEventListener('click',(e)=>{
 const a=e.target.closest('a[href^="#"]');if(!a)return;
 window.AtlasExperience?.reveal(a.getAttribute('href'),{scroll:false});
 let target;try{target=document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));}catch{return;}if(!target)return;
 for(let p=target;p;p=p.parentElement){if(p.tagName==='DETAILS')p.open=true;}
 if($('sidebar').classList.contains('is-open'))closeMenu();
 if(location.hash===a.getAttribute('href'))setTimeout(()=>target.scrollIntoView({block:'start',behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'}),20);
});
const menu=$('menu-btn');
const mobileNavigation=window.matchMedia('(max-width:850px)');
function syncMenu(){ $('sidebar').inert=mobileNavigation.matches&&!$('sidebar').classList.contains('is-open'); }
function closeMenu(returnFocus=false){
 const wasOpen=$('sidebar').classList.contains('is-open');
 $('sidebar').classList.remove('is-open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation');
 if(wasOpen&&returnFocus)menu.focus();syncMenu();
}
menu.addEventListener('click',()=>{
 const open=$('sidebar').classList.toggle('is-open');menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation');syncMenu();
 if(open)$('sidebar').querySelector('a').focus();
});
mobileNavigation.addEventListener('change',()=>{closeMenu();syncMenu();});syncMenu();
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&$('sidebar').classList.contains('is-open')){e.preventDefault();closeMenu(true);}});
document.addEventListener('focusin',event=>{if($('sidebar').classList.contains('is-open')&&event.target!==menu&&!$('sidebar').contains(event.target))closeMenu();});
const roleSelect=$('role-filter');const hideUnlisted=$('hide-unlisted');
const statusEmoji={Essential:'🟢',Recommended:'🟡',Advanced:'🟣',Optional:'🔵','Not required now':'⚪'};
const statusClasses={Essential:'essential',Recommended:'recommended',Advanced:'advanced',Optional:'optional','Not required now':'skipped'};
function updateMatrix(){
 const role=roleSelect.value;const selected=DATA.priorities[role]||{};
 document.querySelectorAll('tr[data-topic]').forEach(row=>{
  const status=role?(selected[row.dataset.topic]||'Not listed'):'Choose a profession';
  const cell=row.querySelector('.matrix-priority');cell.replaceChildren();
  const span=document.createElement('span');span.className='status status-'+(statusClasses[status]||'unlisted');span.textContent=(statusEmoji[status]||'')+' '+status;cell.append(span);
  row.hidden=!!(hideUnlisted.checked&&role&&status==='Not listed');
 });
}
roleSelect.addEventListener('change',updateMatrix);hideUnlisted.addEventListener('change',updateMatrix);updateMatrix();
// Local-only progress. No server or third-party network requests.
const STORE='ai-learning-atlas-progress-v1';let saved={};
try{saved=JSON.parse(localStorage.getItem(STORE)||'{}')||{};if(typeof saved!=='object'||Array.isArray(saved))saved={};}catch(e){saved={};}
const checks=Array.from(document.querySelectorAll('.save-check'));
for(const c of checks)c.checked=!!saved[c.id];
document.addEventListener('change',event=>{const c=event.target;if(!c.matches?.('.save-check'))return;saved[c.id]=c.checked;try{localStorage.setItem(STORE,JSON.stringify(saved));}catch(e){$('progress-notice').textContent='Browser storage blocked; copy a progress summary to back up.';}countChecks();});
function countChecks(){
 const categories=[['Topic scopes',/^complete-topic-/],['Unit checks',/^unit-/],['Workshop lesson checks',/^lesson-/],['Milestones',/^milestone-/]];
 $('check-counter').textContent=categories.map(([label,pattern])=>{const group=checks.filter(c=>pattern.test(c.id));return `${label}: ${group.filter(c=>c.checked).length} of ${group.length}`;}).join(' · ')+' self-reported complete. Practice and transfer checks are counted separately within units and lessons.';
}
countChecks();
async function copyText(text){
 try{if(navigator.clipboard&&window.isSecureContext){await navigator.clipboard.writeText(text);return true;}}catch(e){}
 const previous=document.activeElement;const area=document.createElement('textarea');area.value=text;area.style.cssText='position:fixed;left:-10000px;top:0';document.body.append(area);area.select();let success=false;try{success=document.execCommand('copy');}catch(e){}area.remove();previous?.focus({preventScroll:true});return success;
}
$('copy-progress').addEventListener('click',async()=>{const done=checks.filter(c=>c.checked).map(c=>{const label=c.closest('label');const context=c.closest('.study-unit')?.querySelector('summary')?.textContent||c.closest('.lesson')?.querySelector('h3')?.textContent||c.dataset.progressContext||'';const topic=c.closest('.topic-card')?.querySelector('h3')?.textContent||'';return '- [x] '+[topic,context,label?label.textContent.trim():c.id].filter(Boolean).join(' — ')});const text='My AI Learning Atlas progress\n'+(done.join('\n')||'No completed items yet.');const ok=await copyText(text);$('progress-notice').textContent=ok?'Progress summary copied.':'Copy failed; select text from the page manually.';});
$('reset-progress').addEventListener('click',()=>{if(!confirm('Clear all checkmarks in this browser? Your evidence note and selected role will remain.'))return;for(const c of checks)c.checked=false;saved={};try{localStorage.removeItem(STORE);}catch(e){}countChecks();$('progress-notice').textContent='Progress cleared on this device.';});
// Delegation also covers controls inserted from inert topic templates.
document.addEventListener('click',async event=>{
  const copy=event.target.closest('[data-copy]');
  if(copy){
    const node=$(copy.dataset.copy);
    const ok=await copyText(node?.textContent||'');
    $('progress-notice').textContent=ok?'Prompt copied.':'Clipboard unavailable; select and copy the prompt manually.';
  }
  const button=event.target.closest('[data-copy-topic]');
  if(button){
    const card=button.closest('.topic-card');
    window.AtlasExperience?.hydrate(card);
    const title=card.querySelector('h3').textContent;
    const subs=Array.from(card.querySelectorAll('li[id^="subtopic-"]')).map((li,i)=>`${i+1}. ${li.textContent.trim()}`);
    const number=String(Number(card.id.match(/^topic-(\d+)/)?.[1])).padStart(2,'0');
    const ok=await copyText(`Topic ${number} · ${title}\n\n${subs.join('\n')}`);
    $('progress-notice').textContent=ok?'Topic and subtopics copied.':'Clipboard unavailable; select and copy the original directory manually.';
  }
  const download=event.target.closest('[data-download][data-code]');
  if(download){
    event.preventDefault();
    const code=$(download.dataset.code);
    if(!code){$('progress-notice').textContent='The embedded reference text was not found.';return;}
    const blob=new Blob([code.textContent],{type:'text/plain;charset=utf-8'});
    const url=URL.createObjectURL(blob);
    const anchor=document.createElement('a');anchor.href=url;anchor.download=download.dataset.download;
    document.body.append(anchor);anchor.click();anchor.remove();
    setTimeout(()=>URL.revokeObjectURL(url),1000);
    $('progress-notice').textContent=`Saved embedded reference: ${download.dataset.download}`;
  }
});
const themeBtn=$('theme-btn');const root=document.documentElement;
const preference=window.AtlasThemePreference||{explicit:false};
const systemTheme=window.matchMedia('(prefers-color-scheme: dark)');
let mode=root.dataset.theme==='dark'?'dark':'light';
function setTheme(value){
 mode=value;if(root.dataset.theme!==mode)root.dataset.theme=mode;
 themeBtn.setAttribute('aria-label',mode==='dark'?'Switch to light mode':'Switch to dark mode');
 themeBtn.firstChild.textContent=mode==='dark'?'☀️ ':'🌙 ';
 document.querySelector('meta[name="theme-color"]').content=mode==='dark'?'#0d1527':'#f4f6fc';
}
setTheme(mode);
systemTheme.addEventListener('change',event=>{if(!preference.explicit)setTheme(event.matches?'dark':'light');});
themeBtn.addEventListener('click',()=>{preference.explicit=true;setTheme(mode==='dark'?'light':'dark');try{localStorage.setItem('ai-atlas-theme',mode);}catch{}});
