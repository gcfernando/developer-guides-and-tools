---
layout: default
permalink: /apps/ai-learning-atlas/guide/
title: "AI Learning Atlas — Study Paths and Progress Guide"
description: Follow dependency-ordered AI study paths, complete a supported local beginner workshop, and record learning evidence.
---

[Developer guides and tools](../../README.md) · **Interactive learning**

<a id="-ai-learning-atlas--offline-reader-and-progress-guide"></a>

# AI Learning Atlas — Study Paths and Progress Guide

Open the [AI Learning Atlas](https://gcfernando.github.io/developer-guides-and-tools/apps/ai-learning-atlas/index.html) to choose a professional learning path, complete a supported beginner workshop, search 51 topic groups and 1,607 original subtopics, and record evidence. All sections use the existing reader design, including dark mode and responsive navigation.

<a id="guide-prerequisites"></a>

## Prerequisites

A modern browser reads the generated `index.html` directly, without a server or external assets. JavaScript enables search, role selection and progress. Save this HTML for offline reading: every supplied workshop reference file is also embedded in it. Optional file downloads use the adjacent `exercises/` directory.

The eight-lesson workshop needs Python 3.10 or newer, a text editor and terminal. It uses the standard library, synthetic data and a local-only service. No cloud account, GPU, package installation, model or API key is required after Python is available. Installing Python and following online references need internet. Other topic study briefs state their tool and resource assumptions separately.

<a id="guide-quick-start"></a>

## Quick start

1. Use the entry check to establish starting skills. New programmers can begin the supported beginner workshop before taking a full role path.
2. Choose a profession. Priority labels describe relevance; the sequence follows applied prerequisites, including Recommended bridges before dependent Essential topics.
3. Choose the applied, internals or research depth within a topic. Record selected concepts, deferred material and evidence in the scope note.
4. Complete the guided exercise, then an independent variation. Keep actual results, an explained failure, and clean-folder setup instructions.
5. Use the four-dimension assessment rubric and the role-specific capstone checks. Mark only the scope you demonstrated complete.
6. Export a progress backup before moving files, clearing browser data or changing browser profiles.

The deterministic FAQ workshop teaches engineering foundations. It does not call a language model, train ML, implement production authentication or establish production readiness. The five mathematics units contain worked calculations. Other topic units are explicitly labeled study briefs; they are not fully supplied courses for every listed subtopic.

<a id="guide-search-and-navigation"></a>

## Search and navigation

Search covers roles, topics, original subtopics, workshop lessons and glossary definitions. Type at least two characters; all query terms must appear in a result title or context. Up to 35 results are shown. Selecting a result reveals collapsed content and any lesson hidden by reading focus.

Press `/` outside editable fields to focus search. Down Arrow enters results; Up/Down moves through them. Escape in results closes them and returns focus; Escape in the field clears its query. Mobile navigation is inert while closed, and Escape returns focus to the menu button.

The workshop initially shows Lesson 1. Choose any lesson or show all with Reading view. Lesson links reveal their destination automatically. Print styles show every lesson and remove code-panel height limits.

## Progress, backups and privacy

The page stores checks, role, theme and one evidence note locally when browser storage is available. It makes no network calls to save progress. A hosted reader and a local file have separate browser storage contexts. Local-file storage, private browsing, moving a file or clearing site data can affect persistence; keep a JSON backup.

| Control | Meaning |
|---|---|
| Topic scope check / Mark scope done | Self-reported completion for a declared scope; not proof of all subtopics |
| Unit practice and transfer checks | Separate records for guided practice and independent adaptation |
| Lesson practice and transfer checks | Separate records for the eight supported lessons; do not automatically complete topic scopes |
| Scope and evidence note | Local text with scope, actual results, review and next action; avoid secrets and personal data |
| Copy summary | Checked-item list; copy the note separately or use the JSON backup |
| Export backup | Version 2 JSON: role, time, all checks and evidence note |
| Restore backup | Validates before replacing state; version 1 backups restore old topic/milestone checks and start new checks unchecked |
| Clear progress | Confirms before clearing checks; keeps the note, selected role and theme |

Role percentages count selected Essential + Recommended topic scopes. They do not measure study hours, mastery, certification or expert competence. Unit, lesson and milestone counts are separate from that percentage.

Notes are limited to 50,000 characters and the complete backup to 250,000 bytes. Export checks both limits so it cannot knowingly create an unrestorable backup. Existing oversized notes remain visible for copying or shortening. Version 1 restoration leaves the note unchanged; version 2 replaces it. Unknown roles, missing required checks and non-boolean values are rejected before state changes. If storage fails after restoration, the page reports that the result is session-only.

## Using the tutor prompt

Use the supplied brief with a human tutor, AI assistant or for self-study. Copy a bounded scope, entry evidence and the rubric into your authorized assistant. The tutor prompt uses practical teaching with enough theory for understanding, without a fixed theory/practice ratio. It asks for one step at a time, evidence review, gradual removal of help and recall/transfer checks.

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
| `source/workshop.json` | Eight authored lessons, instructions, expected results, troubleshooting and assessment |
| `source/glossary.json` | Definitions and generated glossary search records |
| `source/learning.html` | Entry checks, rubric, scope note, tutor brief and review information |
| `source/template.html` | Existing reader layout, presentation and stable legacy sections |
| `source/reader.js`, `dashboard.js`, `learning.js`, `learning.css` | Reader behavior and additions using the existing design tokens |
| `exercises/` | Runnable Python references, synthetic CSV and tests |
| `build.py` | Dependency-free generation of one standalone reader |
| `validate.py`, `source/subtopics.sha256` | Source freshness, original subtopics, IDs, links, search and curriculum checks |
| `runtime.test.cjs` | Backup compatibility, invalid restore, storage failures, size limits and lesson revelation |

Run from the repository root:

```text
python apps/ai-learning-atlas/build.py
python -B apps/ai-learning-atlas/build.py --check
python -B apps/ai-learning-atlas/validate.py
python -B -m unittest discover -s apps/ai-learning-atlas/exercises -v
node --check apps/ai-learning-atlas/source/reader.js
node --check apps/ai-learning-atlas/source/dashboard.js
node --check apps/ai-learning-atlas/source/learning.js
node --test apps/ai-learning-atlas/runtime.test.cjs
```

The Node runtime tests use the repository's existing `linkedom` development dependency; run `npm ci` if dependencies are absent. Python build/content checks and reference exercises use the standard library only.

Content review date: 2 November 2026. See [validation notes](VALIDATION.md) for performed checks and review limits. Report corrections through the repository issue tracker with a topic/lesson ID and a minimal synthetic example.

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
