# Cross-validation

**Lesson 194 · Core**

## Your goal

Take turns holding different deliveries back and compare the error on each group.

## Before you start

Calculate an average error and distinguish training from check rows.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Cross-validation takes turns holding groups back so a procedure is checked on several divisions.

**Why and when.** Use it inside model development when the fold design matches the intended new cases.

**A worked example to follow.** For three folds, each part is held back once while the other parts train a fresh fit. The lesson prints training size, check size and each fold’s average error in minutes.

**Input and output.** The supplied sample fields are `distance_km`, `weight_kg`, `delivery_minutes`. In that field order, one original row is:

```text
2 | 1 | 19
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

May you scale every row first and then cross-validate a classifier using the scaled table? Write a reason before running or opening the answer.

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
 Fold  Rows to learn  Rows to check  Average error in minutes
    1              4              2                      0.37
    2              4              2                      0.49
    3              4              2                      0.57
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change the known time for one delivery. Rerun and find which fold errors change.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Refit imputers/scalers inside each training fold. Random folds are unsuitable for some future-time or repeated-customer tasks. Fold variation is not automatically a confidence interval.

<details markdown="1">
<summary>Check your choice and reason</summary>

Fit a preparation/model pipeline separately inside each training fold. Otherwise its check distribution can influence preparation before the check.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| distance_km | weight_kg | delivery_minutes |
| --- | --- | --- |
| 2 | 1 | 19 |
| 4 | 3 | 30 |
| 6 | 2 | 29 |
| 8 | 4 | 40 |
| 10 | 1 | 33 |
| 12 | 3 | 44 |

<!-- teaching-note:start -->
<!-- teaching-profile:cross_validation -->
<!-- teaching-note:end -->
