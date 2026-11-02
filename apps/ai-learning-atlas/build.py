"""Build the standalone reader from local canonical sources (Python standard library).

Run: python apps/ai-learning-atlas/build.py [--check]
"""
import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source"


def esc(value):
    return html.escape(str(value), quote=True)


def read(name):
    return (SOURCE / name).read_text(encoding="utf-8")


def topic_link(topic, label=None):
    return f'<a href="#{topic["id"]}">{esc(label or topic["title"])}</a>'


def ordered(numbers, topics):
    result, visiting = [], set()

    def visit(number):
        if number in result:
            return
        if number in visiting:
            raise ValueError(f"Cyclic prerequisites at topic {number}")
        visiting.add(number)
        for dependency in topics[number]["prerequisites"]:
            visit(dependency)
        visiting.remove(number)
        result.append(number)

    for number in sorted(numbers):
        visit(number)
    return result


def check_label(key, text):
    return f'<label class="checkrow"><input class="save-check" id="{esc(key)}" type="checkbox"/>{esc(text)}</label>'


def render_role(role, topics):
    priorities = role["priorities"]
    core = {int(k) for k, v in priorities.items() if v in ("Essential", "Recommended")}
    sequence = ordered(core, topics)
    if set(sequence) != core:
        raise ValueError(f'Missing core prerequisites for {role["slug"]}')
    if not set(role["capstonePrerequisites"]).issubset(core):
        raise ValueError(f'Unsupported capstone for {role["slug"]}')
    chips = ' → '.join(topic_link(topics[n], f'Topic {n:02}') for n in sequence)
    items = []
    for n in sequence:
        t = topics[n]
        status = priorities[str(n)]
        prerequisites = ', '.join(topic_link(topics[p], f'{p:02}') for p in t['prerequisites']) or 'None'
        items.append(f'''<article class="path-item"><h5>{topic_link(t, f'Topic {n:02}: '+t['title'])}</h5>
<span class="status status-{status.lower()}">{status}</span><p><strong>Outcome:</strong> {esc(t['objective'])}</p>
<p><strong>Applied prerequisites:</strong> {prerequisites}. Demonstrate equivalent skills with the <a href="#entry-check">entry check</a>.</p>
<p><strong>Practice:</strong> {esc(t['lab'])}</p><p><strong>Evidence:</strong> {esc(t['proof'])}</p>
<p>Use the small study units in the topic card; completion applies to your declared scope.</p></article>''')
    later = []
    for status in ('Advanced', 'Optional', 'Not required now'):
        links = [topic_link(topics[int(k)]) for k, v in priorities.items() if v == status]
        if links:
            later.append(f'<p><strong>{esc(status)}:</strong> '+ ' · '.join(links)+'</p>')
    bridge = ', '.join(topic_link(topics[n], f'{n:02}') for n in role['bridgeTopics']) or 'No additional topic groups'
    return f'''<details class="role-detail" id="role-{role['slug']}"><summary><div><h3>{esc(role['title'])}</h3><small>{esc(role['summary'])}</small></div></summary>
<div class="role-body"><div class="role-overview"><div class="mini"><b>Main responsibility</b><p>{esc(role['responsibility'])}</p></div>
<div class="mini"><b>Starting knowledge</b><p>{esc(role['background'])}</p><a href="#entry-check">Check skills before skipping</a></div></div>
<div class="callout">Priority describes relevance; the sequence below follows dependencies. A Recommended prerequisite may come before an Essential topic. Added bridges and capstone support: {bridge}.</div>
<div class="phase"><h4>Your dependency-ordered sequence</h4><div class="chips">{chips}</div></div>
<div class="phase"><h4>Core lessons and evidence</h4><div class="path-list">{''.join(items)}</div></div>
<details class="phase"><summary>Later specializations and topics to defer</summary>{''.join(later)}</details>
<div class="role-final"><h4>Role capstone</h4><p>{esc(role['summary'])}</p><p>Use the role-specific build plan and acceptance checks. Demonstrate a clean setup, an unfamiliar input, a realistic failure and a small independent change.</p>
<a href="#project-{role['slug']}">Open capstone and rubric</a> · <a href="#assessment-guide">Review evidence levels</a>
<p>Plan for several weeks to months of part-time practice, depending on entry skills and chosen scope. A completed prototype does not establish production readiness or expert competence.</p></div></div></details>'''


