# Target Encoding (For Many Different Categories)

**Lesson 077 · Practice**

## Your goal

Summarize each supplier by its learned delay rate and try a supplier the model has never seen.

## Before you start

Count delayed orders and explain training-only preparation.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Target encoding replaces a category with a summary learned from training answers.

**Why and when.** Consider it for many categories when one-hot columns become unwieldy. Validate the whole preparation/model pipeline.

**A worked example to follow.** If two of five supplier orders were delayed, the simple observed rate is 0.40. The lesson uses smoothing for small groups and cross-fitting so a training row does not provide its own encoded answer. An unseen supplier uses broader training information.

**Input and output.** The supplied sample fields are `supplier`, `delayed`. In that field order, one original row is:

```text
S00 | 1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A supplier has one order and its answer is delayed. Is writing 1.0 into that same training row a safe target encoding? Write a reason before running or opening the answer.

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
supplier  delayed
     S00        1
     S01        1
     S02        1
     S03        1
     S04        0
Holdout predictions: [0, 0, 0, 0, 0, 0]
Encoded supplier values: [0.23, 0.57, 0.43]
Delay probabilities: [0.42, 0.44, 0.43]
supplier  delay_probability
     S00               0.42
     S03               0.44
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Enter S00 and a supplier name such as New Supplier. Compare their encoded values and estimated chances of delay.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A supplier with one delayed order does not establish a true delay chance of 100%. Predicting wholly new suppliers needs a supplier-grouped evaluation.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. It can reveal the row’s own answer. Use a training procedure with cross-fitting and appropriate smoothing, and keep evaluation answers out of all preparation.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| supplier | delayed |
| --- | --- |
| S00 | 1 |
| S01 | 1 |
| S02 | 1 |
| S03 | 1 |
| S04 | 0 |
| S05 | 0 |
| S06 | 1 |
| S07 | 1 |

Showing the first 8 of 72 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| supplier |
| --- |
| S00 |
| S03 |
| New |

<!-- teaching-note:start -->
<!-- teaching-profile:target_encoding -->
<!-- teaching-note:end -->
