# Z-score Algorithm

**Lesson 397 · Practice**

## Your goal

Check how many standard deviations a parcel weight lies from the training average.

## Before you start

Explain a mean and standard deviation.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A z-score measures distance from a reference mean in reference standard deviations.

**Why and when.** Use a simple review rule only when reference spread and distribution are meaningful.

**A worked example to follow.** A z-score of 3 means three training standard deviations above the training mean, not a weight of 3 kg.

**Input and output.** The supplied sample fields are `weight_kg`. In that field order, one original row is:

```text
9
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Follow the chosen measurements through their preparation and fitted grouping, projection or review rule. Read the resulting representation or flag using the explanation above; do not invent confirmed group answers. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Should a new request change the reference mean used for its own score? Write a reason before running or opening the answer.

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
Z-scores: [0.0, 24.49, 1.63]
Flagged: [False, True, False]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit the rows in new_inputs.csv. Compare a typical case with an unusually heavy parcel. A flag means check the original record.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Zero spread makes ordinary z-scoring undefined. Skew and extreme reference values affect the rule.

<details>
<summary>Check your choice and reason</summary>

No. Keep the fitted reference; updating it is an explicit monitored training change.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| weight_kg |
| --- |
| 9 |
| 8 |
| 10 |
| 11 |
| 11 |
| 10 |
| 9 |
| 12 |

## 📩 Supplied new inputs

| weight_kg |
| --- |
| 10 |
| 40 |
| 12 |

<!-- teaching-note:start -->
<!-- teaching-profile:zscore -->
<!-- teaching-note:end -->
