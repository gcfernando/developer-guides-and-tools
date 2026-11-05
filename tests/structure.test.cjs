const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {execFileSync} = require('node:child_process');
const MarkdownIt = require('markdown-it');
const {parseHTML} = require('linkedom');
const {ROOT, read, frontMatter, yaml} = require('../scripts/lib.cjs');
const {splitCourse, rebaseLinks} = require('../scripts/build-sql-course.cjs');
const md = new MarkdownIt({html: true});

test('SQL part readers preserve the complete course and every code example', () => {
  const {body} = frontMatter(read('docs/databases/sql-server-and-mysql.md'));
  const parts = splitCourse(body);
  assert.equal(parts.length, 16);
  assert.equal(parts.map(part => part.content).join(''), body);
  const examples = text => md.parse(text, {}).filter(token => ['fence', 'code_block'].includes(token.type))
    .map(token => ({type: token.type, language: token.info, code: token.content}));
  const renderedExamples = [];
  for (const part of parts) {
    const file = `docs/databases/sql-server-and-mysql/${part.slug}.md`;
    const {data, body: generated} = frontMatter(read(file));
    assert.ok(generated.includes(rebaseLinks(part.content)), file);
    assert.ok(generated.includes('[Prerequisites](00-start-here.md)'), file);
    assert.ok(data.permalink.startsWith('/databases/sql-server-and-mysql/parts/'));
    renderedExamples.push(...examples(generated));
    const {document} = parseHTML(md.render(generated));
    assert.equal(document.querySelectorAll('a[href^="#"]').length, 0, 'References must resolve against the full course');
  }
  assert.deepEqual(renderedExamples, examples(body));
  execFileSync(process.execPath, [path.join(ROOT, 'scripts/build-sql-course.cjs'), '--check'], {cwd: ROOT, stdio: 'pipe'});
});

test('SQL link rebasing leaves code, inline code and external links unchanged', () => {
  const source = '[Section](#setup) [Guide](../guide.md#x) [External](https://example.org)\n' +
    '`[literal](#unchanged)`\n<a href="#setup">Setup</a>\n' +
    '```sql\nSELECT \'[literal](#unchanged)\';\n```\n' +
    '\n    [indented](#unchanged)\n';
  const result = rebaseLinks(source);
  assert.ok(result.includes('[Section](../sql-server-and-mysql.md#setup)'));
  assert.ok(result.includes('[Guide](../../guide.md#x)'));
  assert.ok(result.includes('[External](https://example.org)'));
  assert.ok(result.includes('`[literal](#unchanged)`'));
  assert.ok(result.includes('<a href="../sql-server-and-mysql.md#setup">'));
  assert.ok(result.includes("SELECT '[literal](#unchanged)';"));
  assert.ok(result.includes('    [indented](#unchanged)'));
  assert.throws(() => splitCourse('## PART 2 - Wrong order\n'), /consecutively/);
  assert.throws(() => splitCourse('# No parts\n'), /No SQL course parts/);
});

test('publication separates Atlas tooling from downloadable exercises and safe configuration', () => {
  const config = yaml.parse(read('_config.yml'));
  for (const file of ['apps/ai-learning-atlas/source', 'apps/ai-learning-atlas/tools',
    'apps/ai-learning-atlas/tests', 'apps/ai-learning-atlas/build.py',
    'apps/ai-learning-atlas/validate.py', 'examples/containers/local-services/.env']) {
    assert.ok(config.exclude.includes(file), file);
  }
  assert.ok(!config.exclude.some(file => 'apps/ai-learning-atlas/exercises'.startsWith(file)));
  for (const file of config.include) assert.ok(fs.existsSync(path.join(ROOT, file)), file);
  const sample = Object.fromEntries(read('examples/containers/local-services/.env.example').split('\n')
    .filter(line => line && !line.startsWith('#')).map(line => line.split('=')));
  for (const key of ['SQL_PASSWORD', 'ORACLE_PASSWORD', 'DEFAULT_ROOT_PASSWORD']) assert.equal(sample[key], '');
  assert.equal(sample.TZ, 'UTC');
});

test('Atlas fixtures retain the compatibility baseline and both backup formats', () => {
  const baseline = JSON.parse(read('apps/ai-learning-atlas/tests/fixtures/baseline.json'));
  assert.equal(baseline.topics.length, 51);
  assert.equal(baseline.subtopics.length, 1607);
  for (const version of [1, 2]) {
    const backup = JSON.parse(read(`apps/ai-learning-atlas/tests/fixtures/backup-v${version}.json`));
    assert.equal(backup.version, version);
    const ids = version === 1 ? baseline.progress_ids.filter(id => /^(milestone-|complete-topic-)/.test(id)) : baseline.progress_ids;
    assert.deepEqual(Object.keys(backup.checks).sort(), [...ids].sort());
    assert.ok(ids.every(id => typeof backup.checks[id] === 'boolean'));
  }
});

test('CI configures Python before the aggregate checks and root commands cover all generators', () => {
  const {scripts} = JSON.parse(read('package.json'));
  for (const name of ['addons', 'handbook', 'linux', 'atlas', 'sql', 'catalog']) {
    assert.ok(scripts.build.includes(`npm run build:${name}`), name);
  }
  assert.ok(scripts.build.endsWith('npm run build:catalog'));
  assert.ok(scripts.test.includes('npm run check:atlas'));
  for (const file of ['.github/workflows/validate.yml', '.github/workflows/pages.yml']) {
    const workflow = yaml.parse(read(file));
    const job = workflow.jobs.validate || workflow.jobs.build;
    const python = job.steps.findIndex(step => step.uses?.startsWith('actions/setup-python@'));
    const tests = job.steps.findIndex(step => step.run === 'npm test');
    assert.ok(python >= 0 && python < tests, file);
  }
});
