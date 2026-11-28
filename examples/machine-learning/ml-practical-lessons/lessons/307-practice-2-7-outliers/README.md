# Outliers

**Lesson 307 · Practice**

## Your goal

Look for unusual measurements in the invented neighborhood records and see which rows need checking.

## Before you start

Finish the main preparation and checking modules.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

These are small invented practice datasets. Their old famous-dataset headings are historical labels. Use training rows to learn preparation and keep the check rows separate.

## Guess first

Do two correct examples prove that the model will work for a real population? Write your answer before running the script.

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
Missing cells before filling or removing rows: {'crime_per_1000': 0, 'rooms': 0, 'household_income': 1, 'zone': 0, 'price': 0}
           Field  Rows to review
  crime_per_1000               1
           rooms               0
household_income               1
Flagged original rows: [5, 6]
 Original row  Actual answer  Prediction
            7         230000    235290.5
            8         312000    317095.4
 crime_per_1000  rooms  household_income    zone    prediction
              2      3           38000.0   North 180000.000000
              1      5           61000.0   South 317095.435685
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change an input in new_inputs.csv. Compare the predictions with the held-out check above.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. They show the calculation. Check more suitable data and describe what is missing.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| crime_per_1000 | rooms | household_income | zone | price |
| --- | --- | --- | --- | --- |
| 2 | 3 | 38000 | North | 180000 |
| 1 | 5 | 57000 | South | 300000 |
| 4 | 4 | — | Central | 215000 |
| 3 | 4 | 48000 | North | 240000 |
| 1 | 7 | 124000 | South | 620000 |
| 8 | 3 | 41000 | Central | 170000 |
| 2 | 4 | 47000 | North | 230000 |
| 1 | 5 | 61000 | South | 312000 |

## 📩 Supplied new inputs

| crime_per_1000 | rooms | household_income | zone |
| --- | --- | --- | --- |
| 2 | 3 | 38000.0 | North |
| 1 | 5 | 61000.0 | South |
| 4 | 4 | — | Central |
