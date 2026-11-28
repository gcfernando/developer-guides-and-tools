# Teaching improvements and verification

This report describes the implementation reviewed on 28 November 2026. It separates authored improvements, executed checks and work that still requires observation.

## What changed

All 447 numbered entries now have a teaching profile and lesson explanation. The same standard covers the required path, optional topics, shared exercises and dataset subtopics. Shared programs remain shared; each entry explains the particular task it teaches. The coverage CSV also inventories headings, Python sources, code blocks, data fields and visual occurrences in the supporting guides and projects. Inventory coverage does not prove teaching quality.

The lesson structure puts readiness, meaning, suitable use and a traced input/output example before the run instructions. It follows the result with interpretation, common mistakes, a small change, a recovery step and an explained application question. The authoring source is `course_tools/author_teaching.py`; edit it when changing the generated teaching notes.

The Python introduction now teaches the dictionary, decision, loop and object operations used by later examples. The optional network topics include a complete, small weight-update bridge. The Ridge and Lasso lessons include a runnable comparison with coefficients, validation-based selection and a separately reported test result. The source-investigation exercise allows correction, retention or a flag depending on the evidence. Future information and target leakage receive explicit cautions.

The visual source now recreates the graphs and diagrams from course data, code and editable flow wording. Each visual has a teaching question, reading instructions, an observation, a limitation and a text table. Distinct shapes, line styles, labels and hatching supplement colour. Narrow-layout graph variants, full-size access and native text flow cards support reading. Binning markers show discrete column values; decision cards wrap their complete headings.

The setup, glossary, learning path, practice, project guidance and teaching guide were updated together. Generated HTML and lesson ZIPs are rebuilt from the editable sources. These are local changes; no site was published.

## Team responsibilities and agreed decisions

| Role | Contribution and ownership |
| --- | --- |
| Lead ML expert | Reviewed the teaching profiles, learning order, source calculations, row roles, validation choices and example behaviour. Owns technical acceptance and the coverage/evidence tools. |
| Document writer | Wrote the explanations, readiness tasks, input/output traces, application questions and complete added Python examples. Owns simple labels, captions, comments and expected-result explanations. |
| UI/UX engineer | Created the visual source and metadata, regenerated teaching graphs, added narrow-layout variants and improved reading controls. Owns ML visual design and creation. |

The three roles exchanged findings before integration. The agreed sequence was to map the complete scope, correct the teaching and technical examples, create visuals from the same inputs, rebuild the reader and downloads, and run the checks. Review resolved these issues:

- A definition alone does not establish application skill. Add an input trace, a decision, a changed case and an explained answer.
- A successful run does not establish that a beginner can explain or transfer the idea. Keep observed learner testing separate.
- An unusual point does not establish a bad record. Investigate source evidence before deciding what to do.
- A model setting must be chosen using validation, with the final test reserved for the frozen choice.
- A network analogy needs a small numerical bridge before a complex library example. Label the bridge as a demonstration, not a performance evaluation.
- A text description must agree with the actual plotted rows, units, categories and calculations. Rebuild pictures and provide readable source values.

## Verification evidence

| Check | Result and evidence |
| --- | --- |
| Numbered teaching scope | All 447 entries mapped; see `teaching-coverage.csv` and its JSON summary. This also inventories 473 authored learner documents. |
| Distinct lesson programs | 229 source/data groups executed in temporary copies; all exited successfully. The 228 groups with recorded stdout matched it; the saved-model training workflow has no fixed stdout file. See `execution-checks.json`. |
| Added teaching examples | All 10 copies checked against expected output. Controlled changes verify the Lasso coefficient example and the network learning-rate warning. See `teaching-example-checks.json`. |
| Saved-model workflow | Both training and prediction run in a temporary copy. A changed blank weight still gives an estimate; errors use measured answers only; prediction preserves the saved artifact. See `workflow-checks.json`. |
| Learner-change checks | All 10 regression groups passed, including unfamiliar categories and an unavailable-at-prediction input. |
| Course structure | Python syntax, local links, fragments, archive contents, visual source hashes, page controls and lesson manifest checks passed. Re-run after changing sources. |
| Repository checks | `npm test` and `npm run check:repository` passed. |
| Environment | Python 3.12.10 in a new local Windows virtual environment; exact installed versions are in `verification-environment.txt`. This is not a clean operating-system installation test. |
| Real-browser reading checks | Unverified. Chrome failed during startup in this restricted environment, including GPU-process failures and a locked debugging-port file. See `browser-checks.json`. The simulated page-control checks pass separately. |

## Checks that remain open

No beginner study was conducted. The application tasks and delayed-transfer checks in `../TEACHING.md` are ready for a pilot, but no claim of beginner comprehension or independent ML engineering competence is made.

Real-browser checks, screen-reader use, actual phone use, 400% zoom and print review still need observation. Clean Mac and Linux setup and a clean Windows operating-system setup remain unverified. No cloud deployment or hosted site release was tested. The original source PDF and legacy drawing files were not supplied; the new visual sources document the recreated course figures.

No unresolved technical disagreement was recorded by the three roles. The remaining uncertainty concerns observed learning, assistive-technology behaviour and platforms that have not been tested. Future findings should update the source material and this evidence rather than being marked passed without a check.
