# Ridge/Lasso Regression

**Lesson 361 · Practice**

## Your goal

Compare two ways to keep a regression model from putting too much weight on an input.

## Before you start

Read an intercept and input coefficients; explain validation and scaling.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Regularization discourages some complex fits. Ridge penalizes squared weights; Lasso uses an absolute-weight penalty and can make some coefficients zero.

**Why and when.** Compare a penalty when noisy, overlapping or numerous inputs make an unpenalized fit unstable.

**A worked example to follow.** Run the companion penalty_lab.py to compare coefficients and validation MAE at several alpha values on the same split. Its scaler is fitted on training only, so a displayed coefficient corresponds to a one-training-standard-deviation input increase. The final test is used after choosing the setting.

**Input and output.** The supplied sample fields are `km`, `kg`, `minutes`. In that field order, one original row is:

```text
48 | 4 | 90.0
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A setting has smaller coefficient magnitudes but worse validation MAE. Is smaller automatically better? Which rows choose alpha? Write a reason before running or opening the answer.

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
New inputs and predictions:
 km  kg  predicted_minutes
  5   2              22.05
 16   4              42.35
 42   9              90.85
Ridge MAE: 1.27
First actual / predicted: 72.0 69.8
New inputs and predictions:
 km  kg  predicted_minutes
  5   2              22.09
 16   4              42.37
 42   9              90.83
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change km or kg in new_inputs.csv. The model is trained on sample.csv. The new rows only receive predictions.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Larger alpha can remove useful signal. Individual correlated-feature coefficients need not move monotonically. A zero coefficient does not prove a field never matters. Do not compare penalties across arbitrary input units without checking scaling.

<details>
<summary>Check your choice and reason</summary>

No. The penalty is a trade-off, not the goal. Choose a useful validation result with its limits; preserve the final test for the frozen choice.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

### What this particular check asks

This example keeps exact distance-and-weight combinations out of its test training rows. That is a deliberately stricter, special question. Independent orders may have the same measurements. Equal numbers alone do not prove leakage. Use shipment identity and the intended future job to choose a normal split; see lesson 442.

## 📋 Sample data

| km | kg | minutes |
| --- | --- | --- |
| 48 | 4 | 90.0 |
| 32 | 6 | 71.0 |
| 35 | 5 | 72.5 |
| 45 | 3 | 84.5 |
| 29 | 12 | 77.5 |
| 39 | 1 | 71.5 |
| 42 | 2 | 79.0 |
| 12 | 3 | 32.0 |

Showing the first 8 of 60 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| km | kg |
| --- | --- |
| 5 | 2 |
| 16 | 4 |
| 42 | 9 |

<!-- extra-lab:start -->
## See the coefficients change

The first script predicts using a fixed setting. This companion lab shows the learned weights and compares penalty settings fairly. A coefficient is the learned amount attached to one input. Here the inputs use training scales, so a coefficient means minutes per one training-standard-deviation increase, holding the other prepared input fixed.

Open the complete [penalty_lab.py](penalty_lab.py). It uses the supplied `sample.csv` and the same requirements. From this folder, run:

```bash
python penalty_lab.py
```

The lab reserves separate training, validation and final test groups. It fits the scaler on training only, compares settings on validation, and checks the chosen procedure on the final test. The no-penalty comparison uses ordinary linear regression. This special group split tests distance/weight combinations absent from training; equal measurements do not by themselves prove copied events.

**Recorded result.** These values were produced by the supplied lab:

```text
Rows: training 32, validation 12, test 16.
The split asks about new distance/weight combinations.
Coefficients: minutes per one training-standard-deviation input increase.
    method  alpha  km_coefficient  kg_coefficient  validation_mae_minutes
No penalty   0.00          23.541           6.160                   1.019
     Ridge   0.01          23.533           6.156                   1.018
     Ridge   0.10          23.462           6.127                   1.003
     Ridge   1.00          22.776           5.847                   0.896
     Ridge  10.00          17.646           3.928                   3.584
     Ridge 100.00           5.483           0.747                  10.291
     Lasso   0.01          23.529           6.148                   1.017
     Lasso   0.10          23.421           6.039                   1.006
     Lasso   1.00          22.336           4.954                   1.546
     Lasso  10.00          12.492           0.000                   7.706
     Lasso 100.00           0.000           0.000                  13.198
Validation choice: Ridge, alpha 1.
Frozen-choice test MAE: 1.527 minutes.
A smaller coefficient is not automatically a better validation result.
A zero coefficient does not prove that the field never matters.
```

Read coefficients and errors together. A stronger penalty can make a coefficient zero while also making predictions worse. A zero does not prove that the field never matters in the world. The [coefficient table](coefficient-check.csv) contains the unrounded chart values.

**Your task.** Which validation row wins? Why is the largest penalty not the best choice? Name the rows that must stay out of that choice.

<details>
<summary>Answer and reason</summary>

Ridge with alpha 1 has the lowest supplied validation MAE, about 0.896 minutes. Large penalties remove useful signal here. Final test answers do not select the setting; the frozen choice's final test MAE is about 1.527 minutes. These small invented data do not establish real-service performance.

</details>
<!-- extra-lab:end -->


<!-- teaching-note:start -->
<!-- teaching-profile:penalties -->
<!-- teaching-note:end -->
