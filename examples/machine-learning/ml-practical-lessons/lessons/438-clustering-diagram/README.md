# Clustering (diagram)

**Lesson 438 · Reference**

## Your goal

Follow the clustering branch and group shoppers without known labels.

## Before you start

Compare scaled measurements and group means.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Clustering groups inputs without supplied group labels. K-Means chooses K centres and assigns cases by its distance rule.

**Why and when.** Explore whether profiles help a decision; compare sensible K values and data without clear groups.

**A worked example to follow.** Scale age, income and spending, then read each of the three groups in original units. A new shopper uses the saved scale and centres.

**Input and output.** The supplied sample fields are `age`, `income`, `spending`. In that field order, one original row is:

```text
21 | 25 | 71
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Follow the chosen measurements through their preparation and fitted grouping, projection or review rule. Read the resulting representation or flag using the explanation above; do not invent confirmed group answers. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Old group 0 resembles new group 2 after refitting. Must the shoppers have changed? Write a reason before running or opening the answer.

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
Labels: [0, 0, 0, 2, 2, 2, 1, 1, 1]
        age  income  spending
group
0      23.3    28.0      70.7
1      61.7    92.3      79.7
2      43.7    58.7      43.0
[21 25 71] -> 0
[64 95 82] -> 1
[26 31 68] -> 0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change a measurement in new_inputs.csv. The fitted scaler and algorithm process each row.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** IDs are arbitrary names. K-Means favours certain shapes and can impose groups where none are useful.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Compare profiles, membership and stability rather than numeric IDs.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| age | income | spending |
| --- | --- | --- |
| 21 | 25 | 71 |
| 23 | 28 | 73 |
| 26 | 31 | 68 |
| 42 | 55 | 41 |
| 43 | 59 | 45 |
| 46 | 62 | 43 |
| 59 | 89 | 77 |
| 62 | 93 | 80 |

Showing the first 8 of 9 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| age | income | spending |
| --- | --- | --- |
| 21 | 25 | 71 |
| 64 | 95 | 82 |
| 26 | 31 | 68 |

<!-- teaching-note:start -->
<!-- teaching-profile:kmeans -->
<!-- teaching-note:end -->
