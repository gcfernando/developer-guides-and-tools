# Fix typos and spelling variations

**Lesson 059 · Practice**

## Your goal

Map known spelling variants to a single category before encoding it.

## Before you start

Explain the difference between text spelling and field meaning.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A spelling map explicitly lists variants known to mean the same category.

**Why and when.** Use a reviewed map when a source confirms the aliases. Keep an audit of the original value.

**A worked example to follow.** The exercise maps M and male to Male only because its small vocabulary defines that meaning. It then encodes the standardized category.

**Input and output.** The supplied sample fields are `record_id`, `category`. In that field order, one original row is:

```text
1 | Male
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

The file contains an unfamiliar value X. Should you add X → Male to make the script pass? Write a reason before running or opening the answer.

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
category standard
    Male     Male
       M     Male
  Female   Female
  female   Female
Held-out encoded row: [[1.0, 0.0]]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In sample.csv, replace M with male. Rerun and check that the standard value remains Male. Then try an unknown spelling and read the error before restoring the file.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Do not infer sensitive identity or a category from an unfamiliar abbreviation. An unrecognized spelling should raise a review question.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Ask what X means or leave it unresolved. A successful script is not evidence that a guessed mapping is correct.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| record_id | category |
| --- | --- |
| 1 | Male |
| 2 | M |
| 3 | Female |
| 4 | female |

<!-- teaching-note:start -->
<!-- teaching-profile:spellings -->
<!-- teaching-note:end -->
