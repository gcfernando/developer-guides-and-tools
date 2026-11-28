const test = require('node:test');
const assert = require('node:assert/strict');
const {parseHTML} = require('linkedom');
const {renderingProblems} = require('../scripts/link-utils.cjs');

test('rendered checks reject literal disclosure Markdown even when its URL is valid', () => {
  const {document} = parseHTML('<html><body><details><summary>Example</summary>\n### Learn and apply\n[Next step](guide.html)\n```python\nprint(1)\n```\n</details></body></html>');
  assert.match(renderingProblems(document).join('\n'), /1 disclosure blocks contain unrendered Markdown/);
});

test('rendered checks allow actual links and code examples that teach Markdown syntax', () => {
  const {document} = parseHTML('<html><body><details><summary>Example</summary><h3>Learn and apply</h3><a href="guide.html">Next step</a><pre><code>### Example\n[link](file.md)\n```python</code></pre></details></body></html>');
  assert.deepEqual(renderingProblems(document), []);
});

test('rendered checks reject duplicate explicit and generated anchors', () => {
  const {document} = parseHTML('<html><body><a id="notes"></a><h2 id="notes">Notes</h2></body></html>');
  assert.deepEqual(renderingProblems(document), ['duplicate id "notes" (2 elements)']);
});

test('a rendered table number column is not mistaken for an unrendered heading', () => {
  const {document} = parseHTML('<html><body><details><summary>Tasks</summary><table><tr><th>#</th>\n<th>Task</th></tr><tr><td>1</td><td>Read a table</td></tr></table></details></body></html>');
  assert.deepEqual(renderingProblems(document), []);
});
