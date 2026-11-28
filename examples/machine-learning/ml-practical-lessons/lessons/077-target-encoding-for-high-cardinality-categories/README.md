# Target Encoding (For Many Different Categories)

**Lesson 077 · Practice**

## Your goal

Summarize each supplier by its learned delay rate and try a supplier the model has never seen.

## Before you start

Understand categories, training rows and leakage.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

Count how often training orders were delayed for a supplier. A target encoder uses a careful version of this idea. It must not give a training row its own answer.

## Guess first

Why is a supplier with one order uncertain? Write your answer before running the script.

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
supplier  delayed
     S00        1
     S01        1
     S02        1
     S03        1
     S04        0
Holdout predictions: [0, 0, 0, 0, 0, 0]
Encoded supplier values: [0.23, 0.57, 0.43]
Delay probabilities: [0.42, 0.44, 0.43]
supplier  delay_probability
     S00               0.42
     S03               0.44
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Enter S00 and a supplier name such as New Supplier. Compare their encoded values and estimated chances of delay.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

One outcome is little evidence. Smoothing uses broader training information to avoid trusting a tiny group too much.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| supplier | delayed |
| --- | --- |
| S00 | 1 |
| S01 | 1 |
| S02 | 1 |
| S03 | 1 |
| S04 | 0 |
| S05 | 0 |
| S06 | 1 |
| S07 | 1 |

Showing the first 8 of 72 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| supplier |
| --- |
| S00 |
| S03 |
| New |
