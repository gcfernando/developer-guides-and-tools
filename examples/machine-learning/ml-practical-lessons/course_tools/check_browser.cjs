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
const events = {};
const tableRegion = {clientWidth:300,scrollWidth:300,tabIndex:-1,attributes:{},
  setAttribute(name,value){this.attributes[name]=value;},
  removeAttribute(name){delete this.attributes[name];if(name==='tabindex')this.tabIndex=-1;},
};
const document = {
  addEventListener(name,action) {events['document:'+name]=action;},
  documentElement: { dataset: {}, scrollHeight: 2000 },
  getElementById(id) {
    return { theme, 'lesson-search': search, 'lesson-track': track, 'search-status': status }[id];
  },
  querySelectorAll(query) {
    if (query === 'tr[data-track]') return rows;
    if (query === 'input[data-course-check]') return [box];
    if (query === '.table-frame') return [tableRegion];
    return [];
  },
  querySelector() { return progress; },
};
const context = {
  requestAnimationFrame(action) {action();return 1;},
  cancelAnimationFrame() {},
  document,
  localStorage: { getItem(k) { return storage.get(k); }, setItem(k, v) { storage.set(k, v); } },
  location: { pathname: '/LEARNING-PATH.html' },
  matchMedia() { return { matches: false }; },
  addEventListener(name,action) {events[name]=action;}, innerHeight: 800, scrollY: 0,
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
assert.equal(tableRegion.tabIndex,-1,'A table that fits should not add a keyboard stop.');
tableRegion.scrollWidth=600;events.resize();assert.equal(tableRegion.tabIndex,0);
tableRegion.scrollWidth=300;events.resize();assert.equal(tableRegion.tabIndex,-1);
const pathPage=fs.readFileSync(path.join(__dirname,'..','LEARNING-PATH.html'),'utf8');
const labels=[...pathPage.matchAll(/aria-label="(Mark complete:[^"]+)"/g)].map(match=>match[1]);
assert.equal(labels.length,15);assert.equal(new Set(labels).size,labels.length);
assert.match(page,/data-close-visual/);
console.log('Page controls passed: search, track, saved progress, theme, overflow-only table focus, distinct progress names and figure dialog markup.');
