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

## Build the deliverables

Editable lesson files live in `lessons/`. The workbook text is in `Data-Science-and-Machine-Learning.md`. Edit the simple-word help in each lesson README. The main guides explain the shared ideas.

From this course folder, with the course environment active, run:

```bash
python -m pip install -r course_tools/requirements.txt
python course_tools/build_course.py
python course_tools/check_course.py
```

The build makes downloadable ZIPs and readable HTML pages. The checks inspect links, Python syntax and the documented practice changes. Run `python course_tools/check_course.py --run` to also run distinct lesson scripts. Optional packages may be absent; the report must say which lessons did not run. Build tools are for the author. A learner does not need them.

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

Keep a dated check report. Separate code changes, automated checks, manual browser checks, clean setup checks and observed learner results. The original audit remains in `course-review/`; it describes the old state. `course-review/implementation-status.csv` records the response and any checks that still require a person or another computer.
