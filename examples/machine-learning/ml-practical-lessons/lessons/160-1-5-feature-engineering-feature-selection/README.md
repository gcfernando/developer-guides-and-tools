# 1.5. Feature Engineering & Feature Selection

**Lesson 160 · Practice**

## Your goal

See how creating or choosing useful input columns helps the model.

## Before you start

Know the target and which facts exist at prediction time.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

A useful feature must be known in time. Some inputs repeat the same information. Choose features within training, not by inspecting final test answers.

## Guess first

Does a high feature-importance score prove a cause? Write your answer before running the script.

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
accuracy     0.900
precision    0.895
recall       0.944
F1           0.919
AUC-ROC      0.991
 distance  weight  predicted_urgent
        5       2                 0
       28       7                 1
       40       5                 1
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

No. It shows reliance by this model in this check.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.

### What this particular check asks

This example keeps exact distance-and-weight combinations out of its test training rows. That is a deliberately stricter, special question. Independent orders may have the same measurements. Equal numbers alone do not prove leakage. Use shipment identity and the intended future job to choose a normal split; see lesson 442.


## 📋 Sample data

| distance | weight | answer |
| --- | --- | --- |
| 37 | 5 | 1 |
| 25 | 7 | 1 |
| 27 | 5 | 1 |
| 35 | 7 | 1 |
| 23 | 6 | 0 |
| 31 | 7 | 1 |
| 33 | 10 | 1 |
| 9 | 2 | 0 |

Showing the first 8 of 120 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| distance | weight |
| --- | --- |
| 5 | 2 |
| 28 | 7 |
| 40 | 5 |

## 📊 Read the visual

![Raw input. Birth date: 2000-10-03. → Derived feature. Age on 2025-04-01: 24 years. → Reuse the rule. Follow the same reference-date rule for each new row.](features-from-raw-data.png)

**👀 Read the visual.** Choose fields the app can use when the request arrives.

**👉 What to do.** Use a feature only if the app knows it at prediction time. A measured delivery time arrives after the trip.
