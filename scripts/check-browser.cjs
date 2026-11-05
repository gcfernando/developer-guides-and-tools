const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const {pathToFileURL} = require('node:url');
const {ROOT} = require('./lib.cjs');
const {chromium} = require(path.join(ROOT, '.runtime/atlas-tools/node_modules/playwright'));

const edge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const output = path.join(ROOT, 'artifacts/edge-tests/library-browser.json');
const result = {checks: [], errors: [], scope: 'Local Linux and add-ons HTML apps, file/offline and loopback HTTP. No personal browser profile or system clipboard is used.'};
let browser;
let server;
async function check(name, work) {
  try {
    const details = await work();
    result.checks.push({name, pass: true, details});
  } catch (error) {
    result.checks.push({name, pass: false, error: error.stack});
  }
}

async function inspect(app, protocol, base) {
  const context = await browser.newContext({viewport: {width: 1280, height: 900}, offline: protocol === 'file'});
  try {
    const page = await context.newPage();
    page.setDefaultTimeout(10000);
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    const localRequest = url => url.startsWith('file:') || url.startsWith(base + '/');
    page.on('requestfailed', request => {
      if (localRequest(request.url())) errors.push(`${request.url()}: ${request.failure()?.errorText}`);
    });
    page.on('response', response => {
      if (localRequest(response.url()) && response.status() >= 400) errors.push(`${response.url()}: HTTP ${response.status()}`);
    });
    const file = `apps/${app}/index.html`;
    await page.goto(protocol === 'file' ? pathToFileURL(path.join(ROOT, file)).href : base + '/' + file, {waitUntil: 'load'});
    const label = `${app} ${protocol}`;
    if (app === 'linux-command-reference') {
      await check(`${label}: complete command table and category menu`, async () => {
        assert.equal(await page.locator('#tableBody tr').count(), 361);
        assert.equal(await page.locator('#catFilter option').count(), 17);
        assert.equal(await page.locator('#totalCount').textContent(), '361');
      });
      await check(`${label}: literal search and category filters`, async () => {
        for (const query of ['ssh', '[', '__no_such_command_742__']) {
          await page.locator('#searchInput').fill(query);
          const expected = await page.evaluate(q => COMMANDS.filter(row => row.join(' ').toLowerCase().includes(q)).length, query);
          assert.equal(await page.locator('#tableBody tr').count(), expected);
        }
        await page.locator('#searchInput').fill('');
        await page.locator('#catFilter').selectOption('Networking');
        const expected = await page.evaluate(() => COMMANDS.filter(row => row[1] === 'Networking').length);
        assert.equal(await page.locator('#tableBody tr').count(), expected);
        await page.locator('#catFilter').selectOption('');
        assert.equal(await page.locator('#tableBody tr').count(), 361);
      });
      await check(`${label}: stylesheet is loaded locally`, async () => {
        assert.ok(await page.evaluate(() => [...document.styleSheets].some(sheet => sheet.href?.includes('styles.css'))));
      });
    } else {
      await check(`${label}: complete generated add-ons and all navigation anchors`, async () => {
        assert.equal(await page.locator('.tool-card').count(), 39);
        const broken = await page.evaluate(() => [...document.querySelectorAll('a[href^="#"]')]
          .map(a => a.getAttribute('href')).filter(href => !document.getElementById(decodeURIComponent(href.slice(1)))));
        assert.deepEqual(broken, []);
        await page.locator('.nav a').first().click();
        assert.ok(new URL(page.url()).hash.startsWith('#card-'));
      });
      await check(`${label}: search, no-results and client filters`, async () => {
        await page.locator('#query').fill('sonarqube');
        const visible = await page.locator('.tool-card:not(.none)').count();
        assert.ok(visible > 0 && visible < 39);
        await page.locator('#query').fill('__no_such_addon_742__');
        assert.equal(await page.locator('.tool-card:not(.none)').count(), 0);
        assert.equal(await page.locator('#count').textContent(), '0 add-ons shown');
        await page.locator('#query').fill('');
        await page.locator('#clientFilter').selectOption('Codex CLI');
        assert.ok(await page.locator('.tool-card h3').filter({hasText: 'Claude Code CLI'}).first().isHidden());
        assert.ok(await page.locator('.tool-card h3').filter({hasText: 'Codex CLI'}).first().isVisible());
        await page.locator('#clientFilter').selectOption('all');
      });
      await check(`${label}: theme control`, async () => {
        await page.locator('#theme').click();
        assert.ok(await page.locator('body').evaluate(node => node.classList.contains('dark')));
        await page.locator('#theme').click();
        assert.ok(!await page.locator('body').evaluate(node => node.classList.contains('dark')));
      });
      await check(`${label}: sibling Linux navigation`, async () => {
        const current = page.url();
        try {
          await page.locator('footer a').filter({hasText: 'Linux reference'}).click();
          await page.waitForSelector('#tableBody tr');
          assert.equal(await page.locator('#tableBody tr').count(), 361);
        } finally {
          await page.goto(current, {waitUntil: 'load'});
        }
      });
    }
    for (const width of [360, 768, 1280]) {
      await check(`${label}: responsive layout at ${width}px`, async () => {
        await page.setViewportSize({width, height: 900});
        const dimensions = await page.evaluate(() => ({viewport: document.documentElement.clientWidth, document: document.documentElement.scrollWidth}));
        assert.ok(dimensions.document <= dimensions.viewport, JSON.stringify(dimensions));
        await page.screenshot({path: path.join(path.dirname(output), `${app}-${protocol}-${width}.png`)});
        return dimensions;
      });
    }
    await check(`${label}: no JavaScript exceptions or failed local assets`, async () => assert.deepEqual(errors, []));
  } finally {
    await context.close();
  }
}

async function main() {
  if (!fs.existsSync(edge)) throw new Error(`Microsoft Edge is not installed at ${edge}`);
  fs.mkdirSync(path.dirname(output), {recursive: true});
  server = http.createServer((req, res) => {
    const pathname = decodeURIComponent(new URL(req.url, 'http://127.0.0.1').pathname);
    if (pathname === '/favicon.ico') {res.writeHead(204); res.end(); return;}
    const file = path.resolve(ROOT, '.' + pathname, ...(pathname.endsWith('/') ? ['index.html'] : []));
    if (!file.startsWith(path.join(ROOT, 'apps') + path.sep) || !/\.(html|css|js)$/.test(file)) {
      res.writeHead(404); res.end(); return;
    }
    fs.readFile(file, (error, body) => {
      if (error) {res.writeHead(404); res.end(); return;}
      res.setHeader('Content-Type', file.endsWith('.html') ? 'text/html; charset=utf-8' : file.endsWith('.css') ? 'text/css' : 'text/javascript');
      res.end(body);
    });
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  try {
    browser = await chromium.launch({executablePath: edge, headless: !process.argv.includes('--headed')});
    result.browser = {name: 'Microsoft Edge', version: await browser.version(), executable: edge};
    for (const app of ['linux-command-reference', 'ai-coding-addons']) {
      for (const protocol of ['file', 'http']) {
        try {
          await inspect(app, protocol, `http://127.0.0.1:${server.address().port}`);
        } catch (error) {
          result.errors.push({app, protocol, error: error.stack});
        }
      }
    }
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
  fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
  const failures = result.checks.filter(item => !item.pass);
  console.log(JSON.stringify({browser: result.browser, passed: result.checks.length - failures.length, failures, errors: result.errors, output}, null, 2));
  process.exitCode = failures.length || result.errors.length ? 1 : 0;
}
main().catch(error => {console.error(error); process.exitCode = 1;});
