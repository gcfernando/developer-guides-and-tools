# Choose the best Machine Learning model

**Lesson 188 · Practice**

## Your goal

Check which model works better on the same rows and metric.

## Before you start

Know a baseline, a score and a model setting.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

Compare candidates on the same validation rows. A setting controls learning. Cross-validation repeats checks inside training. Do not call the best validation score a final test.

## Guess first

Does the smallest training error always win? Write your answer before running the script.

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
DummyClassifier 0.687
LogisticRegression 0.908
DecisionTreeClassifier 0.744
RandomForestClassifier 0.825
SVC 0.88
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change an input and its known answer consistently in sample.csv. Rerun the comparison and check what changes.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. It may memorize. Use separate validation results to choose.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| km | kg | answer |
| --- | --- | --- |
| 47 | 3 | 1 |
| 31 | 6 | 1 |
| 34 | 11 | 1 |
| 44 | 10 | 1 |
| 29 | 8 | 1 |
| 39 | 8 | 1 |
| 41 | 1 | 1 |
| 12 | 9 | 0 |

Showing the first 8 of 84 rows. The CSV has the full sample.

These scores compare settings on validation folds. Use an independent test set for the final score after you choose a model.
