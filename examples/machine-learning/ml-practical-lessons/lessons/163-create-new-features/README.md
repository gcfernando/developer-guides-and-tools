# Create new features

**Lesson 163 · Practice**

## Your goal

Give the model numbers derived from dates and messages.

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
 age  urgent
  34       0
  24       0
  42       1
  32       0
  27       1
Held-out prediction: [0]
     birth            message  prediction
1996-05-01      urgent parcel           0
1990-07-04     regular update           1
2000-01-01 thanks for writing           0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit the input values in new_inputs.csv and compare the displayed predictions.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. It shows reliance by this model in this check.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| birth | message | review |
| --- | --- | --- |
| 1990-11-16 | please help urgently | 1 |
| 2000-10-03 | regular update | 0 |
| 1983-01-09 | urgent order change | 1 |
| 1992-07-05 | thanks for the update | 0 |
| 1998-03-01 | urgent call requested | 1 |

## 📩 Supplied new inputs

| birth | message |
| --- | --- |
| 1996-05-01 | urgent parcel |
| 1990-07-04 | regular update |
| 2000-01-01 | thanks for writing |
