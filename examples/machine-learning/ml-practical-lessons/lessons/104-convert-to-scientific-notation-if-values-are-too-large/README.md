# Convert to scientific notation (if values are too large)

**Lesson 104 · Practice**

## Your goal

Display large numbers in compact scientific notation and read the original value alongside them.

## Before you start

Read large numbers and know which fields are IDs.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

Scientific notation only changes how a number is displayed. A log changes the numeric input. An ID is a name, even when it contains digits.

## Guess first

Does writing 1000 as 1e3 make its value smaller? Write your answer before running the script.

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

Change visits in sample.csv from 100 to 1000. Compare its written scientific notation and log value. Keep event_id as exact text; do not use it as a measurement.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. The value stays 1000. A log is a different operation.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| event_id | visits | server_cost |
| --- | --- | --- |
| 123456789012345 | 100 | 8 |
| 123456789012346 | 10000 | 15 |
| 123456789012347 | 1000000 | 19 |
| 123456789012348 | 12500000000 | 30 |
