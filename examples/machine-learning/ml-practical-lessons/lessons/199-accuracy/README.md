# Accuracy

**Lesson 199 · Practice**

## Your goal

Count the share of predictions that match their known answers.

## Before you start

Count correct and incorrect category guesses.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Accuracy is correct predictions divided by all predictions.

**Why and when.** Use it when correct classifications have a useful common meaning; inspect class counts and error costs too.

**A worked example to follow.** If 27 of 30 orders are classified correctly, accuracy is 27 ÷ 30 = 90%. It does not say which three orders were wrong.

**Input and output.** The supplied sample fields are `distance`, `weight`, `answer`. In that field order, one original row is:

```text
37 | 5 | 1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

There are 99 regular orders and one urgent order. A model always says regular. Is its 99% accuracy enough? Write a reason before running or opening the answer.

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
Fraction of all rows the model classified correctly.
accuracy 0.9
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

**Common mistakes and limits.** Rare urgent orders can be missed while overall accuracy remains high.

<details>
<summary>Check your choice and reason</summary>

No. It misses the only urgent order. Report the confusion counts, recall and the decision costs.

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
<!-- teaching-profile:accuracy -->
<!-- teaching-note:end -->
