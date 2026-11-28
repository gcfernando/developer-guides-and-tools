# When missing values change the answer

**Lesson 048 · Core**

## Your goal

See how losing the slower trips can make the average delivery time look too low.

## Before you start

Calculate an average from a list.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A missing-data pattern can change which cases a summary represents.

**Why and when.** Investigate missingness when some routes, people or times are less likely to be recorded.

**A worked example to follow.** All six invented times average 23 minutes. The recorded subset averages 18 because two slow trips are absent. The lower number describes recorded trips, not necessarily all deliveries.

**Input and output.** The supplied sample fields are `Route`, `True time`, `Recorded time`. In that field order, one original row is:

```text
Short | 12 | 12.0
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

If a broken recorder misses long routes, does a complete-looking filled table prove its average is representative? Write a reason before running or opening the answer.

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
       Average uses  Average time (min)
      All six times                23.0
Recorded times only                18.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In sample.csv, change the missing Recorded time for the 32-minute delivery to 32. Compare the recorded-only average with the all-times average.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Filling gaps does not establish fairness or recover unknown outcomes. In real data the missing true times may be unavailable.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Compare missing counts by route and time, inspect the recorder/source, and report what is unknown. A fill alone cannot establish the absent outcomes.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| Route | True time | Recorded time |
| --- | --- | --- |
| Short | 12 | 12.0 |
| Short | 14 | 14.0 |
| Short | 16 | 16.0 |
| Long | 30 | 30.0 |
| Long | 32 | — |
| Long | 34 | — |

<!-- teaching-note:start -->
<!-- teaching-profile:missing_bias -->
<!-- teaching-note:end -->
