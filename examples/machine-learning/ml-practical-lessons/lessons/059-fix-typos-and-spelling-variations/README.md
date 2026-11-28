# Fix typos and spelling variations

**Lesson 059 · Practice**

## Your goal

Map known spelling variants to a single category before encoding it.

## Before you start

Read dates, units and names. Know the difference between a number and text.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

Use one clear format for the same meaning. Ten pounds is about 4.54 kilograms. A spelling change is safe only when the source confirms the same meaning.

## Guess first

Should 10 lb be passed to a kg field as the number 10? Write your answer before running the script.

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
category standard
    Male     Male
       M     Male
  Female   Female
  female   Female
Held-out encoded row: [[1.0, 0.0]]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In sample.csv, replace M with male. Rerun and check that the standard value remains Male. Then try an unknown spelling and read the error before restoring the file.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Convert it to about 4.54 kg first.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| record_id | category |
| --- | --- |
| 1 | Male |
| 2 | M |
| 3 | Female |
| 4 | female |
