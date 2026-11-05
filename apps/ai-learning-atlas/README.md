---
layout: default
permalink: /apps/ai-learning-atlas/guide/
title: "AI Learning Atlas — Study Paths and Progress Guide"
description: Follow dependency-ordered AI study paths, complete a supported local beginner workshop, and record learning evidence.
---

[Developer guides and tools](../../README.md) · **Interactive learning**

<a id="-ai-learning-atlas--offline-reader-and-progress-guide"></a>

# AI Learning Atlas — Study Paths and Progress Guide

Open the [AI Learning Atlas](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-learning-atlas/index.html) to choose a professional learning path, complete a supported beginner workshop, study 219 authored units, search 51 topic groups and 1,607 original subtopics, and record evidence. Start with the onboarding choice, follow a role-focused library and use the next-step bar to resume. The reader includes light/dark themes and responsive navigation.

<a id="guide-prerequisites"></a>

## Prerequisites

A modern browser opens the generated `index.html` directly from a local file. Core reading needs no server or external fonts, scripts or assets. JavaScript renders the stored topic bodies and enables search, filters, role selection and progress. Every supplied reference file is embedded; Save buttons create downloads from the displayed text with Blob URLs, so the adjacent `exercises/` directory is not needed for reader downloads. Online reference links are labeled and require internet.

The published URL uses a lighter hosted reader with the same content, anchors, controls and browser-storage keys. It loads versioned assets from the same site and yields between loading sections to keep the page responsive. Its **Download the complete offline HTML** link provides the original standalone file. A loading failure displays an error, Retry and a link to that complete file; it never silently presents a partial reader as ready.

The eight-lesson workshop needs Python 3.10 or newer, a text editor and terminal. It uses the standard library, synthetic data and a local-only service. No cloud account, GPU, package installation, model or API key is required after Python is available. Installing Python and following online references need internet. The optional model-adapter lesson adds a fully offline deterministic mock and a provider-filled real-model stub. Real use needs the chosen provider account, current integration documentation and possibly paid usage. Other topic labs state their tool and resource assumptions separately.

<a id="guide-quick-start"></a>

## Quick start

1. Choose an onboarding route: new programmer, existing coder or ML/research. Use the entry check to establish starting skills; new programmers can begin the supported beginner workshop before taking a full role path.
2. Choose a profession with the main selector. Priority labels describe relevance; the sequence follows applied prerequisites, including Recommended bridges before dependent Essential topics. Eight longer paths have three phases with recommended checkpoint projects. First-pass hour ranges are derived from unit estimates and depend on entry skills; projects and additional practice need more time.
3. Choose the applied, internals or research depth within a topic. Record selected concepts, deferred material and evidence in the scope note.
4. Complete the guided exercise, then an independent variation. Keep actual results, an explained failure, and clean-folder setup instructions.
5. Use the four-dimension, four-level assessment rubric and the role-specific project checks. Mark only the scope you demonstrated complete. Phase checkpoints recommend a next step without locking content.
6. Export a progress backup before moving files, clearing browser data or changing browser profiles.

The eight-lesson FAQ workshop teaches engineering foundations with deterministic rules and synthetic data. Separate runnable ML fixtures cover Topics 07–12 and the Topic 04 uncertainty example; the optional model-adapter lesson distinguishes mock behavior from actual provider observations. All 219 units include an objective, explanation, worked reference example, specific practice, answered check questions and a misconception. Each unit links to related original subtopics as a reference map: one mapping per original subtopic does not mean every listed mechanism is fully taught or every project variant is implemented. Use the original directory to plan deeper study and record deferred concepts. See the assessment section for evidence limits and deployment considerations.

<a id="guide-search-and-navigation"></a>

## Search and navigation

Search covers roles, topics, original subtopics, workshop lessons and glossary definitions. Type at least two characters; all query terms must appear in a result title or context. Up to 35 results are shown. Selecting a result reveals collapsed content and any lesson hidden by reading focus.

Press `/` outside editable fields to focus search. Down/Up Arrow selects results through the combobox active option while focus remains in the field; Enter opens the selected result. Escape closes the results and clears the query and active option. Mobile navigation is inert while closed, and Escape returns focus to the menu button.

