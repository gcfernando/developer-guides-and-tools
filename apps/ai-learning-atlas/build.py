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


def render_authored_units(topic):
    """Render authored concept groups without changing the original directory."""
    units = json.loads(read('units.json'))[str(topic['number'])]
    subtopic_titles = {item['id']: item['title'] for item in topic['subtopics']}
    result = []
    for i, unit in enumerate(units, 1):
        key = f"unit-{topic['number']:02}-{i:02}"
        coverage = ' · '.join(f'<a href="#{esc(s)}" title="{esc(s)}">{esc(subtopic_titles[s])}</a>' for s in unit['covered'])
        questions = ''.join(f'<li>{esc(q["question"])}</li>' for q in unit['questions'])
        answers = ''.join(f'<li>{esc(q["answer"])}</li>' for q in unit['questions'])
        minutes = unit.get('minutes', [30, 60])
        status = '<p class="callout warning">Study brief — full lesson not yet written</p>' if unit.get('status') == 'brief' else ''
        result.append(f'''<details class="study-unit" id="{key}"><summary>Unit {i} · {esc(unit['title'])}</summary>
<div class="topic-details-inner">{status}
<p><strong>Objective:</strong> {esc(unit['objective'])}</p>
<p><strong>Estimate:</strong> {minutes[0]}–{minutes[1]} minutes for this bounded first pass; entry skills and deeper study change the effort.</p>
<p><strong>Key idea:</strong> {esc(unit['idea'])}</p>
<p><strong>Worked example — reference expectation:</strong></p><pre><code>{esc(unit['example'])}</code></pre>
<p class="unit-practice"><strong>Practice:</strong> {esc(unit['practice'])}</p>
<p><strong>Check questions:</strong></p><ol>{questions}</ol>
<details class="answer-key"><summary>Answer key — attempt the questions first</summary><ol>{answers}</ol><p><strong>Common mistake:</strong> {esc(unit['mistake'])}</p></details>
<p><strong>Related original subtopics (reference map):</strong> {coverage}</p>
<p><a href="#tutor-brief">Recovery and recall guidance</a> · <a href="#assessment-guide">Evidence levels and earlier saved scopes</a>.</p>
{check_label(key+'-practice', 'I completed this unit’s practice within my declared scope')}
{check_label(key+'-transfer', 'I explained and independently adapted this unit’s example')}
</div></details>''')
    return result


def reference_file(filename, prefix, caption=None):
    """The download uses exactly the displayed text; adjacent files are authoring inputs."""
    content = (ROOT / 'exercises' / filename).read_text(encoding='utf-8')
    key = prefix + '-' + filename.replace('.', '-')
    return f'''<details class="reference-file"><summary>{esc(caption or 'Reference file: '+filename)}</summary>
<p><button type="button" class="iconbtn" data-download="{esc(filename)}" data-code="{esc(key)}">Save {esc(filename)}</button></p>
<pre id="{esc(key)}" tabindex="0"><code>{esc(content)}</code></pre></details>'''


def render_ml_lab(number):
    lab = json.loads(read('ml-labs.json')).get(str(number))
    if not lab:
        return ''
    checks = ''.join(f'<li>{esc(text)}</li>' for text in lab.get('leakageChecks', []))
    sources = ''
    if number == 7:
        sources = '<div id="ml-reference-files">'+''.join(reference_file(name, 'ml-source') for name in ('ml_core.py', 'test_ml_core.py'))+'</div>'
    return f'''<div class="ml-worked-lab" id="ml-lab-{number:02}"><h4>{esc(lab['title'])}</h4>
<p>{esc(lab['explanation'])}</p><p>Python 3.10+; standard library only. Save <a href="#ml-reference-files">ml_core.py and its tests</a> together, then run <code>python ml_core.py</code> and <code>python -m unittest test_ml_core -v</code>. Run this focused trace from the same folder:</p>
<pre tabindex="0"><code>{esc(lab['code'])}</code></pre><p><strong>Reference expectation:</strong></p><pre tabindex="0">{esc(lab['expected'])}</pre>
{('<h5>Leakage types and detection checks</h5><ul>'+checks+'</ul>') if checks else ''}
<p><strong>Independent experiment:</strong> {esc(lab['practice'])}</p>{sources}</div>'''


