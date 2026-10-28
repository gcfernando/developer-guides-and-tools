const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const {execFileSync}=require('node:child_process');
const {parseHTML}=require('linkedom');
const {read,frontMatter,yaml,ROOT}=require('../scripts/lib.cjs');

test('catalog generation is independent of filesystem enumeration order',()=>{
  const script=path.join(ROOT,'scripts/build-catalog.cjs');
  const preload=path.join(ROOT,'tests/fixtures/reverse-readdir.cjs');
  execFileSync(process.execPath,[script,'--check'],{cwd:ROOT,stdio:'pipe'});
  execFileSync(process.execPath,['--require',preload,script,'--check'],{cwd:ROOT,stdio:'pipe'});
});

test('all catalog resources and stable page routes resolve',()=>{
  const resources=yaml.parse(read('_data/resources.yml'));
  const routes=JSON.parse(read('_data/routes.json'));
  assert.equal(new Set(resources.map(r=>r.path)).size,resources.length);
  assert.equal(new Set(Object.values(routes)).size,Object.keys(routes).length);
  for(const r of resources){
    assert.ok(fs.existsSync(path.join(ROOT,r.path)),r.path);
    if(r.path.endsWith('.md')){
      const data=frontMatter(read(r.path)).data;
      assert.equal(routes[r.path],data.permalink);
      assert.ok(data.title&&data.description,'Page metadata: '+r.path);
    }
  }
});

test('AI add-ons reader contains all source sections and registration clarification',()=>{
  const source=frontMatter(read('docs/ai/coding-addons.md')).body;
  const sections=[...source.matchAll(/^## (\d{2})\. (.+)$/gm)];
  const {document}=parseHTML(read('apps/ai-coding-addons/index.html'));
  const cards=[...document.querySelectorAll('.tool-card')];
  assert.equal(cards.length,sections.length);
  assert.equal(cards.length,39);
  for(let i=0;i<cards.length;i++)assert.equal(cards[i].querySelector('h2').textContent,sections[i][1]+'. '+sections[i][2]);
  assert.ok(document.body.textContent.includes('Registration comes before connection checks.'));
  const ids=[...document.querySelectorAll('[id]')].map(n=>n.id);
  assert.equal(new Set(ids).size,ids.length,'Reader has duplicate IDs');
  for(const a of document.querySelectorAll('a[href^="#"]'))assert.ok(document.getElementById(a.getAttribute('href').slice(1)),a.getAttribute('href'));
});

test('Atlas search, progress controls and role priorities remain aligned',()=>{
  const {document}=parseHTML(read('apps/ai-learning-atlas/index.html'));
  const data=JSON.parse(document.getElementById('atlas-data').textContent);
  for(const record of data.search)assert.ok(document.getElementById(record.href.slice(1)),'Missing Atlas search target '+record.href);
  const topics=[...document.querySelectorAll('article.topic-card')];
  assert.equal(topics.length,51);
  assert.equal(data.search.filter(r=>r.type==='Topic').length,topics.length);
  assert.equal(data.search.filter(r=>r.type==='Profession').length,Object.keys(data.priorities).length);
  for(const [role,priorities] of Object.entries(data.priorities)){
    assert.ok(document.getElementById('role-'+role),role);
    for(const id of Object.keys(priorities))assert.ok(document.getElementById('complete-topic-'+id.padStart(2,'0')),'Missing checkbox '+id);
  }
  assert.ok(read('apps/ai-learning-atlas/index.html').includes("ai-learning-atlas-progress-v1"));
  assert.ok(read('apps/ai-learning-atlas/index.html').includes("ai-atlas-active-role-v2"));
});

test('application JavaScript parses and embedded JSON is valid',()=>{
  for(const file of ['apps/linux-command-reference/index.html','apps/ai-learning-atlas/index.html','apps/ai-coding-addons/index.html']){
    const {document}=parseHTML(read(file));
    for(const script of document.querySelectorAll('script')){
      if(script.hasAttribute('src'))continue;
      if(script.getAttribute('type')?.includes('json'))JSON.parse(script.textContent);
      else new vm.Script(script.textContent,{filename:file});
    }
  }
});

test('Compose passwords are explicit inputs and published ports use loopback',()=>{
  const compose=yaml.parse(read('examples/containers/local-services/compose.yml'));
  assert.deepEqual(Object.keys(compose.services).sort(),['sqlserver','elasticsearch','kibana','oracle','mongodb','rabbitmq','mysql','kafka','kafka-ui','redis','keycloak'].sort());
  for(const service of Object.values(compose.services))for(const port of service.ports||[])assert.match(port,/^127\.0\.0\.1:/);
  for(const key of ['sql_password','oracle_password','default_root_password'])assert.match(compose['x-variables'][key],/^\$\{[A-Z_]+:\?/);
});

test('workflows and configuration documents parse',()=>{
  for(const file of ['_config.yml','_data/navigation.yml','.github/workflows/validate.yml','.github/workflows/pages.yml','.github/ISSUE_TEMPLATE/documentation-error.yml','.github/ISSUE_TEMPLATE/resource-request.yml'])assert.ok(yaml.parse(read(file)),file);
  JSON.parse(read('examples/ai-clients/claude/settings.example.json'));
  assert.equal(fs.existsSync(path.join(ROOT,'examples/ai-clients/copilot/copilot-config.json')),false);
});
