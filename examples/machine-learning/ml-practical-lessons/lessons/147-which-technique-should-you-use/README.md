# Which Technique Should You Use?

**Lesson 147 · Practice**

## Your goal

Use the same validation folds to compare which transformation makes better predictions.

## Before you start

Calculate an error and distinguish training from validation.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A transformation is a candidate preparation choice, not a compulsory checklist.

**Why and when.** Compare a sensible change with unchanged inputs on identical validation folds.

**A worked example to follow.** The script fits each transformation inside a pipeline for each training fold, then reports error on that fold’s held-back rows. This prevents a fold’s check values from choosing its scale or bin edges.

**Input and output.** The supplied sample fields are `signal`, `cost`. In that field order, one original row is:

```text
1 | 10
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Transform A has lower training error but higher validation error than raw inputs. Which setup has better evidence for the next check? Write a reason before running or opening the answer.

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
Raw                         MAE 10.88
Min-Max Scaling             MAE 12.18
Z-Score Standardization     MAE 10.94
Log Transformation          MAE 3.64
Robust Scaling              MAE 10.37
Power Transformations       MAE 3.64
Quantile Transformation     MAE 12.63
Binning                     MAE 12.63
Polynomial Features         MAE 10.80
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing signal from 1 to 12 in sample.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** The best score on this tiny table may be unstable. Do not apply every transform or use repeated final test scores to choose among them.

<details markdown="1">
<summary>Check your choice and reason</summary>

Raw inputs have better validation evidence in this comparison. State the counts and variation, freeze the choice, and assess it on a separate final check.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| signal | cost |
| --- | --- |
| 1 | 10 |
| 5 | 18 |
| 12 | 25 |
| 20 | 31 |
| 35 | 41 |
| 80 | 53 |
| 160 | 64 |
| 10 | 23 |

Showing the first 8 of 9 rows. The CSV has the full sample.

These scores compare settings on validation folds. Use an independent test set for the final score after you choose a model.

<!-- teaching-note:start -->
<!-- teaching-profile:choose_transform -->
<!-- teaching-note:end -->
