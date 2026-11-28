# Flatten JSON

**Lesson 110 · Practice**

## Your goal

Flatten nested parcel details into named table columns.

## Before you start

Read a simple row, a named field and a missing value.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

A nested record holds facts inside other facts. Flattening puts selected facts into columns. A local address lookup has only the addresses in its own list.

## Guess first

What should happen to an address absent from that list? Write your answer before running the script.

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

<details>
<summary>Read the answer after trying</summary>

Flag it for a source lookup. Do not invent coordinates.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| address | weight_kg | minutes |
| --- | --- | --- |
| Depot North | 1 | 10 |
| Depot South | 3 | 16 |
| Depot North | — | 12 |
| Unknown | 2 | 15 |
