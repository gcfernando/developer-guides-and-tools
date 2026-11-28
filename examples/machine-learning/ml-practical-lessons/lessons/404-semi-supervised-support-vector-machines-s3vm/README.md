# Semi-Supervised Support Vector Machines (S3VM)

**Lesson 404 · Practice**

## Your goal

See how a small support-vector example can choose labels for some unknown rows.

## Before you start

Separate confirmed labels from unlabeled inputs.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Semi-supervised learning uses confirmed labels and unlabeled training inputs under extra assumptions.

**Why and when.** Consider it when labels are scarce and unlabeled structure plausibly helps.

**A worked example to follow.** This tiny SVM enumerates balanced label assignments for four unlabeled points and compares weighted objectives. New-row guesses have no confirmed answers, so do not measure accuracy.

**Input and output.** The supplied sample fields are `x`, `y`, `label`. In that field order, one original row is:

```text
-2 | -2 | -1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

May guessed labels count as confirmed evaluation successes? Write a reason before running or opening the answer.

## Run one step at a time

1. Extract this ZIP. Open folders until you see `lesson.py`.
2. Open a terminal in that folder. Activate the course environment as shown in Setup. Every `python` below means that environment's Python.
3. The main path uses the common course packages. If this lesson needs more, use the same Python to install `requirements.txt` with the course constraint file. See Setup step 8. Do not install optional media packages just to read a lesson.
4. Run these lines one at a time. Wait for each to finish.

```bash
python lesson.py
```

## Check the result

Read the column names and units before the numbers. The original files produced this example. Your deliberate data edits may change it.

```text
Chosen training pseudo-labels: (-1, -1, 1, 1)
Predictions for new rows: [-1, 1, 1]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change x or y in new_inputs.csv. Leave four blank labels and both known labels (-1 and 1) in sample.csv.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Guesses are not facts. The search grows exponentially and its balance constraint is an assumption.

<details>
<summary>Check your choice and reason</summary>

No. Compare with a labeled-only baseline on separate confirmed answers.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| x | y | label |
| --- | --- | --- |
| -2 | -2 | -1 |
| -1.6 | -1.9 | -1 |
| 1.8 | 1.9 | 1 |
| 2 | 2 | 1 |
| -1.4 | -1.3 | — |
| -0.8 | -1.2 | — |
| 1 | 0.9 | — |
| 1.5 | 1.3 | — |

## 📩 Supplied new inputs

| x | y |
| --- | --- |
| -1.1 | -1 |
| 1.1 | 1 |
| 0.2 | 0.7 |

This intentionally small illustration searches a few possible labels. The new CSV has inputs without confirmed answers, so its predictions do not measure accuracy.

<!-- teaching-note:start -->
<!-- teaching-profile:s3vm -->
<!-- teaching-note:end -->
