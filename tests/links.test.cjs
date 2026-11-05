const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const {spawnSync} = require('node:child_process');
const {createHash} = require('node:crypto');
const {gzipSync, gunzipSync} = require('node:zlib');
const MarkdownIt = require('markdown-it');
const {parseDocument, cssLinks, decodedFragment} = require('../scripts/link-utils.cjs');
const {ROOT, read} = require('../scripts/lib.cjs');

function archivedText(file) {
  return gunzipSync(fs.readFileSync(path.join(ROOT, file + '.gz'))).toString('utf8')
    .replace(/^\uFEFF/, '').replace(/\r\n/g, '\n');
}

function fixture(t, built = false) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'library-link-test-'));
  t.after(() => fs.rmSync(root, {recursive: true, force: true}));
  const write = (file, content) => {
    const target = path.join(root, file);
    fs.mkdirSync(path.dirname(target), {recursive: true});
    fs.writeFileSync(target, content);
  };
  for (const name of ['lib.cjs', 'link-utils.cjs', 'check-links.cjs', 'check-site.cjs', 'build-atlas-hosted.cjs']) {
    write('scripts/' + name, read('scripts/' + name));
  }
  fs.symlinkSync(path.join(ROOT, 'node_modules'), path.join(root, 'node_modules'), 'junction');
  write('_config.yml', 'url: https://example.test\nbaseurl: /library\nrepository: example/library\nexclude: [private]\n');
  write('_data/routes.json', '{"README.md":"/","guide.md":"/guide/"}');
  write('_data/navigation.yml', '- title: Guide\n  url: /guide/\n');
  write('README.md', '# Start\n\n[Guide](guide.md#example)\n');
  write('guide.md', '# Example\n');
  if (built) {
    const page = body => '<html><head><title>Guide</title><meta name="description" content="Guide">' +
      '<link rel="canonical" href="https://example.test/library/"></head><body>' + body + '</body></html>';
    write('_site/index.html', page('<a href="guide/#example">Guide</a><img src="image.svg#shape">'));
    write('_site/guide/index.html', page('<h1 id="example">Example</h1>'));
    write('_site/image.svg', '<svg><g id="shape"></g></svg>');
    write('_site/examples/containers/local-services/.env.example', 'PASSWORD=\n');
    write('_site/apps/ai-learning-atlas/exercises/assistant.py', '');
    write('_site/sitemap.xml', '<urlset><url><loc>https://example.test/library/guide/</loc></url></urlset>');
  }
  const run = (...args) => spawnSync(process.execPath, [path.join(root, 'scripts', built ? 'check-site.cjs' : 'check-links.cjs'), ...args], {
    cwd: root, encoding: 'utf8'
  });
  return {root, write, run};
}

test('Markdown links include nested disclosures, reference links and GitHub heading suffixes', async () => {
  const {default: Slugger} = await import('github-slugger');
  const input = '# Hello, world!\n\n## Hello, world!\n\n<details>\n<summary>Open</summary>\n\n' +
    '## Hidden `code`\n\n[Reference][guide]\n\n</details>\n\n[guide]: other.md#section\n\n' +
    '~~~html\n<a href="not-a-link.md">Example</a>\n~~~\n';
  const result = parseDocument(input, true, Slugger);
  assert.ok(result.anchors.has('hello-world'));
  assert.ok(result.anchors.has('hello-world-1'));
  assert.ok(result.anchors.has('hidden-code'));
  assert.ok(result.links.some(link => link.url === 'other.md#section'));
  assert.ok(!result.links.some(link => link.url === 'not-a-link.md'));
});

