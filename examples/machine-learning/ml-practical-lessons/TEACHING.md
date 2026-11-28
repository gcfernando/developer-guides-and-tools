# Check and teach this course

The course is written for a reader with no ML or Python background. Use short, clear sentences. Explain each new word and action. Keep the correct names next to the plain explanation.

## Before a lesson

1. Ask the learner to explain the prior skill.
2. Read one tiny example together.
3. Ask for a prediction before showing the result.
4. Give a hint before giving a solution.
5. Ask the learner to explain the result in their own words.
6. Finish with a new case that is similar but not identical.

Do not measure progress by the number of files run. Use the checks in the learning path. Keep the complete solution to the independent project out of the learner's first attempt.

## Who owns the work

The same teaching standard applies to every section and nested topic, including Practice, Reference and extra topics. One-hot encoding and outliers are examples of the approach, not its boundary. Keep shared exercises when they serve several topics, but explain what each topic asks the learner to do with them.

| Role | Owns | Checks with the other two roles |
| --- | --- | --- |
| Lead ML expert | Technical accuracy, prior skills, learning order, suitable uses, fair evaluation and technical acceptance. | Check every claim, code example, result and visual. Distinguish a useful demonstration from evidence about a real service. |
| Document writer | Simple explanations and complete runnable Python teaching files; data and package instructions; comments, result explanations, exercises and answers. | Keep names, units, row identities and steps consistent across the writing, code and visuals. |
| UI/UX engineer | Design and creation of all ML images, graphs, diagrams and visual learning flows; accessible page controls and layouts; editable visual sources. | Use data and results checked by the ML expert. Use the writer's simple labels, captions and reading instructions. |

Review a whole teaching unit together. A correct script, a correct paragraph and a correct image can still explain different things. Follow the same row through all three. Ask whether the exercise tests the skill promised in the goal.

## Check every teaching unit

Use this checklist for a concept, subtopic or feature. A navigation heading can point to a shared explanation. Record that mapping instead of silently omitting it. A new picture or script is useful only when it helps teach the idea.

1. State one task the learner will be able to do.
2. Check the needed prior skill with a small task and link to help.
3. Explain the meaning in ordinary words, then introduce the technical name.
4. Explain why and when the method helps, and when it is unsuitable.
5. Start with a familiar situation, then use a small ML example.
6. Show the inputs, their meanings and units, and the output shape.
7. Follow one row through numbered steps. Explain why each important step exists.
8. Give complete runnable code where code teaches the idea. Supply imports, package requirements and sample files. Clearly distinguish Python, terminal commands and output.
9. Run the example and its documented changes. Record the actual output, explain it and mark anything not run as unverified.
10. Explain likely mistakes and recovery. Do not change a measurement simply to make the result look better.
11. Supply a partly completed task, then an unfamiliar case with a separate explained answer.
12. Return to the idea later in a mixed task, where the learner must choose the method.

For each visual, state its question; explain the axes, units, markers and reading order; trace one case; state what to notice and what the picture cannot establish. Include important values or relationships as readable text or a table. Colour must have a second cue such as a label, shape or line style.

## Keep evidence of full coverage

`coverage.csv` preserves the historical lesson and download map. `course-review/teaching-coverage.csv` adds an inventory of all authored learner headings, code blocks, figure uses and runnable sources. Its JSON summary records counts and limitations. Regenerate it after a reviewed content change:

```bash
python course_tools/audit_teaching.py --write
python course_tools/audit_teaching.py
```

An inventory row means the source is accounted for. It does not mean a beginner has understood it. Keep the course check results, team review, actual browser observations, clean-install checks and learner observations separate. Never turn "not applicable" into a way to hide missing teaching material. Give a reason for a shared example or text-only treatment.

The original PDF mentioned in the historical page map and editable sources for some original figures were not supplied. Preserve their provenance. Any replacement visual must be based on the supplied data or an explicitly labelled illustration, with an editable source.

## Research behind the teaching approach

The recommendations below guide the design. Their application to this workbook still needs learner testing.

