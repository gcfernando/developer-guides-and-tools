# Multivariate Regression

**Lesson 433 · Practice**

## Your goal

Predict delivery minutes and fuel use for each new delivery.

## Before you start

Distinguish several predictors from several outcomes.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Multiple regression uses several predictors; multivariate/multioutput regression predicts several numeric targets.

**Why and when.** Use several outputs when each has defined meaning and suitable training/check answers.

**A worked example to follow.** The lesson predicts minutes and a separately constructed fuel value from distance and weight. Each output needs its own unit and error interpretation.

**Input and output.** The supplied sample fields are `distance_km`, `weight_kg`, `delivery_minutes`. In that field order, one original row is:

```text
2 | 1 | 19
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Does adding weight as a second input make a single-time-output task multioutput? Write a reason before running or opening the answer.

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
Simple predictions: [45.0, 51.2]
Multiple-predictor predictions: [31.0, 42.0]
Two outcomes per row: [[31.0, 1.55], [42.0, 1.95]]
 distance_km  weight_kg  predicted_minutes  predicted_fuel_litres
           5          2               27.5                   0.85
          13          3               43.5                   2.10
          20          7               70.0                   3.35
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Enter another distance and weight. Read the separate columns for estimated minutes and fuel litres.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Fuel is a created teaching rule, not measured consumption. Do not combine litres and minutes into an unexplained score.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Multioutput needs multiple target columns, each evaluated meaningfully.

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

## 📩 Supplied new inputs

| distance_km | weight_kg |
| --- | --- |
| 5 | 2 |
| 13 | 3 |
| 20 | 7 |

<!-- teaching-note:start -->
<!-- teaching-profile:multioutput -->
<!-- teaching-note:end -->