test('HTML audit checks both href and src, media, inline CSS and encoded Atlas templates', () => {
  const inner = '<section id="hidden"><a href="#visible">Back</a></section>';
  const input = `<a id="visible" href="guide.html"><img src="image.png" srcset="small.png 1x, large.png 2x"></a>
    <link rel="preconnect" href="https://fonts.example.org">
    <video src="movie.mp4" poster="poster.jpg"></video><form action="submit.html"></form>
    <svg><use href="#visible" xlink:href="icons.svg#icon"></use></svg>
    <div style="background:url(background.png)"></div>
    <template><script type="application/json" data-topic-json>${JSON.stringify(inner)}</script></template>`;
  const result = parseDocument(input, false);
  for (const url of ['guide.html', 'image.png', 'small.png', 'large.png', 'movie.mp4', 'poster.jpg',
    'submit.html', '#visible', 'icons.svg#icon', 'background.png']) {
    assert.ok(result.links.some(link => link.url === url), url);
  }
  assert.ok(result.anchors.has('hidden'));
  assert.ok(!result.links.some(link => link.url === 'https://fonts.example.org'));
});

test('CSS assets and encoded text fragments are handled without inventing URLs', () => {
  assert.deepEqual(cssLinks('/* url(ignored.png) */ @import "theme.css"; a{background:url("../a.png");mask:url(#mask)}'),
    ['theme.css', '../a.png', '#mask']);
  assert.equal(decodedFragment('hello%20world:~:text=sample'), 'hello world');
  assert.equal(decodedFragment(':~:text=sample'), '');
  assert.throws(() => decodedFragment('%invalid'), URIError);
});

test('generated add-ons reader does not auto-link instruction filenames as websites', () => {
  const result = parseDocument(read('apps/ai-coding-addons/index.html'), false);
  assert.ok(!result.links.some(link => /^https?:\/\/claude\.md(?:\/|$)/i.test(link.url)));
});

test('add-ons sibling navigation names the HTML file for offline browsing', () => {
  const {document} = parseDocument(read('apps/ai-coding-addons/index.html'), false);
  assert.equal(document.querySelector('footer a[href*="linux-command-reference"]').getAttribute('href'),
    '../linux-command-reference/index.html');
});

test('Linux reader runtime assets remain relative for both offline and hosted use', () => {
  const {document} = parseDocument(read('apps/linux-command-reference/index.html'), false);
  assert.equal(document.querySelector('script[src$="data.js"]').getAttribute('src'), 'data.js');
  assert.equal(document.querySelector('script[src$="app.js"]').getAttribute('src'), 'app.js');
  assert.match(document.querySelector('link[href*="styles.css"]').getAttribute('href'), /^styles\.css(?:\?|$)/);
});

test('source audit rejects broken routes, wrong case, missing fragments and malformed encoding', t => {
  const f = fixture(t);
  let result = f.run();
  assert.equal(result.status, 0, result.stderr);
  f.write('README.md', '# Start\n\n[Wrong case](Guide.md) [Fragment](guide.md#missing) ' +
    '[Route](https://example.test/library/absent/) <a href="guide.md#%ZZ">Bad encoding</a>\n');
  result = f.run();
  assert.equal(result.status, 1);
  for (const expected of ['case-mismatched path: Guide.md', 'missing anchor "missing"', 'absent', 'invalid URL encoding']) {
    assert.ok(result.stderr.includes(expected), result.stderr);
  }
});

test('source audit validates both assets and links and does not publish excluded paths', t => {
  const f = fixture(t);
  f.write('private/notes.md', '# Notes\n');
  f.write('page.html', '<a href="guide.md#example" src="missing.png">Both attributes</a>' +
    '<a href="https://example.test/library/private/notes.md">Private</a>');
  const result = f.run();
  assert.equal(result.status, 1);
  assert.match(result.stderr, /missing\.png/);
  assert.match(result.stderr, /excluded from publication/);
});

test('source audit includes legacy reading copies without treating compressed originals as documents', t => {
  const f = fixture(t);
  f.write('maintenance/migration/legacy/README.original.md.gz', gzipSync('[Original](removed.md)\n'));
  f.write('maintenance/migration/legacy/README.md', '[Current guide](../../../guide.md#example)\n');
  f.write('maintenance/migration/legacy/reader.html', '<a href="../../../guide.md#example">Current guide</a>');
  let result = f.run();
  assert.equal(result.status, 0, result.stderr);
  f.write('maintenance/migration/legacy/README.md', '[Missing guide](removed.md)\n');
  f.write('maintenance/migration/legacy/reader.html', '<a href="missing.html">Missing reader</a>');
  result = f.run();
  assert.equal(result.status, 1);
  assert.match(result.stderr, /legacy\/README\.md/);
  assert.match(result.stderr, /legacy\/reader\.html/);
  assert.ok(!result.stderr.includes('README.original.md.gz'));
});

