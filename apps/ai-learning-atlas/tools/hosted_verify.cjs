const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {createReaderServer, waitForReader} = require('./browser_support.cjs');
const repo = path.resolve(__dirname, '../../..');
const {chromium} = require(path.join(repo, '.runtime/atlas-tools/node_modules/playwright'));
const target = path.join(repo, '.runtime/atlas-hosted/index.html');
const report = {checks: []};
async function check(name, work) {
  try { await work(); report.checks.push({name, pass: true}); }
  catch (error) { report.checks.push({name, pass: false, error: error.stack}); }
}
(async () => {
  const server = createReaderServer(target, true);
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  try {
    browser = await chromium.launch({executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', headless: true});
    report.browser = {name: 'Microsoft Edge', version: await browser.version()};
    const base = `http://127.0.0.1:${server.address().port}`;
    await check('published offline download matches the original HTML', async () => {
      const response = await fetch(base + '/offline.html');
      assert.equal(response.status, 200);
      assert.deepEqual(Buffer.from(await response.arrayBuffer()), fs.readFileSync(path.join(repo, 'apps/ai-learning-atlas/index.html')));
    });
    await check('hosted reader restores existing same-origin progress, role and note', async () => {
      const context = await browser.newContext();
      try {
        const page = await context.newPage();
        await page.goto(base + '/offline.html');
        await page.locator('#role-home').selectOption('backend-software-engineer');
        await page.locator('[data-complete-topic="01"]').click();
        await page.evaluate(() => { location.hash = '#' + document.getElementById('study-note').closest('.section').id; });
        await page.locator('#study-note').fill('Hosted migration test note');
        await page.goto(base + '/index.html');
        await waitForReader(page);
        assert.equal(await page.locator('#role-home').inputValue(), 'backend-software-engineer');
        assert.ok(await page.locator('#complete-topic-01').isChecked());
        assert.equal(await page.locator('#study-note').inputValue(), 'Hosted migration test note');
        assert.equal(await page.locator('.save-check').count(), 514);
      } finally { await context.close(); }
    });
    await check('content failures are explicit and Retry restores the complete reader', async () => {
      const context = await browser.newContext();
      try {
        await context.route('**/reader-assets/content.*.json', route => route.fulfill({status: 503, body: 'Unavailable'}));
        const page = await context.newPage();
        await page.goto(base + '/index.html');
        await page.waitForFunction(() => document.documentElement.dataset.atlasReady === 'error');
        assert.match(await page.locator('#atlas-load-status').textContent(), /HTTP 503/);
        assert.ok(await page.locator('.shell').evaluate(node => node.inert));
        await context.unroute('**/reader-assets/content.*.json');
        await Promise.all([page.waitForEvent('load'), page.locator('#atlas-load-status button').click()]);
        await waitForReader(page);
        assert.equal(await page.locator('.save-check').count(), 514);
        assert.ok(!await page.locator('.shell').evaluate(node => node.inert));
      } finally { await context.close(); }
    });
  } finally {
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
  const output = path.join(repo, 'artifacts/edge-tests/hosted-recovery.json');
  fs.mkdirSync(path.dirname(output), {recursive: true});
  fs.writeFileSync(output, JSON.stringify(report, null, 2));
  console.log(JSON.stringify(report, null, 2));
  process.exitCode = report.checks.some(check => !check.pass) ? 1 : 0;
})().catch(error => {console.error(error); process.exitCode = 1;});
