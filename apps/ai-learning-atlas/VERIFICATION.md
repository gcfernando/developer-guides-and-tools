# AI Learning Atlas verification

Revision and review date: **3 November 2026**. All twelve workstreams have been implemented and checked, and nine independent reviewers have returned scores. This record preserves executed results, earlier failures and actual verification limits. The completed static, main-browser, additional-browser and contrast reports fingerprint the reviewed revision; that fingerprint is recorded below.

## Baseline and preserved contracts

The pre-edit `tests/fixtures/baseline.json` records **51 original topic titles, 1,607 original subtopic IDs/text/order and 514 progress-check IDs**. Original-format restore fixtures are `tests/fixtures/backup-v1.json` and `tests/fixtures/backup-v2.json`. These fixtures were relocated from `tools/` without changing their bytes; paths in historical command output describe their original locations. Original HTML SHA-256: `12a35942ed0fdc4bf92865f1f91669197483725c59d87df2a695e7a66f791346`. The original browser measured **16,082 initial DOM elements**.

The final-mode audit preserves all original titles, subtopic wording/order and stored progress identifiers; every original subtopic has exactly one unit reference-map assignment. The map is labeled **“Related original subtopics (reference map)”**. It is a navigation and study-scope relationship, not a claim that a small example fully teaches every advanced subject in the list. Progress remains self-reported and existing localStorage keys/v1/v2 backups are retained.

## Environment and evidence snapshots

Checks ran on Windows with **Python 3.12.10**, **Node 22.23.4**, headless Microsoft Edge, Playwright, axe-core, Lighthouse and **Nu HTML Checker 26.10.12 (973e40b)**. Audit packages are development tools, not reader runtime dependencies. Exercises use Python's standard library. Python 3.10 compatibility was reviewed; actual execution used Python 3.12.

Selected baseline comparisons, final JSON reports and command output are retained in `tools/results/`. Intermediate stage dumps, screenshots, PDFs and local caches were removed during pre-PR cleanup; the historical measurements remain summarized below. The completed `final-static.json`, `final-browser.json`, `final-extra.json` and `final-contrast.json` all identify HTML SHA-256 **`d0645bf9509bfbf7293d2e7722daefa78e7633e3e7005b70dbd5eb4e06a5aa3b`**. These four reports describe the reviewed artifact, before the subsequent change that gave all three practical-route buttons the same `action-blue` style. Their browser scores and screenshots are historical evidence for that revision. Fresh source-consistency, numeric and runtime results after cleanup are recorded in `cleanup-*.txt`; the historical reports were not rewritten to imply a new browser run.

## Executed workstream results

Checker columns are **passed / failed / warnings**. Browser columns are **passed / failed recorded assertions**. Nu columns are **errors / other messages**. Lighthouse columns are **Performance / Accessibility**. Rows follow implementation priority order: P0, P1, P2, P3, then the final audit.

| Stage | Consistency checker | Extracted Python tests | Node runtime | Nu errors / other | Main browser assertions | Mobile Lighthouse P / A | Initial browser DOM |
|---|---|---|---|---|---|---|---|
| WS1 | 25/0/1 | 15 passed | 8 passed; 3 skipped | 0 / 0 | 52 / 0 | 50 / 100 | 20,333 |
| WS2 | 25/0/1 | 23 passed | 9 passed; 2 skipped | 0 / 0 | 52 / 0 | 52 / 100 | 20,449 |
| WS3 | 26/0/0 | 23 passed | 9 passed; 2 skipped | 0 / 0 | 52 / 0 | 49 / 100 | 21,327 |
| WS4 | 26/0/0 | 23 passed | 10 passed; 1 skipped | 0 / 0 | 52 / 0 | 42 / 100 | 21,412 |
| WS5 | 26/0/0 | 23 passed | 10 passed; 1 skipped | 0 / 51 | 52 / 0 | Separate run below | 7,156 |
| WS9 | 27/0/0 | 23 passed | 11 passed; 0 skipped | 0 / 51 | 52 / 0 | Separate run below | 7,156 |
| WS10 | 31/0/0 | 23 passed | 11 passed; 0 skipped | 0 / 51 | 53 / 0 | 92 / 100 | 7,156 |
| WS6 | 31/0/0 | 23 passed | 11 passed; 0 skipped | 0 / 51 | 53 / 0 | 93 / 97 | 7,292 |
| WS7 | 31/0/0 | 31 passed | 11 passed; 0 skipped | 0 / 51 | 53 / 0 | 90 / 97 | 7,350 |
| WS8 | 31/0/0 | 31 passed | 11 passed; 0 skipped | 0 / 51 | 53 / 0 | 91 / 100 | 7,348 |
| WS11 | 31/0/0 | 31 passed | 11 passed; 0 skipped | 0 / 51 | 53 / 0 | 92 / 100 | 7,349 |
| WS12 | 31/0/0 | 31 passed | 11 passed; 0 skipped | 0 / 51 | 52 / 1 | 89 / 100 | 7,349 |
| FINAL | 31/0/0 | 31 passed | 11 passed; 0 skipped | 0 / 51 | 54 / 0 | 93 / 100 | 7,349 |