test('source audit checks plain-text and alternate Markdown filenames and their fragments', t => {
  const f = fixture(t);
  f.write('notes.txt', '# Notes\n\n[Guide](guide.md#example)\n');
  f.write('guide.MARKDOWN', '# More\n\n[Notes](notes.txt#notes)\n');
  let result = f.run();
  assert.equal(result.status, 0, result.stderr);
  f.write('notes.txt', '# Notes\n\n[Missing guide](old-guide.md)\n');
  f.write('guide.MARKDOWN', '# More\n\n[Missing section](notes.txt#missing)\n');
  result = f.run();
  assert.equal(result.status, 1);
  assert.match(result.stderr, /notes\.txt: missing or case-mismatched path: old-guide\.md/);
  assert.match(result.stderr, /guide\.MARKDOWN: missing anchor "missing"/);
});

test('source audit rejects unresolved Liquid URLs in readable Markdown', t => {
  const f = fixture(t);
  f.write('guide.md', '# Example\n\n<a href="{{ guide.url | absolute_url }}">Guide</a>\n' +
    '<a href="{{ guide.path | uri_escape | absolute_url }}">Source</a>\n');
  f.write('notes.txt', '<a href="{{ guide.url | absolute_url }}">Unrendered text link</a>\n');
  const result = f.run();
  assert.equal(result.status, 1);
  assert.match(result.stderr, /unrendered template URL in Markdown/);
  assert.match(result.stderr, /guide\.url/);
  assert.match(result.stderr, /guide\.path/);
  assert.match(result.stderr, /notes\.txt: unrendered template URL/);
});

test('optional runtime documentation audit checks Markdown and text without scanning previews or node_modules', t => {
  const f = fixture(t);
  f.write('.runtime/tool/README.md', '[English](doc/doc.md)\n');
  f.write('.runtime/tool/notes.txt', '[English](doc/doc.md)\n');
  f.write('.runtime/tool/node_modules/package/README.md', '[Dependency](missing.md)\n');
  f.write('.runtime/preview/index.html', '<a href="missing.html">Generated preview</a>');
  let result = f.run();
  assert.equal(result.status, 0, result.stderr);
  result = f.run('--include-runtime-docs');
  assert.equal(result.status, 1);
  assert.match(result.stderr, /\.runtime\/tool\/README\.md/);
  assert.match(result.stderr, /\.runtime\/tool\/notes\.txt/);
  assert.ok(!result.stderr.includes('node_modules') && !result.stderr.includes('preview'));
  f.write('.runtime/tool/doc/doc.md', '# Documentation\n');
  result = f.run('--include-runtime-docs');
  assert.equal(result.status, 0, result.stderr);
});

test('provenance verifies decompressed original bytes and rejects altered archive contents', t => {
  const f = fixture(t);
  const original = Buffer.from('# Original\r\n\r\n[Historical link](old-guide.md)\r\n');
  const hash = createHash('sha256').update(original).digest('hex');
  f.write('scripts/verify-migration.cjs', read('scripts/verify-migration.cjs'));
  f.write('original.md.gz', gzipSync(original));
  f.write('maintenance/migration/source-map.csv',
    'source_folder,source_repository,source_path,source_sha256,source_bytes,destination,disposition\n' +
    `Original,example/history,README.md,${hash},${original.length},original.md.gz,archived-original\n`);
  const run = () => spawnSync(process.execPath, [path.join(f.root, 'scripts/verify-migration.cjs')], {
    cwd: f.root, encoding: 'utf8'
  });
  let result = run();
  assert.equal(result.status, 0, result.stderr);
  f.write('original.md.gz', gzipSync('# Changed original\n'));
  result = run();
  assert.equal(result.status, 1);
  assert.match(result.stderr, /Preserved file changed: original\.md\.gz/);
});

