# Tune model settings

**Lesson 190 · Practice**

## Your goal

Try different Ridge settings and compare how search methods find them.

## Before you start

Know a baseline, a score and a model setting.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

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
GridSearchCV 1 MAE 0.81
RandomizedSearchCV 0.062 MAE 0.837
Bayesian 1.585 MAE 0.802
 input_1  input_2  input_3  prediction
       1        0       -1        5.85
       0        0        0       -0.20
      -1        1        2       -7.36
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit new_inputs.csv and rerun the script. Change an input and its known answer consistently in sample.csv. Rerun the comparison and check what changes.

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

| input_1 | input_2 | input_3 | answer |
| --- | --- | --- | --- |
| 0.5003818664186679 | 1.588855203878302 | 1.102742760980774 | 1.7477369467801798 |
| -1.0991712400376326 | -0.7993348603550983 | 1.4942137815850476 | -10.313014425497869 |
| -1.978938781737701 | 1.2849136735310651 | 1.188277715008185 | -8.160788361954944 |
| -0.1282601886251169 | -0.7878702927227459 | -0.8862975515969067 | -1.2744124194033088 |
| -0.9805216493835016 | -0.2196947764694137 | 0.018193035831813198 | -3.421428943002779 |
| 0.21398940829796986 | 1.9820011337375707 | 1.1706476768550123 | -0.34883361965989845 |
| 0.48871691776465065 | 1.9558405907275396 | -1.1387652070576042 | 6.9672297602438125 |
| -1.3591518645686218 | 0.4501584170921231 | -1.8242319681544665 | -1.2070338972886316 |

Showing the first 8 of 42 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| input_1 | input_2 | input_3 |
| --- | --- | --- |
| 1 | 0 | -1 |
| 0 | 0 | 0 |
| -1 | 1 | 2 |

These scores compare settings on validation folds. Use an independent test set for the final score after you choose a model.