The early WS1/WS2 warnings were the Topic 17/47 prerequisite-difficulty inversions. WS3 corrected them without altering original titles. The stricter final-mode checks run from WS10 onward and include phase order, checkpoint/session metadata, derived effort ranges, displayed priorities/difficulties, headings, online labels and self-contained downloads. The latest static result is **31 passed, zero failed, zero warnings**. Original progress IDs, all internal/search targets and 219 distinct Practice paragraphs pass their checks. No unfinished generic briefs are reported.

All **11 Node runtime tests** execute with zero failures/skips from WS9 onward. Earlier staged skips are recorded above and are not counted as passes. Coverage includes v1/v2 restores, invalid restore rejection, storage failures, export limits, lesson revelation, combobox state, stable toggle names, lazy unit restore/deep links and exact Blob content.

Nu reports **zero errors and 51 informational notices** in the final inspected snapshot. All 51 say `aria-hidden` is unnecessary on an element already bearing `hidden`; these are redundant attributes on hidden live progress holders. They are retained as notices, not mislabeled as errors or hidden behind a no-message claim. WS1–WS4 Nu reports contain no messages.

The lead also ran repository **`npm test`**, with **8/8 library tests**, generated-file checks, **456 relative-file links** and **176 provenance items** passing. Its initial failure involved a test helper that opened disclosures without materializing the new inert body format. The helper was corrected to execute the actual hydrator while retaining its original assertions; the later repository run passed. No valid behavior assertion was removed to obtain that pass.

## Browser, accessibility and mobile execution

The last inspected fingerprinted main-browser run has **54 passed assertions, zero failed assertions and zero JavaScript/console errors**. All four expanded axe scans—file/light, file/dark, HTTP/light and HTTP/dark—report **zero serious or critical violations**. The scans report all hydrated topic bodies, path details, lesson bodies and open main disclosures; their stated scope is preserved in the report. The separate contrast run also materializes session-plan content. Incomplete axe contrast observations are discussed below and are not counted as verified passes.

The fingerprinted additional run has **64 passed assertions, zero failures and zero JavaScript errors**, including the following exercised behavior on file and HTTP:

- Role selection, topic toggles, reload persistence, JSON export/clear/restore, and original-format v1/v2 imports retain every original progress check.
- Search slash shortcut, typing, Arrow Down/Enter/Escape, active-descendant state, skip link, keyboard menu toggling and Escape focus return work in the tested states.
- At **360, 768, 1280 and 1600 px**, selected-role and expanded-code views have `document.documentElement.scrollWidth === innerWidth`. Long code scrolls inside its panel. Sampled button/toggle/checkbox-label targets meet the harness's 44-pixel checks and sampled focus remains unobscured by sticky controls.
- My-path/All-topics behavior preserves original topic order; filters announce actual counts; primary/matrix role selectors synchronize; onboarding choices persist; sidebar section tracking passes its corrected rerun.
- All 12 workshop download controls produce exact inline text and filenames. Original-subtopic copy checks include the topic number and unchanged directory entries. Browser capture/mocks verify the produced copy text, not the operating-system clipboard.
- Initial unit/subtopic links land in unobscured view at 360/1280 px. A resumed lesson view, dismiss-button focus and unit feedback behavior pass their added checks.
- OS theme default, live preference changes, stored manual override and theme-color follow the recorded state. Reduced motion disables smooth scrolling.
- Actual first-two-page PDFs are generated on file/HTTP; beforeprint hydrates content and opens disclosures, and afterprint restores prior states without leaving answer keys open.

