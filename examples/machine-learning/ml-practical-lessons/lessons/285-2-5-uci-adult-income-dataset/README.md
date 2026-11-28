# Invented income records

**Lesson 285 · Practice**

## Your goal

Use age, education and working hours from invented income records to estimate income group.

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
Missing cells before filling or removing rows: {'age': 0, 'hours': 0, 'education': 0, 'workclass': 1, 'occupation': 1, 'marital_status': 0, 'income_group': 0}
Field  Rows to review
  age               0
hours               0
Flagged original rows: []
 Original row Actual answer  Prediction
            7   50k_or_less 50k_or_less
            8     above_50k   above_50k
 age  hours education workclass occupation marital_status  prediction
  22     25    school   private     retail         single 50k_or_less
  38     45    degree    public   engineer        married   above_50k
  36     45    degree    public    manager        married   above_50k
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

| age | hours | education | workclass | occupation | marital_status | income_group |
| --- | --- | --- | --- | --- | --- | --- |
| 22 | 25 | school | private | retail | single | 50k_or_less |
| 30 | 35 | degree | private | analyst | single | 50k_or_less |
| 36 | 45 | degree | public | manager | married | above_50k |
| 49 | 47 | graduate | private | — | married | above_50k |
| 47 | 50 | degree | — | engineer | married | above_50k |
| 73 | 17 | school | private | retail | single | 50k_or_less |
| 28 | 28 | school | public | — | single | 50k_or_less |
| 38 | 45 | degree | public | engineer | married | above_50k |

## 📩 Supplied new inputs

| age | hours | education | workclass | occupation | marital_status |
| --- | --- | --- | --- | --- | --- |
| 22 | 25 | school | private | retail | single |
| 38 | 45 | degree | public | engineer | married |
| 36 | 45 | degree | public | manager | married |
