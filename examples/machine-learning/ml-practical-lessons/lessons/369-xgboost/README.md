# XGBoost

**Lesson 369 · Practice**

## Your goal

Use XGBoost to predict delivery time and check the error in minutes.

## Before you start

Explain a fitted tree, an error and validation.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Boosting adds models in sequence so later components address remaining fitting errors under a chosen loss.

**Why and when.** Consider it for structured-table tasks after a simple baseline, with controlled complexity and validation.

**A worked example to follow.** The supplied boosting model receives distance and weight. Read prediction minutes for regression or late/on-time labels for classification, then inspect held-back errors. XGBoost and LightGBM are separate implementations with their own settings.

**Input and output.** The supplied sample fields are `km`, `kg`, `minutes`. In that field order, one original row is:

```text
48 | 4 | 90.0
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A boosted model beats a baseline on training but loses on validation. Should it replace the baseline? Write a reason before running or opening the answer.

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
XGBRegressor MAE: 5.71
First actual / predicted: 72.0 61.7
New inputs and predictions:
 km  kg  predicted_minutes
  5   2          22.840000
 16   4          51.450001
 42   9          89.629997
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change km or kg in new_inputs.csv. The model is trained on sample.csv. The new rows only receive predictions.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Sequential fitting can overfit; model size, learning rate and tree complexity need care. Package availability and fast execution are not evidence of better learning.

<details>
<summary>Check your choice and reason</summary>

Not on that evidence. Keep the stronger validated procedure or investigate a justified simpler setting without using the final test for selection.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

### What this particular check asks

This example keeps exact distance-and-weight combinations out of its test training rows. That is a deliberately stricter, special question. Independent orders may have the same measurements. Equal numbers alone do not prove leakage. Use shipment identity and the intended future job to choose a normal split; see lesson 442.

## 📋 Sample data

| km | kg | minutes |
| --- | --- | --- |
| 48 | 4 | 90.0 |
| 32 | 6 | 71.0 |
| 35 | 5 | 72.5 |
| 45 | 3 | 84.5 |
| 29 | 12 | 77.5 |
| 39 | 1 | 71.5 |
| 42 | 2 | 79.0 |
| 12 | 3 | 32.0 |

Showing the first 8 of 60 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| km | kg |
| --- | --- |
| 5 | 2 |
| 16 | 4 |
| 42 | 9 |

<!-- teaching-note:start -->
<!-- teaching-profile:boosting -->
<!-- teaching-note:end -->