An earlier additional run timed out on sidebar location tracking; later recorded reruns pass that behavior. WS11 initially deferred topic-number copy checks to WS12; WS12/final additional runs execute them rather than treating the deferral as a pass.

The lead visually inspected final 360/1280 screenshots and the first two print pages, observing no page overflow and confirming that the skip link is absent from print. This is a bounded visual review of those artifacts, not a review of every viewport, page or assistive-technology interaction.

## Lighthouse and initial DOM measurements

| Retained measurement | HTTP transport | Performance | Accessibility | Initial browser DOM |
|---|---|---|---|---|
| Original baseline | Uncompressed | 53 | 96 | 16,082 |
| Original transport comparison | Gzip when accepted | 92 | 96 | 16,082 |
| Earlier full WS5 run | Gzip when accepted | 89 | 100 | 7,170 |
| WS5 targeted rerun | Gzip when accepted | 90 | 100 | Not measured in performance-only mode |
| WS9 targeted rerun | Gzip when accepted | 93 | 100 | Not measured in performance-only mode |
| WS10 full run | Gzip when accepted | 92 | 100 | 7,156 |
| WS6 full run | Gzip when accepted | 93 | 97 | 7,292 |
| WS7 full run | Gzip when accepted | 90 | 97 | 7,350 |
| WS8 full run | Gzip when accepted | 91 | 100 | 7,348 |
| WS11 full run | Gzip when accepted | 92 | 100 | 7,349 |
| Earlier full WS12 run | Gzip when accepted | 89 | 100 | 7,349 |
| WS12 targeted rerun | Gzip when accepted | 90 | 100 | Not measured in performance-only mode |
| Last inspected final full run | Gzip when accepted | 93 | 100 | 7,349 |

The last inspected browser count of 7,349 represents a **54.303%** reduction from 16,082 original DOM elements while retaining 514 live progress checks. The static parser separately counts 7,309 initial live elements; dynamically created controls explain the difference. Browser and parser figures are not interchangeable.

Lighthouse uses a 412×823 mobile viewport, device scale 1.75, simulated mobile networking and 4× CPU slowdown. Comparable gzip baseline/later runs use the same profile. Gzip is an explicit transport condition, not a rendering optimization attributed to the reader: the original uncompressed 53 and compressed 92 are both preserved. The compressed baseline already scored 92, so these results do not justify an across-the-board performance-score improvement claim. The expanded curriculum and DOM reduction are reported separately.

Earlier WS5 trials reported performance 84 and onboarding layout shift around 0.53; onboarding timing and lazy JSON/delegation changes addressed the observed behavior. The retained WS5 targeted rerun recorded performance 90, FCP/LCP 2,485 ms, total blocking time 233 ms and layout shift 0. Earlier overwritten trials are identified as historical observations rather than independently retained reports. WS12's earlier complete run at 89 remains in the table; its targeted 90 and final 93 are distinct actual reruns.

## CSS and contrast evidence

The fingerprinted contrast report records **129 unique sampled text/style/background pairs in light mode and 130 in dark mode**, and **11 light / 11 dark unique sampled UI-indicator pairs** after search-indicator sampling was added. It reports zero sampled text pairs below their size-dependent AA threshold and zero sampled UI-indicator pairs below 3:1. It also reports no dead/invalid selectors in the states and selector rules examined. Interaction/pseudo-element exclusions mean that an empty selector list is not proof about every possible state.

Representative actual text ratios include:

| Sampled style | Light | Dark |
|---|---|---|
| `.eyebrow-small` | 5.893:1 | 9.357:1 |
| `.muted` on the sampled soft surface | 5.327:1 | 8.406:1 |
| `.chip` | 6.417:1 | 7.130:1 |
| Essential status pill | 5.872:1 | 8.414:1 |
| Recommended status pill | 6.445:1 | 7.807:1 |
| Unlisted status pill | 4.796:1 | 7.824:1 |
| `.action-blue` text | 6.317:1 | 6.317:1 |

