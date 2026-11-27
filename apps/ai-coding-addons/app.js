(() => {
  'use strict';
  const byId = id => document.getElementById(id);
  const cards = [...document.querySelectorAll('.tool-card')];
  const clientNames = {claude:'Claude Code CLI',codex:'Codex CLI',copilot:'GitHub Copilot CLI',vscode:'VS Code Copilot Chat',canvas:'Copilot app (canvas)'};
  // Cache searchable text before adding UI state. Exclude other clients and evidence metadata.
  const searchable = new Map(cards.map(card => [card, {
    shared: [...card.querySelector('.card-shared').children].filter(el => !el.classList.contains('compatibility')).map(el=>el.textContent).join(' ').toLowerCase(),
    sections: [...card.querySelectorAll('.client-section')].map(el=>({client:el.dataset.client,text:el.textContent.toLowerCase()}))
  }]));
  const metadata = JSON.parse(byId('compatibility-data')?.textContent || '{}');
  function filter() {
    const q = byId('query').value.trim().toLowerCase();
    const client = byId('clientFilter').value;
    const include = byId('includeUnverified').checked;
    let count = 0;
    cards.forEach(card => {
      const data = searchable.get(card);
      const documented = card.dataset.clients.split(' ').includes(client);
      const unverified = metadata[card.id]?.[client] === 'unverified';
      const compatible = client === 'all' || documented || (include && unverified);
      const text = data.shared + ' ' + data.sections.filter(s => client === 'all' || s.client === client).map(s=>s.text).join(' ');
      const show = compatible && (!q || text.includes(q));
      card.hidden = !show;
      document.querySelector('.nav a[href="#'+card.id+'"]').hidden = !show;
      document.querySelector('tr[data-card="'+card.id+'"]').hidden = !show;
      card.querySelectorAll('.client-section').forEach(section => {
        section.hidden = client !== 'all' && section.dataset.client !== client;
        if (client !== 'all' && !section.hidden) section.open = true;
      });
      let notice = card.querySelector('.unverified-notice');
      if (!notice) {notice=document.createElement('p');notice.className='unverified-notice warning';card.querySelector('.card-shared').append(notice);}
      notice.hidden = !(client !== 'all' && !documented && compatible);
      if (!notice.hidden) notice.textContent = 'Unverified for '+clientNames[client]+'. Open Compatibility, versions and evidence for the qualification. No setup recipe is claimed for this path.';
      if (show) count++;
    });
    byId('count').textContent = count+' add-ons shown';
    byId('empty').hidden = count !== 0;
  }
  function reset() {
    byId('query').value='';byId('clientFilter').value='all';byId('includeUnverified').checked=false;filter();
  }
  function revealHash() {
    let id;
    try {id=decodeURIComponent(location.hash.slice(1));} catch {return;}
    let target=byId(id);
    if(!target) target=byId('card-'+id); // Preserve original public fragments.
    if(!target) return;
    const card=target.closest('.tool-card');
    if(card) {
      if(card.hidden) reset();
      card.querySelectorAll('.client-section:not([hidden])').forEach(section=>{section.open=true;});
      target=card;
    }
    if(target.tagName==='DETAILS') target.open=true;
    requestAnimationFrame(()=>{target.scrollIntoView({block:'start'});if(card)card.focus({preventScroll:true});});
  }
  byId('query').addEventListener('input',filter);
  byId('clientFilter').addEventListener('change',filter);
  byId('includeUnverified').addEventListener('change',filter);
  byId('reset').addEventListener('click',()=>{reset();byId('query').focus();});
  byId('emptyReset').addEventListener('click',()=>{reset();byId('query').focus();});
  document.addEventListener('click',event=>{
    const link=event.target.closest('a[href^="#"]');
    if(link && link.hash===location.hash) revealHash();
  });
  window.addEventListener('hashchange',revealHash);
  const media=window.matchMedia('(prefers-color-scheme: dark)');
  let preference=null;
  try{preference=localStorage.getItem('ai-addons-theme');}catch{}
  function theme(dark){document.body.classList.toggle('dark',dark);byId('theme').setAttribute('aria-pressed',String(dark));byId('theme').textContent=dark?'Light mode':'Dark mode';}
  theme(preference?preference==='dark':media.matches);
  media.addEventListener('change',event=>{if(!preference)theme(event.matches);});
  byId('theme').addEventListener('click',()=>{
    const dark=!document.body.classList.contains('dark');theme(dark);preference=dark?'dark':'light';
    try{localStorage.setItem('ai-addons-theme',preference);}catch{}
  });
  document.querySelectorAll('.command').forEach(wrapper=>{
    const code=wrapper.querySelector('code');const button=wrapper.querySelector('.copy');
    let timer;
    button.addEventListener('click',async()=>{
      clearTimeout(timer);
      try{await navigator.clipboard.writeText(code.textContent);button.textContent='Copied';byId('copyStatus').textContent='Example copied.';}
      catch{const selection=window.getSelection();const range=document.createRange();range.selectNodeContents(code);selection.removeAllRanges();selection.addRange(range);button.textContent='Selected — copy manually';byId('copyStatus').textContent='Clipboard unavailable. Example selected; press Control+C or Command+C.';}
      timer=setTimeout(()=>{button.textContent='Copy';},2500);
    });
  });
  filter();revealHash();
})();
