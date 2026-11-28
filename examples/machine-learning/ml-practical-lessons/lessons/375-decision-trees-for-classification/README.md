# Decision Trees (for Classification)

**Lesson 375 · Practice**

## Your goal

Use a tree of yes/no decisions to predict whether a delivery will be late.

## Before you start

Read a yes/no condition and count classes.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A classification tree learns conditions that divide rows into regions with class evidence.

**Why and when.** Use it for threshold/interacting patterns while controlling depth and checking separate cases.

**A worked example to follow.** A branch asks about one input, then another. A new delivery follows the same conditions to a leaf; its class comes from the training evidence there.

**Input and output.** The supplied sample fields are `km`, `kg`, `late`. In that field order, one original row is:

```text
48 | 4 | 1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A leaf contains one urgent training order and no others. Should its apparently perfect training purity establish certainty? Write a reason before running or opening the answer.

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
Accuracy: 1.0
Predicted: [0, 1, 0, 1]
Actual: [0, 1, 0, 1]
 km  kg  predicted_late
  5   2               0
 16   4               0
 42   9               1
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change km or kg in new_inputs.csv. The model is trained on sample.csv. The new rows only receive predictions.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Deep leaves can contain very few cases. A readable rule is not automatically a reliable or causal rule.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. One case is weak evidence. Check independent rows, constrain complexity and report the available counts.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

### What this particular check asks

This example keeps exact distance-and-weight combinations out of its test training rows. That is a deliberately stricter, special question. Independent orders may have the same measurements. Equal numbers alone do not prove leakage. Use shipment identity and the intended future job to choose a normal split; see lesson 442.

## 📋 Sample data

| km | kg | late |
| --- | --- | --- |
| 48 | 4 | 1 |
| 32 | 6 | 1 |
| 35 | 5 | 1 |
| 45 | 3 | 1 |
| 29 | 12 | 1 |
| 39 | 1 | 1 |
| 42 | 2 | 1 |
| 12 | 3 | 0 |

Showing the first 8 of 60 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| km | kg |
| --- | --- |
| 5 | 2 |
| 16 | 4 |
| 42 | 9 |

<!-- teaching-note:start -->
<!-- teaching-profile:classification_tree -->
<!-- teaching-note:end -->
