# Category encoding

**Lesson 299 · Practice**

## Your goal

Turn categories in the invented wine measurements into numbers the model can read.

## Before you start

Read the named fields and explain the preparation taught earlier.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Encoding gives a name a consistent numeric representation while preserving whether it is an input category or an answer label.

**Why and when.** Use it before the numeric estimator receives the drink measurements fields.

**A worked example to follow.** The drink measurements exercise uses alcohol, citric acid and sulphates. Its output is quality. Read the script’s selected category fields or target encoder. A class ID names a class; it does not turn that class into a measured amount. The exercise explores both a number and a separately defined higher/lower category.

**Input and output.** The supplied sample fields are `alcohol`, `citric_acid`, `sulphates`, `quality`. In that field order, one original row is:

```text
8 | .2 | .3 | 4
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Find one category or target label in this drink measurements exercise. Is it a model input or the answer? What happens if a new name arrives? Write a reason before running or opening the answer.

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
Missing cells before filling or removing rows: {'alcohol': 0, 'citric_acid': 0, 'sulphates': 1, 'quality': 0}
      Field  Rows to review
    alcohol               1
citric_acid               0
  sulphates               0
Flagged original rows: [6]
 Original row  Actual answer  Prediction
            7              5         5.2
            8              7         7.1
Class predictions: ['lower', 'higher']
 alcohol  citric_acid  sulphates  prediction
     8.0          0.2        0.3    4.279202
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change an input in new_inputs.csv. Compare the predictions with the held-out check above.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Do not invent a category ranking or fit a separate column list on new rows. One-hot target labels in a drawing demonstration are separate from input encoding.

<details>
<summary>Check your choice and reason</summary>

Trace the named field into features or target. Inputs use the saved category schema; unknown names need a stated policy. Targets remain the known classes the classifier was trained to distinguish.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| alcohol | citric_acid | sulphates | quality |
| --- | --- | --- | --- |
| 8 | .2 | .3 | 4 |
| 9 | .2 | .4 | 5 |
| 10 | .3 | — | 5 |
| 11 | .3 | .6 | 6 |
| 12 | .4 | .7 | 7 |
| 16 | .3 | 1.1 | 8 |
| 9.5 | .2 | .4 | 5 |
| 12.1 | .4 | .7 | 7 |

## 📩 Supplied new inputs

| alcohol | citric_acid | sulphates |
| --- | --- | --- |
| 8.0 | 0.2 | 0.3 |
| 12.1 | 0.4 | 0.7 |
| 10.0 | 0.3 | — |

<!-- teaching-note:start -->
<!-- teaching-profile:dataset_299 -->
<!-- teaching-note:end -->
