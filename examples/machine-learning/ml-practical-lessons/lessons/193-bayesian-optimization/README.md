# Bayesian Optimization

**Lesson 193 · Practice**

## Your goal

Use scores from earlier trials to choose another setting to try.

## Before you start

Explain a model setting, validation folds and an error.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A search compares settings. Grid tries a list; random search samples it; Bayesian search uses earlier results to suggest a later trial.

**Why and when.** Use a small justified search after a working baseline. Keep each setting’s preparation inside its training folds.

**A worked example to follow.** The script varies Ridge alpha and uses the same folds for error comparisons. Its small Bayesian example fits a helper model to tried settings and estimates which untried setting may improve the score.

**Input and output.** The supplied sample fields are `input_1`, `input_2`, `input_3`, `answer`. In that field order, one original row is:

```text
0.5003818664186679 | 1.588855203878302 | 1.102742760980774 | 1.7477369467801798
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

You try 100 settings and report the best validation result as guaranteed future error. What is missing? Write a reason before running or opening the answer.

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

**Common mistakes and limits.** More search can overfit the validation process. A winning validation score is optimistic as a final claim. Record the search budget and use separate final evaluation.

<details>
<summary>Check your choice and reason</summary>

A separate final assessment of the selected procedure, plus counts and limits. The many comparisons used validation information to make a choice.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

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

<!-- teaching-note:start -->
<!-- teaching-profile:search -->
<!-- teaching-note:end -->