MATH_UNITS = [
    ('Vectors and similarity', 'For a=(1,0) and b=(1,1), calculate dot product, norms and cosine similarity. Compare b with 2b.', 'The dot product sums coordinate products: 1×1+0×1=1. A Euclidean norm is the square root of the sum of squared coordinates: ||a||=1 and ||b||=√2. Cosine=dot/(||a||×||b||)=1/√2≈0.707. For 2b the numerator and its norm both double, leaving the ratio unchanged. Zero vectors require explicit handling because the denominator becomes zero.'),
    ('Derivatives and gradients', 'For L(w)=(w−3)² at w=0, compute the derivative and one gradient step with learning rate 0.1. Compare rate 2.', 'The derivative is the local slope: dL/dw=2(w−3), so at zero it is −6. Gradient descent uses w_new=w−η×dL/dw. With η=0.1: 0−0.1×(−6)=0.6. New loss=(0.6−3)²=5.76, down from 9. With η=2: w_new=12 and loss=81. A larger step can overshoot.'),
    ('Conditional probability', 'Of 100 examples, 10 have a condition. A test flags 8 of those 10 and 9 of the other 90. Find precision and recall.', 'There are 8 true positives, 9 false positives and 2 false negatives. Precision asks what fraction of flagged examples have the condition: TP/(TP+FP)=8/(8+9)≈47%. Recall asks what fraction of condition examples were found: TP/(TP+FN)=8/(8+2)=80%. The denominators answer different questions; high recall alone does not make a positive result reliable.'),
    ('Samples and uncertainty', 'Compare observed rates 4/5 and 80/100. Explain why the same fraction is different evidence. Change one result in each sample.', 'Sample rate=successes/n: 4÷5=0.8 and 80÷100=0.8. Increasing successes by one changes the rate by 1/n: 1/5=20 percentage points versus 1/100=1 percentage point. The small sample is more sensitive to one observation. This is not a confidence interval; inference also depends on representativeness and sampling assumptions.'),
    ('Optimization and numerical checks', 'For a binary target y=1, calculate −ln(p) for p=0.5 and p=0.9. Explain what happens at p=0 and why stable implementations matter.', 'For target y=1, binary log loss reduces to −ln(p), where ln is the natural logarithm. ln(0.5)≈−0.693 gives loss 0.693; ln(0.9)≈−0.105 gives loss 0.105. Assigning more probability to the true outcome lowers this loss. As p approaches zero the loss grows without bound; ln(0) is not finite. Clipping changes the calculation: document it and prefer numerically stable library operations.'),
]


