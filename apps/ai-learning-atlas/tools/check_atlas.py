"""Check the standalone Atlas against its immutable pre-edit baseline.

Python 3.10+ standard library only. Run from any working directory:
    python tools/check_atlas.py [--stage baseline|ws1|final] [--page PATH]

The baseline stage records existing defects as warnings; preservation, IDs,
links, search, curriculum and executable fixtures still fail on regressions.
The ws1 stage enforces authored-unit acceptance before later workstreams.
This does not replace Nu, browser, axe, Lighthouse or human content review.
"""
from __future__ import annotations

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
import math
import os
from pathlib import Path
import py_compile
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())


class Element:
    def __init__(self, tag, attrs=(), parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children: list[Element | str] = []

    def text(self):
        return ''.join(c.text() if isinstance(c, Element) else c for c in self.children)

    def classes(self):
        return self.attrs.get('class', '').split()

    def descendants(self, predicate=lambda n: True):
        for child in self.children:
            if isinstance(child, Element):
                if predicate(child):
                    yield child
                yield from child.descendants(predicate)

    def find(self, predicate):
        return next(self.descendants(predicate), None)

    def ancestor(self, predicate):
        node = self.parent
        while node:
            if predicate(node):
                return node
            node = node.parent
        return None


class Document(HTMLParser):
    def __init__(self, content, search=None):
        super().__init__(convert_charrefs=True)
        self.root = Element('document')
        self.current = self.root
        self.feed(content)
        self.close()
        if search is None:
            atlas = self.root.find(lambda n: n.attrs.get('id') == 'atlas-data')
            search = json.loads(atlas.text()).get('search', []) if atlas else []
        # Authored bodies are JSON text until first use. Decode them in their
        # original topic positions to audit the same tree the browser hydrates.
        for template in list(self.root.descendants(lambda n: n.tag == 'template' and 'data-topic-body' in n.attrs)):
            encoded = template.find(lambda n: n.tag == 'script' and 'data-topic-json' in n.attrs)
            if encoded:
                decoded = Document(json.loads(encoded.text()), search=search)
                template.children = decoded.root.children
                for child in template.children:
                    if isinstance(child, Element):
                        child.parent = template
        for directory in self.root.descendants(lambda n: 'data-topic-subtopics' in n.attrs):
            if directory.children:
                continue
            prefix = '#subtopic-'+directory.attrs['data-topic-subtopics']+'-'
            for entry in search:
                if entry.get('type') == 'Subtopic' and entry.get('href', '').startswith(prefix):
                    item = Element('li', [('id', entry['href'][1:])], directory)
                    item.children = [entry['title']]
                    directory.children.append(item)
        self.nodes = list(self.root.descendants())
        self.ids = {n.attrs['id']: n for n in self.nodes if n.attrs.get('id')}

    def handle_starttag(self, tag, attrs):
        node = Element(tag, attrs, self.current)
        self.current.children.append(node)
        if tag not in VOID:
            self.current = node

    def handle_startendtag(self, tag, attrs):
        node = Element(tag, attrs, self.current)
        self.current.children.append(node)

    def handle_endtag(self, tag):
        node = self.current
        while node is not self.root:
            if node.tag == tag:
                self.current = node.parent
                break
            node = node.parent

    def handle_data(self, text):
        self.current.children.append(text)


class Checks:
    def __init__(self):
        self.failures = 0
        self.warnings = 0
        self.passes = 0

    def check(self, name, condition, detail='', warning=False):
        if condition:
            self.passes += 1
            print(f'PASS {name}' + (f': {detail}' if detail else ''))
        elif warning:
            self.warnings += 1
            print(f'WARN {name}' + (f': {detail}' if detail else ''))
        else:
            self.failures += 1
            print(f'FAIL {name}' + (f': {detail}' if detail else ''))


def topic_number(href):
    match = re.match(r'#topic-(\d\d)-', href)
    return int(match[1]) if match else None


def run(args):
    checks = Checks()
    page = args.page.resolve()
    content = page.read_text(encoding='utf-8')
    doc = Document(content)
    baseline = json.loads((ROOT/'tests/fixtures/baseline.json').read_text(encoding='utf-8'))
    curriculum = json.loads((ROOT/'source/curriculum.json').read_text(encoding='utf-8'))
    topics = {t['number']: t for t in curriculum['topics']}
    roles = curriculum['roles']
    cards = [n for n in doc.nodes if 'topic-card' in n.classes()]
    actual_topics = [{'id': n.attrs.get('id'), 'title': n.find(lambda x: x.tag == 'h3').text()}
                     for n in cards]
    actual_numbers = [n.find(lambda x: 'topic-number' in x.classes()).text().strip() for n in cards]
    checks.check('51 original topic IDs, titles and order',
                 actual_topics == baseline['topics'] and actual_numbers == [f'{i:02}' for i in range(1, 52)],
                 f'{len(cards)} topic cards')
    subtopics = [{'id': n.attrs['id'], 'text': n.text()} for n in doc.nodes
                 if n.tag == 'li' and re.fullmatch(r'subtopic-\d\d-\d{3}', n.attrs.get('id', ''))]
    checks.check('original subtopic IDs, text and order', subtopics == baseline['subtopics'],
                 f'{len(subtopics)} actual; {len(baseline["subtopics"])} baseline; claimed 1,607')
    checks.check('true subtopic count matches page claims', len(subtopics) == 1607,
                 'Baseline confirms the published 1,607 count')
    counts = Counter(n.attrs['id'] for n in doc.nodes if n.attrs.get('id'))
    duplicates = [key for key, count in counts.items() if count > 1]
    checks.check('all IDs unique including inert templates', not duplicates,
                 f'{len(counts)} IDs' if not duplicates else ', '.join(duplicates))
    broken = sorted({n.attrs['href'] for n in doc.nodes if n.tag == 'a'
                     and n.attrs.get('href', '').startswith('#')
                     and unquote(n.attrs['href'][1:]) not in doc.ids})
    checks.check('every internal fragment resolves including templates', not broken,
                 ', '.join(broken[:20]) if broken else 'No unresolved fragment links')
    atlas = doc.ids.get('atlas-data')
    try:
        data = json.loads(atlas.text()) if atlas else {}
    except json.JSONDecodeError as error:
        data = {}
        checks.check('atlas-data parses', False, str(error))
    search = data.get('search', [])
    expected = {
        'Topic': {t['id'] for t in topics.values()},
        'Subtopic': {s['id'] for s in baseline['subtopics']},
        'Profession': {'role-'+r['slug'] for r in roles},
        'Lesson': {n.attrs['id'] for n in doc.nodes if 'lesson' in n.classes() or 'optional-lesson' in n.classes()},
        'Glossary': {n.attrs['id'] for n in doc.nodes if n.attrs.get('id', '').startswith('glossary-')},
    }
    for category, ids in expected.items():
        indexed = {unquote(s.get('href', '')[1:]) for s in search if s.get('type') == category}
        checks.check(f'search covers every {category.lower()}', ids <= indexed,
                     f'{len(ids)} required; missing {sorted(ids-indexed)}')
    bad_search = [s.get('href') for s in search if not s.get('href', '').startswith('#')
                  or unquote(s['href'][1:]) not in doc.ids]
    checks.check('every search href resolves', not bad_search, f'{len(search)} records; broken {bad_search[:10]}')
    checks.check('atlas-data priorities equal canonical source',
                 data.get('priorities') == {r['slug']: r['priorities'] for r in roles})

    role_errors = []
    for role in roles:
        slug = role['slug']
        path = doc.ids.get('role-'+slug)
        core = {int(k) for k, value in role['priorities'].items() if value in ('Essential', 'Recommended')}
        items = list(path.descendants(lambda n: 'path-item' in n.classes())) if path else []
        sequence = []
        for item in items:
            heading = item.find(lambda n: n.tag in ('h4', 'h5', 'h6'))
            anchor = heading.find(lambda n: n.tag == 'a' and topic_number(n.attrs.get('href', '')) is not None) if heading else None
            number = topic_number(anchor.attrs['href']) if anchor else None
            badge = item.find(lambda n: 'status' in n.classes())
            if number is None:
                role_errors.append(f'{slug}: path item lacks numbered topic heading')
                continue
            sequence.append(number)
            if not badge or badge.text().strip() != role['priorities'][str(number)]:
                role_errors.append(f'{slug}: topic {number:02} priority badge mismatch')
        if set(sequence) != core or len(sequence) != len(core):
            role_errors.append(f'{slug}: core sequence mismatch or duplication')
        for i, number in enumerate(sequence):
            if role['priorities'][str(number)] not in ('Essential', 'Recommended'):
                role_errors.append(f'{slug}: non-core topic {number:02} in core sequence')
            for prerequisite in topics[number]['prerequisites']:
                if prerequisite not in sequence[:i]:
                    role_errors.append(f'{slug}: prerequisite {prerequisite:02} not before {number:02}')
        project = doc.ids.get('project-'+slug)
        chips = list(project.descendants(lambda n: 'chips' in n.classes())) if project else []
        sources = {topic_number(a.attrs.get('href', '')) for chip in chips
                   for a in chip.descendants(lambda n: n.tag == 'a')}
        sources.discard(None)
        additional = set(role.get('additionalCapstoneTopics', []))
        if not set(role['capstonePrerequisites']) <= set(sequence) | additional:
            role_errors.append(f'{slug}: canonical capstone prerequisite outside sequence')
        if not sources <= set(sequence) | additional:
            role_errors.append(f'{slug}: rendered capstone source outside sequence')
        if not project:
            role_errors.append(f'{slug}: missing project')
    checks.check('role prerequisites, priority badges and capstone source topics', not role_errors,
                 f'{len(roles)} roles; ' + ('; '.join(role_errors[:20]) if role_errors else 'all consistent'))

    difficulty = {'Beginner': 0, 'Intermediate': 1, 'Advanced': 2}
    inversions = []
    for topic in topics.values():
        label = next((v for v in difficulty if any(v in m for m in topic['meta'])), None)
        for prerequisite in topic['prerequisites']:
            prior = next((v for v in difficulty if any(v in m for m in topics[prerequisite]['meta'])), None)
            if label and prior and difficulty[label] < difficulty[prior]:
                inversions.append(f'{topic["number"]:02} ({label}) requires {prerequisite:02} ({prior})')
    checks.check('difficulty is not below an applied prerequisite', not inversions,
                 '; '.join(inversions) if inversions else 'All 51 checked', warning=args.stage != 'final')
    if args.stage == 'final':
        phase_errors = []
        authored = json.loads((ROOT/'source/units.json').read_text(encoding='utf-8'))
        for role in roles:
            core = {int(k) for k,v in role['priorities'].items() if v in ('Essential', 'Recommended')}
            phases = role.get('phases', [])
            if len(core) > 12 and len(phases) < 2:
                phase_errors.append(role['slug']+': no phases for long path')
            if not phases:
                phase_errors.append(role['slug']+': no role checkpoint/session plan')
                continue
            flattened = [number for phase in phases for number in phase.get('topics', [])]
            if set(flattened) != core or len(flattened) != len(core):
                phase_errors.append(role['slug']+': phases do not cover the core exactly once')
            for i, number in enumerate(flattened):
                if any(prerequisite not in flattened[:i] for prerequisite in topics[number]['prerequisites']):
                    phase_errors.append(f'{role["slug"]}: phase sequence violates topic {number:02} prerequisite')
            estimated = [sum(unit.get('minutes', [30, 60])[bound]
                             for number in core for unit in authored[str(number)])/60 for bound in (0, 1)]
            hours = role.get('hours', [])
            if len(hours) != 2 or any(not math.isclose(hours[i], estimated[i], abs_tol=0.01) for i in (0,1)):
                phase_errors.append(role['slug']+': role hours do not derive from authored unit estimates')
            for phase in phases:
                checkpoint = phase.get('checkpoint', {})
                if not 3 <= len(checkpoint.get('tasks', [])) <= 5:
                    phase_errors.append(role['slug']+': checkpoint needs 3–5 tasks')
                if set(checkpoint.get('rubric', {})) != {'Not yet', 'Partial', 'Pass', 'Strong'}:
                    phase_errors.append(role['slug']+': checkpoint rubric levels missing')
                if sum(item.get('minutes', 0) for item in phase.get('sessionPlan', [])) != 60:
                    phase_errors.append(role['slug']+': session plan does not total 60 minutes')
                if phase.get('id') not in doc.ids:
                    phase_errors.append(role['slug']+': checkpoint phase not rendered')
        checks.check('phases, optional checkpoints, session plans and derived hours', not phase_errors,
                     '; '.join(phase_errors) if phase_errors else 'Every role checked; all long paths split')

        display_errors = []
        for topic in topics.values():
            label = next((value for value in difficulty if any(value in meta for meta in topic['meta'])), '')
            card = doc.ids.get(topic['id'])
            meta = card.find(lambda n: 'topic-meta' in n.classes()) if card else None
            if not meta or label not in meta.text():
                display_errors.append(f'{topic["number"]:02}: card difficulty differs from canonical source')
            row = next((n for n in doc.nodes if n.tag == 'tr' and n.attrs.get('data-topic') == str(topic['number'])), None)
            if not row or label not in row.text():
                display_errors.append(f'{topic["number"]:02}: relevance matrix difficulty differs from canonical source')
        checks.check('difficulty labels agree across cards and matrix', not display_errors, '; '.join(display_errors))

    units = [n for n in doc.nodes if 'study-unit' in n.classes()]
    practices = []
    missing_structure, coverage = [], []
    briefs = []
    for unit in units:
        paragraphs = list(unit.descendants(lambda n: n.tag == 'p'))
        practice = next((n.text().strip() for n in paragraphs if n.text().strip().startswith('Practice:')), '')
        practices.append(practice)
        label = unit.attrs.get('id', '(no ID)')
        brief = 'Study brief — full lesson not yet written' in unit.text()
        if brief:
            briefs.append(label)
        required = ('Objective:', 'Key idea:', 'Worked example', 'Practice:', 'Check questions:', 'Common mistake:', 'Related original subtopics (reference map):')
        if not brief and (not all(s in unit.text() for s in required)
                          or not unit.find(lambda n: n.tag == 'details' and 'Answer key' in n.text())):
            missing_structure.append(label)
        covered = next((n for n in paragraphs if n.text().strip().startswith('Related original subtopics (reference map):')), None)
        if covered:
            coverage += [a.attrs.get('href', '')[1:] for a in covered.descendants(lambda n: n.tag == 'a')]
    duplicates = {text: count for text, count in Counter(practices).items() if count > 1}
    checks.check('no duplicate study-unit practice paragraphs', not duplicates and all(practices),
                 f'{len(units)} units; {len(duplicates)} duplicate paragraphs', warning=args.stage == 'baseline')
    checks.check('completed units have all teaching fields and hidden answers', not missing_structure,
                 ', '.join(missing_structure[:20]) if missing_structure else f'{len(units)-len(briefs)} complete units',
                 warning=args.stage == 'baseline')
    coverage_counts = Counter(coverage)
    expected_ids = {s['id'] for s in baseline['subtopics']}
    missing = sorted(expected_ids - coverage_counts.keys())
    multiply = [key for key, value in coverage_counts.items() if value != 1]
    unknown = sorted(coverage_counts.keys() - expected_ids)
    checks.check('every original subtopic maps to exactly one unit', not missing and not multiply and not unknown,
                 f'{len(coverage)} assignments; missing {len(missing)}; multiple {multiply[:10]}; unknown {unknown[:10]}',
                 warning=args.stage == 'baseline')
    print('INFO remaining labeled briefs: '+(', '.join(briefs) if briefs else 'none'))

    progress = {n.attrs['id'] for n in doc.nodes if 'save-check' in n.classes() and n.attrs.get('id')}
    absent = set(baseline['progress_ids']) - progress
    checks.check('every original progress ID preserved', not absent,
                 f'{len(baseline["progress_ids"])} original; {len(progress)} current; missing {sorted(absent)}')
    added = progress-set(baseline['progress_ids'])
    scripts = '\n'.join(n.text() for n in doc.nodes if n.tag == 'script' and n.attrs.get('type') != 'application/json')
    checks.check('new progress IDs use backup version 3', not added or bool(re.search(r'version\s*:\s*3', scripts)),
                 f'{len(added)} added progress IDs')
    keys = ('ai-learning-atlas-progress-v1', 'ai-atlas-active-role-v2', 'ai-atlas-study-note-v1', 'ai-atlas-theme')
    checks.check('all original localStorage keys retained', all(key in scripts for key in keys))
    checks.check('one document H1', sum(n.tag == 'h1' for n in doc.nodes) == 1)
    previous, heading_errors = 0, []
    for node in doc.nodes:
        if re.fullmatch(r'h[1-6]', node.tag):
            level = int(node.tag[1])
            if level > previous+1:
                heading_errors.append(node.tag+': '+node.text()[:70])
            previous = level
    checks.check('heading outline has no skipped levels', not heading_errors, '; '.join(heading_errors))
    external = [n for n in doc.nodes if n.tag == 'a' and n.attrs.get('href', '').startswith(('https://', 'http://'))]
    if args.stage == 'final':
        checks.check('external links labeled online including deferred bodies', all('(online)' in n.text() for n in external), f'{len(external)} anchors')
        checks.check('workshop downloads need no adjacent exercise files', not any(n.tag == 'a' and n.attrs.get('href', '').startswith('exercises/') for n in doc.nodes))
    assets = [n.attrs.get('src', n.attrs.get('href', '')) for n in doc.nodes
              if (n.tag == 'script' and n.attrs.get('src'))
              or (n.tag == 'link' and n.attrs.get('rel') == 'stylesheet')
              or (n.tag in ('img', 'iframe') and n.attrs.get('src', '').startswith(('http:', 'https:')))]
    checks.check('no external runtime assets', not assets and not re.search(r'@import\s', content), str(assets))

    extracted = {}
    extraction_errors = []
    for anchor in doc.nodes:
        if anchor.tag not in ('a', 'button'):
            continue
        href = anchor.attrs.get('href', '')
        filename = anchor.attrs.get('data-filename') or anchor.attrs.get('data-download')
        if not filename and href.startswith('exercises/'):
            filename = unquote(urlsplit(href).path).split('/')[-1]
        if not filename:
            continue
        target_id = anchor.attrs.get('data-code') or anchor.attrs.get('data-download-source')
        node = doc.ids.get(target_id) if target_id else None
        container = anchor.ancestor(lambda n: n.tag == 'details')
        code = node or (container.find(lambda n: n.tag == 'pre') if container else None)
        if not code:
            extraction_errors.append(filename+': no embedded text')
            continue
        text = code.text()
        if filename in extracted and extracted[filename] != text:
            extraction_errors.append(filename+': differing embedded copies')
        extracted[filename] = text
    checks.check('download reference files have exact, consistent inline text', not extraction_errors,
                 f'{len(extracted)} files; '+'; '.join(extraction_errors))
    if args.skip_exercises:
        print('UNVERIFIED extracted Python compilation and unittest suites (--skip-exercises)')
    else:
        runtime = ROOT/'.runtime'
        runtime.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='atlas-check-', dir=runtime) as directory:
            folder = Path(directory)
            compile_errors = []
            for name, text in extracted.items():
                path = folder/Path(name).name
                path.write_text(text, encoding='utf-8', newline='')
                if path.suffix == '.py':
                    try:
                        py_compile.compile(str(path), cfile=str(folder/(path.name+'.pyc')), doraise=True)
                    except py_compile.PyCompileError as error:
                        compile_errors.append(str(error))
            checks.check('extracted Python reference files compile', not compile_errors and bool(extracted),
                         f'{sum(name.endswith(".py") for name in extracted)} Python files; '+'; '.join(compile_errors))
            env = os.environ.copy()
            env.update(TEMP=str(folder), TMP=str(folder), TMPDIR=str(folder), PYTHONDONTWRITEBYTECODE='1')
            completed = subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', str(folder), '-v'],
                                       cwd=folder, env=env, text=True, capture_output=True, timeout=120)
            output = completed.stdout+completed.stderr
            print('--- Extracted unittest output ---\n'+output.rstrip())
            checks.check('extracted supplied unittest suites pass', completed.returncode == 0 and bool(re.search(r'Ran [1-9]\d* tests?', output)),
                         f'exit {completed.returncode}')
    if args.page.resolve() == (ROOT/'index.html').resolve():
        try:
            sys.path.insert(0, str(ROOT))
            from build import build
            checks.check('standalone HTML matches canonical sources', content == build())
        except Exception as error:
            checks.check('standalone HTML matches canonical sources', False, repr(error))
    live = [n for n in doc.nodes if not n.ancestor(lambda x: x.tag == 'template')]
    print(f'INFO parsed elements {len(doc.nodes)}; initial live elements excluding template contents {len(live)}')
    print(f'RESULT {checks.passes} passed; {checks.failures} failed; {checks.warnings} warnings; stage={args.stage}')
    return 1 if checks.failures else 0


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stage', choices=('baseline', 'ws1', 'final'), default='final')
    parser.add_argument('--page', type=Path, default=ROOT/'index.html')
    parser.add_argument('--skip-exercises', action='store_true')
    arguments = parser.parse_args()
    try:
        raise SystemExit(run(arguments))
    except (OSError, ValueError, KeyError, AttributeError, subprocess.TimeoutExpired) as error:
        print(f'FAIL checker could not finish: {type(error).__name__}: {error}')
        raise SystemExit(1)
