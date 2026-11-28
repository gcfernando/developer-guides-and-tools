# Median

**Lesson 039 · Core**

## Your goal

Fill an empty weight with the middle training weight after sorting.

## Before you start

Find a missing input and a missing answer. Keep training and checks separate.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

A fill is an estimate, not a recovered fact. Learn a fill rule on training rows. Reuse it on new rows. Do not invent training answers.

## Guess first

May a new request change the saved training median? Write your answer before running the script.

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
 distance_km  weight_kg  filled_weight_kg  predicted_minutes  actual_minutes
          10          —               2.0              32.14            33.0
           6        2.0               2.0              29.00            29.0
          14          —               2.0              35.29               —
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change a distance in new_inputs.csv. Clear actual_minutes on that row: the old measured time does not describe your invented request. Compare the new guess.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Apply the saved rule. A deliberate retraining step is a separate action.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| distance_km | weight_kg | zone | delivery_minutes |
| --- | --- | --- | --- |
| 2 | 1 | north | 19 |
| 4 | — | north | 30 |
| 6 | 2 | — | 29 |
| 8 | 4 | south | 40 |
| 10 | 1 | ? | 33 |
| 12 | 3 | south | 44 |

## 📩 Supplied new inputs

| distance_km | weight_kg | actual_minutes |
| --- | --- | --- |
| 10 | — | 33 |
| 6 | 2 | 29 |
| 14 | — | — |
