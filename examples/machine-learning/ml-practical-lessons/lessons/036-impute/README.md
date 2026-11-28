# Fill a blank

**Lesson 036 · Practice**

## Your goal

Fill a missing parcel weight before estimating the delivery time.

## Before you start

Sort 1, 2 and 4; calculate their average and identify their middle.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Imputation supplies an estimate for a missing input. Mean, median and mode use training summaries; KNN uses similar training rows.

**Why and when.** Use a fill when an input is unavailable but a justified prediction is still possible. Learn the rule on training data and reuse it.

**A worked example to follow.** The observed training weights are 1, 2 and 4 kg. Their mean is about 2.33; median is 2. All occur once, so the most-frequent imputer breaks this tie by taking the smallest value, 1. KNN uses distance and scaled input differences to find two neighbours.

**Input and output.** The supplied sample fields are `distance_km`, `weight_kg`, `zone`, `delivery_minutes`. In that field order, one original row is:

```text
2 | 1 | north | 19
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Training weights are 1, 2, 4, 5 and 8 kg. Fill a new blank by median. Does a new 90 kg request change that saved median? Write a reason before running or opening the answer.

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
 New row               Method  Filled kg  Prediction in minutes  Actual minutes
       1                 Mean       2.33                  33.59            33.0
       2                 Mean       2.00                  28.56            29.0
       3                 Mean       2.33                  36.85               —
       1               Median       2.00                  32.14            33.0
       2               Median       2.00                  29.00            29.0
       3               Median       2.00                  35.29               —
       1 Most frequent (mode)       1.00                  45.00            33.0
       2 Most frequent (mode)       2.00                  32.60            29.0
       3 Most frequent (mode)       1.00                  57.40               —
       1  KNN (two neighbors)       3.00                  41.00            33.0
       2  KNN (two neighbors)       2.00                  31.00            29.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change a distance in new_inputs.csv. Clear actual_minutes on that row: the old measured time does not describe your invented request. Compare the new guess.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A fill is not a recovered measurement. Nearest neighbours depend on scaling. Comparing methods on one case does not establish the best method for future deliveries.

<details>
<summary>Check your choice and reason</summary>

The median is 4 kg. Apply 4 to the blank and keep the saved rule unchanged for the 90 kg request. Only an explicit new training procedure learns a new median.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| distance_km | weight_kg | zone | delivery_minutes |
| --- | --- | --- | --- |
| 2 | 1 | north | 19 |
| 4 | — | north | 30 |
| 6 | 2 | — | 29 |
| 8 | 4 | south | 40 |
| 10 | 1 | ? | 33 |
| 12 | 3 | south | 44 |

## 📩 Supplied new inputs

| distance_km | weight_kg | actual_minutes |
| --- | --- | --- |
| 10 | — | 33 |
| 6 | 2 | 29 |
| 14 | — | — |

<!-- teaching-note:start -->
<!-- teaching-profile:numeric_fill -->
<!-- teaching-note:end -->
