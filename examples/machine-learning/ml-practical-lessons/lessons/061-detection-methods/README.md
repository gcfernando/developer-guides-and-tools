# Detection Methods

**Lesson 061 · Practice**

## Your goal

Compare two ways to flag unusual parcel weights and inspect the chart.

## Before you start

Sort weights and read graph axes in kg.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

An outlier is unusual under a stated comparison rule. A flag asks for investigation.

**Why and when.** Use plots and numerical rules to find records that deserve attention before fitting or reporting.

**A worked example to follow.** The 80 kg value lies far from most weights. A z-score compares it with the average and standard deviation. IQR compares it with the middle half. On a box plot, read kg on the value axis; a whisker limit is a review rule, not a physical weight limit.

**Input and output.** The supplied sample fields are `weight_kg`. In that field order, one original row is:

```text
2
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A weighing slip confirms an unusual 80 kg shipment. What should you do before choosing a model that cannot handle it? Write a reason before running or opening the answer.

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
 weight_kg  Z-score  IQR
        80     True True
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Compare 80 kg with 8 kg. Change or add a measured weight in sample.csv, then look for the flag and the boxplot.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Do not delete every flagged value. Large valid deliveries may be exactly the cases a service must support. Small samples and skew affect the rules.

<details markdown="1">
<summary>Check your choice and reason</summary>

Keep the confirmed fact, check whether such shipments are in scope, gather suitable training/check examples, or state a service limit. Do not edit a real value merely to improve a score.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| weight_kg |
| --- |
| 2 |
| 3 |
| 3 |
| 4 |
| 4 |
| 4 |
| 5 |
| 5 |

Showing the first 8 of 12 rows. The CSV has the full sample.

<!-- teaching-note:start -->
<!-- teaching-profile:outlier_detection -->
<!-- teaching-note:end -->
