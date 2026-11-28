# Invented shopper groups

**Lesson 318 · Practice**

## Your goal

Use age, annual income and spending score from invented shopper records to estimate shopper group.

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
       age  annual_income  score
0.05  21.4        25050.0  40.70
0.95  62.4       117400.0  78.95
passthrough         age  annual_income  score
group
0      21.5        25500.0   69.0
1      60.7       104666.7   77.3
2      39.0        57666.7   51.3
New group: [1]
 age  annual_income  score region  cluster
  21        24000.0   68.0  north        0
  61        96000.0   78.0   west        1
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change annual_income or score in new_inputs.csv. Compare the new cluster with scaling turned on and off.

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

| age | annual_income | score | region |
| --- | --- | --- | --- |
| 21 | 24000 | 68 | north |
| 24 | — | 72 | north |
| 22 | 27000 | 70 | north |
| 42 | 57000 | 40 | south |
| 46 | 60000 | — | south |
| 44 | 56000 | 42 | south |
| 60 | 94000 | 75 | west |
| 58 | 90000 | 77 | west |

Showing the first 8 of 10 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| age | annual_income | score | region |
| --- | --- | --- | --- |
| 21 | 24000.0 | 68.0 | north |
| 61 | 96000.0 | 78.0 | west |
| 22 | 27000.0 | 70.0 | north |
