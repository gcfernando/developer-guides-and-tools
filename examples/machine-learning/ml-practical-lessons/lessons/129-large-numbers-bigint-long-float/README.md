# Large Numbers (BigInt, Long Float)

**Lesson 129 · Practice**

## Your goal

Read large values and display them in a shorter format.

## Before you start

Distinguish an identifier from a measured count.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Scientific notation writes the same value compactly. An ID remains a name even when all its characters are digits.

**Why and when.** Use compact notation to display large measurements, and exact strings to preserve long IDs.

**A worked example to follow.** 1000 and 1e3 mean the same number. The script preserves event_id as text and separately passes log-transformed visits to the cost model.

**Input and output.** The supplied sample fields are `event_id`, `visits`, `server_cost`. In that field order, one original row is:

```text
123456789012345 | 100 | 8
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A table has an account ID 000123 and a count of 1000000. Which may be formatted as 1e6 and which should preserve characters? Write a reason before running or opening the answer.

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
First ID: 123456789012345
Traffic display: ['1.000e+02', '1.000e+04', '1.000e+06', '1.250e+10']
Numeric log features: [4.62, 9.21, 13.82, 23.25]
Held-out cost estimate: [30.8]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing event_id from 123456789012345 to 123456789012347 in sample.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Rounding an ID or treating its magnitude as a useful measurement can destroy identity or invent a relationship.

<details>
<summary>Check your choice and reason</summary>

The count may be displayed as 1e6. Preserve 000123 exactly as text; its leading zeros can be part of its identity.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| event_id | visits | server_cost |
| --- | --- | --- |
| 123456789012345 | 100 | 8 |
| 123456789012346 | 10000 | 15 |
| 123456789012347 | 1000000 | 19 |
| 123456789012348 | 12500000000 | 30 |

<!-- teaching-note:start -->
<!-- teaching-profile:scientific_notation -->
<!-- teaching-note:end -->
