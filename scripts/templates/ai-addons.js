const byId=id=>document.getElementById(id);
function filter(){
  const q=byId('query').value.toLowerCase().trim(),client=byId('clientFilter').value;
  let count=0;
  document.querySelectorAll('.tool-card').forEach(card=>{
    const match=!q||card.textContent.toLowerCase().includes(q);
    card.classList.toggle('none',!match);if(match)count++;
    card.querySelectorAll('h3').forEach(h=>{
      const clientHeading=['Claude Code CLI','Codex CLI','GitHub Copilot CLI','Visual Studio Code'].some(x=>h.textContent.includes(x));
      if(!clientHeading)return;
      const hide=client!=='all'&&!h.textContent.includes(client);
      h.classList.toggle('none',hide);
      let current=h.nextElementSibling;
      while(current&&!['H2','H3'].includes(current.tagName)){
        current.classList.toggle('none',hide);current=current.nextElementSibling;
      }
    });
  });
  byId('count').textContent=count+' add-ons shown';
}
byId('query').addEventListener('input',filter);
byId('clientFilter').addEventListener('change',filter);
byId('theme').addEventListener('click',()=>{
  document.body.classList.toggle('dark');
  byId('theme').textContent=document.body.classList.contains('dark')?'Light mode':'Dark mode';
});
document.querySelectorAll('pre code').forEach(code=>{
  const button=document.createElement('button');button.className='copy';button.type='button';button.textContent='Copy';
  button.addEventListener('click',async()=>{
    try{await navigator.clipboard.writeText(code.textContent);button.textContent='Copied';}
    catch{button.textContent='Select and copy the command';}
    setTimeout(()=>{button.textContent='Copy';},1800);
  });
  code.parentElement.before(button);
});
