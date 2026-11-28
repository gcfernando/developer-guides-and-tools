# ANOVA

**Lesson 172 · Practice**

## Your goal

Use ANOVA to ask whether a numeric measurement differs across groups.

## Before you start

Know the target and which facts exist at prediction time.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

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
ANOVA selected: ['minutes']
Held-out labels: [0, 1]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In sample.csv, change one keyword indicator from 0 to 1. Keep the recorded review answer. Compare which field is selected. Changing id alone should not affect the model.

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

| id | minutes | duplicate_minutes | keyword | review |
| --- | --- | --- | --- | --- |
| 0 | 2 | 2 | 0 | 0 |
| 1 | 18 | 18 | 1 | 1 |
| 2 | 3 | 3 | 0 | 0 |
| 3 | 20 | 20 | 1 | 1 |
| 4 | 4 | 4 | 1 | 0 |
| 5 | 23 | 23 | 0 | 1 |
| 6 | 5 | 5 | 0 | 0 |
| 7 | 24 | 24 | 1 | 1 |
