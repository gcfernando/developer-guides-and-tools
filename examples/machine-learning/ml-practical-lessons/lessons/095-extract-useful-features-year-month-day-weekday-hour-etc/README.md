# Extract useful features (Year, Month, Day, Weekday, Hour, etc.)

**Lesson 095 · Practice**

## Your goal

Turn one timestamp into model inputs such as weekday and hour.

## Before you start

Read a calendar date and a clock time.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Parsing turns a written time into a date value; feature extraction selects parts such as year, weekday or hour.

**Why and when.** Use a part only if it is known when predicting and relevant to the job. Record the date convention and timezone.

**A worked example to follow.** 2025-02-03 08:00 has year 2025, month 2, day 3, weekday 0 (Monday in pandas) and hour 8. The lesson fits the named date parts and reuses the same parser on later inputs.

**Input and output.** The supplied sample fields are `timestamp`, `orders`. In that field order, one original row is:

```text
2025-02-03 08:00 | 10
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Two systems write 02/03/2025. What must be known before combining them? Can using a later correction time leak information? Write a reason before running or opening the answer.

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
 Year  Month  Day  Weekday  Hour
 2025      2    3        0     8
 2025      2    3        0    10
 2025      2    4        1     8
 2025      2    4        1    10
       timestamp  Weekday  Hour  estimated_orders
2025-02-05 09:00        2     9              18.0
2025-03-08 17:30        5    17              43.0
2026-01-12 08:30        0     8              10.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try 2025-02-05 09:00 and 2026-01-12 08:30 in new_inputs.csv. Keep the YYYY-MM-DD HH:MM format.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Written hour numbers are not distances around a clock: 23:00 and 00:00 are one hour apart. A Unix timestamp needs a stated unit and time convention. Do not guess ambiguous formats.

<details>
<summary>Check your choice and reason</summary>

Confirm month/day versus day/month and the timezone. A later correction time may be unavailable at prediction time; use only fields actually known then.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| timestamp | orders |
| --- | --- |
| 2025-02-03 08:00 | 10 |
| 2025-02-03 10:00 | 14 |
| 2025-02-04 08:00 | 13 |
| 2025-02-04 10:00 | 17 |

## 📩 Supplied new inputs

| timestamp |
| --- |
| 2025-02-05 09:00 |
| 2025-03-08 17:30 |
| 2026-01-12 08:30 |

<!-- teaching-note:start -->
<!-- teaching-profile:dates -->
<!-- teaching-note:end -->
