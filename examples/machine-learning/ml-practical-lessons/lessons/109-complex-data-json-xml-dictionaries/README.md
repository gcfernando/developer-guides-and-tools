# Complex Data (JSON, XML, Dictionaries)

**Lesson 109 · Practice**

## Your goal

Read the same delivery fields from a nested dictionary, JSON, and XML.

## Before you start

Find a field name and value in a row.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A nested record holds values inside named groups. Flattening selects those values into columns.

**Why and when.** Use it when JSON, XML or dictionaries must supply a fixed model input table.

**A worked example to follow.** A parcel object with kg inside it becomes parcel.kg after flattening. A missing kg key must remain missing rather than being assumed zero. XML field extraction similarly reads an explicitly named field.

**Input and output.** The supplied sample fields are `address`, `weight_kg`, `minutes`. In that field order, one original row is:

```text
Depot North | 1 | 10
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

One parcel has no kg key and another has kg equal to zero. Should flattening make those records identical? Write a reason before running or opening the answer.

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
    address  minutes  parcel.kg  latitude  longitude
Depot North       10        1.0     59.35      18.05
Depot South       16        3.0     59.28      18.02
Depot North       12        NaN     59.35      18.05
    Unknown       15        2.0       NaN        NaN
XML weight: 2.0
Held-out estimate: [12.0]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change address in sample.csv, for example from Depot North to Depot South. Compare the printed rows.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A flattened table can still contain absent fields, repeated records or mixed units. Do not pass IDs, nested text or unavailable answers to a model by accident.

<details>
<summary>Check your choice and reason</summary>

No. One weight is unknown and the other is a recorded zero requiring a domain check. Preserve missingness and validate the expected schema and units.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| address | weight_kg | minutes |
| --- | --- | --- |
| Depot North | 1 | 10 |
| Depot South | 3 | 16 |
| Depot North | — | 12 |
| Unknown | 2 | 15 |

<!-- teaching-note:start -->
<!-- teaching-profile:nested -->
<!-- teaching-note:end -->
