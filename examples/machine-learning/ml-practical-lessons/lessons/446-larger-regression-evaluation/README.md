# Evaluate delivery errors by route, weight and zone

**Lesson 446 · Core**

## Your goal

Compare a delivery model to a median baseline on a larger batch of future deliveries.

## Before you start

Calculate MAE and a training-median baseline.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Group evaluation finds different error behavior hidden by an overall average.

**Why and when.** Inspect meaningful routes, missing inputs and zones with counts beside scores.

**A worked example to follow.** The lesson checks later deliveries, compares model and baseline in minutes, then groups errors. Reporting-boundary changes affect membership, not already-computed predictions.

**Input and output.** The supplied sample fields are `shipment_id`, `delivery_date`, `distance_km`, `weight_kg`, `zone`, `actual_minutes`. In that field order, one original row is:

```text
D00001 | 2025-01-01 | 51.86 | (missing) | North | 89.1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A missing-weight group has high MAE and few orders. What belongs in the report? Write a reason before running or opening the answer.

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
Test deliveries: 180. First test day: 2025-02-24.
  Method  MAE (min)  RMSE (min)  R squared
baseline      23.70       28.43      -0.00
   model       2.89        3.73       0.98

By route
        orders  model_mae  baseline_mae
route
Long        61       2.57         31.79
Medium      63       3.13          9.92
Short       56       2.99         30.38

```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change short_route_max_km from 25 to 20. The route-group counts should change while the overall model MAE stays the same.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Small-group scores are uncertain. Inspect actual cases before claiming a cause or repeatedly selecting from final-test subgroup results.

<details>
<summary>Check your choice and reason</summary>

Its count, error, underlying cases, missingness pattern and limitations; investigate source/pipeline behavior and check further suitable examples.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:group_errors -->
<!-- teaching-note:end -->
