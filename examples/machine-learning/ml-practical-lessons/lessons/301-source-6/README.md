# Source

**Lesson 301 · Reference**

## Your goal

Read the dataset name from the PDF and inspect the invented wine measurements used in this exercise.

## Before you start

Read the named fields and explain the preparation taught earlier.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A source note states where a table came from; a description explains what one row and each field mean.

**Why and when.** Use it before treating the drink measurements as evidence about a real population.

**A worked example to follow.** The drink measurements exercise uses alcohol, citric acid and sulphates. Its output is quality. These are original invented practice rows, even where the folder preserves an old benchmark name. The exercise explores both a number and a separately defined higher/lower category.

**Input and output.** The supplied sample fields are `alcohol`, `citric_acid`, `sulphates`, `quality`. In that field order, one original row is:

```text
8 | .2 | .3 | 4
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Trace the named source fields into the printed table, file or request result. Check names and counts before interpreting what the program reports. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Write a source note for this drink measurements exercise: are the rows invented, what does one row represent, and what does the final answer mean? Write a reason before running or opening the answer.

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
PDF reference: UCI Wine Quality Dataset
Origin of this CSV: original synthetic practice rows
Rows: 8
     Column    Type
    alcohol float64
citric_acid float64
  sulphates float64
    quality   int64
 alcohol  citric_acid  sulphates  quality
     8.0          0.2        0.3        4
     9.0          0.2        0.4        5
    10.0          0.3        NaN        5
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Add another original example in sample.csv. Rerun to check that its columns and row count make sense.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Do not claim that a historical benchmark was downloaded or that a made-up label was measured. The separate Wine project has its own real source and licence.

<details>
<summary>Check your choice and reason</summary>

Say that the rows were created for this workbook, name the row entity and target, and state the limitation. A familiar folder name is not proof of provenance.

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

<!-- teaching-note:start -->
<!-- teaching-profile:dataset_301 -->
<!-- teaching-note:end -->
