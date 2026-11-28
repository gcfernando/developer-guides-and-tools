# Anomaly Detection

**Lesson 394 · Practice**

## Your goal

Compare a typical parcel with one that needs a closer look.

## Before you start

Understand an unusual value and a source check.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

An anomaly detector flags a row unlike the usual training rows. A flag does not prove an error or harm. Investigate the source before removing it.

## Guess first

Should every flagged parcel be deleted? Write your answer before running the script.

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
Example training shipments: [[10.0, 4.15], [9.73, 3.55], [9.55, 3.5]]
Typical / unusually large: [1, -1, -1]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit the rows in new_inputs.csv. Compare a typical case with an unusually heavy parcel. A flag means check the original record.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. A valid unusual parcel may be important.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| minutes | kg |
| --- | --- |
| 10.001230153357483 | 4.149372768754235 |
| 9.725862144637782 | 3.554704080621363 |
| 9.545329214828277 | 3.504176722501769 |
| 10.060143602597439 | 4.670107622777267 |
| 9.50779348144867 | 3.68976255009003 |
| 10.489842050185198 | 4.178443504080031 |
| 10.1054142489979 | 3.5347659776458977 |
| 9.970748177536727 | 4.347651597229144 |

Showing the first 8 of 45 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| minutes | kg |
| --- | --- |
| 10 | 4 |
| 50 | 34 |
| 12 | 6 |