Both themes retain **52 axe color-contrast incomplete observations**, classified from the detailed report as 45 non-text/decorative observations, four partially clipped code observations and three dashboard observations affected by a pseudo-element. The dashboard accent is a 5-pixel top decoration; the lead inspected its nonoverlap with the sampled text. Code panels have independently measured code text/background pairs and scrollable clipping. These explanations bound the manual/computed review; incomplete results are not relabeled as automated passes. Gradient and dynamic-state limitations remain stated by the sampler. The evidence does **not** establish universal WCAG conformance.

## Teaching, technical checks and current references

The reader contains **219 authored bounded units**, answer keys and misconceptions, the eight supported workshop lessons plus an optional ninth model-adapter lesson, 30 role-phase session plans and a four-level common rubric. Original-topic reference maps distinguish listed related material from the narrower observable unit outcome.

The latest executed numeric/example result is:

```text
PASS 195 numeric/Python reference assertions across 74 authored units.
Checks cover worked calculations and numeric answer keys; illustrative IDs, dates, budgets and scenario constants are assumptions, not empirical claims.
```

The lead also executed **seven runnable ML snippets**. The latest embedded-reference extraction compiles **13 Python files** from **14 reference files** and runs **31 tests**, all passing: the original 15, eight ML tests, three injection-policy tests and five optional adapter tests. The tests cover the stated tiny fixtures, leakage-sensitive predictions, gradients/overshoot, calibration, confusion denominators, cross-validation/sample standard deviation, Wilson intervals, schema/malformed responses, explicit unimplemented real mode, symbolic cost arithmetic and allowlist/separate-approval enforcement. They do not establish learner execution, real-provider performance, current provider pricing or general injection resistance.

`tools/reference-checks.json` records **26 unique external URLs**, all resolving with status 200 after GET redirects on **2026-11-03**, reading the first 1,024 bytes. The consistency checker separately finds 34 outbound anchors labeled online, including deferred content. Reachability does not prove every linked statement or legal interpretation. Fast-moving protocols, SDKs, model names and phased legal obligations are subject to the reader's current-status guidance and scoped review.

## Independent reviewer results and fixes

Nine independent reviewer agents assessed the final files against section 4. The table records initial scores and the actual follow-up scores supplied after cited fixes; unchanged scores are carried as the original result rather than presented as a new review.

| Reviewer | Initial | After cited fixes | Evidence |
|---|---|---|---|
| Student | 94 | 96 | Clear onboarding/my-path route, authored lessons, effort ranges and corrected examples. |
| Tutor | 89 | 94 | Session demo/guided/independent tasks now form a coherent progression; answer keys, misconceptions, compact prompt and rubric remain available. |
| AI Expert | 94 | 94 | Dated references/current-status notes, optional mock/real adapter, scoped injection fixture and judge-bias practice. |
| ML Expert | 90 | 96 | Recomputed rate wording, regularization/CV examples, uncertainty and numeric rolling-origin comparison. |
| Course Design | 91 | 91 | Concept-group outcomes, consistent dependencies, phased long paths and recommended checkpoints with derived estimates. |
| UI/UX | 93 | 93 | Ordered navigation, role view/filtering, next-step bar, lazy rendering and tested interactions. |
| CSS & Style | 86 | 92 | Consolidated tokens/styles, corrected contrast/UI indicators, mobile/progress/focus refinements and bounded measured evidence. |
| Validation | 93 | 96 | Preserved baseline contracts, consistent final-mode script, zero Nu errors, combobox and exact self-contained downloads. |
| End User | 89 | 94 | Mobile targets/focus and meaningful progress plus resumed lesson view/dismissal behavior were corrected. |

One follow-up review round addressed the below-90 scores; no second round was needed. Related improvements included coherent session plans; Topic 04 rate wording; Topic 08 penalty/CV arithmetic; Topic 37 numeric origin-by-origin comparison; Topic 33 judge-bias practice; truthy approval/injection tests; CSS/mobile/progress behavior; and lesson-view resumption. All final assigned scores are at least 90. These are independent AI-assisted role reviews, not external certification, observed student outcomes or a guarantee that every inherited factual claim is correct.

