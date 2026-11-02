
'use strict';
const DATA=JSON.parse(document.getElementById('atlas-data').textContent);
const $=(id)=>document.getElementById(id);
const field=$('site-search'),results=$('search-results');
const clean=(s)=>String(s||'').toLocaleLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
const safeText=(s)=>document.createTextNode(String(s));
function showResults(){
  const query=clean(field.value.trim());results.replaceChildren();
  if(query.length<2){results.hidden=true;field.setAttribute('aria-expanded','false');return;}
  const terms=query.split(/\s+/).filter(Boolean);
  let found=DATA.search.map(entry=>({entry, score:clean(entry.title).includes(query)?4:0})).filter(o=>terms.every(t=>clean(o.entry.title+' '+o.entry.context).includes(t)));
  found.sort((a,b)=>b.score-a.score||['Topic','Profession','Lesson','Subtopic','Glossary'].indexOf(a.entry.type)-['Topic','Profession','Lesson','Subtopic','Glossary'].indexOf(b.entry.type));
  const summary=document.createElement('div');summary.className='sr-summary';summary.textContent=`${found.length} match${found.length===1?'':'es'} — showing up to 35. Select a result to jump to it.`;results.append(summary);
  if(!found.length){let empty=document.createElement('p');empty.className='empty';empty.textContent='No exact matches. Try fewer words (for example: RAG, Python, embeddings).';results.append(empty);}
  for(const {entry} of found.slice(0,35)){
    const link=document.createElement('a');link.href=entry.href;
    const heading=document.createElement('strong');heading.textContent=`${entry.type}: ${entry.title}`;
    const detail=document.createElement('small');detail.textContent=entry.context;
    link.append(heading,detail);link.addEventListener('click',()=>{results.hidden=true;field.setAttribute('aria-expanded','false');});results.append(link);
  }
  results.hidden=false;field.setAttribute('aria-expanded','true');
}
field.addEventListener('input',showResults);
field.addEventListener('keydown',(e)=>{if(e.key==='Escape'){field.value='';showResults();field.focus();}if(e.key==='Enter'&&!results.hidden){const a=results.querySelector('a');if(a){a.click();}}});
document.addEventListener('click',(e)=>{if(!e.target.closest('.searchbox')){results.hidden=true;field.setAttribute('aria-expanded','false');}});
function openDeepLink(){
  if(!location.hash)return;
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
for(const c of checks){c.checked=!!saved[c.id];c.addEventListener('change',()=>{saved[c.id]=c.checked;try{localStorage.setItem(STORE,JSON.stringify(saved));}catch(e){$('progress-notice').textContent='Browser storage blocked; copy a progress summary to back up.';}countChecks();});}
function countChecks(){const n=checks.filter(x=>x.checked).length;$('check-counter').textContent=`${n} of ${checks.length} checklist items self-reported complete (milestones, units and lessons)`;}
countChecks();
async function copyText(text){
 try{if(navigator.clipboard&&window.isSecureContext){await navigator.clipboard.writeText(text);return true;}}catch(e){}
 const previous=document.activeElement;const area=document.createElement('textarea');area.value=text;area.style.cssText='position:fixed;left:-10000px;top:0';document.body.append(area);area.select();let success=false;try{success=document.execCommand('copy');}catch(e){}area.remove();previous?.focus({preventScroll:true});return success;
}
$('copy-progress').addEventListener('click',async()=>{const done=checks.filter(c=>c.checked).map(c=>{const label=c.closest('label');const context=c.closest('.study-unit')?.querySelector('summary')?.textContent||c.closest('.lesson')?.querySelector('h3')?.textContent||'';const topic=c.closest('.topic-card')?.querySelector('h3')?.textContent||'';return '- [x] '+[topic,context,label?label.textContent.trim():c.id].filter(Boolean).join(' — ')});const text='My AI Learning Atlas progress\n'+(done.join('\n')||'No completed items yet.');const ok=await copyText(text);$('progress-notice').textContent=ok?'Progress summary copied.':'Copy failed; select text from the page manually.';});
$('reset-progress').addEventListener('click',()=>{if(!confirm('Clear all checkmarks in this browser? Your evidence note and selected role will remain.'))return;for(const c of checks)c.checked=false;saved={};try{localStorage.removeItem(STORE);}catch(e){}countChecks();$('progress-notice').textContent='Progress cleared on this device.';});
document.querySelectorAll('[data-copy]').forEach(button=>button.addEventListener('click',async()=>{const node=$(button.dataset.copy);const ok=await copyText(node?.innerText||'');$('copy-feedback').textContent=ok?'Copied! Paste into your AI assistant.':'Clipboard unavailable; select and copy the prompt below.';}));
document.querySelectorAll('[data-copy-topic]').forEach(button=>button.addEventListener('click',async()=>{const card=button.closest('.topic-card');const title=card.querySelector('h3').innerText;const subs=Array.from(card.querySelectorAll('li[id^="subtopic-"]')).map((li,i)=>`${i+1}. ${li.innerText.trim()}`);const ok=await copyText(`${title}\n\n${subs.join('\n')}`);button.nextElementSibling.textContent=ok?'Topic and subtopics copied.':'Clipboard unavailable; select and copy the list below.';}));
const themeBtn=$('theme-btn');const root=document.documentElement;
let mode='light';try{mode=localStorage.getItem('ai-atlas-theme')||'light';}catch(e){}
function setTheme(value){mode=value;root.dataset.theme=mode;themeBtn.setAttribute('aria-label',mode==='dark'?'Switch to light mode':'Switch to dark mode');themeBtn.firstChild.textContent=mode==='dark'?'☀️ ':'🌙 ';}
setTheme(mode==='dark'?'dark':'light');themeBtn.addEventListener('click',()=>{setTheme(mode==='dark'?'light':'dark');try{localStorage.setItem('ai-atlas-theme',mode);}catch(e){}});