def organize_reader(template):
    """Keep primary navigation and static reading order aligned, preserving each section."""
    order = ['start', 'entry-check', 'beginner-workshop', 'choose-role', 'role-paths',
             'projects', 'progress', 'library', 'relevance', 'glossary',
             'assessment-guide', 'learn-with-ai', 'official-resources']
    matches = list(re.finditer(r'<section\b[^>]*>.*?</section>', template, re.S))
    sections = {}
    for match in matches:
        identifier = re.search(r'\bid="([^"]+)"', match.group())
        if not identifier:
            raise ValueError('A primary section needs an ID')
        sections[identifier[1]] = match.group()
    if not set(order) <= sections.keys():
        raise ValueError('Missing primary navigation destination')
    # Section contents include every topic in the original order; move whole sections.
    template = template[:matches[0].start()]+'\n'.join(sections[key] for key in order+[
        key for key in sections if key not in order])+template[matches[-1].end():]
    for identifier, label in [('topic-index', 'Browse the complete topic index by level'),
                              ('relevance', 'Open the profession relevance matrix'),
                              ('learn-with-ai', 'Open the full AI tutor workbook and examples')]:
        pattern = r'(<section\b[^>]*id="'+identifier+r'"[^>]*>)(.*?)(</section>)'
        def collapse_reference(match):
            body = match[2]
            heading = re.search(r'<div class="section-heading">.*?</div></div>', body, re.S)
            if not heading:
                raise ValueError('Missing reference section heading')
            compact = compact_tutor() if identifier == "learn-with-ai" else ""
            return match[1]+body[:heading.end()]+compact+'<details class="reference-panel"><summary>'+label+'</summary>'+body[heading.end():]+'</details>'+match[3]
        template = re.sub(pattern, collapse_reference, template, flags=re.S)
    # External addresses are optional online destinations, never runtime assets.
    head, scripts = template.split('<script id="atlas-data"', 1)
    head = re.sub(r'(<a\b[^>]*href="https?://[^"]*"[^>]*>)(.*?)(</a>)',
                  lambda m: m[1]+m[2]+' <small class="online-label">(online)</small>'+m[3], head, flags=re.S)
    return head+'<script id="atlas-data"'+scripts


def label_online_links(markup):
    return re.sub(r'(<a\b[^>]*href="https?://[^"]*"[^>]*>)(.*?)(</a>)',
                  lambda m: m[1]+m[2]+' <small class="online-label">(online)</small>'+m[3], markup, flags=re.S)


def graded_rubric():
    tutor = json.loads(read('tutor-materials.json'))
    levels = ['Not yet', 'Partial', 'Pass', 'Strong']
    headings = ''.join('<th scope="col">'+level+'</th>' for level in levels)
    rows = []
    for dimension in tutor['rubric']:
        cells = ''.join('<td>'+esc(dimension['levels'][level]['description'])+'<p><em>Example:</em> '+esc(dimension['levels'][level]['example'])+'</p></td>' for level in levels)
        rows.append('<tr><th scope="row">'+esc(dimension['dimension'])+'</th>'+cells+'</tr>')
    return '<div class="tablewrap" tabindex="0" role="region" aria-label="Four-level assessment rubric"><table><caption>Assess all four dimensions for your declared scope</caption><thead><tr><th scope="col">Dimension</th>'+headings+'</tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'


def compact_tutor():
    prompt = json.loads(read('tutor-materials.json'))['compactPrompt']
    return '<div class="card tutor-content compact-tutor"><h3>Compact tutor prompt</h3><p>Use this focused brief for one declared scope. <button class="iconbtn" type="button" data-copy="compact-tutor-prompt">Copy compact prompt</button></p><pre id="compact-tutor-prompt" tabindex="0">'+esc(prompt)+'</pre></div>'


