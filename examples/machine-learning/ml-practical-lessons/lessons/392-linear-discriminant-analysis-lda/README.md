# Use labels to make fewer inputs (supervised LDA)

**Lesson 392 · Practice**

## Your goal

Use known group labels to build a smaller set of measurements that separates the groups.

## Before you start

Explain supplied labels and a projection.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

LDA uses known class labels to find separating directions under its assumptions.

**Why and when.** Use it as a supervised projection/classifier with suitable validation.

**A worked example to follow.** The fit receives group labels. New inputs use the saved projection without their true answers. With C classes, the discriminant projection has at most C−1 directions.

**Input and output.** The supplied sample fields are `long`, `wide`, `score`, `group`. In that field order, one original row is:

```text
2 | 1 | 3 | 0
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

May final test labels help fit the projection before evaluating a classifier? Write a reason before running or opening the answer.

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
Training class predictions: [0, 0, 0, 1, 1, 1, 1, 1]
Output shape: (8, 1)
First two rows: [[-3.92], [-2.91]]
[2 1 3] -> [-3.92]
[10  9 10] -> [3.76]
[4 1 2] -> [-5.26]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change long, wide or score in one new row. Compare the resulting projection with the training projections.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** This is supervised. A separated training picture does not establish held-back performance.

<details>
<summary>Check your choice and reason</summary>

No. Fit the supervised projection inside training; otherwise it leaks test answers.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| long | wide | score | group |
| --- | --- | --- | --- |
| 2 | 1 | 3 | 0 |
| 3 | 2 | 4 | 0 |
| 4 | 1 | 2 | 0 |
| 5 | 6 | 7 | 1 |
| 6 | 7 | 8 | 1 |
| 7 | 6 | 9 | 1 |
| 8 | 8 | 7 | 1 |
| 10 | 9 | 10 | 1 |

## 📩 Supplied new inputs

| long | wide | score |
| --- | --- | --- |
| 2 | 1 | 3 |
| 10 | 9 | 10 |
| 4 | 1 | 2 |

<!-- teaching-note:start -->
<!-- teaching-profile:lda -->
<!-- teaching-note:end -->
