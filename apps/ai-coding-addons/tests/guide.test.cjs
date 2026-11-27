const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {execFileSync}=require('node:child_process');
const {parseHTML}=require('linkedom');
const root=path.join(__dirname,'..');
const source=JSON.parse(fs.readFileSync(path.join(root,'guide.json'),'utf8'));
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const {document}=parseHTML(html);
test('generated reader matches maintained sources',()=>{execFileSync(process.execPath,['build.cjs','--check'],{cwd:root});});
test('39 unique cards, five explicit statuses and evidence for every path',()=>{
  assert.equal(source.cards.length,39);
  assert.equal(new Set(source.cards.map(c=>c.id)).size,39);
  for(const card of source.cards){
    assert.equal(Object.keys(card.clients).length,5);
    for(const [client,value] of Object.entries(card.clients)){
      assert.ok(['documented','unverified','unavailable'].includes(value.status));
      assert.ok(value.note);
      if(value.status==='documented'){
        assert.ok(value.body.length>250,card.title+' '+client);
        assert.match(value.body,/verif|evidence|prove|require/i,card.title+' '+client);
      }
    }
    for(const key of ['shared','cleanup','warning','version','os','account','cost','processing']) assert.ok(card[key],key+' '+card.title);
    assert.ok(card.sources.length>0);
    card.sources.forEach(s=>{assert.equal(new URL(s.url).protocol,'https:');assert.ok(!s.url.includes('/README.md/README.md'),'Malformed publisher link');});
  }
});
test('all internal links resolve to unique IDs in correct cards',()=>{
  const ids=[...document.querySelectorAll('[id]')].map(el=>el.id);
  assert.equal(new Set(ids).size,ids.length);
  for(const a of document.querySelectorAll('a[href^="#"]')) assert.ok(document.getElementById(a.getAttribute('href').slice(1)),a.outerHTML);
  for(const card of source.cards){
    const node=document.getElementById('card-'+card.id);
    assert.ok(node);assert.equal(node.querySelector('h2').textContent,card.title);
    assert.ok(node.querySelector('.warning'));
    assert.ok(node.querySelector('.card-cleanup'));
  }
  assert.ok(document.getElementById('documentation-and-verification-notes').classList.contains('closing'));
});
test('compatibility metadata matches documented sections and navigation',()=>{
  const metadata=JSON.parse(document.getElementById('compatibility-data').textContent);
  for(const card of source.cards){
    const node=document.getElementById('card-'+card.id);
    const expected=Object.entries(card.clients).filter(([,v])=>v.status==='documented').map(([k])=>k);
    assert.deepEqual([...node.querySelectorAll('.client-section')].map(s=>s.dataset.client),expected);
    assert.deepEqual(node.dataset.clients.split(' '),expected);
    assert.deepEqual(metadata[node.id],Object.fromEntries(Object.entries(card.clients).map(([k,v])=>[k,v.status])));
  }
  assert.equal(document.querySelectorAll('.nav a').length,39);
  assert.equal(document.querySelectorAll('tr[data-card]').length,39);
});
test('commands have copy controls; JSON/TOML examples parse or are labeled',()=>{
  assert.ok(document.querySelectorAll('pre code').length>50);
  for(const wrapper of document.querySelectorAll('.command')){
    assert.ok(wrapper.querySelector('pre code').textContent.trim());
    assert.ok(wrapper.querySelector('button.copy[aria-label]'));
  }
  for(const code of document.querySelectorAll('code.language-json')) assert.doesNotThrow(()=>JSON.parse(code.textContent));
  assert.ok(!/No second copy|No verified installation path for this particular|@agentPlugins/.test(document.querySelector('#cards').textContent),'Card setup must not use obsolete blanket instructions');
});
test('corrected prerequisites and observable activation steps are present',()=>{
  const card=n=>source.cards[n-1];
  assert.equal(card(5).clients.copilot.status,'unavailable');
  assert.equal(card(28).clients.vscode.status,'unverified');
  assert.match(card(5).shared,/22\.13/);
  assert.match(card(12).clients.codex.body,/\/hooks/);
  assert.match(card(29).shared,/coderabbit auth status --agent/);
  assert.match(card(30).clients.vscode.body,/\$\{input:sonarqube-token\}/);
  assert.match(card(32).version,/2\.1\.144/);
  assert.match(card(34).clients.claude.body,/setup_semgrep_plugin/);
  assert.match(card(25).clients.codex.body,/--no-usage-statistics --no-performance-crux/);
});
