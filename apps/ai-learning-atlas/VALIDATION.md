# AI Learning Atlas validation

Review date: 2 November 2026.

The reader preserves its existing colors, typography, cards, sidebar, buttons, dark mode and standalone delivery. New lessons and embedded reference files use those same components.

## Content and curriculum checks

- Compared the source directory with the original Git version: all 1,607 original subtopic IDs, names and ordering are preserved.
- `build.py --check` verifies that the standalone HTML matches its authoring sources.
- `validate.py` checks 51 topics, 14 roles, one H1, unique IDs, internal links, local exercise links, 1,700 search targets, preserved subtopic digest, prerequisite order and capstone coverage.
- Separate AI/ML, tutor/course-design and page-design review agents reviewed the source and generated artifact in two passes. Findings were corrected, including project-variant dependencies, deeper-study guidance, beginner scope, tool requirements, worked mathematics explanations, keyboard behavior and backup limits.

These are AI-assisted reviews of the supplied material. They do not constitute external professional certification, observed student outcomes, a full WCAG audit or independent verification of every named tool/resource.

## Executed checks

- Fifteen Python reference tests passed, covering pure answers, invalid inputs, user isolation, deletion, instruction-like data, HTTP responses, unavailable service, CSV profiling and conflicting-record cleaning.
- Six Node runtime tests passed, covering legacy backup compatibility, version 2 round trips, invalid restore rejection before mutation, storage failure notices, export/restore size consistency and hidden-lesson revelation.
- All three source JavaScript files passed Node syntax checks.
- Generated-content and structural validation passed.
- Repository `npm test` passed: generated artifacts, eight library tests, source provenance and 459 relative-file links. `git diff --check` passed.

The Python test suite initially encountered a sandbox restriction writing a temporary CSV. The authorized rerun passed all fifteen tests. No assertion or test was weakened to obtain that result.

## Browser checks

Checked the local generated reader in Microsoft Edge:

- Desktop rendering retains the original visual design.
- Role selection updates the dashboard with dependency-ordered topic scopes and self-reported progress wording.
- Search finds glossary entries and original subtopics; keyboard entry and Escape synchronize the expanded state.
- Lesson reading focus initially shows Lesson 1; lesson practice checks update their separate counter.
- The evidence note updates its visible character count.
- At a 320-pixel viewport, document width equals viewport width, the reading selector remains inside its card, and closed mobile navigation is inert.
- Escape from open mobile navigation returns focus to the menu button.
- Dark-mode workshop rendering remains readable within the existing palette. The action button background was corrected to the original higher-contrast blue.

The browser checks sample important views and interactions. They do not establish compatibility with every browser, assistive technology, device or print engine.

## Teaching coverage and limits

The eight-lesson beginner workshop supplies runnable local examples, troubleshooting, independent variations, staged cleaning hints and reference solutions. Five mathematics units supply worked calculations. Other topic groups contain explicitly labeled study briefs, original subtopics, applied/internals/research guidance, tools, lab goals and assessment criteria; they are not represented as fully authored courses for every subtopic.

The local assistant is deterministic. It does not call an LLM, train a model or implement a real login system. Passing its regression tests does not establish general model reliability, prompt-injection resistance or production readiness. Progress records remain self-reported and assessment applies only to the learner's declared scope.
