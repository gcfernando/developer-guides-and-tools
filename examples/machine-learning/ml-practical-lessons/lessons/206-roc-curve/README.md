# ROC Curve

**Lesson 206 · Practice**

## Your goal

Compare catches and false alarms at two fixed practice cutoffs.

## Before you start

Count correct and wrong categories before calculating fractions.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

A missed urgent order and a false alarm are different mistakes. Precision counts correct alerts out of alerts. Recall counts caught urgent orders out of real urgent orders.

## Guess first

Which denominator belongs to recall? Write your answer before running the script.

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
 Cutoff  Urgent caught  Urgent missed  False alarms  Urgent recall  False alarm rate
   0.25             18              0             2          1.000             0.167
   0.75             17              1             1          0.944             0.083
AUC-ROC: 0.991
Here the test cutoffs are fixed for teaching. Choose an app cutoff on validation data.
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Replace 0.75 with 0.5. Compare detections and false alarms with the first row. These are practice cutoffs on the test set.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

All truly urgent orders. Write the counts first.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.

### What this particular check asks

This example keeps exact distance-and-weight combinations out of its test training rows. That is a deliberately stricter, special question. Independent orders may have the same measurements. Equal numbers alone do not prove leakage. Use shipment identity and the intended future job to choose a normal split; see lesson 442.
