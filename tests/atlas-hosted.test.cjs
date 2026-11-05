const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {ROOT} = require('../scripts/lib.cjs');
const {parseDocument} = require('../scripts/link-utils.cjs');
const {hostedFiles, expandHosted} = require('../scripts/build-atlas-hosted.cjs');

const source = fs.readFileSync(path.join(ROOT, 'apps/ai-learning-atlas/index.html'));
const files = hostedFiles(source);
const shell = parseDocument(files['index.html'], false);
const loader = shell.document.querySelector('script[data-atlas-content]');
const payload = JSON.parse(files[loader.getAttribute('data-atlas-content')]);

test('hosted Atlas preserves the complete standalone download byte-for-byte', () => {
  assert.deepEqual(files['offline.html'], source);
  assert.ok(Buffer.byteLength(files['index.html']) < source.length / 20);
  assert.ok(shell.document.querySelector('.shell').hasAttribute('inert'));
  assert.ok(shell.document.querySelector('noscript a[href="offline.html"]'));
  for (const node of shell.document.querySelectorAll('script[src],link[rel="stylesheet"]')) {
    assert.ok(files[node.getAttribute('src') || node.getAttribute('href')]);
  }
  assert.ok(files[loader.getAttribute('data-atlas-runtime')]);
});

test('hosted payload retains every anchor, example and learning-data record', () => {
  const original = parseDocument(source.toString(), false);
  const hosted = parseDocument(expandHosted(files['index.html'], payload), false);
  for (const id of original.anchors) assert.ok(hosted.anchors.has(id), id);
  const code = doc => [...doc.document.querySelectorAll('pre')].map(node => node.textContent);
  assert.deepEqual(code(hosted), code(original));
  assert.equal(hosted.document.getElementById('atlas-data').textContent,
    original.document.getElementById('atlas-data').textContent);
  const controls = doc => [...doc.document.querySelectorAll('.save-check')].map(node => node.id);
  assert.deepEqual(controls(hosted), controls(original));
  assert.equal(hosted.document.querySelector('link[rel="canonical"]').href,
    original.document.querySelector('link[rel="canonical"]').href);
});

test('hosted expansion rejects missing, malformed and out-of-order fragments', () => {
  assert.throws(() => expandHosted(files['index.html'], payload.slice(1)), /count/);
  assert.throws(() => expandHosted(files['index.html'], [null, ...payload.slice(1)]), /Invalid/);
  assert.throws(() => expandHosted(files['index.html'].replace('data-atlas-fragment="0"', 'data-atlas-fragment="99"'), payload), /order/);
});

test('published site commands and both workflows prepare the hosted reader before validation', () => {
  const scripts = JSON.parse(fs.readFileSync(path.join(ROOT, 'package.json'), 'utf8')).scripts;
  assert.equal(scripts['site:build'], 'bundle exec jekyll build && node scripts/build-atlas-hosted.cjs --site');
  for (const name of ['pages.yml', 'validate.yml']) {
    const workflow = fs.readFileSync(path.join(ROOT, '.github/workflows', name), 'utf8');
    assert.ok(workflow.indexOf('npm run site:build') < workflow.indexOf('npm run check:site'));
    assert.ok(workflow.includes('npm run site:build'));
  }
});
