# Log1p and base-10 log

**Lesson 137 · Practice**

## Your goal

Compare what happens when you apply log1p to a reading and when you use a base-10 log.

## Before you start

Understand scaling, a baseline and validation.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

Use a transformation only for a stated reason. Compare it with unchanged inputs on the same validation rows. Learn every data-based rule inside training.

## Guess first

Must all eight transformations be applied? Write your answer before running the script.

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
 signal  log1p  log10
      1  0.693  0.000
      5  1.792  0.699
     12  2.565  1.079
     20  3.045  1.301
     35  3.584  1.544
     80  4.394  1.903
    160  5.081  2.204
     10  2.398  1.000
     55  4.025  1.740
Log Transformation first two training rows: [[0.69], [1.79]]
Actual costs: [23, 48]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try a reading of 3, 15, or 40 in new_inputs.csv. Read the log1p and base-10 comparison for the positive training readings.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Start simple. Compare a suitable candidate and keep separate final test rows.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


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
