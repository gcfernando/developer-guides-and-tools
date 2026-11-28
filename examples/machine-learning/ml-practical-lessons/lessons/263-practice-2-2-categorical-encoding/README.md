# Category encoding

**Lesson 263 · Practice**

## Your goal

Turn categories in the invented ferry bookings into numbers the model can read.

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
Missing cells before filling or removing rows: {'age': 1, 'fare': 0, 'family_size': 0, 'cabin_recorded': 0, 'pass_type': 0, 'terminal': 1, 'priority': 0}
         Field  Rows to review
           age               0
          fare               1
   family_size               0
cabin_recorded               0
Flagged original rows: [7]
 Original row  Actual answer  Prediction
            8              0           0
            9              1           1
 age  fare pass_type terminal cabin  siblings  parents  family_size  cabin_recorded  prediction
18.0    12  standard    north   NaN         0        1            2               0           0
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

| age | fare | pass_type | terminal | cabin | siblings | parents | priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 18 | 12 | standard | north | — | 0 | 1 | 0 |
| — | 18 | standard | — | A | 1 | 0 | 0 |
| 52 | 46 | premium | south | B | 0 | 0 | 1 |
| 34 | 24 | standard | north | — | 1 | 1 | 0 |
| 62 | 64 | premium | south | C | 0 | 0 | 1 |
| 65 | 22 | standard | south | B | 0 | 0 | 1 |
| 29 | 120 | premium | north | A | 2 | 0 | 1 |
| 19 | 19 | standard | north | — | 0 | 1 | 0 |

Showing the first 8 of 9 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| age | fare | pass_type | terminal | cabin | siblings | parents |
| --- | --- | --- | --- | --- | --- | --- |
| 18.0 | 12 | standard | north | — | 0 | 1 |
| 57.0 | 42 | premium | south | B | 1 | 1 |
| 52.0 | 46 | premium | south | B | 0 | 0 |
