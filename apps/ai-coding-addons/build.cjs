const fs = require('node:fs');
const path = require('node:path');
const MarkdownIt = require('markdown-it');
const {parseHTML} = require('linkedom');
const root = __dirname;
const read = file => fs.readFileSync(path.join(root, file), 'utf8').replace(/\r\n/g, '\n');
const escape = text => String(text).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const md = new MarkdownIt({html: false, linkify: false});
const clients = {claude:'Claude Code CLI',codex:'Codex CLI',copilot:'GitHub Copilot CLI',vscode:'VS Code Copilot Chat',canvas:'Copilot app (canvas)'};
const guide = JSON.parse(read('guide.json'));
if (guide.cards.length !== 39) throw new Error('Expected 39 add-ons');
const labels = {documented:'Documented',unverified:'Unverified',unavailable:'Unavailable'};
function render(markdown) {
  const {document} = parseHTML('<html><body>'+md.render(markdown)+'</body></html>');
  for (const pre of document.querySelectorAll('pre')) {
    const code = pre.querySelector('code');
    const language = (code.className || '').replace('language-', '');
    const label = ({terminal:'Terminal · PowerShell / macOS / Linux',powershell:'PowerShell',bash:'macOS / Linux shell',chat:'Assistant chat',json:'JSON configuration',toml:'TOML configuration',text:'Form values / output'})[language] || language || 'Example';
    const wrapper = document.createElement('div'); wrapper.className = 'command';
    const bar = document.createElement('div'); bar.className = 'command-bar';
    const title = document.createElement('span'); title.textContent = label;
    const button = document.createElement('button'); button.type = 'button'; button.className = 'copy'; button.textContent = 'Copy'; button.setAttribute('aria-label', 'Copy '+label+' example');
    bar.append(title,button); pre.before(wrapper); wrapper.append(bar,pre);
    pre.tabIndex = 0;
  }
  for (const table of document.querySelectorAll('table')) {
    const wrapper=document.createElement('div');wrapper.className='table-scroll';
    wrapper.tabIndex=0;wrapper.setAttribute('role','region');wrapper.setAttribute('aria-label','Scrollable guide table');
    table.querySelectorAll('thead th').forEach(th=>th.setAttribute('scope','col'));
    table.before(wrapper);wrapper.append(table);
  }
  return document.body.innerHTML;
}
function card(c) {
  for (const key of Object.keys(clients)) if (!c.clients[key]) throw new Error('Missing client status: '+c.id+' '+key);
  const supported = Object.entries(c.clients).filter(([,v]) => v.status === 'documented').map(([k])=>k);
  const shared = render(c.shared);
  const badges = supported.map(k=>'<span class="badge">'+clients[k]+'</span>').join('');
  const compatibility = Object.entries(c.clients).map(([k,v])=>'<tr><th scope="row">'+clients[k]+'</th><td>'+labels[v.status]+'</td><td>'+escape(v.note || (v.status === 'documented'?'Publisher documents this integration; live setup not executed in this review.':'No confirmed path in this edition.'))+'</td></tr>').join('');
  const sections = Object.entries(c.clients).filter(([,v])=>v.status==='documented').map(([k,v])=>'<details class="client-section" data-client="'+k+'"><summary><h3>'+clients[k]+'</h3></summary><div class="client-content">'+render(v.body)+'</div></details>').join('\n');
  return '<article class="tool-card" id="card-'+c.id+'" tabindex="-1" data-clients="'+supported.join(' ')+'" aria-labelledby="title-'+c.id+'"><div class="card-shared"><p class="eyebrow">'+c.number+' · '+escape(c.type)+'</p><h2 id="title-'+c.id+'">'+escape(c.title)+'</h2><p>'+escape(c.description)+'</p><div class="badges">'+badges+'</div><p class="metadata">'+escape(c.difficulty)+' · '+escape(c.time)+' estimate · '+escape(c.cost)+'</p>'+shared+'<p class="warning"><strong>Before use:</strong> '+escape(c.warning)+'</p><details class="compatibility"><summary>Compatibility, versions and evidence</summary><div class="table-scroll"><table><caption>'+escape(c.title)+' compatibility</caption><thead><tr><th>Environment</th><th>Status</th><th>Qualification</th></tr></thead><tbody>'+compatibility+'</tbody></table></div><p><strong>Reviewed:</strong> '+guide.reviewed+' · <strong>Package / minimum version:</strong> '+escape(c.version)+' · <strong>OS:</strong> '+escape(c.os)+'</p><p>Evidence: '+c.sources.map(s=>'<a href="'+escape(s.url)+'">'+escape(s.label)+'</a>').join(' · ')+'</p><p><strong>Execution status:</strong> Integration setup not run in this review. Record your actual OS, assistant version, package version and smoke-test result using the validation template below.</p></details></div>'+sections+'<details class="card-cleanup"><summary>Disable or remove '+escape(c.title)+'</summary>'+render(c.cleanup)+'</details></article>';
}
const cards = guide.cards.map(card).join('\n');
const rows = guide.cards.map(c=>'<tr data-card="card-'+c.id+'"><th scope="row"><a href="#card-'+c.id+'">'+escape(c.title)+'</a></th><td>'+escape(c.type)+'</td><td>'+Object.entries(c.clients).filter(([,v])=>v.status==='documented').map(([k])=>clients[k]).join(', ')+'</td><td>'+escape(c.difficulty)+'<br>'+escape(c.time)+' estimate</td><td>'+escape(c.processing)+'</td><td>'+escape(c.account)+'</td><td>'+escape(c.cost)+'</td></tr>').join('');
const title='AI Coding Add-ons — Beginner’s Project Guide';
const canonical='https://gcfernando.github.io/developer-guides-and-tools/apps/ai-coding-addons/';
const desc='Compare 39 AI coding add-ons with explicit compatibility, scoped setup, verification and removal guidance.';
const schema=JSON.stringify({'@context':'https://schema.org','@type':'Article',headline:title,description:desc,url:canonical,dateModified:guide.reviewed,author:{'@type':'Person',name:'Gehan Fernando'}}).replace(/</g,'\\u003c');
const page='<!doctype html>\n<!-- Generated locally by build.cjs from guide.json, intro.md, closing.md, styles.css and app.js. See README.md before running a repository-wide build. -->\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light dark"><title>'+title+'</title><meta name="description" content="'+desc+'"><link rel="canonical" href="'+canonical+'"><meta property="og:type" content="article"><meta property="og:title" content="'+title+'"><meta property="og:description" content="'+desc+'"><meta property="og:url" content="'+canonical+'"><meta name="twitter:card" content="summary"><script type="application/ld+json">'+schema+'</script><style>'+read('styles.css')+'</style></head><body><a class="skip" href="#main">Skip to guide</a><header class="hero"><p class="eyebrow">Developer Guides, Cheat Sheets &amp; Tools</p><h1>AI Coding Add-ons</h1><p>A practical guide to choosing, setting up and verifying one add-on at a time.</p><p>39 entries · explicit compatibility · reviewed '+guide.reviewed+'</p></header><div class="shell"><aside class="sidebar" aria-label="Guide navigation"><label for="query">Find an add-on</label><input id="query" type="search" placeholder="Name, task or technology"><label for="clientFilter">Coding environment</label><select id="clientFilter"><option value="all">All environments</option>'+Object.entries(clients).map(([k,v])=>'<option value="'+k+'">'+v+'</option>').join('')+'</select><label class="checkbox"><input id="includeUnverified" type="checkbox"> Include unverified paths</label><p class="help">Results match documented integrations by default. Canvas apps have their own environment.</p><div class="controls"><button type="button" id="reset">Clear filters</button><button type="button" id="theme" aria-pressed="false">Dark mode</button></div><p id="count" role="status" aria-live="polite">39 add-ons shown</p><nav class="nav" aria-label="Matching add-ons">'+guide.cards.map(c=>'<a href="#card-'+c.id+'">'+c.number+' '+escape(c.title)+'</a>').join('')+'</nav><a href="#comparison">Compare all add-ons</a><a href="#documentation-and-verification-notes">Verification notes</a></aside><main id="main" tabindex="-1"><section class="instructions intro">'+render(read('intro.md'))+'</section><details class="comparison" id="comparison"><summary>Compare 39 add-ons: compatibility, effort, data and cost</summary><p>Only documented clients are listed. Estimates are planning aids, not measured setup times. Rows follow the current filters.</p><div class="table-scroll"><table><caption>Add-on selection matrix</caption><thead><tr><th>Add-on</th><th>Purpose</th><th>Documented environments</th><th>Effort / time</th><th>Processing</th><th>Accounts</th><th>Cost model</th></tr></thead><tbody>'+rows+'</tbody></table></div></details><p id="empty" class="empty" hidden>No matching add-ons. Try a shorter search or <button type="button" id="emptyReset">clear filters</button>.</p><div id="cards">'+cards+'</div><section class="instructions closing" id="documentation-and-verification-notes">'+render(read('closing.md'))+'</section><footer>By Gehan Fernando · <a href="https://gcfernando.github.io/developer-guides-and-tools/">Developer library</a> · <a href="https://gcfernando.github.io/developer-guides-and-tools/apps/linux-command-reference/">Linux reference</a></footer></main></div><p id="copyStatus" class="sr-only" role="status" aria-live="polite"></p><script>'+read('app.js')+'</script></body></html>\n';
const output=path.join(root,'index.html');
const compatibilityData=JSON.stringify(Object.fromEntries(guide.cards.map(c=>['card-'+c.id,Object.fromEntries(Object.entries(c.clients).map(([k,v])=>[k,v.status]))]))).replace(/</g,'\\u003c');
const outputPage=page.replace('<div id="cards">','<script type="application/json" id="compatibility-data">'+compatibilityData+'</script><div id="cards">');
if(process.argv.includes('--check')) {if(read('index.html')!==outputPage) throw new Error('index.html is stale. Run node build.cjs.');}
else fs.writeFileSync(output,outputPage);
console.log((process.argv.includes('--check')?'Verified':'Built')+' standalone reader: 39 add-ons.');
