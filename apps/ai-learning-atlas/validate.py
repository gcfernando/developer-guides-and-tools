"""Validate generated content, curriculum dependencies and preserved anchors."""
import hashlib
import json
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build import ROOT, build, ordered


class Reader(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.scripts, self.headings = [], [], [], []
        self.capture = None
        self.script_text = ''
        self.subtopics = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'script':
            self.script_type = attrs.get('type')
            self.script_text = ''
            self.capture = 'script'
        if tag == 'li' and attrs.get('id', '').startswith('subtopic-'):
            self.capture = 'subtopic'
            self.subtopics.append([attrs['id'], ''])
        if tag == 'h1':
            self.headings.append(tag)

    def handle_data(self, data):
        if self.capture == 'script':
            self.script_text += data
        if self.capture == 'subtopic':
            self.subtopics[-1][1] += data

    def handle_endtag(self, tag):
        if tag == 'script':
            if self.script_type == 'application/json':
                self.data = json.loads(self.script_text)
            else:
                self.scripts.append(self.script_text)
            self.capture = None
        if tag == 'li' and self.capture == 'subtopic':
            self.capture = None


def main():
    page = (ROOT/'index.html').read_text(encoding='utf-8')
    assert page == build(), 'Generated page is stale'
    reader = Reader()
    reader.feed(page)
    assert len(reader.headings) == 1, 'Expected one H1'
    assert not [key for key, count in Counter(reader.ids).items() if count > 1], 'Duplicate IDs'
    ids = set(reader.ids)
    for href in reader.links:
        if href.startswith('#'):
            assert unquote(href[1:]) in ids, f'Broken fragment {href}'
        elif href and not urlsplit(href).scheme:
            assert (ROOT/unquote(urlsplit(href).path)).exists(), f'Missing local file {href}'
    for result in reader.data['search']:
        assert result['href'][1:] in ids, f'Broken search target {result}'
    curriculum = json.loads((ROOT/'source/curriculum.json').read_text(encoding='utf-8'))
    topics = {t['number']: t for t in curriculum['topics']}
    assert len(topics) == 51 and len(curriculum['roles']) == 14
    assert len(reader.subtopics) == 1607
    expected_subtopics = [[s['id'], s['title']] for t in topics.values() for s in t['subtopics']]
    assert reader.subtopics == expected_subtopics, 'Directory differs from canonical subtopics'
    digest = hashlib.sha256(json.dumps(reader.subtopics, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
    assert digest == (ROOT/'source/subtopics.sha256').read_text().strip(), 'Original subtopics or their order changed'
    for role in curriculum['roles']:
        core = {int(k) for k,v in role['priorities'].items() if v in ('Essential', 'Recommended')}
        sequence = ordered(core, topics)
        assert set(sequence) == core, f'Missing prerequisites: {role["slug"]}'
        assert set(role['capstonePrerequisites']) <= core, f'Capstone gap: {role["slug"]}'
        for number in sequence:
            assert all(sequence.index(p) < sequence.index(number) for p in topics[number]['prerequisites'])
    assert '5% essential theory' not in page and '10% theory' not in page
    assert all(f'lesson-{name}' in ids for name in ('setup','function','data','baseline','endpoint','permissions','evaluation','capstone'))
    assert 'http-equiv="refresh"' not in page.lower()
    print(f'Validated 51 topics, 1,607 preserved subtopics, 14 dependency-ordered paths, {len(reader.ids)} unique IDs and {len(reader.data["search"])} search targets.')


if __name__ == '__main__':
    main()
