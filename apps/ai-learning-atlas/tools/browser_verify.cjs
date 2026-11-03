/* Browser verification infrastructure only; never loaded by the reader. */
'use strict';
const fs = require('node:fs');
const crypto = require('node:crypto');
const path = require('node:path');
const http = require('node:http');
const zlib = require('node:zlib');
const {pathToFileURL} = require('node:url');
const ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(ROOT, '../..');
const TOOLS = path.join(REPO, '.runtime/atlas-tools/node_modules');
const {chromium} = require(path.join(TOOLS, 'playwright'));
const args = process.argv.slice(2);
const arg = (name, fallback) => {const i = args.indexOf(name); return i < 0 ? fallback : args[i+1];};
const stage = arg('--stage', 'final');
const target = path.resolve(arg('--page', path.join(ROOT, 'index.html')));
const output = path.resolve(arg('--output', path.join(REPO, '.runtime', `atlas-browser-${stage}.json`)));
const baseline = JSON.parse(fs.readFileSync(path.join(__dirname, 'baseline.json'), 'utf8'));
const EDGE = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe';
const pageHash=()=>crypto.createHash('sha256').update(fs.readFileSync(target)).digest('hex');
const initialHash=pageHash();
const result = {page_sha256:initialHash,stage, target, transport:args.includes('--gzip')?'gzip when accepted':'uncompressed', checks: [], errors: [], unverified: [
  'No actual screen reader was driven; ARIA and keyboard observations are not a screen-reader test.',
  'Automated screenshots and print layout probes are not a complete human visual review.'
]};
function check(name, pass, details) {result.checks.push({name, pass: !!pass, details});}
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
async function restore(page, backup) {
  await page.locator('#progress-notice').evaluate(node => {node.textContent='';});
  await page.locator('#import-progress-file').setInputFiles({name:'backup.json', mimeType:'application/json', buffer:Buffer.from(JSON.stringify(backup))});
  await page.waitForFunction(() => /restored|Could not restore/i.test(document.getElementById('progress-notice').textContent));
  return page.locator('#progress-notice').textContent();
}
async function inspect(page, protocol) {
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', msg => {if(msg.type() === 'error') errors.push(msg.text());});
  page.on('dialog', dialog => dialog.accept());
  await page.goto(protocol === 'file' ? pathToFileURL(target).href : result.httpURL, {waitUntil:'load'});
  check(`${protocol}: console at initial load`, errors.length === 0, [...errors]);
  const initial = await page.evaluate(() => ({nodes:document.querySelectorAll('*').length, checks:document.querySelectorAll('.save-check').length,
    width:innerWidth, scrollWidth:document.documentElement.scrollWidth}));
  result[`${protocol}Initial`] = initial;
  for (const width of [360,768,1280,1600]) {
    await page.setViewportSize({width,height:900});
    await page.screenshot({path:path.join(path.dirname(output), `atlas-${stage}-${protocol}-${width}.png`), fullPage:false});
    const overflow = await page.evaluate(() => ({width:innerWidth,scrollWidth:document.documentElement.scrollWidth}));
    check(`${protocol}: viewport ${width} no horizontal overflow`, overflow.width === overflow.scrollWidth, overflow);
  }
  await page.setViewportSize({width:1280,height:900});
  const role = await page.locator('#role-home option').evaluateAll(options => options.find(o => o.value)?.value);
  await page.locator('#role-home').selectOption(role);
  const button = page.locator('[data-complete-topic="01"]');
  await button.click();
  check(`${protocol}: topic done toggles checkbox`, await page.locator('#complete-topic-01').isChecked());
  await page.reload({waitUntil:'load'});
  check(`${protocol}: role and progress persist on reload`, (await page.locator('#role-home').inputValue()) === role && await page.locator('#complete-topic-01').isChecked());
  const downloadPromise = page.waitForEvent('download');
  await page.locator('#download-progress').click();
  const download = await downloadPromise;
  const backup = JSON.parse(fs.readFileSync(await download.path(), 'utf8'));
  check(`${protocol}: export includes every original check`, baseline.progress_ids.every(id => typeof backup.checks[id] === 'boolean'), {version:backup.version,fields:Object.keys(backup.checks).length});
  await page.locator('#reset-progress').click();
  check(`${protocol}: clear progress`, !(await page.locator('#complete-topic-01').isChecked()));
  const imported = await restore(page, backup);
  check(`${protocol}: exported backup restores`, /Backup restored/.test(imported) && await page.locator('#complete-topic-01').isChecked(), imported);
  for (const version of [1,2]) {
    const fixture = JSON.parse(fs.readFileSync(path.join(__dirname, `backup-v${version}.json`), 'utf8'));
    const notice = await restore(page, fixture);
    check(`${protocol}: original v${version} backup restores`, /Backup restored/.test(notice) && await page.locator('#complete-topic-01').isChecked(), notice);
  }
  await page.keyboard.press('/');
  check(`${protocol}: slash shortcut focuses search`, await page.locator('#site-search').evaluate(el => el === document.activeElement));
  await page.keyboard.type('Python');
  await page.keyboard.press('ArrowDown');
  const searchState = await page.evaluate(() => ({focus:document.activeElement.id || document.activeElement.tagName,
    active:document.getElementById('site-search').getAttribute('aria-activedescendant'), expanded:document.getElementById('site-search').getAttribute('aria-expanded'),
    options:document.querySelectorAll('#search-results [role="option"]').length}));
  check(`${protocol}: search keyboard selects a result`, !!searchState.active || searchState.focus === 'A', searchState);
  await page.keyboard.press('Enter');
  await delay(100);
  check(`${protocol}: search Enter navigates`, (await page.evaluate(() => location.hash)).startsWith('#'));
  await page.locator('#site-search').focus();
  await page.keyboard.type('vector');
  await page.keyboard.press('Escape');
  check(`${protocol}: Escape closes search`, await page.locator('#search-results').isHidden());
  await page.goto((protocol === 'file' ? pathToFileURL(target).href : result.httpURL)+'#subtopic-51-020');
  await page.waitForTimeout(150);
  check(`${protocol}: lazy subtopic deep link resolves visibly`, await page.locator('#subtopic-51-020').isVisible());
  await page.goto(protocol === 'file' ? pathToFileURL(target).href : result.httpURL);
  await page.keyboard.press('Tab');
  const firstFocus = await page.evaluate(() => ({tag:document.activeElement.tagName,href:document.activeElement.getAttribute('href')}));
  check(`${protocol}: first tab is skip link`, firstFocus.href === '#main-content', firstFocus);
  await page.keyboard.press('Enter');
  check(`${protocol}: skip link focuses main`, await page.locator('#main-content').evaluate(el => el === document.activeElement));
  await page.setViewportSize({width:360,height:800});
  const menu = page.locator('#menu-btn');
  await menu.focus(); await page.keyboard.press('Enter');
  check(`${protocol}: keyboard menu opens`, await menu.getAttribute('aria-expanded') === 'true');
  await page.keyboard.press('Escape');
  check(`${protocol}: Escape closes menu and returns focus`, await menu.getAttribute('aria-expanded') === 'false' && await menu.evaluate(el => el === document.activeElement));
  await page.setViewportSize({width:1280,height:900});
  if(args.includes('--expanded-axe')) {
    await page.evaluate(() => {
      for(const section of document.querySelectorAll('main > .section'))section.style.contentVisibility='visible';
      for(const card of document.querySelectorAll('.topic-card')) window.AtlasExperience?.hydrate(card);
      for(const template of document.querySelectorAll('template[data-path-body]')) {template.parentElement.append(template.content);template.remove();}
      for(const list of document.querySelectorAll('.path-list')) list.dataset.showAll='true';
      const lessons=document.getElementById('lesson-focus');lessons.value='';lessons.dispatchEvent(new Event('change',{bubbles:true}));
      for(const details of document.querySelectorAll('main details')) details.open=true;
      for(const item of document.querySelectorAll('.path-item')) item.hidden=false;
    });
    result[`${protocol}AxeCoverage`]='All hydrated topic bodies, path details, lesson bodies and open main disclosures';
  } else result[`${protocol}AxeCoverage`]='Initially visible reader plus navigated states; closed disclosures excluded by axe';
  for (const theme of ['light','dark']) {
    await page.evaluate(theme => {document.documentElement.dataset.theme = theme;}, theme);
    await page.screenshot({path:path.join(path.dirname(output), `atlas-${stage}-${protocol}-${theme}.png`),fullPage:false});
    await page.addScriptTag({path:path.join(TOOLS,'axe-core/axe.min.js')});
    const axe = await page.evaluate(async () => {const r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa','wcag22aa']}});return {violations:r.violations.map(v=>({id:v.id,impact:v.impact,description:v.description,nodes:v.nodes.map(n=>({target:n.target,failureSummary:n.failureSummary}))})),incomplete:r.incomplete.map(v=>({id:v.id,nodes:v.nodes.length})),passes:r.passes.length};});
    result[`${protocol}Axe${theme}`] = axe;
    check(`${protocol}: ${theme} axe no serious/critical violations`, !axe.violations.some(v=>['serious','critical'].includes(v.impact)), axe.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.length})));
  }
  await page.emulateMedia({media:'print'});
  const print = await page.evaluate(() => ({sidebar:getComputedStyle(document.getElementById('sidebar')).display,
    lesson:getComputedStyle(document.getElementById('lesson-function')).display}));
  check(`${protocol}: print hides navigation and shows lessons`, print.sidebar === 'none' && print.lesson !== 'none', print);
  await page.emulateMedia({media:'screen',reducedMotion:'reduce'});
  const motion = await page.evaluate(() => getComputedStyle(document.documentElement).scrollBehavior);
  check(`${protocol}: reduced motion disables smooth scrolling`, motion === 'auto', motion);
  await page.emulateMedia({reducedMotion:'no-preference'});
  check(`${protocol}: console after interactions`, errors.length === 0, errors);
}

