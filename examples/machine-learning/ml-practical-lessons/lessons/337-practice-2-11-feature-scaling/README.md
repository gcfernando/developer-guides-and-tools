# Feature scaling

**Lesson 337 · Practice**

## Your goal

Put the numerical inputs on a common scale before using the invented health-related rows in a model.

## Before you start

Read the named fields and explain the preparation taught earlier.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Scaling changes numerical representation using one saved training rule.

**Why and when.** Use it when units or pixel ranges affect the model in the health-related practice rows exercise.

**A worked example to follow.** The health-related practice rows exercise uses age, cholesterol, blood_pressure, exercise_score and categories. Its output is example_label. Learn numeric scales from training rows and apply them unchanged to the kept-back rows. The fabricated labels have no diagnostic or clinical use.

**Input and output.** The supplied sample fields are `age`, `cholesterol`, `blood_pressure`, `exercise_score`, `sex`, `chest_pain`, `example_label`. In that field order, one original row is:

```text
29 | 155 | 111 | 80 | F | none | 0
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Explain one actual scaled input in this health-related practice rows exercise. Would changing only that input’s unit during prediction preserve the contract? Write a reason before running or opening the answer.

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
Missing cells before filling or removing rows: {'age': 0, 'cholesterol': 0, 'blood_pressure': 0, 'exercise_score': 0, 'sex': 0, 'chest_pain': 0, 'example_label': 0}
         Field  Rows to review
           age               0
   cholesterol               0
blood_pressure               0
exercise_score               0
Flagged original rows: []
 Original row  Actual answer  Prediction
            7              0           0
            8              1           1
 age  cholesterol  blood_pressure  exercise_score sex chest_pain  prediction
  29          155             111              80   F       none           0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change an input in new_inputs.csv. Compare the predictions with the held-out check above.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Do not fit a fresh scale to each request. An ordinary linear model may retain its predictions after rescaling; distance models or penalties can behave differently.

<details markdown="1">
<summary>Check your choice and reason</summary>

Name the input, original unit/range and training rule. The same rule and units must prepare later rows. Changing only the request unit makes the saved model interpret a different quantity.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| age | cholesterol | blood_pressure | exercise_score | sex | chest_pain | example_label |
| --- | --- | --- | --- | --- | --- | --- |
| 29 | 155 | 111 | 80 | F | none | 0 |
| 38 | 166 | 118 | 72 | M | none | 0 |
| 58 | 250 | 147 | 39 | F | reported | 1 |
| 62 | 273 | 157 | 33 | M | reported | 1 |
| 45 | 172 | 123 | 66 | F | none | 0 |
| 67 | 300 | 163 | 29 | M | reported | 1 |
| 41 | 169 | 122 | 70 | M | none | 0 |
| 65 | 277 | 155 | 34 | F | reported | 1 |

## 📩 Supplied new inputs

| age | cholesterol | blood_pressure | exercise_score | sex | chest_pain |
| --- | --- | --- | --- | --- | --- |
| 29 | 155 | 111 | 80 | F | none |
| 65 | 277 | 155 | 34 | F | reported |
| 58 | 250 | 147 | 39 | F | reported |

<!-- teaching-note:start -->
<!-- teaching-profile:dataset_337 -->
<!-- teaching-note:end -->