On a first visit, the workshop shows Lesson 1. Choose any core lesson or show all with Reading view; your choice resumes after reload when local storage is available. This local reading preference is separate from exported progress. The optional model-adapter lesson has its own link. Topic and unit links render their deferred content and open ancestor disclosures before navigation. The role-focused library offers level, priority, difficulty and completion filters; All topics restores the full directory. Print preparation reveals deferred reading content and removes code-panel height limits.

## Progress, backups and privacy

The page stores checks, role, theme, workshop reading view and one evidence note locally when browser storage is available. It makes no network calls to save progress. A hosted reader and a local file have separate browser storage contexts. Local-file storage, private browsing, moving a file or clearing site data can affect persistence; keep a JSON backup.

| Control | Meaning |
|---|---|
| Topic scope check / Topic NN scope done | Self-reported completion for a declared scope; not proof of all subtopics |
| Unit practice and transfer checks | Separate records for guided practice and independent adaptation |
| Lesson practice and transfer checks | Separate records for the eight supported lessons; the optional model-adapter lesson adds no stored checks |
| Workshop reading view | Local-only preference under `ai-atlas-lesson-view-v1`; not included in exported v1/v2 progress backups |
| Scope and evidence note | Local text with scope, actual results, review and next action; avoid secrets and personal data |
| Copy summary | Checked-item list; copy the note separately or use the JSON backup |
| Export backup | Version 2 JSON: role, time, all checks and evidence note |
| Restore backup | Validates before replacing state; version 1 backups restore old topic/milestone checks and start new checks unchecked |
| Clear progress | Confirms before clearing checks; keeps the note, selected role and theme |

Role percentages count selected Essential + Recommended topic scopes. They do not measure study hours or mastery, and checkmarks are not certification. The separate counters show 51 topic scopes, 438 unit practice/transfer checks, 16 core-lesson practice/transfer checks and 9 milestones. The next-step bar also shows unit-check progress for the next unfinished topic; checking a unit does not automatically finish that topic. Earlier unit checkmarks retain their IDs and describe the scope originally recorded; review old evidence against the regrouped lesson before claiming the new scope complete.

Notes are limited to 50,000 characters and the complete backup to 250,000 bytes. Export checks both limits so it cannot knowingly create an unrestorable backup. Existing oversized notes remain visible for copying or shortening. Version 1 restoration leaves the note unchanged; version 2 replaces it. Unknown roles, missing required checks and non-boolean values are rejected before state changes. If storage fails after restoration, the page reports that the result is session-only.

## Using the tutor prompt

Use the compact 15-line prompt or full brief with a human tutor, AI assistant or for self-study. Each role phase has a coherent 60-minute plan whose demo, guided task, independent variation and final check share a bounded outcome; the four-dimension rubric uses Not yet, Partial, Pass and Strong levels. Copy a bounded scope, entry evidence and the rubric into your authorized assistant. The tutor prompt uses practical teaching with enough theory for understanding, without a fixed theory/practice ratio. It asks for one step at a time, evidence review, gradual removal of help and recall/transfer checks.

`DONE`, `DEBUG` and other workshop words are conversational conventions, not built-in commands. The reader does not run exercises or verify mastery automatically. The Topic 05 filled prompt example illustrates the start of a tutoring conversation; the supported workshop supplies the fuller local exercise.

## Troubleshooting and maintenance

- **Cannot run the first exercise:** use Lesson 1's working-directory and filename checks. Use `python3` or `py -3` consistently if that is your installed Python command.
- **A prerequisite is unfamiliar:** demonstrate it using the entry check or study it first. The applied route and deeper-study route have distinct dependency guidance.
- **Progress disappeared:** check the original browser profile and file location, then restore a backup.
- **Copy fails:** manually select the text; the fallback preserves keyboard focus.
- **Backup is too large:** copy the note separately and shorten it. Do not discard evidence without keeping another copy.
- **A tool differs:** use the publisher's documentation for your installed version. Tool directories and proposed stacks are a content snapshot.

## Authoring and validation

Edit the sources and rebuild; do not maintain `index.html` manually.

