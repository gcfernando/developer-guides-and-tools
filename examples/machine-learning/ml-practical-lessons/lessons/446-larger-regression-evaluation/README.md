# Evaluate delivery errors by route, weight and zone

**Lesson 446 · Core**

## Your goal

Compare a delivery model to a median baseline on a larger batch of future deliveries.

## Before you start

Calculate MAE and explain a baseline.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

Read overall error and errors by route, weight and zone. Put counts beside scores. A small group is less certain.

## Guess first

Which matters beside a group's MAE? Write your answer before running the script.

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

<details>
<summary>Read the answer after trying</summary>

Its size and the actual examples behind its errors.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.
