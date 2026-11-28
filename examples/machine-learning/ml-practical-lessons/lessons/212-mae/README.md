# MAE

**Lesson 212 · Practice**

## Your goal

Read the average size of the error in the original unit, minutes. Worked calculation using two test trips.

## Before you start

Subtract times and average mistake sizes.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A residual is actual minus predicted. MAE averages its size; RMSE gives large errors more weight; R squared compares squared errors with a mean benchmark.

**Why and when.** Use errors in the target’s units to assess number predictions. Inspect counts and individual mistakes beside a summary.

**A worked example to follow.** Actual times 30 and 40 with predictions 28 and 36 have errors 2 and 4 minutes. MAE is 3 minutes; RMSE is √10, about 3.16 minutes. A positive residual means the estimate was too short. These are worked arithmetic values, not a new measured experiment.

**Input and output.** The supplied sample fields are `distance_km`, `weight_kg`, `delivery_minutes`. In that field order, one original row is:

```text
2 | 1 | 19
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Errors 0, 0, 0, 0, 10 and errors 2, 2, 2, 2, 2 both have MAE 2. Why could a customer prefer the second model? Write a reason before running or opening the answer.

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
Worked calculation: two test deliveries. Use lesson 446 for a larger evaluation.
Average absolute error in minutes.
2.0
 distance_km  weight_kg  prediction
           5          2        27.5
          13          3        43.5
          20          7        70.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit the input values in new_inputs.csv and compare the displayed predictions.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Two rows teach arithmetic, not stable model performance. R squared’s mean benchmark uses the same check outcomes and is not the trained deployment baseline.

<details>
<summary>Check your choice and reason</summary>

The first has one very large miss. Examine tail errors, limits and how errors affect decisions, not just a matching average.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:regression_errors -->
<!-- teaching-note:end -->
