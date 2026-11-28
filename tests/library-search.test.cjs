const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const {parseHTML} = require('linkedom');
const {searchRecords} = require('../assets/js/library-search.js');

const root = path.resolve(__dirname, '..');
const records = JSON.parse(fs.readFileSync(path.join(root, 'assets/data/library-search.json'), 'utf8'));
const layout = fs.readFileSync(path.join(root, '_layouts/default.html'), 'utf8');
const script = fs.readFileSync(path.join(root, 'assets/js/library-search.js'), 'utf8');
const base = '/developer-guides-and-tools';

function fixture() {
  // Exercise the actual search markup. This substitution supplies URLs only;
  // it is not a Liquid/Jekyll rendering or real-browser test.
  const panel = layout.match(/<details class="library-search"[\s\S]*?<\/details>/)[0]
    .replace(/\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}/g, (_, url) => base + url);
  return parseHTML('<html><body><a href="#library-search">Search library</a>' + panel + '</body></html>');
}

async function load(data = records, responseOK = true) {
  const {document, window} = fixture();
  const select = document.querySelector('[data-search-topic]');
  // Linkedom provides a select getter but no native-browser value setter.
  Object.defineProperty(select, 'value', {
    get() {return [...this.options].find(option => option.hasAttribute('selected'))?.value || '';},
    set(value) {for (const option of this.options) option.toggleAttribute('selected', option.value === value);}
  });
  const location = {href: 'https://example.test' + base + '/documentation/', hash: ''};
  const events = {};
  const requests = [];
  vm.runInNewContext(script, {
    document, location, URL, setTimeout, clearTimeout,
    addEventListener(name, action) {events[name] = action;},
    async fetch(url) {requests.push(String(url));return {ok: responseOK, async json() {return data;}};}
  });
  await new Promise(resolve => setImmediate(resolve));
  return {document, window, location, events, requests,
    input: document.querySelector('[data-search-input]'),
    form: document.querySelector('[data-search-form]'),
    topic: select,
    results: document.querySelector('[data-search-results]'),
    status: document.querySelector('[data-search-status]')};
}

function submit(ui, query) {
  ui.input.value = query;
  const event = new ui.window.Event('submit', {cancelable: true});
  ui.form.dispatchEvent(event);
  assert.equal(event.defaultPrevented, true, 'Submitting search must not reload the page.');
}

test('metadata search finds filenames, combined terms, topics and empty results', () => {
  assert(searchRecords(records, 'LEARNING-PATH').some(record => record.source.endsWith('LEARNING-PATH.md')));
  assert(searchRecords(records, 'sql performance').some(record => record.source.includes('10-performance')));
  const python = searchRecords(records, 'Python', 'Python');
  assert(python.length > 0);
  assert(python.every(record => record.topic === 'Python'));
  assert.deepEqual(searchRecords(records, 'no-such-resource-93741'), []);
});

test('every existing public route is searchable without indexing an excluded file', () => {
  const routes = JSON.parse(fs.readFileSync(path.join(root, '_data/routes.json'), 'utf8'));
  const config = require('yaml').parse(fs.readFileSync(path.join(root, '_config.yml'), 'utf8'));
  assert.equal(new Set(records.map(record => record.url)).size, records.length);
  for (const [source, route] of Object.entries(routes)) {
    if (config.exclude.some(item => source === item || source.startsWith(item + '/'))) continue;
    assert(records.some(record => record.url === base + route), source);
  }
  for (const record of records) {
    assert(!config.exclude.some(item => record.source === item || record.source.startsWith(item + '/')), record.source);
    assert(record.url.startsWith(base + '/'), record.url);
  }
});

