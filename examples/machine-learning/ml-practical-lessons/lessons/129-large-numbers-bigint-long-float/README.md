# Large Numbers (BigInt, Long Float)

**Lesson 129 · Practice**

## Your goal

Read large values and display them in a shorter format.

## Before you start

Read the Files and data terms in the glossary.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

Choose a representation based on meaning. A number, name, yes/no value and date need different checks before a model can use them.

## Guess first

Is every field made of digits a measured number? Write your answer before running the script.

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

<details>
<summary>Read the answer after trying</summary>

No. An event ID may be a name and should stay exact text.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| event_id | visits | server_cost |
| --- | --- | --- |
| 123456789012345 | 100 | 8 |
| 123456789012346 | 10000 | 15 |
| 123456789012347 | 1000000 | 19 |
| 123456789012348 | 12500000000 | 30 |
