# Convert date formats (MM/DD/YYYY to YYYY-MM-DD)

**Lesson 056 · Practice**

## Your goal

Read US-style and ISO dates and convert both to YYYY-MM-DD.

## Before you start

Read a date format and distinguish pounds from kilograms.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Standardizing formats gives the same meaning one consistent representation.

**Why and when.** Do this before combining systems whose dates, units or category spellings differ.

**A worked example to follow.** The lesson knows that 01/02/2025 uses month/day/year, so it becomes 2025-01-02. A 10 lb measurement becomes about 4.54 kg. Trimming NORTH gives north; its meaning stays the same.

**Input and output.** The supplied sample fields are `ship_date`, `weight`, `unit`, `zone`, `minutes`. In that field order, one original row is:

```text
01/02/2025 | 10 | lb | NORTH  | 19
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A new source says 02/03/2025 but gives no date convention. May you assume the same format? What is 22 lb in kg? Write a reason before running or opening the answer.

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
Original date Standard date Original weight  Weight (kg) Original zone Standard zone  South flag
   01/02/2025    2025-01-02           10 lb         4.54         NORTH         north           0
   2025-01-03    2025-01-03            8 kg         8.00         south         south           1
   01/04/2025    2025-01-04          35 lbs        15.88         NORTH         north           0
   2025-01-05    2025-01-05           16 kg        16.00         south         south           1
   2025-01-06    2025-01-06           12 kg        12.00         north         north           0
   Shipment  Actual time (min)  Predicted time (min)
Check row 5                 35                  34.5
      date  weight_kg  zone  weekday  is_south  predicted_minutes
2025-01-07   8.164663 north        1         0              26.89
2025-01-09   7.000000 south        3         1              25.89
2025-01-10  13.607771 north        4         0              34.61
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing ship_date from 01/07/2025 to 2025-01-10 in new_inputs.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Do not guess an ambiguous date format. A unit conversion is a fixed known rule, unlike a training median learned from data. Check unsupported names rather than silently treating them as a known zone.

<details>
<summary>Check your choice and reason</summary>

Ask the source about its date convention. The fixed conversion gives about 9.98 kg. Apply the same confirmed conversion rules to training and later requests.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| ship_date | weight | unit | zone | minutes |
| --- | --- | --- | --- | --- |
| 01/02/2025 | 10 | lb | NORTH | 19 |
| 2025-01-03 | 8 | kg | south | 27 |
| 01/04/2025 | 35 | lbs | NORTH | 38 |
| 2025-01-05 | 16 | kg | south | 40 |
| 2025-01-06 | 12 | kg | north | 35 |

## 📩 Supplied new inputs

| ship_date | weight | unit | zone |
| --- | --- | --- | --- |
| 01/07/2025 | 18 | lb | NORTH |
| 2025-01-09 | 7 | kg | south |
| 2025-01-10 | 30 | lbs | north |

<!-- teaching-note:start -->
<!-- teaching-profile:standard_formats -->
<!-- teaching-note:end -->
