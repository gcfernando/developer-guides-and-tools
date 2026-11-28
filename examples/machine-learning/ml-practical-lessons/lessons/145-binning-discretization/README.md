# Binning (Discretization)

**Lesson 145 · Practice**

## Your goal

Put continuous sensor readings into bins and use the bins as model inputs.

## Before you start

Place a value between two stated limits.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Binning puts a continuous measurement into one of several intervals.

**Why and when.** Use bins when a coarse representation is useful and the information lost inside an interval is acceptable.

**A worked example to follow.** The lesson learns training edges and makes indicator columns for bins. Two readings inside the same interval receive the same bin representation.

**Input and output.** The supplied sample fields are `signal`, `cost`. In that field order, one original row is:

```text
1 | 10
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Read the printed edges. If readings 20 and 30 fall in the same bin, can a model receiving only that bin distinguish them? Write a reason before running or opening the answer.

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
Binning first two training rows: [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]
Actual costs: [23, 48]
Predicted costs: [25.0, 53.0]
Training edges: [1.0, 54.0, 107.0, 160.0]
 signal  predicted_cost
      3            25.0
     15            25.0
     40            25.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Enter 3, 60, and 150 as signal values. Compare their predictions with the printed bin limits.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** An edge convention determines which interval owns a boundary value. Relearning edges on each request changes what a column means.

<details>
<summary>Check your choice and reason</summary>

No. It sees the same representation. Compare this loss with using the original signal, and keep training edges fixed for later rows.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| signal | cost |
| --- | --- |
| 1 | 10 |
| 5 | 18 |
| 12 | 25 |
| 20 | 31 |
| 35 | 41 |
| 80 | 53 |
| 160 | 64 |
| 10 | 23 |

Showing the first 8 of 9 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| signal |
| --- |
| 3 |
| 15 |
| 40 |

<!-- teaching-note:start -->
<!-- teaching-profile:bins -->
<!-- teaching-note:end -->