def render_topic(t, topics):
    n = t['number']
    prerequisites = ' · '.join(topic_link(topics[p], f'Topic {p:02}') for p in t['prerequisites']) or 'No formal topic prerequisite'
    internals = ' · '.join(topic_link(topics[p], f'Topic {p:02}') for p in t['internalPrerequisites']) or 'See the original subtopics below'
    units = []
    if n == 4:
        groups = [(title, task, result) for title, task, result in MATH_UNITS]
    else:
        subs = t['subtopics']
        groups = []
        for start in range(0, len(subs), 8):
            chunk = subs[start:start+8]
            title = chunk[0]['title']+' to '+chunk[-1]['title'] if len(chunk)>1 else chunk[0]['title']
            task = ('Choose two concepts from this unit. Define each in your own words, work one small example, and compare an appropriate use with a counterexample. '
                    'Then apply one concept to this topic’s lab: '+t['lab']+' Record the input, expected result and actual evidence. '
                    'For the remaining concepts, record explain / apply / defer, with a reason for every deferral. Split into more sessions rather than rushing unfamiliar material.')
            groups.append((title, task, 'A passing brief names its chosen concepts, shows a worked example and counterexample, and explains how the lab result supports the claim. A list of definitions alone is partial. Deferred concepts remain outside the completion claim.'))
    for i, (title, task, result) in enumerate(groups, 1):
        key = f'unit-{n:02}-{i:02}'
        units.append(f'''<details class="study-unit" id="{key}"><summary>Unit {i} · {esc(title)}</summary>
<div class="topic-details-inner"><p><strong>Format:</strong> {'Worked mathematics lesson' if n==4 else 'Study brief for independent or tutor-guided learning'}; plan 30–60 minutes for a first pass, longer when concepts are new.</p>
<p><strong>Practice:</strong> {esc(task)}</p><p><strong>Before you begin:</strong> choose a small synthetic example, state the relevant terms and predict the outcome.</p>
<p><strong>Check:</strong> explain why the result occurs, change one input and diagnose one wrong result. Compare your evidence with the <a href="#assessment-guide">rubric</a>.</p>
<details><summary>Review notes — attempt the work first</summary><p>{esc(result)}</p></details>
<p><strong>If stuck:</strong> reduce the example to one concept, compare expected and actual behavior, and use the topic reference or <a href="#tutor-brief">tutor brief</a>. Record unresolved questions.</p>
<p><strong>Recall:</strong> revisit this example after two days and adapt it after one week without copying the original solution.</p>
{check_label(key+'-practice', 'I completed this unit’s practice within my declared scope')}
{check_label(key+'-transfer', 'I explained and independently adapted this unit’s example')}
</div></details>''')
    original = ''.join(f'<li id="{s["id"]}">{esc(s["title"])}</li>' for s in t['subtopics'])
    meta = ''.join(f'<span>{esc(v)}</span>' for v in t['meta'])
    workshop = '<p><a href="#beginner-workshop">Use the fully guided local beginner workshop</a> for selected skills in this topic.</p>' if t.get('workshop') or n==2 else ''
    return f'''<article class="topic-card {t['level']}" id="{t['id']}"><div class="topic-header"><span class="topic-number">{n:02}</span><div class="topic-header-main"><h3>{esc(t['title'])}</h3><div class="topic-meta">{meta}</div><p>{esc(t['objective'])}</p></div>
<button type="button" class="topic-done-btn no-print" data-complete-topic="{n:02}" aria-pressed="false">○ Mark scope done</button></div>
<details class="topic-details"><summary>Open learning units, lab, prerequisites and all {len(t['subtopics'])} subtopics</summary><div class="topic-details-inner">
<div class="matrix-actions"><button type="button" class="iconbtn" data-copy-topic="">Copy original subtopics</button><span role="status" class="muted"></span></div>
<div class="labgrid"><div><strong>Before the applied lab</strong>{prerequisites}. <a href="#entry-check">Check equivalent knowledge</a>.</div>
<div><strong>Hands-on lab</strong>{esc(t['lab'])}</div><div><strong>Evidence to collect</strong>{esc(t['proof'])}</div><div><strong>Tools and access</strong>{esc(t['requirements'])}</div></div>
<p class="callout">{esc(t['practiceScope'])}</p>{workshop}
<div class="level-wrap"><h4>Choose your depth</h4><p><strong>Apply now:</strong> the small lab and its input/output, failure and safety checks. <strong>Understand internals:</strong> study the mechanisms and original prerequisite guidance: {internals}. <strong>Train or research:</strong> add mathematical derivations, controlled experiments and <a href="#topic-46-ai-research-methodology">research methods</a>. The applied route does not require every internal subject.</p>
<p>Use your role to choose context, not to claim automatic proficiency. Mark each original subtopic explain / apply / defer in your own notes. <a href="#scope-planner">Create a scope and evidence note</a>.</p></div>
<h4>Small study units</h4><p>Each unit separates practice from independent transfer. Only the beginner workshop and five mathematics units contain supplied worked teaching examples; other units are study briefs, not complete courses.</p>{''.join(units)}
<details><summary>Original subtopic directory — exact names and order</summary><ol class="subtopics">{original}</ol></details>
<p><strong>Reference:</strong> <a href="{esc(t['resource'])}">Topic documentation or reference directory</a>. Online references need internet; check installed versions before using commands.</p>
<p>Before marking this topic scope complete, record selected units, deferred concepts, actual results, a diagnosed failure and an independent variation. See the <a href="#assessment-guide">assessment guide</a>.</p>
</div></details></article>'''