def optional_model_lesson():
    files = ''.join(reference_file(name, 'model-adapter') for name in ('model_adapter.py', 'test_model_adapter.py'))
    return f'''<details class="card optional-model-panel"><summary>Optional Lesson 9 — model adapter practice after the core workshop</summary>
<article class="optional-lesson" id="lesson-model-adapter"><h3>Optional Lesson 9 · Observe a model through a checked contract</h3>
<p>The deterministic MockModel runs fully offline with Python 3.10+ and no account. The RealModel is an intentionally unimplemented provider adapter for you to fill using current official documentation. That branch requires an account and may cost money; choose it deliberately and keep credentials out of code, notes and backups.</p>
<ol><li>Save both files together. Run <code>python model_adapter.py</code> and <code>python -m unittest test_model_adapter -v</code>.</li>
<li>Inspect SCHEMA: require exactly answer (string) and source (string or null). The supplied validator checks this particular schema contract; it is not a general JSON Schema implementation. Explain why valid structure does not establish factuality or authorization.</li>
<li>Pass the malformed mock response through validation, observe its rejection, and add a wrong-type test without silently accepting the content.</li>
<li>Compare all three responses and record the measured seconds. Mock outputs match by design. With a real provider, record observed variation or no variation; three matching runs do not prove determinism. Mock timings are local measurements, not provider benchmarks.</li>
<li>If you choose a real provider, implement generate() returning its response text, using its current SDK and credential instructions. Record real token usage where provided. Look up that provider’s published current input/output prices and pass those rates into estimate_cost; state currency and assumptions. Cached, reasoning, batch, tool and other billing rules may require a different calculation. Do not invent usage or prices.</li></ol>
<p><strong>Reference expectation:</strong> mock responses contain answer “Open 09:00–17:00.” and source “public-hours”; malformed JSON is rejected. Real responses, latency, token usage and billing remain untested until you actually run and record them.</p>
<p><strong>Independent variation:</strong> make the mock return a missing source field, then repair the contract and add a regression assertion. Keep reference, simulated and measured evidence distinct.</p>{files}</article></details>'''


def currency_note(number):
    notes = {
        16: 'Model and architecture names are examples. Check the actual model’s current availability, license, context limits and documented behavior before choosing it.',
        27: 'MCP and A2A change over time. Check the current <a href="https://modelcontextprotocol.io/specification/latest">MCP specification</a> and <a href="https://a2a-protocol.org/latest/">A2A specification</a> before implementing either protocol. A protocol format does not grant tool authority.',
        28: 'Vendor SDKs and frameworks evolve. Pin the installed version and verify its current official API documentation, including <a href="https://developers.openai.com/api/docs/">OpenAI’s documentation</a> when relevant. This directory does not promise a currently supported signature or model.',
        34: 'EU AI Act obligations apply in phases and depend on the system and role. Check the current <a href="https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai">European Commission guidance and official legal text</a> for applicable requirements; this lesson does not establish compliance.'
    }
    return '<p class="callout currency-note"><strong>Check current status:</strong> '+notes[number]+'</p>' if number in notes else ''


def defer_topic_body(markup, topic):
    """Keep stable progress controls live; defer explanatory nodes until first use."""
    holder = []
    units = json.loads(read('units.json'))[str(topic['number'])]
    def move_check(match):
        unit_number = int(match[2].split('-')[2])
        context = f'Unit {unit_number} · '+units[unit_number-1]['title']
        holder.append(match[1].replace('<input ', '<input data-progress-context="'+esc(context)+'" ', 1))
        return ''
    markup = re.sub(r'(<label class="checkrow"><input class="save-check" id="(unit-\d{2}-\d{2}-(?:practice|transfer))" type="checkbox"/?>.*?</label>)', move_check, markup, flags=re.S)
    if len(holder) != 2*len(units):
        raise ValueError(f"Missing stable progress controls in topic {topic['number']}")
    match = re.search(r'(<details class="topic-details"><summary>.*?</summary>)(.*)(</details></article>)', markup, re.S)
    if not match:
        raise ValueError('Topic body boundary not found')
    lab = f'<p class="topic-lab-line"><strong>Lab:</strong> {esc(topic["lab"])}</p>'
    header = markup[:match.start()].replace('</p></div>\n<button', '</p>'+lab+'</div>\n<button', 1)
    if lab not in header:
        raise ValueError('Missing lightweight lab header')
    encoded_body = json.dumps(label_online_links(match[2]), ensure_ascii=False).replace('<', r'\u003c')
    return header+\
        '<div hidden aria-hidden="true" data-progress-holder="">'+''.join(holder)+'</div>'+match[1]+\
        '<div class="topic-body-host"></div><template data-topic-body=""><script type="application/json" data-topic-json="">'+encoded_body+'</script></template>'+match[3]