| File | Responsibility |
|---|---|
| `source/curriculum.json` | Canonical topics, subtopics, applied/deeper prerequisites, role priorities and capstone requirements |
| `source/units.json` | 219 authored concept groups, original-subtopic reference mapping, estimates, examples, practice and answer keys |
| `source/workshop.json` | Eight core lessons, instructions, expected results, troubleshooting and assessment |
| `source/ml-labs.json` | Runnable ML traces, numeric reference expectations and leakage checks |
| `source/tutor-materials.json` | Compact prompt and graded rubric (phase session plans live in `curriculum.json`) |
| `source/glossary.json` | Definitions and generated glossary search records |
| `source/learning.html` | Entry checks, rubric, scope note, tutor brief and review information |
| `source/template.html` | Existing reader layout, presentation and stable legacy sections |
| `source/reader.js`, `dashboard.js`, `learning.js`, `experience.js` | Reader, persistence, lesson, filter, navigation and lazy-rendering behavior |
| `source/atlas.css` | Consolidated reader stylesheet, semantic color tokens, themes, responsive and print rules |
| `source/hosted.css`, root `scripts/templates/atlas-loader.js` | Hosted-only offscreen rendering and explicit incremental loading/error recovery |
| `exercises/` | Runnable Python references, synthetic CSV and tests |
| `build.py` | Dependency-free generation of one standalone reader |
| Root `scripts/build-atlas-hosted.cjs` | Derives hosted assets and a byte-identical offline download without changing the standalone source |
| `tools/check_atlas.py`, `tests/fixtures/baseline.json`, `source/subtopics.sha256` | Preserved content/progress baseline, source freshness, IDs, links, search, units, curriculum and extracted exercise checks |
| `tools/check_unit_examples.py`, `tools/check_ml_labs.py` | Recomputed teaching arithmetic and executed ML-snippet expectations |
| `tools/results/` | Frozen historical reports; new routine output belongs in ignored root `artifacts/` or `.runtime/` |
| `tests/fixtures/` | Immutable baseline and v1/v2 backup compatibility fixtures |
| `tests/runtime.test.cjs` | Backup compatibility, invalid restore, storage failures, size limits and lesson revelation |

Run from the repository root:

Use `npm run build:atlas` to regenerate this reader and `npm run check:atlas` for the content, embedded-exercise, arithmetic and runtime checks. Both are included in the root build/test commands. The individual commands below remain available for focused work.

```text
python apps/ai-learning-atlas/build.py
python -B apps/ai-learning-atlas/build.py --check
python -B apps/ai-learning-atlas/tools/check_atlas.py --stage final
python -B apps/ai-learning-atlas/tools/check_unit_examples.py
python -B apps/ai-learning-atlas/tools/check_ml_labs.py
python -B -m unittest discover -s apps/ai-learning-atlas/exercises -v
node --check apps/ai-learning-atlas/source/reader.js
node --check apps/ai-learning-atlas/source/dashboard.js
node --check apps/ai-learning-atlas/source/learning.js
node --check apps/ai-learning-atlas/source/experience.js
node --test apps/ai-learning-atlas/tests/runtime.test.cjs
```

The Node runtime tests use the repository's existing `linkedom` development dependency; run `npm ci` if dependencies are absent. Python build/content checks and reference exercises use the standard library only.

Content review date: 3 November 2026. See [verification](VERIFICATION.md), [change log](CHANGELOG.md) and the actual files in `tools/results/` for current checks and limits. The [validation notes](VALIDATION.md) point to the current verification record. Report corrections through the repository issue tracker with a topic/lesson ID and a minimal synthetic example.

## Related documentation

[Repository overview](../../README.md) · [Documentation index](../../documentation.md) · [AI coding add-ons guide](../../docs/ai/coding-addons.md)

<!-- Preserve links to earlier README sections. -->
<a id="-prerequisites"></a>
<a id="-progress-backups-and-privacy"></a>
<a id="-quick-start"></a>
<a id="-related-documentation"></a>
<a id="-search-and-navigation"></a>
<a id="-troubleshooting-and-maintenance"></a>
<a id="-using-the-tutor-prompt"></a>
