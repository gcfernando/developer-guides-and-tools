# Isolation Forest

**Lesson 395 · Practice**

## Your goal

Train on regular parcels and see which new measurements are unusual.

## Before you start

Read a training reference and unusual parcel.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

An anomaly detector flags inputs unlike its reference under a selected rule.

**Why and when.** Prioritize source review using a suitable reference and acceptable alert workload.

**A worked example to follow.** Isolation Forest uses random partitions; One-Class SVM learns a reference boundary. Here −1 flags a new parcel unlike routine training measurements.

**Input and output.** The supplied sample fields are `minutes`, `kg`. In that field order, one original row is:

```text
10.001230153357483 | 4.149372768754235
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Follow the chosen measurements through their preparation and fitted grouping, projection or review rule. Read the resulting representation or flag using the explanation above; do not invent confirmed group answers. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A valid new parcel type repeatedly gets flagged. What comes before deleting it? Write a reason before running or opening the answer.

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

**Common mistakes and limits.** A flag proves neither harm nor recording error. An incomplete or contaminated reference changes what looks unusual.

<details markdown="1">
<summary>Check your choice and reason</summary>

Verify its source and scope, inspect counts and examples, then validate any reference or service-policy change.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

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

<!-- teaching-note:start -->
<!-- teaching-profile:anomaly -->
<!-- teaching-note:end -->
