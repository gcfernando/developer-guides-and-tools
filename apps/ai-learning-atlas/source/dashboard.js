
/* Personal-learning layer: offline-first, no tracking or network calls. */
(() => {
  'use strict';
  const roles = Object.keys(DATA.priorities);
  const coreStatuses = new Set(['Essential','Recommended']);
  const profileKey = 'ai-atlas-active-role-v2';
  const home = document.getElementById('role-home');
  const matrix = document.getElementById('role-filter');
  const records = new Map(Array.from(document.querySelectorAll('article.topic-card')).map((node,i) => [
    String(i+1), {title: node.querySelector('h3')?.textContent.trim() || `Topic ${i+1}`, href:'#'+node.id}
  ]));
  const checkFor = (n) => document.getElementById(`complete-topic-${String(n).padStart(2,'0')}`);
  const selectedLabel = () => home.options[home.selectedIndex]?.textContent.trim() || '';
  let currentRole = '';
  function getCore(role) {
    const d=DATA.priorities[role] || {};
    return Object.entries(d).filter(([,v])=>coreStatuses.has(v)).map(([id,v])=>({id:Number(id),priority:v,...records.get(id)}))
      .filter(x=>x.title);
  }
  function orderedCore(role) {
    const d=DATA.priorities[role] || {};
    const path=document.getElementById(`role-${role}`);
    if(!path) return getCore(role);
    const seen=new Set();
    const ordered=[];
    path.querySelectorAll('.path-list .path-item h5 a').forEach(link=>{
      const idmatch=(link.textContent || '').match(/Topic\s+(\d+)/);
      if(!idmatch) return;
      const id=Number(idmatch[1]);
      if(seen.has(id) || !coreStatuses.has(d[String(id)])) return;
      seen.add(id);ordered.push({id,priority:d[String(id)],...records.get(String(id))});
    });
    return ordered;
  }
  function updateDoneButtons() {
    document.querySelectorAll('[data-complete-topic]').forEach(btn=>{
      const completed=!!checkFor(btn.dataset.completeTopic)?.checked;
      btn.setAttribute('aria-pressed',String(completed));
      btn.classList.toggle('is-complete',completed);
      btn.textContent=completed?'✓ Scope complete':'○ Mark scope done';
      btn.setAttribute('aria-label',`${completed?'Mark as not completed':'Mark as completed'}: ${records.get(String(Number(btn.dataset.completeTopic)))?.title || 'topic'}`);
    });
  }
  function renderDashboard(){
    const valid=roles.includes(currentRole);
    document.getElementById('role-dashboard-empty').hidden=valid;
    document.getElementById('role-dashboard-active').hidden=!valid;
    document.getElementById('progress-role-empty').hidden=valid;
    document.getElementById('progress-role-active').hidden=!valid;
    document.querySelectorAll('.role-tile').forEach(tile=>{
      const active=tile.getAttribute('href')===`#role-${currentRole}`;
      tile.classList.toggle('is-selected',active);
      if(active) tile.setAttribute('aria-current','true'); else tile.removeAttribute('aria-current');
    });
    if(!valid){
      refreshVisibleChecks();updateDoneButtons();
      return;
    }
    const entries=orderedCore(currentRole);
    const essentials=entries.filter(x=>x.priority==='Essential');
    const recommends=entries.filter(x=>x.priority==='Recommended');
    const done=entries.filter(x=>checkFor(x.id)?.checked);
    const pct=entries.length ? Math.round(100*done.length/entries.length) : 0;
    const next=entries.find(x=>!checkFor(x.id)?.checked);
    document.getElementById('essential-count').textContent=String(essentials.length);
    document.getElementById('recommended-count').textContent=String(recommends.length);
    document.getElementById('relevant-completed').textContent=`${done.length} / ${entries.length}`;
    document.getElementById('home-role-meter').value=pct;
    document.getElementById('progress-role-meter').value=pct;
    document.getElementById('role-meter-label').textContent=`${pct}% of ${entries.length} selected topic scopes self-reported complete; this is not a mastery score`;
    document.getElementById('progress-role-caption').textContent=`${done.length} of ${entries.length} topic scopes self-reported complete for ${selectedLabel()}`;
    document.getElementById('active-role-path').href=`#role-${currentRole}`;
    document.getElementById('active-role-project').href=`#project-${currentRole}`;
    const link=document.getElementById('next-topic-link');
    if(next){
      document.getElementById('next-topic-name').textContent=`Topic ${String(next.id).padStart(2,'0')} · ${next.title}`;
      document.getElementById('next-topic-context').textContent=`${next.priority} · Choose study units and collect the stated evidence inside the topic library.`;
      document.getElementById('progress-next-step').textContent=`Next: Topic ${String(next.id).padStart(2,'0')} · ${next.title}. Review your declared scope and evidence before marking it complete.`;
      link.href=next.href;link.textContent='Open next topic →';
    } else {
      document.getElementById('next-topic-name').textContent='🏆 Your selected topic scopes are checked';
      document.getElementById('next-topic-context').textContent='Review your capstone, then choose an advanced topic only if your role needs it.';
      document.getElementById('progress-next-step').textContent='All selected topic scopes checked. Review your evidence and complete the capstone assessment; checkmarks alone do not demonstrate proficiency.';
      link.href=`#project-${currentRole}`;link.textContent='Open my capstone →';
    }
    refreshVisibleChecks();updateDoneButtons();
  }
  function refreshVisibleChecks(){
    const showAll=document.getElementById('show-all-topic-checks').checked;
    const eligible=new Set(currentRole?getCore(currentRole).map(x=>x.id):[]);
    let shown=0;
    document.querySelectorAll('.topic-check-grid label').forEach(label=>{
      const input=label.querySelector('input[id^="complete-topic-"]');
      if(!input)return;
      const id=Number(input.id.replace('complete-topic-',''));
      label.hidden=!!(currentRole&&!showAll&&!eligible.has(id));
      if(!label.hidden)shown++;
    });
    const top=document.querySelector('#progress .topic-check-grid');
    top.setAttribute('aria-label',currentRole&&!showAll?`${shown} essential and recommended topics for ${selectedLabel()}`:'All 51 AI topics');
  }
  function chooseRole(next,{persist=true}={}){
    currentRole=roles.includes(next)?next:'';
    home.value=currentRole;matrix.value=currentRole;
    updateMatrix();
    renderDashboard();
    if(persist){try{localStorage.setItem(profileKey,currentRole);}catch(e){}}
  }
  home.addEventListener('change',()=>chooseRole(home.value));
  matrix.addEventListener('change',()=>chooseRole(matrix.value));
  document.getElementById('show-all-topic-checks').addEventListener('change',refreshVisibleChecks);
  document.addEventListener('click',e=>{
    const tile=e.target.closest('.role-tile');
    if(tile){
      const selected=tile.getAttribute('href')?.replace(/^#role-/,'');
      if(roles.includes(selected))chooseRole(selected);
    }
    const link=e.target.closest('a[href^="#role-"]');
    if(link&&!tile){
      const selected=link.getAttribute('href')?.replace(/^#role-/,'');
      if(roles.includes(selected))chooseRole(selected);
    }
    const doneButton=e.target.closest('[data-complete-topic]');
    if(doneButton){
      const control=checkFor(doneButton.dataset.completeTopic);
      if(control){
        control.checked=!control.checked;
        control.dispatchEvent(new Event('change',{bubbles:true}));
      }
    }
  });
  // The existing checkboxes are the canonical state; all displays react to them.
  document.querySelectorAll('.save-check').forEach(c=>c.addEventListener('change',renderDashboard));
  document.getElementById('reset-progress').addEventListener('click',()=>setTimeout(renderDashboard,0));
  document.getElementById('download-progress').addEventListener('click',()=>{
    const state={version:2,selectedRole:currentRole,savedAt:new Date().toISOString(),note:document.getElementById('study-note').value,checks:Object.fromEntries(
      Array.from(document.querySelectorAll('.save-check')).map(c=>[c.id,c.checked])
    )};
    const blob=new Blob([JSON.stringify(state,null,2)],{type:'application/json'});
    if(state.note.length>50000||blob.size>250000){document.getElementById('progress-notice').textContent='Backup exceeds the restore limit. Copy your note separately and shorten it before exporting (50,000 characters and 250 KB maximum).';return;}
    const objectURL=URL.createObjectURL(blob);
    const anchor=document.createElement('a');anchor.href=objectURL;anchor.download='ai-learning-atlas-progress.json';
    document.body.append(anchor);anchor.click();anchor.remove();setTimeout(()=>URL.revokeObjectURL(objectURL),1000);
    document.getElementById('progress-notice').textContent='Progress and evidence note exported. Keep your backup private.';
  });
  document.getElementById('import-progress-file').addEventListener('change',async e=>{
    const input=e.currentTarget,file=input.files?.[0],notice=document.getElementById('progress-notice');
    if(!file)return;
    try{
      if(file.size>250000)throw new Error('Backup too large (250 KB maximum).');
      const parsed=JSON.parse(await file.text());
      if(!parsed||![1,2].includes(parsed.version)||!parsed.checks||Array.isArray(parsed.checks)||typeof parsed.checks!=='object')
        throw new Error('Not a recognized AI Learning Atlas backup.');
      if(typeof parsed.selectedRole!=='string'||(parsed.selectedRole&&!roles.includes(parsed.selectedRole)))throw new Error('Unknown profession.');
      if(parsed.version===2&&(typeof parsed.note!=='string'||parsed.note.length>50000))throw new Error('Invalid evidence note.');
      const known=Array.from(document.querySelectorAll('.save-check'));
      const legacy=c=>c.id.startsWith('complete-topic-')||c.id.startsWith('milestone-');
      const own=(id)=>Object.prototype.hasOwnProperty.call(parsed.checks,id);
      if(known.some(c=>(parsed.version===2||legacy(c))&&(!own(c.id)||typeof parsed.checks[c.id]!=='boolean'))||
         Object.values(parsed.checks).some(value=>typeof value!=='boolean'))throw new Error('Missing or invalid checklist fields.');
      if(!confirm('Restore this backup? Current checkmarks will be replaced. Version 2 also replaces the evidence note; a legacy backup leaves it unchanged.'))return;
      const nextSaved={};
      known.forEach(c=>{c.checked=own(c.id)?parsed.checks[c.id]:false;nextSaved[c.id]=c.checked;});
      saved=nextSaved;
      if(parsed.version===2)document.getElementById('study-note').value=parsed.note;
      let persisted=true;
      try{
        localStorage.setItem(STORE,JSON.stringify(saved));
        localStorage.setItem(profileKey,parsed.selectedRole);
        if(parsed.version===2)localStorage.setItem('ai-atlas-study-note-v1',parsed.note);
      }catch{persisted=false;}
      countChecks();chooseRole(parsed.selectedRole,{persist:false});
      document.dispatchEvent(new Event('atlas-progress-restored'));
      notice.textContent=persisted?'Backup restored. Review your role, note and evidence.':'Restored for this session only; storage unavailable. Keep your backup file.';
    }catch(error){notice.textContent=`Could not restore backup: ${error.message}`;}
    finally{input.value='';}
  });
  // Additional search keyboard support and concise result counts for assistive tech.
  const field=document.getElementById('site-search');
  const results=document.getElementById('search-results');
  const status=document.getElementById('search-status');
  let searchLiveTimer;
  field.addEventListener('input',()=>{
    clearTimeout(searchLiveTimer);
    searchLiveTimer=setTimeout(()=>{
      const txt=results.querySelector('.sr-summary')?.textContent || 'Enter at least two characters to search.';
      status.textContent=txt;
    },250);
  });
  field.addEventListener('keydown',e=>{
    if(e.key==='ArrowDown'&&!results.hidden){
      const first=results.querySelector('a');
      if(first){e.preventDefault();first.focus();}
    }
  });
  results.addEventListener('keydown',e=>{
    if(!['ArrowDown','ArrowUp','Escape'].includes(e.key))return;
    e.preventDefault();
    if(e.key==='Escape'){results.hidden=true;field.setAttribute('aria-expanded','false');field.focus();return;}
    const links=Array.from(results.querySelectorAll('a'));
    const idx=links.indexOf(document.activeElement);
    if(!links.length){field.focus();return;}
    if(e.key==='ArrowDown')links[Math.min(links.length-1,idx+1)].focus();
    else if(idx<=0)field.focus();
    else links[idx-1].focus();
  });
  // "/" shortcut only when not typing in editable fields.
  document.addEventListener('keydown',e=>{
    if(e.key==='/'&&!e.altKey&&!e.ctrlKey&&!e.metaKey&&
      !['INPUT','TEXTAREA','SELECT'].includes(document.activeElement?.tagName)&&
      !document.activeElement?.isContentEditable){
      e.preventDefault();field.focus();
    }
  });
  // Reveal the currently selected role when arriving from a deep link.
  const hashRole=window.location.hash.replace(/^#role-/,'');
  let persisted='';
  try{persisted=localStorage.getItem(profileKey)||'';}catch(e){}
  chooseRole(roles.includes(hashRole)?hashRole:persisted,{persist:false});
})();
