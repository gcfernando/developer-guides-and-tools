# Age from Date of Birth

**Lesson 164 · Practice**

## Your goal

Calculate age at a reference date before using it in a prediction.

## Before you start

Read dates and messages; know when the prediction happens.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Feature engineering derives a useful input from recorded information.

**Why and when.** Create a feature when its meaning is justified and its source is available at prediction time.

**A worked example to follow.** Age is computed at the stated reference date with a birthday check. A separate flag marks the complete word urgent in a message. The same function prepares old and new rows.

**Input and output.** The supplied sample fields are `birth`, `message`, `review`. In that field order, one original row is:

```text
1990-11-16 | please help urgently | 1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

On a date before someone’s birthday, should subtracting birth year alone give their age? Does not urgent mean the same thing as urgent? Write a reason before running or opening the answer.

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

**Common mistakes and limits.** A keyword can miss negation or other languages. Age depends on the reference date; using a future reference or later field can introduce unavailable information.

<details markdown="1">
<summary>Check your choice and reason</summary>

Subtract one when the birthday is still ahead. The keyword flag alone does not distinguish not urgent, so inspect and validate that failure rather than treating the flag as meaning.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

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

<!-- teaching-note:start -->
<!-- teaching-profile:feature_creation -->
<!-- teaching-note:end -->
