// Compare compatibility targets and reader behaviour after rebuilding the course.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {parseHTML} = require('linkedom');
const MarkdownIt = require('markdown-it');
const root = path.resolve(__dirname, '..');
const repository = path.resolve(__dirname, '../../../..');
const {frontMatter} = require(path.join(repository, 'scripts/lib.cjs'));
const {parseDocument} = require(path.join(repository, 'scripts/link-utils.cjs'));
const read = name => fs.readFileSync(path.join(root, name), 'utf8');

async function main() {
  const {default: Slugger} = await import('github-slugger');
  const baseline = JSON.parse(read('course_tools/reader-compatibility.json'));
  for (const [name, previous] of Object.entries(baseline.pages)) {
    const source = parseDocument(frontMatter(read(name+'.md')).body, true, Slugger);
    const reader = parseHTML(read(name+'.html')).document;
    const ids = [...reader.querySelectorAll('[id]')].map(node => node.id);
    for (const anchor of previous.source_ids) assert(source.anchors.has(anchor), name+': lost source anchor '+anchor);
    for (const anchor of previous.reader_ids) assert(ids.includes(anchor), name+': lost reader anchor '+anchor);
    assert.equal(new Set(ids).size, ids.length, name+': duplicate reader IDs');
    assert.deepEqual([...reader.querySelectorAll('input[data-course-check]')].map(node=>node.getAttribute('aria-label')),
      previous.progress_controls, name+': progress control order or labels changed');
    assert(reader.querySelector('nav[aria-label="Library navigation"] a[href="https://gcfernando.github.io/developer-guides-and-tools/"]'), name+': missing library return');
    assert(reader.querySelector('nav[aria-label="Course pages"] a[href="README.html"]'), name+': missing course overview');
  }
  const workbookSource = read('Data-Science-and-Machine-Learning.md');
  assert.equal((workbookSource.match(/<!-- workbook-teaching:\d+:start -->/g)||[]).length,447);
  assert(!/^<details>$/m.test(workbookSource), 'All workbook disclosures must enable Jekyll Markdown.');
  let previousLevel = 0;
  for (const heading of new MarkdownIt().parse(frontMatter(workbookSource).body,{}).filter(token=>token.type==='heading_open')) {
    const level = Number(heading.tag.slice(1));
    assert(!previousLevel || level<=previousLevel+1, 'Workbook skips a heading level near source line '+(heading.map[0]+1));
    previousLevel = level;
  }
  const workbook = parseHTML(read('Data-Science-and-Machine-Learning.html')).document;
  const teachingNotes = [...workbook.querySelectorAll('details')].filter(node=>
    [...node.querySelectorAll('strong')].some(label=>label.textContent.startsWith('Learn and apply:')));
  assert.equal(teachingNotes.length,447, 'Every teaching disclosure must contain rendered content.');
  for (const note of teachingNotes) {
    assert(note.querySelector('a[href]'), 'Teaching links must be clickable.');
    assert(note.querySelector('pre code'), 'Recorded input and output must render as code.');
  }
  for (const name of ['README','START-HERE','SETUP','GLOSSARY','Data-Science-and-Machine-Learning']) {
    const source = parseDocument(frontMatter(read(name+'.md')).body,true,Slugger);
    assert(!source.links.some(link=>/\/(?:LEARNING-PATH|PYTHON-BASICS|PRACTICE|PROJECT-CHOICES|ELECTIVES|TEACHING|INDEPENDENT-PROJECT)\.md(?:#|$)/.test(link.url)), name+': raw guide destination');
  }
  const project = parseHTML(read('projects/wine/README.html')).document;
  for (const file of ['training.csv','validation.csv','test_inputs.csv','data_dictionary.csv','starter.py','instructor/check_predictions.py']) {
    assert(project.querySelector('a[href="'+file+'"]'), 'Missing project file link: '+file);
  }
  assert(project.querySelector('a[href="../../README.html"]'), 'Wine reader needs a course return.');
  assert(fs.existsSync(path.join(root,'projects/wine/SOURCE.html')), 'Wine source needs a readable page.');
  console.log('Reader compatibility passed: all previous source/HTML anchors and progress controls, 447 rendered notes, heading outline, reader navigation and project links.');
}
main().catch(error=>{console.error(error);process.exitCode=1;});
