// Compare the built site with an explicitly captured set of existing public URLs/IDs.
// The input is evidence from before a change, not a regenerated expected result.
const fs = require('node:fs');
const path = require('node:path');
const {parseHTML} = require('linkedom');
const {ROOT} = require('./lib.cjs');
const baseline = process.argv[2];
if (!baseline) throw new Error('Pass a pre-change public navigation baseline JSON file.');
const record = JSON.parse(fs.readFileSync(path.resolve(ROOT, baseline), 'utf8'));
const site = path.resolve(ROOT, '_site');
const errors = [];
let anchors = 0;
for (const page of record.pages) {
  const name = page.path.replace(/^\//, '') + (page.path.endsWith('/') ? 'index.html' : '');
  const target = path.resolve(site, name);
  if (!target.startsWith(site + path.sep)) throw new Error('Baseline path escapes built site.');
  if (!fs.existsSync(target)) {errors.push('Existing public page missing: ' + page.path);continue;}
  const {document} = parseHTML(fs.readFileSync(target, 'utf8'));
  const ids = new Set([...document.querySelectorAll('[id], a[name]')].flatMap(element =>
    [element.getAttribute('id'), element.localName === 'a' && element.getAttribute('name')].filter(Boolean)));
  for (const id of page.ids) {
    anchors++;
    if (!ids.has(id)) errors.push(`Existing anchor missing: ${page.path}#${id}`);
  }
}
if (errors.length) {console.error(errors.join('\n'));process.exitCode = 1;}
else console.log(`PASS: ${record.pages.length} pre-change public URLs and ${anchors} anchors preserved.`);
