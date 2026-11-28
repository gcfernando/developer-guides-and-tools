# Co-Training

**Lesson 407 · Practice**

## Your goal

Let models trained on different input columns teach each other from unlabeled rows.

## Before you start

Finish supervised learning and separate validation first.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

Some training answers are missing. Extra guesses can help or spread mistakes. Use a separate set of confirmed answers to check what happened.

## Guess first

Is a pseudo-label a confirmed fact? Write your answer before running the script.

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
Labeled / unlabeled training rows: 8 46
Labels per view: [13, 13]
Holdout accuracy: 1.0
New guesses: [0, 1, 1]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit x or y in new_inputs.csv. These rows are kept separate from the rows with masked labels and the labeled check rows.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. It is a model guess.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| x | y | label |
| --- | --- | --- |
| -1.9990158773140139 | -1.761003569993224 | 0 |
| -2.219310284289774 | -2.7124734710058194 | 0 |
| -2.363736628137378 | -2.79331724399717 | 0 |
| -1.951885117922049 | -0.9278278035563732 | 0 |
| -2.3937652148410637 | -2.4963799198559524 | 0 |
| -1.6081263598518414 | -1.7144903934719513 | 0 |
| -1.9156686008016812 | -2.744374435766564 | 0 |
| -2.023401457970619 | -1.4437574444333698 | 0 |

Showing the first 8 of 72 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| x | y |
| --- | --- |
| -2 | -2 |
| 2 | 2 |
| 0.3 | 0.4 |