def defer_path_bodies(markup):
    return re.sub(r'(<article class="path-item"><h5>.*?</h5>\s*<span\b[^>]*>.*?</span>)(.*?)(</article>)',
                  lambda m: m[1]+'<template data-path-body="">'+m[2]+'</template>'+m[3], markup, flags=re.S)


def render_role(role, topics):
    priorities = role["priorities"]
    core = {int(k) for k, v in priorities.items() if v in ("Essential", "Recommended")}
    sequence = role.get('sequence') or ordered(core, topics)
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
    phases = []
    for i, phase in enumerate(role.get('phases', []), 1):
        tasks = ''.join(f'<li>{esc(task)}</li>' for task in phase['checkpoint']['tasks'])
        rubric = ''.join(f'<dt>{esc(level)}</dt><dd>{esc(description)}</dd>' for level, description in phase['checkpoint']['rubric'].items())
        phase_chips = ' → '.join(topic_link(topics[n], f'Topic {n:02}') for n in phase['topics'])
        hours = phase['hours']
        stages = ''.join(f'<li><strong>{stage["minutes"]} min:</strong> {esc(stage["activity"])}</li>' for stage in phase['sessionPlan'])
        session = f'<details class="session-plan"><summary>60-minute tutor session</summary><template data-session-body=""><p>Use after the relevant phase units or equivalent entry demonstrations. Demo: <a href="#{esc(phase["demoUnit"])}">{esc(phase["demoUnit"])}</a>.</p><ol>{stages}</ol></template></details>'
        phases.append(f'''<div class="role-phase" id="{esc(phase['id'])}"><h4>Phase {i}: {esc(phase['title'])}</h4>
<p>{hours[0]:g}–{hours[1]:g} first-pass hours for {phase['unitCount']} units. {'Recommended after the preceding checkpoint; all phases remain open.' if i > 1 else 'Begin here or demonstrate equivalent entry skills.'}</p>
<div class="chips">{phase_chips}</div>
<details class="phase-gate"><summary>{esc(phase['checkpoint']['title'])}</summary><ol>{tasks}</ol><dl>{rubric}</dl><p>{esc(phase['checkpoint']['next'])}</p></details>
{session}
</div>''')
    effort = ''
    if role.get('hours'):
        effort = f'<p class="path-estimate"><strong>First-pass effort:</strong> {role["hours"][0]:g}–{role["hours"][1]:g} hours. {esc(role["effortBasis"])}</p>'
    return f'''<details class="role-detail" id="role-{role['slug']}"><summary><span class="role-summary-text"><strong>{esc(role['title'])}</strong><small>{esc(role['summary'])}</small></span></summary>
<div class="role-body"><h3>{esc(role['title'])}</h3>{effort}<div class="role-overview"><div class="mini"><b>Main responsibility</b><p>{esc(role['responsibility'])}</p></div>
<div class="mini"><b>Starting knowledge</b><p>{esc(role['background'])}</p><a href="#entry-check">Check skills before skipping</a></div></div>
<div class="callout">Priority describes relevance; the sequence below follows dependencies. A Recommended prerequisite may come before an Essential topic. Added bridges and capstone support: {bridge}.</div>
<div class="phase"><h4>Your dependency-ordered sequence</h4><div class="chips">{chips}</div></div>{''.join(phases)}
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
    units = render_authored_units(t)
    original = ''.join(f'<li id="{s["id"]}">{esc(s["title"])}</li>' for s in t['subtopics'])
    meta = ''.join(f'<span>{esc(v)}</span>' for v in t['meta'])
    workshop = '<p><a href="#beginner-workshop">Use the fully guided local beginner workshop</a> for selected skills in this topic.</p>' if t.get('workshop') or n==2 else ''
    return f'''<article class="topic-card {t['level']}" id="{t['id']}"><div class="topic-header"><span class="topic-number">{n:02}</span><div class="topic-header-main"><h3>{esc(t['title'])}</h3><div class="topic-meta">{meta}</div><p>{esc(t['objective'])}</p></div>