- Alternate worked solutions and problems; connect everyday examples with formal representations; explain pictures in words; revisit key ideas after a delay. The [IES practice guide](https://ies.ed.gov/ncee/WWC/PracticeGuide/1/Published) gives different evidence strengths for different recommendations. It rates repeated retrieval and deep explanatory questions more strongly than pre-questions. Do not claim all methods have the same evidence.
- Check what learners can do before starting. [Carnegie Mellon's prior-knowledge guidance](https://www.cmu.edu/teaching/assessment/priorknowledge/index.html) distinguishes direct tasks from learners' self-reports. Neither an adult job title nor interest in ML establishes prior coding knowledge.
- Keep learned preparation inside training and reuse it on later rows. [Scikit-learn's common pitfalls](https://scikit-learn.org/1.8/common_pitfalls.html) explain inconsistent preparation and leakage. The course pins scikit-learn 1.8; check examples against that version before introducing a newer API.
- Give graphs and diagrams descriptions that communicate essential values, relationships and trends. Follow [W3C complex-image guidance](https://www.w3.org/WAI/tutorials/images/complex/) and [use-of-colour guidance](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).
- Test enlarged and narrow reading layouts. [W3C reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) allows necessary two-dimensional scrolling in charts and tables. Do not shrink their labels until they become unreadable merely to avoid a local scrollbar.

## Build the deliverables

Editable lesson files live in `lessons/`. The workbook text is in `Data-Science-and-Machine-Learning.md`. Edit the simple-word help in each lesson README. The main guides explain the shared ideas.

From this course folder, with the course environment active, run:

```bash
python -m pip install -r course_tools/requirements.txt
python -m pip install -r course_tools/requirements-visuals.txt
python course_tools/author_teaching.py
python course_tools/build_visuals.py
python course_tools/build_course.py
python course_tools/audit_teaching.py --write
python course_tools/check_course.py
python course_tools/check_teaching_examples.py
python course_tools/check_saved_workflow.py
python course_tools/audit_teaching.py
```

The build makes downloadable ZIPs and readable HTML pages. The checks inspect links, Python syntax and the documented practice changes. Run `python course_tools/check_course.py --run` to also run distinct lesson scripts. Its new evidence is written to `course-review/execution-checks.json`; older review records remain historical evidence. Optional packages may be absent; the report must say which lessons did not run. Build tools are for the author. A learner does not need them.

Before publishing, also run the full repository checks. From the repository root (`DeveloperResources`), run:

```bash
npm ci
npm test
npm run check:repository
```

In Windows PowerShell, use `npm.cmd` if PowerShell blocks `npm.ps1`. The repository checks include rules for links in Markdown. Course checks alone do not cover all publication rules. Keep repository lesson links relative to `lessons/<lesson>/`; the build adjusts guide links in each ZIP's browser page for a folder extracted directly inside the course folder.

For a website release, also set up Ruby and Bundler as required by the repository. Install the gems with `bundle install`, then run these commands from the repository root:

```bash
npm run site:build
npm run check:site
```

The website check runs after the site build. It checks the published pages, including each page's title, short description and canonical URL (its main web address). A passing `npm test` does not replace this website check. If Ruby is unavailable, record that the full site build still needs verification.

## Test a clean computer setup

This is a release task, not a claim that it has already passed.

| Computer | Python version | Installation commands | First prediction | Main path | Tester and date |
| --- | --- | --- | --- | --- | --- |
| Windows | | | | | |
| Mac | | | | | |
| Linux | | | | | |

Use a clean environment. Follow only the learner instructions. Record the full package versions and any missing operating-system tools. Keep the test output. Do not mark the platform passed just because code worked in an old environment.

## Observe new learners

Ask several people who have never coded to try the first modules. Include students and working professionals. Ask them to say what they think each step means. Do not silently repair files for them.

| Module and route | What the learner could explain | Where they stopped | Help needed | Time spent | Change to try next |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Record observed times before publishing course-time estimates. After a few days, ask learners to solve a small new case without the notes. The independent project checks transfer. A successful install or a copied output does not establish that.

Use a small first pilot to find problems, then revise and try again. Include readers with little technical experience and different ages and devices. Explain the task without explaining the answer. Record which hints or assistance were needed. Ask younger readers to work with appropriate teacher or family support.

| Task | Evidence to observe |
| --- | --- |
| Prepare a new category | The learner keeps the fitted column names and order, explains the unknown-name policy, and distinguishes an encoded value from evidence of a reliable prediction. |
| Investigate an unusual value | The learner reads the axes, locates the record, asks for source evidence, and justifies keeping, correcting or flagging it. |
| Explain a model setting | The learner reads the changed setting and result, explains what was learned, and chooses with validation rather than final test answers. |
| Build a new small project | The learner identifies available inputs, reserves a fair check, trains a baseline, inspects errors and explains limitations. |
| Return after a delay | The learner applies an earlier idea to a different case without copying its supplied answer. |

These are proposed observation tasks, not results of a completed study. A small pilot cannot establish success for every reader. Record what failed as carefully as what worked.

## Check the reading experience

Run `node course_tools/check_browser_real.cjs` from the course folder to check a locally installed Chrome or Edge. Set `ML_COURSE_BROWSER` to its executable if needed. This serves only the course on a local address and records actual results in `course-review/browser-checks.json`. A browser launch failure is an unverified check, not a pass. The structural page checks run separately in `check_course.py`.

Use real browsers after automated page checks. Test keyboard navigation, named progress controls, code-copy actions, image descriptions and full-size views. Check phone-sized layouts at 320 CSS pixels, text enlargement, a 400% zoom view, light and dark themes, and grayscale printing. Check that essential content remains available even when an image cannot be seen. Record the browser, viewport, assistive technology if used, and actual observation. A simulated DOM check is not a screen-reader test.

## Score an independent project

Give 0 to 4 points in each area. Zero means missing. One means a claim with little evidence. Two means partly correct work. Three means correct work with a clear reason. Four means correct work plus a useful limitation or alternative.

| Area | Evidence |
| --- | --- |
| Problem and baseline | A decision, target, available inputs and a simple comparison. |
| Data quality | Source, meanings, units, missingness and uncertain labels. |
| Fair check | Separate row roles and a split suited to the intended use. |
| Results | Counts, suitable errors, large mistakes and limits. |
| Handoff | Reproducible files, a readable explanation and next action. |

Require evidence in every area. A high total cannot excuse leakage or using test answers to choose a model. Ask for a corrected project and a new fair check when those occur.

## Release evidence

Read the [implementation and verification report](course-review/IMPLEMENTATION.md) for the current changes, executed checks and open observation tasks. Keep the generated coverage CSV separate from claims about learner success.

Keep a dated check report. Separate code changes, automated checks, manual browser checks, clean setup checks and observed learner results. The original audit remains in `course-review/`; it describes the old state. `course-review/implementation-status.csv` records the response and any checks that still require a person or another computer.