## Latest complete consistency output

The output below is copied from the last inspected `final-check.txt`; its matching static hash is recorded above.

```text
PASS 51 original topic IDs, titles and order: 51 topic cards
PASS original subtopic IDs, text and order: 1607 actual; 1607 baseline; claimed 1,607
PASS true subtopic count matches page claims: Baseline confirms the published 1,607 count
PASS all IDs unique including inert templates: 2583 IDs
PASS every internal fragment resolves including templates: No unresolved fragment links
PASS search covers every topic: 51 required; missing []
PASS search covers every subtopic: 1607 required; missing []
PASS search covers every profession: 14 required; missing []
PASS search covers every lesson: 9 required; missing []
PASS search covers every glossary: 20 required; missing []
PASS every search href resolves: 1701 records; broken []
PASS atlas-data priorities equal canonical source
PASS role prerequisites, priority badges and capstone source topics: 14 roles; all consistent
PASS difficulty is not below an applied prerequisite: All 51 checked
PASS phases, optional checkpoints, session plans and derived hours: Every role checked; all long paths split
PASS difficulty labels agree across cards and matrix
PASS no duplicate study-unit practice paragraphs: 219 units; 0 duplicate paragraphs
PASS completed units have all teaching fields and hidden answers: 219 complete units
PASS every original subtopic maps to exactly one unit: 1607 assignments; missing 0; multiple []; unknown []
INFO remaining labeled briefs: none
PASS every original progress ID preserved: 514 original; 514 current; missing []
PASS new progress IDs use backup version 3: 0 added progress IDs
PASS all original localStorage keys retained
PASS one document H1
PASS heading outline has no skipped levels
PASS external links labeled online including deferred bodies: 34 anchors
PASS workshop downloads need no adjacent exercise files
PASS no external runtime assets: []
PASS download reference files have exact, consistent inline text: 14 files;
PASS extracted Python reference files compile: 13 Python files;
--- Extracted unittest output ---
test_deleted_document_is_unavailable (test_assistant.AnswerTests.test_deleted_document_is_unavailable) ... ok
test_instruction_is_treated_as_data (test_assistant.AnswerTests.test_instruction_is_treated_as_data) ... ok
test_invalid_input (test_assistant.AnswerTests.test_invalid_input) ... ok
test_public_answer_and_normalization (test_assistant.AnswerTests.test_public_answer_and_normalization) ... ok
test_unknown_question_abstains (test_assistant.AnswerTests.test_unknown_question_abstains) ... ok
test_users_are_isolated (test_assistant.AnswerTests.test_users_are_isolated) ... ok
test_http_contract (test_assistant.EndpointTests.test_http_contract) ... ok
test_invalid_request_gets_400 (test_assistant.EndpointTests.test_invalid_request_gets_400) ... ok
test_request_cannot_choose_identity (test_assistant.EndpointTests.test_request_cannot_choose_identity) ... ok
test_unavailable_service (test_assistant.EndpointTests.test_unavailable_service) ... ok
test_conflicting_identifier_quarantines_both_versions (test_clean_data.CleaningTests.test_conflicting_identifier_quarantines_both_versions) ... ok
test_exact_duplicate_and_missing_value (test_clean_data.CleaningTests.test_exact_duplicate_and_missing_value) ... ok
test_missing_identifier_is_rejected (test_clean_data.CleaningTests.test_missing_identifier_is_rejected) ... ok
test_changed_fixture_is_measured (test_data.DataTests.test_changed_fixture_is_measured) ... ok
test_known_fixture (test_data.DataTests.test_known_fixture) ... ok
test_allowlisted_action_needs_separate_approval (test_injection_lab.InjectionTests.test_allowlisted_action_needs_separate_approval) ... ok
test_prohibited_tool_blocked_even_with_approval (test_injection_lab.InjectionTests.test_prohibited_tool_blocked_even_with_approval) ... ok
test_retrieved_text_is_returned_as_inert_data (test_injection_lab.InjectionTests.test_retrieved_text_is_returned_as_inert_data) ... ok
test_calibration_bins (test_ml_core.MLCoreTests.test_calibration_bins) ... ok
test_clustering_update (test_ml_core.MLCoreTests.test_clustering_update) ... ok
test_confusion_denominators (test_ml_core.MLCoreTests.test_confusion_denominators) ... ok
test_cv_has_baseline_and_sample_sd (test_ml_core.MLCoreTests.test_cv_has_baseline_and_sample_sd) ... ok
test_gradient_and_overshoot (test_ml_core.MLCoreTests.test_gradient_and_overshoot) ... ok
test_leakage_changes_validation_predictions (test_ml_core.MLCoreTests.test_leakage_changes_validation_predictions) ... ok
test_overfitting_measured_trend (test_ml_core.MLCoreTests.test_overfitting_measured_trend) ... ok
test_wilson_independent_reference_values (test_ml_core.MLCoreTests.test_wilson_independent_reference_values) ... ok
test_malformed_response_is_rejected (test_model_adapter.ModelAdapterTests.test_malformed_response_is_rejected) ... ok
test_mock_three_observations (test_model_adapter.ModelAdapterTests.test_mock_three_observations) ... ok
test_real_model_is_explicitly_unimplemented (test_model_adapter.ModelAdapterTests.test_real_model_is_explicitly_unimplemented) ... ok
test_schema_contract_requires_fields_types_and_no_extras (test_model_adapter.ModelAdapterTests.test_schema_contract_requires_fields_types_and_no_extras) ... ok
test_symbolic_cost_arithmetic_not_actual_provider_pricing (test_model_adapter.ModelAdapterTests.test_symbolic_cost_arithmetic_not_actual_provider_pricing) ... ok

----------------------------------------------------------------------
Ran 31 tests in 2.161s

OK
PASS extracted supplied unittest suites pass: exit 0
PASS standalone HTML matches canonical sources
INFO parsed elements 22373; initial live elements excluding template contents 7309
RESULT 31 passed; 0 failed; 0 warnings; stage=final
```

