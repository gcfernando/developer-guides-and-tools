// Check the page controls without needing a browser or extra Node packages.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');

function element(value = '') {
  return {
    value, dataset: {}, style: {}, handlers: {},
    addEventListener(name, action) { this.handlers[name] = action; },
  };
}

const theme = element(), search = element(), track = element();
const status = element(), box = element(), progress = element();
const rows = [
  { dataset: { track: 'Core' }, textContent: '032 Missing values' },
  { dataset: { track: 'Practice' }, textContent: 'Extra patterns' },
];
const storage = new Map();
const document = {
  documentElement: { dataset: {}, scrollHeight: 2000 },
  getElementById(id) {
    return { theme, 'lesson-search': search, 'lesson-track': track, 'search-status': status }[id];
  },
  querySelectorAll(query) {
    if (query === 'tr[data-track]') return rows;
    if (query === 'input[data-course-check]') return [box];
    return [];
  },
  querySelector() { return progress; },
};
const context = {
  document,
  localStorage: { getItem(k) { return storage.get(k); }, setItem(k, v) { storage.set(k, v); } },
  location: { pathname: '/LEARNING-PATH.html' },
  matchMedia() { return { matches: false }; },
  addEventListener() {}, innerHeight: 800, scrollY: 0,
};

const page = fs.readFileSync(path.join(__dirname, '..', 'Data-Science-and-Machine-Learning.html'), 'utf8');
const scripts = [...page.matchAll(/<script>([\s\S]*?)<\/script>/g)];
assert.equal(scripts.length, 1);
vm.runInNewContext(scripts[0][1], context);
search.value = 'missing values';
search.handlers.input();
assert.equal(rows[0].hidden, false);
assert.equal(rows[1].hidden, true);
track.value = 'Practice';
track.handlers.change();
assert.equal(rows[0].hidden, true);
assert.match(status.textContent, /0 matching/);
box.checked = true;
box.handlers.change();
assert.equal(storage.get('ml-course-check:/LEARNING-PATH.html:0'), 'yes');
theme.handlers.click();
assert.equal(document.documentElement.dataset.theme, 'dark');
console.log('Page controls passed: multi-word search, track choice, saved progress and theme.');
