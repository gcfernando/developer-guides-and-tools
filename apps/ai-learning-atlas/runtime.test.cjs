// Behavioral checks for restore compatibility, storage failures and lesson state.
// Uses the repository's existing linkedom dependency; no browser is required.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const {parseHTML} = require('linkedom');

function reader() {
  const {document, Event} = parseHTML(fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8'));
  // linkedom does not implement browser select value/selectedIndex behavior.
  for (const select of document.querySelectorAll('select')) {
    Object.defineProperty(select, 'value', {get() {return this._value || '';}, set(value) {this._value = value;}});
    Object.defineProperty(select, 'selectedIndex', {get() {return [...this.options].findIndex(o => o.value === this.value);}});
  }
  const values = new Map();
  const blobs = [];
  let blocked = false;
  const localStorage = {
    getItem(key) {if (blocked) throw Error('Storage blocked'); return values.get(key) ?? null;},
    setItem(key, value) {if (blocked) throw Error('Storage blocked'); values.set(key, String(value));},
    removeItem(key) {if (blocked) throw Error('Storage blocked'); values.delete(key);}
  };
  const context = vm.createContext({
    document, Event, localStorage, console, Blob, navigator: {}, confirm: () => true,
    location: {hash: ''},
    URL: {createObjectURL(blob) {blobs.push(blob); return 'blob:fixture';}, revokeObjectURL() {}},
    setTimeout: () => 0, clearTimeout() {},
    window: {isSecureContext: false, location: {hash: ''}, addEventListener() {},
      matchMedia: () => ({matches: false, addEventListener() {}})}
  });
  for (const script of document.querySelectorAll('script:not([type])')) {
    new vm.Script(script.textContent).runInContext(context);
  }
  const fire = (node, type) => node.dispatchEvent(new Event(type, {bubbles: true}));
  const restore = async data => {
    const input = document.getElementById('import-progress-file');
    input.files = [{size: Buffer.byteLength(JSON.stringify(data)), text: async () => JSON.stringify(data)}];
    fire(input, 'change');
    await new Promise(resolve => setImmediate(resolve));
  };
  const state = () => ({version: 2, selectedRole: '', note: '', checks: Object.fromEntries(
    [...document.querySelectorAll('.save-check')].map(c => [c.id, !!c.checked]))});
  return {document, fire, restore, state, blobs, values, block() {blocked = true;}};
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