The lead self-assessment adopts the final nine reviewer scores above after verifying their cited corrections against the frozen sources and recorded checks. These scores assess the section 4 criteria within the stated limits.

The contrast report’s `css_sha256` hashes the authored stylesheet bytes (CRLF); the generated style uses LF line endings. Their normalized text is identical. The authored-byte hash is `21f1f55dea636788dbc1542609af09681df8df468ec8f747b2ac48099a15f19a`; both normalized-source and embedded-style hashes are `28dc7e40557b67685cddca0af3693330409039fc336bc7ed0a036e656e32cd5f`. The page fingerprint binds the contrast measurements to the frozen HTML.

## Remaining verification limits

- **Actual screen reader:** none was driven. ARIA, DOM, keyboard and live-region observations do not constitute an actual screen-reader sanity check.
- **Operating-system clipboard:** captured/mocked copy output was checked; no real system-clipboard readback was verified.
- **Python 3.10 runtime:** not executed. Compatibility review and successful Python 3.12.10 execution do not constitute a Python 3.10 test run.
- **Real provider:** no provider account/API or paid inference was invoked. The real adapter is explicitly learner-filled; mock results do not predict real model latency, cost or nondeterminism.
- **Every printed page:** first-two-page PDFs were generated and visually inspected; full-document pagination and appearance were not manually verified.
- **Universal accessibility or factual correctness:** the actual-size samples, expanded axe, keyboard/mobile checks, technical fixture tests and reviewer judgments establish their stated scope only. Browser/assistive-technology coverage, dynamic states, all original service/model/tool descriptions and future regulatory changes remain bounded by the documented review.

## Post-cleanup verification

After the practical-route button style change and removal of temporary artifacts, `build.py --check` confirms the standalone page matches its sources. Fresh retained output records 31 consistency checks passed (including 31 extracted Python tests), 11 runtime tests passed, and 195 numeric assertions passed; all seven ML snippets also matched their expected output. The repository suite passed all eight tests and checked 456 relative links across the remaining 55 documents/applications. These source/runtime checks do not constitute a new Lighthouse or browser-accessibility run.
