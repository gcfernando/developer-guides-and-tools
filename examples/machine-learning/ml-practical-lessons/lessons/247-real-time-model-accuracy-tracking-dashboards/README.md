# Real-time model accuracy tracking dashboards

**Lesson 247 · Practice**

## Your goal

Watch how accuracy changes as batches with known results arrive.

## Before you start

Read a model score and wait for actual outcomes.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

Monitoring watches later inputs and results. Drift means change over time. A change is a reason to investigate, not an automatic instruction to replace a model.

## Guess first

Can we measure new accuracy before the true answers arrive? Write your answer before running the script.

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
Recent accuracy: 0.53 median km change: 7.0
ALERT: investigate before promoting a candidate.
Later batch, live / candidate: 0.5 1.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing km from 19 to 14 in sample.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Record predictions and wait for outcomes.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| batch | km | late |
| --- | --- | --- |
| historical | 19 | True |
| historical | 13 | True |
| historical | 14 | True |
| historical | 18 | True |
| historical | 12 | True |
| historical | 16 | True |
| historical | 17 | True |
| historical | 5 | False |

Showing the first 8 of 160 rows. The CSV has the full sample.