test('search controls load same-site metadata, respond to typing and clear filters', async () => {
  const ui = await load();
  assert.equal(ui.form.hidden, false);
  assert.deepEqual(ui.requests, ['https://example.test' + base + '/assets/data/library-search.json']);
  assert.equal(ui.results.children.length, 0);
  ui.input.value = 'Python';
  ui.input.dispatchEvent(new ui.window.Event('input'));
  await new Promise(resolve => setTimeout(resolve, 180));
  assert(ui.results.querySelectorAll('a').length > 0);
  ui.topic.value = 'Python';
  ui.topic.dispatchEvent(new ui.window.Event('change'));
  assert([...ui.results.querySelectorAll('.search-result-meta')].every(node => node.textContent.startsWith('Python')));
  ui.form.dispatchEvent(new ui.window.Event('reset', {cancelable: true}));
  assert.equal(ui.input.value, '');
  assert.equal(ui.topic.value, '');
  assert.equal(ui.results.children.length, 0);
  assert.match(ui.status.textContent, /Enter words or choose a topic/);
});

test('search reports no matches and caps long results without hiding their total', async () => {
  const ui = await load();
  submit(ui, 'no-such-resource-93741');
  assert.equal(ui.results.children.length, 0);
  assert.match(ui.status.textContent, /No matches/);
  submit(ui, '');
  ui.topic.value = 'Data science and machine learning';
  ui.topic.dispatchEvent(new ui.window.Event('change'));
  const total = searchRecords(records, '', ui.topic.value).length;
  assert.equal(ui.results.children.length, Math.min(total, 20));
  assert.match(ui.status.textContent, new RegExp('^' + total + ' match'));
  const crowded = await load(Array.from({length: 27}, (_, index) => ({
    title: 'Demonstration ' + index, description: 'A matching resource', topic: 'Test',
    source: 'example-' + index + '.md', url: base + '/example-' + index + '/'
  })));
  submit(crowded, 'Demonstration');
  assert.equal(crowded.results.children.length, 20);
  assert.match(crowded.status.textContent, /^27 matches\. Showing the first 20/);
});

test('metadata cannot add external links, escape the site base or insert HTML', async () => {
  const item = {title: 'Safe <img src=x onerror=alert(1)>', description: '<script>bad()</script>', topic: 'Test', source: '<b>source.md</b>', type: 'Guide'};
  const ui = await load([
    {...item, url: base + '/documentation/'},
    {...item, url: 'https://elsewhere.invalid/'},
    {...item, url: 'javascript:alert(1)'},
    {...item, url: '/outside-the-library/'},
    null
  ]);
  submit(ui, 'Safe');
  assert.equal(ui.results.querySelectorAll('a').length, 1);
  assert.equal(ui.results.querySelectorAll('img, script, b').length, 0);
  assert.match(ui.results.textContent, /<img src=x onerror=alert\(1\)>/);
  assert.equal(ui.results.querySelector('a').getAttribute('href'), base + '/documentation/');
});

test('a failed metadata fetch keeps catalog and learning-path fallback links usable', async () => {
  const ui = await load([], false);
  assert.equal(ui.form.hidden, true);
  assert.match(ui.status.textContent, /Search could not load/);
  assert(ui.document.querySelector('a[href="' + base + '/documentation/"]'));
  assert(ui.document.querySelector('a[href="' + base + '/learning-paths/"]'));
});

test('without JavaScript, search explains its limit and supplies ordinary navigation', () => {
  const {document} = fixture();
  assert.equal(document.querySelector('[data-search-form]').hidden, true);
  assert.match(document.querySelector('noscript').textContent, /JavaScript/);
  assert(document.querySelector('a[href="' + base + '/documentation/"]'));
  assert(document.querySelector('a[href="' + base + '/learning-paths/"]'));
  assert(document.querySelector('summary').textContent.includes('Search this library'));
});

test('the shared search link opens its disclosure and fragment navigation also opens it', async () => {
  const ui = await load();
  ui.document.querySelector('a[href="#library-search"]').dispatchEvent(new ui.window.Event('click'));
  assert.equal(ui.document.querySelector('[data-library-search]').open, true);
  ui.document.querySelector('[data-library-search]').open = false;
  ui.location.hash = '#library-search';
  ui.events.hashchange();
  assert.equal(ui.document.querySelector('[data-library-search]').open, true);
});
