// Behavioral checks for restore compatibility, storage failures and lesson state.
// Uses the repository's existing linkedom dependency; no browser is required.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const {parseHTML} = require('linkedom');

function reader() {
  const {document, Event, CustomEvent} = parseHTML(fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8'));
  // linkedom does not implement browser select value/selectedIndex behavior.
  // Define the shim on the prototype to cover selects built by experience.js too.
  const selectPrototype = Object.getPrototypeOf(document.createElement('select'));
  Object.defineProperty(selectPrototype, 'value', {configurable:true, get() {return this._value ?? this.options[0]?.value ?? '';}, set(value) {this._value = value;}});
  Object.defineProperty(selectPrototype, 'selectedIndex', {configurable:true, get() {return [...this.options].findIndex(o => o.value === this.value);}});
  const values = new Map();
  const blobs = [];
  let blocked = false;
  const localStorage = {
    getItem(key) {if (blocked) throw Error('Storage blocked'); return values.get(key) ?? null;},
    setItem(key, value) {if (blocked) throw Error('Storage blocked'); values.set(key, String(value));},
    removeItem(key) {if (blocked) throw Error('Storage blocked'); values.delete(key);}
  };
  const windowEvents = new Map();
  const browserWindow = {isSecureContext: false, location: {hash: ''},
    addEventListener(type, handler) {windowEvents.set(type, [...(windowEvents.get(type)||[]), handler]);},
    matchMedia: () => ({matches: false, addEventListener() {}})};
  const context = vm.createContext({
    document, Event, CustomEvent, localStorage, console, Blob, navigator: {}, confirm: () => true,
    location: {hash: ''},
    URL: {createObjectURL(blob) {blobs.push(blob); return 'blob:fixture';}, revokeObjectURL() {}},
    setTimeout: () => 0, clearTimeout() {},
    requestAnimationFrame: () => 0,
    window: browserWindow
  });
  for (const script of document.querySelectorAll('script:not([type])')) {
    new vm.Script(script.textContent).runInContext(context);
  }
  const fire = (node, type, properties={}) => {
    const event = new Event(type, {bubbles: true, cancelable:true});
    Object.assign(event, properties);
    return node.dispatchEvent(event);
  };
  const restore = async data => {
    const input = document.getElementById('import-progress-file');
    input.files = [{size: Buffer.byteLength(JSON.stringify(data)), text: async () => JSON.stringify(data)}];
    fire(input, 'change');
    await new Promise(resolve => setImmediate(resolve));
  };
  const state = () => ({version: 2, selectedRole: '', note: '', checks: Object.fromEntries(
    [...document.querySelectorAll('.save-check')].map(c => [c.id, !!c.checked]))});
  return {document, fire, restore, state, blobs, values, window:browserWindow,
    emitWindow(type) {for (const handler of windowEvents.get(type)||[]) handler(new Event(type));},
    block() {blocked = true;}};
}

test('legacy backups restore original checks and default new lesson/unit checks to false', async () => {
  const r = reader();
  const backup = r.state();
  backup.version = 1;
  delete backup.note;
  for (const id of Object.keys(backup.checks)) if (!/^(complete-topic-|milestone-)/.test(id)) delete backup.checks[id];
  backup.checks['complete-topic-01'] = true;
  await r.restore(backup);
  assert.equal(r.document.getElementById('complete-topic-01').checked, true);
  assert.equal(r.document.getElementById('lesson-setup-practice').checked, false);
  assert.match(r.document.getElementById('progress-notice').textContent, /Backup restored/);
});

test('v2 backup round trip preserves lesson checks, note and an intentionally empty role', async () => {
  const r = reader();
  const backup = r.state();
  backup.note = 'Synthetic evidence: permission test passed.';
  backup.checks['lesson-function-practice'] = true;
  await r.restore(backup);
  assert.equal(r.document.getElementById('study-note').value, backup.note);
  assert.equal(r.document.getElementById('role-home').value, '');
  assert.match(r.document.getElementById('lesson-counter').textContent, /^1 of 8/);
  assert.equal(r.document.getElementById('complete-topic-03').checked, false);
  assert.match(r.document.getElementById('check-counter').textContent, /Topic scopes: 0 of 51.*Unit checks: 0 of 438.*Workshop lesson checks: 1 of 16.*Milestones: 0 of 9/);
  r.fire(r.document.getElementById('download-progress'), 'click');
  const exported = JSON.parse(await r.blobs[0].text());
  assert.equal(exported.note, backup.note);
  assert.equal(exported.checks['lesson-function-practice'], true);
  assert.equal(exported.selectedRole, '');
});

test('invalid backup fails before changing current checks or notes', async () => {
  const r = reader();
  const original = r.document.getElementById('complete-topic-01');
  original.checked = true;
  const backup = r.state();
  backup.checks['complete-topic-01'] = false;
  delete backup.checks['lesson-function-transfer'];
  await r.restore(backup);
  assert.equal(original.checked, true);
  assert.match(r.document.getElementById('progress-notice').textContent, /Could not restore/);
});

test('blocked storage is reported as session-only after restoration', async () => {
  const r = reader();
  r.block();
  await r.restore(r.state());
  assert.match(r.document.getElementById('progress-notice').textContent, /session only/);
});

test('export refuses notes which cannot pass the restore size limits', () => {
  const r = reader();
  r.document.getElementById('study-note').value = 'x'.repeat(50001);
  r.fire(r.document.getElementById('download-progress'), 'click');
  assert.equal(r.blobs.length, 0);
  assert.match(r.document.getElementById('progress-notice').textContent, /restore limit/);
  // JSON escaping can exceed byte limits even below the character limit.
  r.document.getElementById('study-note').value = '\u0001'.repeat(49000);
  r.fire(r.document.getElementById('download-progress'), 'click');
  assert.equal(r.blobs.length, 0);
});

test('lesson view can reveal a destination hidden by focus mode', () => {
  const r = reader();
  assert.equal(r.document.getElementById('lesson-function').hidden, true);
  const link = r.document.querySelector('a[href="#lesson-function"]');
  r.fire(link, 'click');
  assert.equal(r.document.getElementById('lesson-function').hidden, false);
  assert.equal(r.document.getElementById('lesson-setup').hidden, true);
});

test('combobox arrows expose the selected option and Escape clears active state', () => {
  const r = reader();
  const field = r.document.getElementById('site-search');
  field.value = 'Python';
  r.fire(field, 'input');
  assert.equal(field.getAttribute('aria-expanded'), 'true');
  r.fire(field, 'keydown', {key:'ArrowDown'});
  const first = field.getAttribute('aria-activedescendant');
  assert.ok(first);
  assert.equal(r.document.getElementById(first).getAttribute('role'), 'option');
  assert.equal(r.document.getElementById(first).getAttribute('aria-selected'), 'true');
  r.fire(field, 'keydown', {key:'ArrowDown'});
  assert.notEqual(field.getAttribute('aria-activedescendant'), first);
  assert.equal(r.document.getElementById(first).getAttribute('aria-selected'), 'false');
  r.fire(field, 'keydown', {key:'Escape'});
  assert.equal(field.getAttribute('aria-expanded'), 'false');
  assert.equal(field.hasAttribute('aria-activedescendant'), false);
  assert.equal(r.document.getElementById('search-results').hidden, true);
});

test('topic toggle retains its accessible name across pressed states', () => {
  const r = reader();
  const button = r.document.querySelector('[data-complete-topic="05"]');
  const name = button.getAttribute('aria-label');
  assert.equal(name, 'Topic 05 scope done');
  r.fire(button, 'click');
  assert.equal(button.getAttribute('aria-label'), name);
  assert.equal(button.getAttribute('aria-pressed'), 'true');
  r.fire(button, 'click');
  assert.equal(button.getAttribute('aria-label'), name);
  assert.equal(button.getAttribute('aria-pressed'), 'false');
});

test('v2 restore preserves unopened unit checks through lazy hydration', async t => {
  const r = reader();
  assert.ok(r.window.AtlasExperience, 'Lazy reader is required');
  const card = r.document.querySelector('.topic-card');
  assert.ok(card.querySelector('template[data-topic-body]'));
  const backup = JSON.parse(fs.readFileSync(path.join(__dirname,'fixtures/backup-v2.json'),'utf8'));
  backup.checks['unit-01-01-practice'] = true;
  await r.restore(backup);
  const check = r.document.getElementById('unit-01-01-practice');
  assert.equal(check.checked, true);
  r.window.AtlasExperience.hydrate(card);
  assert.equal(r.document.getElementById(check.id), check, 'Hydration moves the same prebound input');
  assert.equal(check.checked, true);
  assert.equal(check.closest('.study-unit').id, 'unit-01-01');
  r.fire(r.document.getElementById('download-progress'), 'click');
  assert.equal(JSON.parse(await r.blobs[0].text()).checks[check.id], true);
});

test('lazy unit deep link reveals its topic and all ancestor disclosures', t => {
  const r = reader();
  assert.ok(r.window.AtlasExperience, 'Lazy reader is required');
  const target = r.window.AtlasExperience.reveal('#unit-51-01', {scroll:false});
  assert.ok(target);
  assert.equal(target.id, 'unit-51-01');
  assert.equal(target.open, true);
  assert.equal(target.closest('.topic-card').hidden, false);
  assert.equal(target.closest('.topic-details').open, true);
});

test('Blob downloads contain the exact inline reference text', async t => {
  const r = reader();
  const button = r.document.querySelector('[data-download][data-code]');
  assert.ok(button, 'Embedded workshop Blob downloads are required');
  const expected = r.document.getElementById(button.dataset.code).textContent;
  r.fire(button, 'click');
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(r.blobs.length, 1);
  assert.equal(await r.blobs[0].text(), expected);
});