def render_workshop(workshop):
    lessons = []
    for i, lesson in enumerate(workshop['lessons'], 1):
        code = f'<pre><code>{esc(lesson["code"])}</code></pre>' if lesson.get('code') else ''
        files = ''
        for filename in lesson.get('files', []):
            content = (ROOT/'exercises'/filename).read_text(encoding='utf-8')
            files += f'<details><summary>Reference file: {esc(filename)} — read, then copy into your practice folder</summary><p><a href="exercises/{filename}" download>Save {filename}</a> or copy the full text below.</p><pre><code>{esc(content)}</code></pre></details>'
        hints = ''
        if lesson.get('hints'):
            hints = '<details><summary>Challenge hints — open one before the solution</summary><ol>'+''.join('<li>'+esc(h)+'</li>' for h in lesson['hints'])+'</ol></details>'
        for filename in lesson.get('solutionFiles', []):
            content = (ROOT/'exercises'/filename).read_text(encoding='utf-8')
            hints += f'<details><summary>Challenge reference solution: {esc(filename)} — attempt first</summary><p>Explain the solution, then try another input without copying it. <a href="exercises/{filename}" download>Save file</a>.</p><pre><code>{esc(content)}</code></pre></details>'
        actions = ''.join(f'<li>{esc(a)}</li>' for a in lesson['actions'])
        lessons.append(f'''<article class="card lesson" id="lesson-{lesson['id']}"><h3>Lesson {i} · {esc(lesson['title'])}</h3>
<p class="muted">{esc(lesson['time'])} of active practice; estimates depend on entry skills. Covers selected skills in Topic {lesson['topic']:02}.</p>
<p><strong>Outcome:</strong> {esc(lesson['objective'])}</p><p><strong>Essential concept:</strong> {esc(lesson['concept'])}</p>
<h4>Do the work</h4><ol>{actions}</ol>{code}{files}
<p><strong>Expected result:</strong> {esc(lesson['expected'])} These are reference expectations, not claims that your exercise ran.</p>
<p><strong>Verify:</strong> {esc(lesson['verify'])}</p><div class="callout warning"><strong>If blocked:</strong> {esc(lesson['troubleshoot'])}</div>
<h4>Independent variation</h4><p>{esc(lesson['challenge'])}</p>{hints}<p><strong>Recall and transfer:</strong> {esc(lesson['recall'])}</p>
<p><strong>Pass when:</strong> {esc(lesson['pass'])}</p>
{check_label('lesson-'+lesson['id']+'-practice', 'I reproduced the guided exercise and saved actual evidence')}
{check_label('lesson-'+lesson['id']+'-transfer', 'I completed and explained the independent variation')}
<p><a href="#scope-planner">Save a local evidence note</a> · <a href="#{'lesson-'+workshop['lessons'][i]['id'] if i<len(workshop['lessons']) else 'assessment-guide'}">{'Next lesson' if i<len(workshop['lessons']) else 'Assess the project'}</a></p></article>''')
    return f'''<section class="section" id="beginner-workshop"><div class="section-heading"><div><h2>{esc(workshop['title'])}</h2><p>Eight supported lessons, from your first file to a tested service. Start here for a manageable first project; use the role path afterward to expand your skills.</p></div></div>
<div class="card"><h3>Before starting</h3><p>{esc(workshop['requirements'])}</p><p>This is a deterministic teaching fixture. It does not call or train an AI model. You will practice interfaces, data, testing, permissions and evidence before adding model uncertainty.</p>
<p><strong>Accessibility:</strong> every core exercise is text-based. No image/audio perception task or timed assessment is required. A plain text explanation can replace a diagram. Use your editor’s zoom and assistive tools and divide a lesson into shorter sessions.</p>
<p><strong>Finish safely:</strong> stop the local service with Ctrl+C. Keep your evidence; the exercise creates no cloud resources. Delete only the practice folder you created if you choose to remove it.</p>
<label for="lesson-focus">Reading view</label> <select id="lesson-focus"><option value="">Show all lessons</option>{''.join(f'<option value="lesson-{l["id"]}">{i}. {esc(l["title"])}</option>' for i,l in enumerate(workshop['lessons'],1))}</select><p id="lesson-counter" role="status">Lesson progress is self-reported.</p></div>
{''.join(lessons)}<details class="card"><summary>Sample extension — compare after attempting Lesson 8</summary><p>Add a public record with id public-location, question location and an explicitly synthetic answer. A passing test checks both the answer and public-location source for input ' LOCATION '. Keep permission tests passing. Merely adding a record without tests is partial completion.</p><pre><code>DOCUMENTS.append({{"id": "public-location", "owner": "public", "question": "location", "answer": "Practice Room 1."}})
assert answer(' LOCATION ') == {{"answer": "Practice Room 1.", "source": "public-location"}}</code></pre><p>Failing example: accepting a request’s user field as a trusted identity. Correct it by establishing identity at a trusted boundary; the fixture intentionally keeps every HTTP caller as guest.</p></details></section>'''


