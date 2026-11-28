# Forward Fill (ffill)

**Lesson 046 · Practice**

## Your goal

Carry the most recent known count forward to fill a missing day.

## Before you start

Put days in order and say when a reading becomes available.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Forward fill copies the last available reading. Backward fill copies a later reading into an earlier gap.

**Why and when.** Forward fill may suit a value that stays current until replaced. Backward fill is for retrospective repair when the later reading is already known.

**A worked example to follow.** With counts 10, blank, 16 on days 1, 2, 3, forward fill gives day 2 a value of 10 and backward fill gives 16. These are estimates with different timing assumptions.

**Input and output.** The supplied sample fields are `day`, `requests`. In that field order, one original row is:

```text
1 | 10
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Day 3 changes to 18. Which day-2 fill changes? Which fill is available during day 2? Write a reason before running or opening the answer.

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
 day  requests  forward  backward
   1      10.0     10.0      10.0
   2       NaN     10.0      16.0
   3      16.0     16.0      16.0
   4      19.0     19.0      19.0
Day 5 forecast: [22.0]
 day  prediction
   6        25.3
   7        28.6
  10        38.5
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit the input values in new_inputs.csv and compare the displayed predictions.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A live day-2 decision cannot use a day-3 reading. Long gaps, resets and rapidly changing measurements may make either fill unsuitable.

<details>
<summary>Check your choice and reason</summary>

Backward fill changes to 18; forward fill stays 10. Only the past value is available during day 2. Whether carrying it forward is useful still needs validation.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| day | requests |
| --- | --- |
| 1 | 10 |
| 2 | — |
| 3 | 16 |
| 4 | 19 |
| 5 | 22 |

## 📩 Supplied new inputs

| day |
| --- |
| 6 |
| 7 |
| 10 |

<!-- teaching-note:start -->
<!-- teaching-profile:time_fill -->
<!-- teaching-note:end -->
