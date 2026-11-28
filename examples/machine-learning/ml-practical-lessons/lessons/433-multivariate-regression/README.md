# Multivariate Regression

**Lesson 433 · Practice**

## Your goal

Predict delivery minutes and fuel use for each new delivery.

## Before you start

Explain number prediction, categories, groups and rewards.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

Choose a learning task from the answer and feedback available. Multiple regression means several inputs. Multivariate regression can mean several outputs.

## Guess first

Does the word regression mean the answer is a known category? Write your answer before running the script.

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
Simple predictions: [45.0, 51.2]
Multiple-predictor predictions: [31.0, 42.0]
Two outcomes per row: [[31.0, 1.55], [42.0, 1.95]]
 distance_km  weight_kg  predicted_minutes  predicted_fuel_litres
           5          2               27.5                   0.85
          13          3               43.5                   2.10
          20          7               70.0                   3.35
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Enter another distance and weight. Read the separate columns for estimated minutes and fuel litres.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Regression predicts numbers.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| distance_km | weight_kg | delivery_minutes |
| --- | --- | --- |
| 2 | 1 | 19 |
| 4 | 3 | 30 |
| 6 | 2 | 29 |
| 8 | 4 | 40 |
| 10 | 1 | 33 |
| 12 | 3 | 44 |

## 📩 Supplied new inputs

| distance_km | weight_kg |
| --- | --- |
| 5 | 2 |
| 13 | 3 |
| 20 | 7 |
