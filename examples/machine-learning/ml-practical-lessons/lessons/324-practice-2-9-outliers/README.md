# Outliers

**Lesson 324 · Practice**

## Your goal

Look for unusual measurements in the invented shopper records and see which rows need checking.

## Before you start

Read the named fields and explain the preparation taught earlier.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

An outlier check identifies an unusual recorded value or pattern without establishing that it is wrong.

**Why and when.** Use it to choose source records for review in this shopper records exercise.

**A worked example to follow.** The shopper records exercise uses age, annual_income, score and region. Its output is cluster assignment. Read the printed flags beside their field names, then return to the original row. There are no supplied correct cluster labels. A numeric group ID is just a name.

**Input and output.** The supplied sample fields are `age`, `annual_income`, `score`, `region`. In that field order, one original row is:

```text
21 | 24000 | 68 | north
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Pick one possibly unusual case in this shopper records exercise. List evidence that would justify keeping it, correcting it, or leaving it flagged. Write a reason before running or opening the answer.

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
       age  annual_income  score
0.05  21.4        25050.0  40.70
0.95  62.4       117400.0  78.95
passthrough         age  annual_income  score
group
0      21.5        25500.0   69.0
1      60.7       104666.7   77.3
2      39.0        57666.7   51.3
New group: [1]
 age  annual_income  score region  cluster
  21        24000.0   68.0  north        0
  61        96000.0   78.0   west        1
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change annual_income or score in new_inputs.csv. Compare the new cluster with scaling turned on and off.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A rare but valid case should not be deleted just to improve a fit. Pixel outliers need inspection of drawings rather than a parcel-weight rule.

<details markdown="1">
<summary>Check your choice and reason</summary>

Keep a source-confirmed valid case; correct only from a reliable source; preserve uncertainty when evidence is absent. State whether the case belongs within the model’s intended scope.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| age | annual_income | score | region |
| --- | --- | --- | --- |
| 21 | 24000 | 68 | north |
| 24 | — | 72 | north |
| 22 | 27000 | 70 | north |
| 42 | 57000 | 40 | south |
| 46 | 60000 | — | south |
| 44 | 56000 | 42 | south |
| 60 | 94000 | 75 | west |
| 58 | 90000 | 77 | west |

Showing the first 8 of 10 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| age | annual_income | score | region |
| --- | --- | --- | --- |
| 21 | 24000.0 | 68.0 | north |
| 61 | 96000.0 | 78.0 | west |
| 22 | 27000.0 | 70.0 | north |

<!-- teaching-note:start -->
<!-- teaching-profile:dataset_324 -->
<!-- teaching-note:end -->
