# Practice

**Lesson 295 · Practice**

## Your goal

Use alcohol, citric acid and sulphates from invented wine measurements to estimate quality.

## Before you start

Finish the main preparation and checking modules.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

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
Missing cells before filling or removing rows: {'alcohol': 0, 'citric_acid': 0, 'sulphates': 1, 'quality': 0}
      Field  Rows to review
    alcohol               1
citric_acid               0
  sulphates               0
Flagged original rows: [6]
 Original row  Actual answer  Prediction
            7              5         5.2
            8              7         7.1
Class predictions: ['lower', 'higher']
 alcohol  citric_acid  sulphates  prediction
     8.0          0.2        0.3    4.279202
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

| alcohol | citric_acid | sulphates | quality |
| --- | --- | --- | --- |
| 8 | .2 | .3 | 4 |
| 9 | .2 | .4 | 5 |
| 10 | .3 | — | 5 |
| 11 | .3 | .6 | 6 |
| 12 | .4 | .7 | 7 |
| 16 | .3 | 1.1 | 8 |
| 9.5 | .2 | .4 | 5 |
| 12.1 | .4 | .7 | 7 |

## 📩 Supplied new inputs

| alcohol | citric_acid | sulphates |
| --- | --- | --- |
| 8.0 | 0.2 | 0.3 |
| 12.1 | 0.4 | 0.7 |
| 10.0 | 0.3 | — |
