# Scatter Plots

**Lesson 156 · Practice**

## Your goal

Put distance on one axis and delivery time on the other.

## Before you start

Read axes, units and one point per row.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

A chart answers a question about the data. A histogram counts ranges; a scatterplot compares two facts. A correlation shows movement together, not a cause.

## Guess first

Does a strong correlation prove what causes the result? Write your answer before running the script.

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
        distance  route_distance  weight  minutes
mean         7.0             7.7    4.33    35.33
median       7.0             7.7    2.50    31.50
skew         0.0            -0.0    2.20     1.26
Distance overlap: 1.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change one measured time in sample.csv. Find the dot that moves up or down.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Check other explanations and what was actually measured.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| distance | route_distance | weight | minutes |
| --- | --- | --- | --- |
| 2 | 2.2 | 1 | 19 |
| 4 | 4.4 | 3 | 30 |
| 6 | 6.6 | 2 | 29 |
| 8 | 8.8 | 4 | 40 |
| 10 | 11 | 1 | 33 |
| 12 | 13.2 | 15 | 61 |