async function main() {
  fs.mkdirSync(path.dirname(output),{recursive:true});
  const server = http.createServer((req,res) => {
    if(req.url.split('?')[0] === '/favicon.ico') {res.writeHead(204);res.end();return;}
    const relative = decodeURIComponent(req.url.split('?')[0]);
    const file = relative === '/' || relative === '/index.html' ? target : path.resolve(path.dirname(target),'.'+relative);
    if(!file.startsWith(path.dirname(target))) {res.writeHead(403);res.end();return;}
    fs.readFile(file,(error,data)=>{
      if(error){res.writeHead(404);res.end();return;}
      res.setHeader('Content-Type',file.endsWith('.html')?'text/html; charset=utf-8':'text/plain');
      if(args.includes('--gzip')&&/\bgzip\b/.test(req.headers['accept-encoding']||'')) {
        res.setHeader('Content-Encoding','gzip');res.setHeader('Vary','Accept-Encoding');res.end(zlib.gzipSync(data));
      } else res.end(data);
    });
  });
  await new Promise(resolve => server.listen(0,'127.0.0.1',resolve));
  result.httpURL = `http://127.0.0.1:${server.address().port}/index.html`;
  let browser;
  try {
    browser = await chromium.launch({executablePath:EDGE,headless:true});
    for (const protocol of (args.includes('--lighthouse-only') ? [] : ['file','http'])) {
      const context = await browser.newContext({viewport:{width:360,height:800},acceptDownloads:true});
      const page = await context.newPage();
      try {await inspect(page,protocol);} catch(error) {result.errors.push(`${protocol}: ${error.stack}`);}
      await context.close();
    }
    if(args.includes('--lighthouse')) {
      const chromeLauncher = await import(pathToFileURL(path.join(TOOLS,'chrome-launcher/dist/index.js')).href);
      const lighthouse = (await import(pathToFileURL(path.join(TOOLS,'lighthouse/core/index.js')).href)).default;
      const chrome = await chromeLauncher.launch({chromePath:EDGE,chromeFlags:['--headless','--no-first-run']});
      try {
        const run = await lighthouse(result.httpURL,{port:chrome.port,output:'json',logLevel:'error',onlyCategories:['performance','accessibility'],formFactor:'mobile'});
        result.lighthouse = {performance:run.lhr.categories.performance.score*100,accessibility:run.lhr.categories.accessibility.score*100,
          config:run.lhr.configSettings,dom:run.lhr.audits['dom-size'],metrics:run.lhr.audits.metrics.details.items[0],warnings:run.lhr.runWarnings};
        fs.writeFileSync(output.replace(/\.json$/,'.lighthouse.json'),JSON.stringify(run.lhr,null,2));
        if(['baseline','ws1','ws2','ws3','ws4'].includes(stage)) {
          result.lighthouse.targetStatus=`Measured ${result.lighthouse.performance}; the >=90 aim is evaluated after WS5 performance changes.`;
        } else check('mobile Lighthouse performance at least 90',result.lighthouse.performance>=90,result.lighthouse.performance);
      } finally {await chrome.kill();}
    }
  } finally {if(browser)await browser.close();server.close();}
  check('page source unchanged during verification',pageHash()===initialHash);
  fs.writeFileSync(output,JSON.stringify(result,null,2));
  console.log(JSON.stringify({stage,passed:result.checks.filter(c=>c.pass).length,failed:result.checks.filter(c=>!c.pass),errors:result.errors,
    fileInitial:result.fileInitial,httpInitial:result.httpInitial,lighthouse:result.lighthouse&&{performance:result.lighthouse.performance,accessibility:result.lighthouse.accessibility},output},null,2));
  process.exitCode = result.errors.length || result.checks.some(c=>!c.pass) ? 1 : 0;
}
main().catch(error=>{console.error(error);process.exitCode=1;});