def build():
    data = json.loads(read('curriculum.json'))
    workshop = json.loads(read('workshop.json'))
    topics = {t['number']: t for t in data['topics']}
    template = read('template.html')
    learning = read('learning.html')
    entry, remainder = learning.split('</section>', 1)
    replacements = {'ENTRY_SECTION': entry+'</section>',
                    'LEARNING_SECTIONS': render_workshop(workshop)+remainder,
                    'EXTRA_STYLE': '<style>'+read('learning.css')+'</style>',
                    'READER_JS': read('reader.js'), 'DASHBOARD_JS': read('dashboard.js'),
                    'LEARNING_JS': '<script>'+read('learning.js')+'</script>'}
    search = []
    for t in topics.values():
        replacements[f'TITLE_{t["number"]}'] = esc(t['title'])
        replacements[f'TOPIC_{t["number"]}'] = render_topic(t, topics)
        search.append(dict(type='Topic', title=t['title'], context=t['objective'], href='#'+t['id']))
        search.extend(dict(type='Subtopic', title=sub['title'], context=t['title'], href='#'+sub['id']) for sub in t['subtopics'])
    for role in data['roles']:
        replacements['ROLE_'+role['slug']] = render_role(role, topics)
        project = re.sub(r'<div class="chips">.*?</div>', '<div class="chips">'+''.join(topic_link(topics[n], f'{n:02} · '+topics[n]['title']) for n in ordered(role['capstonePrerequisites'], topics))+'</div>', role['project'], flags=re.S)
        project = project.replace('</article>', '<p><a href="#assessment-guide">Use the common assessment rubric</a>. Add a measured comparison with a simpler alternative; record quality, latency, cost and maintenance assumptions. Rehearse a changed requirement and document what would still be needed for real deployment.</p></article>')
        replacements['PROJECT_'+role['slug']] = project
        search.append(dict(type='Profession', title=role['title'], context=role['responsibility'], href='#role-'+role['slug']))
    for i, lesson in enumerate(workshop['lessons'], 1):
        search.append(dict(type='Lesson', title=lesson['title'], context=lesson['objective'], href='#lesson-'+lesson['id']))
    # Canonical glossary records also feed search; their definitions are rendered in learning.html.
    for term in json.loads(read('glossary.json')):
        search.append(dict(type='Glossary', title=term['term'], context=term['definition'], href='#glossary-'+term['id']))
    replacements['GLOSSARY_ROWS'] = ''.join(f'<div id="glossary-{esc(t["id"])}"><dt>{esc(t["term"])}</dt><dd>{esc(t["definition"])}</dd></div>' for t in json.loads(read('glossary.json')))
    replacements['ATLAS_DATA'] = json.dumps(dict(search=search, priorities={r['slug']:r['priorities'] for r in data['roles']}), ensure_ascii=False).replace('<', '\\u003c')
    # Replace the template once, then tokens belonging to authored learning sections.
    for key, value in replacements.items():
        template = template.replace('{{'+key+'}}', value)
    template = template.replace('{{GLOSSARY_ROWS}}', replacements['GLOSSARY_ROWS'])
    if re.search(r'\{\{[A-Z_0-9-]+\}\}', template):
        raise ValueError('Unresolved build token')
    return template


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    output = build()
    target = ROOT/'index.html'
    if args.check:
        if target.read_text(encoding='utf-8') != output:
            raise SystemExit('index.html is stale; run build.py')
        print('Standalone reader matches its sources.')
    else:
        target.write_text(output, encoding='utf-8', newline='\n')
        print('Built', target)
