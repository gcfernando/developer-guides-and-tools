# Semi-Supervised Support Vector Machines (S3VM)

**Lesson 404 · Practice**

## Your goal

See how a small support-vector example can choose labels for some unknown rows.

## Before you start

Finish supervised learning and separate validation first.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

Some training answers are missing. Extra guesses can help or spread mistakes. Use a separate set of confirmed answers to check what happened.

## Guess first

Is a pseudo-label a confirmed fact? Write your answer before running the script.

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
Chosen training pseudo-labels: (-1, -1, 1, 1)
Predictions for new rows: [-1, 1, 1]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change x or y in new_inputs.csv. Leave four blank labels and both known labels (-1 and 1) in sample.csv.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. It is a model guess.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| x | y | label |
| --- | --- | --- |
| -2 | -2 | -1 |
| -1.6 | -1.9 | -1 |
| 1.8 | 1.9 | 1 |
| 2 | 2 | 1 |
| -1.4 | -1.3 | — |
| -0.8 | -1.2 | — |
| 1 | 0.9 | — |
| 1.5 | 1.3 | — |

## 📩 Supplied new inputs

| x | y |
| --- | --- |
| -1.1 | -1 |
| 1.1 | 1 |
| 0.2 | 0.7 |

This intentionally small illustration searches a few possible labels. The new CSV has inputs without confirmed answers, so its predictions do not measure accuracy.
