# Handle missing dates using interpolation

**Lesson 101 · Practice**

## Your goal

Estimate a missing time-series reading from the readings on either side.

## Before you start

Put dates in order and check that each date appears once.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

A daily calendar can reveal a missing measurement. Interpolation estimates it using readings around the gap. Here we are looking back, not predicting live.

## Guess first

If February 3 rises, can the estimate for February 2 rise? Write your answer before running the script.

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
            observed  interpolated
day
2025-02-01      10.0          10.0
2025-02-02       NaN          13.0
2025-02-03      16.0          16.0
2025-02-04      19.0          19.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In sample.csv, change orders for 2025-02-03 from 16 to 18. The February 2 estimate should become 14. Keep each date unique.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

Yes. The past-series estimate uses that later reading. Do not use it for a live February 2 decision.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| day | orders |
| --- | --- |
| 2025-02-01 | 10 |
| 2025-02-03 | 16 |
| 2025-02-04 | 19 |
