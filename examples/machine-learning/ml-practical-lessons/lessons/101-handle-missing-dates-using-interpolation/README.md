# Handle missing dates using interpolation

**Lesson 101 · Practice**

## Your goal

Estimate a missing time-series reading from the readings on either side.

## Before you start

Sort dates and check one reading per date.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Interpolation estimates a gap between known readings on a stated calendar.

**Why and when.** Use it for a retrospective series when the neighboring readings and a smooth-change assumption make sense.

**A worked example to follow.** February 1 has 10 orders and February 3 has 16. A straight time interpolation gives February 2 a value of 13. Changing February 3 to 18 makes the midpoint 14.

**Input and output.** The supplied sample fields are `day`, `orders`. In that field order, one original row is:

```text
2025-02-01 | 10
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

May a real-time February 2 forecast report the interpolated 13 as though it used only available information? Write a reason before running or opening the answer.

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
            observed  interpolated
day
2025-02-01      10.0          10.0
2025-02-02       NaN          13.0
2025-02-03      16.0          16.0
2025-02-04      19.0          19.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In sample.csv, change orders for 2025-02-03 from 16 to 18. The February 2 estimate should become 14. Keep each date unique.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** This estimates the missing measurement, not the missing date. It uses the later reading; a live February 2 prediction could not use February 3.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. That would use a future observation. For live forecasting restrict information to what had arrived; keep retrospective repair clearly labelled.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| day | orders |
| --- | --- |
| 2025-02-01 | 10 |
| 2025-02-03 | 16 |
| 2025-02-04 | 19 |

<!-- teaching-note:start -->
<!-- teaching-profile:interpolation -->
<!-- teaching-note:end -->