<button type="button" class="topic-done-btn no-print" data-complete-topic="{n:02}" aria-pressed="false" aria-label="Topic {n:02} scope done">○ Scope done</button></div>
<details class="topic-details"><summary>Open learning units, lab, prerequisites and all {len(t['subtopics'])} subtopics</summary><div class="topic-details-inner">
<div class="matrix-actions"><button type="button" class="iconbtn" data-copy-topic="">Copy original subtopics</button></div>
<div class="labgrid"><div><strong>Before the applied lab</strong>{prerequisites}. <a href="#entry-check">Check equivalent knowledge</a>.</div>
<div><strong>Hands-on lab</strong>{esc(t['lab'])}</div><div><strong>Evidence to collect</strong>{esc(t['proof'])}</div><div><strong>Tools and access</strong>{esc(t['requirements'])}</div></div>
<p class="callout">{esc(t['practiceScope'])}</p>{workshop}
<div class="level-wrap"><h4>Choose your depth</h4><p><strong>Apply now:</strong> the small lab and its input/output, failure and safety checks. <strong>Understand internals:</strong> study the mechanisms and original prerequisite guidance: {internals}. <strong>Train or research:</strong> add mathematical derivations, controlled experiments and <a href="#topic-46-ai-research-methodology">research methods</a>. The applied route does not require every internal subject.</p>
<p>Use your role to choose context, not to claim automatic proficiency. Mark each original subtopic explain / apply / defer in your own notes. <a href="#scope-planner">Create a scope and evidence note</a>.</p></div>
<h4>Small study units</h4><p>Each concept group separates practice from independent transfer. Coverage links map the unchanged directory to one unit each; an example teaches a bounded starting point rather than every advanced detail. Units awaiting full lessons are labeled explicitly.</p>{''.join(units)}
{currency_note(n)}
{render_ml_lab(n)}
<details><summary>Original subtopic directory — exact names and order</summary><ol class="subtopics" data-topic-subtopics="{n:02}"></ol></details>
<p><strong>Reference:</strong> <a href="{esc(t['resource'])}">Topic documentation or reference directory</a>. Online references need internet; check installed versions before using commands.</p>
<p>Before marking this topic scope complete, record selected units, deferred concepts, actual results, a diagnosed failure and an independent variation. See the <a href="#assessment-guide">assessment guide</a>.</p>
</div></details></article>'''


def render_workshop(workshop):
    lessons = []
    for i, lesson in enumerate(workshop['lessons'], 1):
        code = f'<pre><code>{esc(lesson["code"])}</code></pre>' if lesson.get('code') else ''
        files = ''
        for filename in lesson.get('files', []):
            files += reference_file(filename, 'lesson-'+lesson['id'])
        hints = ''
        if lesson.get('hints'):
            hints = '<details><summary>Challenge hints — open one before the solution</summary><ol>'+''.join('<li>'+esc(h)+'</li>' for h in lesson['hints'])+'</ol></details>'
        for filename in lesson.get('solutionFiles', []):
            hints += reference_file(filename, 'solution-'+lesson['id'], 'Challenge reference solution: '+filename+' — attempt first')
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
{''.join(lessons)}{optional_model_lesson()}<details class="card"><summary>Sample extension — compare after attempting Lesson 8</summary><p>Add a public record with id public-location, question location and an explicitly synthetic answer. A passing test checks both the answer and public-location source for input ' LOCATION '. Keep permission tests passing. Merely adding a record without tests is partial completion.</p><pre><code>DOCUMENTS.append({{"id": "public-location", "owner": "public", "question": "location", "answer": "Practice Room 1."}})
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
                    'EXTRA_STYLE': '', 'ATLAS_STYLE': '<style>'+read('atlas.css')+'</style>',
                    'READER_JS': read('experience.js')+'\n'+read('reader.js'), 'DASHBOARD_JS': read('dashboard.js'),
                    'LEARNING_JS': '<script>'+read('learning.js')+'</script>'}
    replacements['GRADED_RUBRIC'] = graded_rubric()
    search = []
    lazy_targets = {}
    for t in topics.values():
        replacements[f'TITLE_{t["number"]}'] = esc(t['title'])
        replacements[f'DIFFICULTY_{t["number"]}'] = esc(t['meta'][-1].split()[-1])
        topic_markup = defer_topic_body(render_topic(t, topics), t)
        replacements[f'TOPIC_{t["number"]}'] = topic_markup
        for identifier in re.findall(r'\bid="([^"]+)"', topic_markup):
            if not re.match(r'(?:topic|subtopic|unit)-\d{2}(?:-|$)', identifier):
                lazy_targets[identifier] = t['number']
        search.append(dict(type='Topic', title=t['title'], context=t['objective'], href='#'+t['id']))
        search.extend(dict(type='Subtopic', title=sub['title'], context=t['title'], href='#'+sub['id']) for sub in t['subtopics'])
    for role in data['roles']:
        replacements['ROLE_'+role['slug']] = defer_path_bodies(render_role(role, topics))
        if role.get('hours'):
            tile = re.compile(r'(<a class="role-tile" href="#role-'+re.escape(role['slug'])+r'">.*?)(</a>)', re.S)
            template = tile.sub(lambda match: match[1]+f'<small class="path-estimate">{role["hours"][0]:g}–{role["hours"][1]:g} first-pass hours; depends on entry skills.</small>'+match[2], template)
        project = re.sub(r'<div class="chips">.*?</div>', '<div class="chips">'+''.join(topic_link(topics[n], f'{n:02} · '+topics[n]['title']) for n in ordered(role['capstonePrerequisites'], topics))+'</div>', role['project'], flags=re.S)
        project = project.replace('</article>', '<p><a href="#assessment-guide">Use the common assessment rubric</a>. Add a measured comparison with a simpler alternative; record quality, latency, cost and maintenance assumptions. Rehearse a changed requirement and document what would still be needed for real deployment.</p></article>')
        replacements['PROJECT_'+role['slug']] = project
        search.append(dict(type='Profession', title=role['title'], context=role['responsibility'], href='#role-'+role['slug']))
    for i, lesson in enumerate(workshop['lessons'], 1):
        search.append(dict(type='Lesson', title=lesson['title'], context=lesson['objective'], href='#lesson-'+lesson['id']))
    search.append(dict(type='Lesson', title='Optional model adapter practice', context='MockModel, provider stub, JSON schema, latency and token-cost assumptions', href='#lesson-model-adapter'))
    # Canonical glossary records also feed search; their definitions are rendered in learning.html.
    for term in json.loads(read('glossary.json')):
        search.append(dict(type='Glossary', title=term['term'], context=term['definition'], href='#glossary-'+term['id']))
    replacements['GLOSSARY_ROWS'] = ''.join(f'<div id="glossary-{esc(t["id"])}"><dt>{esc(t["term"])}</dt><dd>{esc(t["definition"])}</dd></div>' for t in json.loads(read('glossary.json')))
    effort = {r['slug']: {'hours': r['hours'], 'unitCount': r['unitCount'], 'basis': r['effortBasis']} for r in data['roles'] if r.get('hours')}
    replacements['ATLAS_DATA'] = json.dumps(dict(search=search, priorities={r['slug']:r['priorities'] for r in data['roles']}, effort=effort, lazyTargets=lazy_targets), ensure_ascii=False).replace('<', '\\u003c')
    # Replace the template once, then tokens belonging to authored learning sections.
    for key, value in replacements.items():
        template = template.replace('{{'+key+'}}', value)
    template = template.replace('{{GLOSSARY_ROWS}}', replacements['GLOSSARY_ROWS'])
    if re.search(r'\{\{[A-Z_0-9-]+\}\}', template):
        raise ValueError('Unresolved build token')
    template = organize_reader(template)
    # HTML void tags have no XML self-closing syntax; avoid hundreds of Nu notices.
    template = re.sub(r'(<(?:area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)\b[^>]*?)/>', r'\1>', template)
    # Scrolling code examples must be reachable without a pointing device.
    template = re.sub(r'<pre(?![^>]*\btabindex=)([^>]*)>', r'<pre tabindex="0"\1>', template)
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
