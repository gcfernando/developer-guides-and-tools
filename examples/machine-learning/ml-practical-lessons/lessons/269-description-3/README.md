# Description

**Lesson 269 · Reference**

## Your goal

Inspect the columns in the invented property listings and see what each row represents.

## Before you start

Read the named fields and explain the preparation taught earlier.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A source note states where a table came from; a description explains what one row and each field mean.

**Why and when.** Use it before treating the house listings as evidence about a real population.

**A worked example to follow.** The house listings exercise uses area, rooms and property categories. Its output is price. These are original invented practice rows, even where the folder preserves an old benchmark name. An explicit no-pool category differs from an unresolved field.

**Input and output.** The supplied sample fields are `area`, `rooms`, `neighborhood`, `street`, `exterior`, `pool`, `garage`, `price`. In that field order, one original row is:

```text
55 | 2 | North | paved | wood | (missing) | none | 165000
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Trace the named source fields into the printed table, file or request result. Check names and counts before interpreting what the program reports. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Write a source note for this house listings exercise: are the rows invented, what does one row represent, and what does the final answer mean? Write a reason before running or opening the answer.

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
PDF reference: Kaggle House Prices Dataset
Origin of this CSV: original synthetic practice rows
Rows: 8
      Column   Type
        area  int64
       rooms  int64
neighborhood object
      street object
    exterior object
        pool object
      garage object
       price  int64
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Add another original example in sample.csv. Rerun to check that its columns and row count make sense.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Do not claim that a historical benchmark was downloaded or that a made-up label was measured. The separate Wine project has its own real source and licence.

<details markdown="1">
<summary>Check your choice and reason</summary>

Say that the rows were created for this workbook, name the row entity and target, and state the limitation. A familiar folder name is not proof of provenance.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| area | rooms | neighborhood | street | exterior | pool | garage | price |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 55 | 2 | North | paved | wood | — | none | 165000 |
| 72 | 3 | South | paved | brick | — | single | 215000 |
| 105 | 4 | North | gravel | wood | — | single | 280000 |
| 200 | 6 | South | paved | brick | good | double | 760000 |
| 85 | 3 | North | paved | wood | — | single | 220000 |
| 95 | 4 | South | gravel | brick | — | double | 270000 |
| 68 | 3 | North | paved | wood | — | none | 187000 |
| 140 | 5 | South | paved | brick | good | double | 395000 |

<!-- teaching-note:start -->
<!-- teaching-profile:dataset_269 -->
<!-- teaching-note:end -->
