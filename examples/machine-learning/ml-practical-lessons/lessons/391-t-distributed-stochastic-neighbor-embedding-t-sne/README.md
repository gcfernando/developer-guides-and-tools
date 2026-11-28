# t-Distributed Stochastic Neighbor Embedding (t-SNE)

**Lesson 391 · Practice**

## Your goal

Draw similar rows near one another in a two-dimensional plot.

## Before you start

Compare nearby rows and read a two-axis plot.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

t-SNE draws a low-dimensional view emphasizing local neighbors.

**Why and when.** Inspect local structure in the displayed sample and compare settings.

**A worked example to follow.** The lesson projects scaled long, wide and score into two display coordinates. The axes have no original physical unit.

**Input and output.** The supplied sample fields are `long`, `wide`, `score`, `group`. In that field order, one original row is:

```text
2 | 1 | 3 | 0
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Follow the chosen measurements through their preparation and fitted grouping, projection or review rule. Read the resulting representation or flag using the explanation above; do not invent confirmed group answers. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Are far-apart islands a reliable distance in the original units? Write a reason before running or opening the answer.

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
Output shape: (8, 2)
First two rows: [[-0.47999998927116394, 21.760000228881836], [-2.5999999046325684, 13.529999732971191]]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Add or edit a row in sample.csv, then rerun to refit. This method works on the whole group of rows.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Distant gaps, group sizes and orientations can mislead. This example refits the sample rather than transforming separate new rows.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Inspect original measurements and neighbors before interpreting the gap.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| long | wide | score | group |
| --- | --- | --- | --- |
| 2 | 1 | 3 | 0 |
| 3 | 2 | 4 | 0 |
| 4 | 1 | 2 | 0 |
| 5 | 6 | 7 | 1 |
| 6 | 7 | 8 | 1 |
| 7 | 6 | 9 | 1 |
| 8 | 8 | 7 | 1 |
| 10 | 9 | 10 | 1 |

When you edit the CSV, this lesson recomputes the result for the whole table. It does not project a separate new row with an existing fitted estimator.

<!-- teaching-note:start -->
<!-- teaching-profile:tsne -->
<!-- teaching-note:end -->