test('historical reading copies preserve the original Markdown anchors and code examples', async () => {
  const {default: Slugger} = await import('github-slugger');
  const md = new MarkdownIt();
  const examples = text => md.parse(text, {}).filter(token => ['fence', 'code_block'].includes(token.type))
    .map(token => ({info: token.info, content: token.content}));
  for (const folder of ['KnowledgeBase', 'Other_Projects']) {
    for (const name of ['README.original.md', 'documentation.md']) {
      const file = `maintenance/migration/legacy/${folder}/${name}`;
      assert.ok(!fs.existsSync(path.join(ROOT, file + '.txt')), `Indexed archive must not remain: ${file}.txt`);
      const originalText = archivedText(file);
      const currentText = read(file);
      const original = parseDocument(originalText, true, Slugger);
      const current = parseDocument(currentText, true, Slugger);
      for (const anchor of original.anchors) assert.ok(current.anchors.has(anchor), `${file}#${anchor}`);
      assert.deepEqual(examples(currentText), examples(originalText), file);
    }
  }
});

test('historical HTML link repairs preserve anchors, styles and executable scripts', () => {
  const file = 'maintenance/migration/legacy/ai-coding-addons.html';
  assert.ok(!fs.existsSync(path.join(ROOT, file + '.txt')), 'The HTML original must not remain as indexed plain text');
  const original = parseDocument(archivedText(file), false);
  const current = parseDocument(read(file), false);
  for (const anchor of original.anchors) assert.ok(current.anchors.has(anchor), `${file}#${anchor}`);
  const code = result => [...result.document.querySelectorAll('style, script:not([type])')]
    .map(node => node.textContent);
  assert.deepEqual(code(current), code(original));
});

test('rendered audit resolves query-only URLs, SVG fragments, CSS assets and sitemap links', t => {
  const f = fixture(t, true);
  f.write('_site/style.css', 'svg{mask:url(image.svg#shape)}');
  let result = f.run();
  assert.equal(result.status, 0, result.stderr);
  f.write('_site/style.css', 'svg{mask:url(image.svg#missing)}');
  f.write('_site/guide/index.html', '<title>Guide</title><meta name="description" content="Guide">' +
    '<link rel="canonical" href="https://example.test/library/guide/"><h1 id="example">Example</h1>' +
    '<a href="?view=print#example">Print</a><a href="/outside/">Outside</a><img src="../Image.svg">');
  result = f.run();
  assert.equal(result.status, 1);
  assert.match(result.stderr, /missing anchor image\.svg#missing/);
  assert.match(result.stderr, /escapes configured site base path/);
  assert.match(result.stderr, /case-mismatched target/);
  assert.ok(!result.stderr.includes('missing anchor ?view=print#example'));
});

test('rendered audit checks deferred hosted Atlas anchors and every runtime asset', t => {
  const f = fixture(t, true);
  f.write('_site/index.html', '<title>Reader</title><meta name="description" content="Reader">' +
    '<link rel="canonical" href="https://example.test/library/">' +
    '<script src="loader.js" data-atlas-content="content.json" data-atlas-runtime="runtime.js"></script>' +
    '<a href="#deferred-heading">Read</a><section data-atlas-fragment="0"></section>');
  f.write('_site/loader.js', '');
  f.write('_site/runtime.js', '');
  f.write('_site/content.json', JSON.stringify(['<h1 id="deferred-heading">Reader</h1>']));
  let result = f.run();
  assert.equal(result.status, 0, result.stderr);
  f.write('_site/content.json', JSON.stringify(['<h1 id="wrong-heading">Reader</h1><a href="missing.html">Broken</a>']));
  result = f.run();
  assert.equal(result.status, 1);
  assert.match(result.stderr, /missing anchor #deferred-heading/);
  assert.match(result.stderr, /missing or case-mismatched target missing.html/);
  fs.unlinkSync(path.join(f.root, '_site/runtime.js'));
  result = f.run();
  assert.match(result.stderr, /missing or case-mismatched target runtime.js/);
});
