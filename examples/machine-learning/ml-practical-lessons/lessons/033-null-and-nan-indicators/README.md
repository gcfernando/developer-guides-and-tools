# Null and NaN indicators

**Lesson 033 · Practice**

## Your goal

Use pandas to count blank cells and question marks as missing.

## Before you start

Explain why a blank weight differs from a weight of zero.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A missing value means a fact was not recorded. NaN is one marker Python uses for a missing number.

**Why and when.** Count missing cells and inspect their rows before deciding whether to recover, fill or remove them.

**A worked example to follow.** In sample.csv one weight is blank and two zones are missing after treating ? as a missing marker. A row can have a measured time even when one input is missing.

**Input and output.** The supplied sample fields are `distance_km`, `weight_kg`, `zone`, `delivery_minutes`. In that field order, one original row is:

```text
2 | 1 | north | 19
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Turn the blank weight into a source-confirmed 2 kg. Predict the weight missing-count change. Would writing a guess of 2 recover the fact? Write a reason before running or opening the answer.

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
          Column  Missing cells
     distance_km              0
       weight_kg              1
            zone              2
delivery_minutes              0

Rows to review
 distance_km  weight_kg  zone
           4        NaN north
           6        2.0   NaN
          10        1.0   NaN
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Enter a blank cell and a question mark in sample.csv. Check that both appear in the missing count.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Zero is a known quantity. Replacing every blank with zero can invent measurements. A question mark becomes missing only because the reader was told to interpret it that way.

<details>
<summary>Check your choice and reason</summary>

The count falls by one. A confirmed measurement recovers the fact; an invented fill does not. Keep that distinction in the project notes.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| distance_km | weight_kg | zone | delivery_minutes |
| --- | --- | --- | --- |
| 2 | 1 | north | 19 |
| 4 | — | north | 30 |
| 6 | 2 | — | 29 |
| 8 | 4 | south | 40 |
| 10 | 1 | ? | 33 |
| 12 | 3 | south | 44 |

<!-- teaching-note:start -->
<!-- teaching-profile:missing_detection -->
<!-- teaching-note:end -->
