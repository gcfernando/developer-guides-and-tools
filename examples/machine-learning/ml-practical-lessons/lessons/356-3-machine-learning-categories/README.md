# 3. Machine Learning Categories

**Lesson 356 · Practice**

## Your goal

Try a delivery prediction, then explore the other types of learning.

## Before you start

Finish the main path through overfitting and validation.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

Different algorithms learn different rules. The catalog is practice, not a leaderboard for choosing from final test scores. Use a common validation comparison for your own choice.

## Guess first

Should you choose a model by opening many final test results? Write your answer before running the script.

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
LinearRegression MAE: 1.26
First actual / predicted: 72.0 69.9
New inputs and predictions:
 km  kg  predicted_minutes
  5   2              22.02
 16   4              42.33
 42   9              90.87
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change km or kg in new_inputs.csv. The model is trained on sample.csv. The new rows only receive predictions.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Use validation first, then one final check.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.

### What this particular check asks

This example keeps exact distance-and-weight combinations out of its test training rows. That is a deliberately stricter, special question. Independent orders may have the same measurements. Equal numbers alone do not prove leakage. Use shipment identity and the intended future job to choose a normal split; see lesson 442.


## 📋 Sample data

| km | kg | minutes |
| --- | --- | --- |
| 48 | 4 | 90.0 |
| 32 | 6 | 71.0 |
| 35 | 5 | 72.5 |
| 45 | 3 | 84.5 |
| 29 | 12 | 77.5 |
| 39 | 1 | 71.5 |
| 42 | 2 | 79.0 |
| 12 | 3 | 32.0 |

Showing the first 8 of 60 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| km | kg |
| --- | --- |
| 5 | 2 |
| 16 | 4 |
| 42 | 9 |
