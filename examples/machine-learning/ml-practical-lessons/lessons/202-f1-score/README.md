# F1-score

**Lesson 202 · Practice**

## Your goal

Use one score that drops when either precision or recall is low.

## Before you start

Explain precision and recall.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

F1 combines precision and recall with their harmonic mean.

**Why and when.** Use it when that balance suits the class of interest, but still report the underlying counts.

**A worked example to follow.** When precision and recall are both 0.5, F1 is 0.5. When one is low, F1 is pulled down rather than taking a simple arithmetic average.

**Input and output.** The supplied sample fields are `distance`, `weight`, `answer`. In that field order, one original row is:

```text
37 | 5 | 1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A business considers misses ten times more costly than false alarms. Does maximizing F1 automatically express that policy? Write a reason before running or opening the answer.

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
Combines precision and recall. It falls when either score is low.
F1 0.919
 distance  weight  predicted_urgent
        5       2                 0
       28       7                 1
       40       5                 1
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit new_inputs.csv and rerun the script. Change an input and its known answer consistently in sample.csv. Rerun the comparison and check what changes.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** F1 ignores true negatives and does not encode every business cost. Zero-denominator handling needs a stated rule.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Define the costs and capacity explicitly and choose a cutoff using validation. Report precision and recall beside F1.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

### What this particular check asks

This example keeps exact distance-and-weight combinations out of its test training rows. That is a deliberately stricter, special question. Independent orders may have the same measurements. Equal numbers alone do not prove leakage. Use shipment identity and the intended future job to choose a normal split; see lesson 442.

## 📋 Sample data

| distance | weight | answer |
| --- | --- | --- |
| 37 | 5 | 1 |
| 25 | 7 | 1 |
| 27 | 5 | 1 |
| 35 | 7 | 1 |
| 23 | 6 | 0 |
| 31 | 7 | 1 |
| 33 | 10 | 1 |
| 9 | 2 | 0 |

Showing the first 8 of 120 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| distance | weight |
| --- | --- |
| 5 | 2 |
| 28 | 7 |
| 40 | 5 |

<!-- teaching-note:start -->
<!-- teaching-profile:f1 -->
<!-- teaching-note:end -->
