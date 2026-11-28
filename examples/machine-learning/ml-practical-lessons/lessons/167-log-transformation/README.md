# Log transformation

**Lesson 167 · Practice**

## Your goal

Take a log of large sensor readings before predicting cost.

## Before you start

Compare 10, 100 and 1000 and explain a zero.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A logarithm compresses large positive gaps; log1p applies natural log to 1 + value.

**Why and when.** Try a log for a skewed measurement or a multiplicative relationship, then compare validation results with unchanged input.

**A worked example to follow.** Base-10 log maps 1, 10, 100, 1000 to 0, 1, 2, 3. log1p keeps zero valid and uses a different base. The lesson trains on the transformed signal and predicts cost in its original unit.

**Input and output.** The supplied sample fields are `signal`, `cost`. In that field order, one original row is:

```text
1 | 10
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Does writing 1000 as 1e3 make it a log feature? What happens to zero under log10 and log1p? Write a reason before running or opening the answer.

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
Log Transformation first two training rows: [[0.69], [1.79]]
Actual costs: [23, 48]
Predicted costs: [26.7, 47.2]
 signal  predicted_cost
      3           13.94
     15           31.43
     40           43.30
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try a signal reading of 3, 15, or 40 in new_inputs.csv. Compare the predicted cost for each row.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Scientific notation is only a display choice. A log actually changes the numeric feature. Check the domain; logging negative values can fail, and a target log needs its inverse before interpreting predictions.

<details>
<summary>Check your choice and reason</summary>

1e3 is still 1000. log10(0) is not finite, while log1p(0) is 0. Choose a justified valid transformation and reuse it consistently.

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
<!-- teaching-profile:log -->
<!-- teaching-note:end -->
