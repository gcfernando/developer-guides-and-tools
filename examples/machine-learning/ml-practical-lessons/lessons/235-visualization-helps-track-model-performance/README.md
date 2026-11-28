# Visualization helps track model performance!

**Lesson 235 · Practice**

## Your goal

Plot how accuracy and input distances change between batches.

## Before you start

Read an error or category score and distinguish prediction from later outcome.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Monitoring watches inputs and measured results over time. Drift means a change worth investigating.

**Why and when.** Use it after a model starts receiving new cases, with a named owner and action for each alert.

**A worked example to follow.** Later trips may be longer than historical trips. Compare their input distributions, then calculate accuracy or error only after outcomes arrive. A candidate retrained on recent labeled rows needs a separate later comparison with the current model.

**Input and output.** The supplied sample fields are `batch`, `km`, `late`. In that field order, one original row is:

```text
historical | 19 | True
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

West-zone error rises. Name three checks before replacing the model. Write a reason before running or opening the answer.

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
Recent accuracy: 0.53 median km change: 7.0
ALERT: investigate before promoting a candidate.
Later batch, live / candidate: 0.5 1.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing km from 19 to 14 in sample.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Input change alone does not prove worse predictions. An alert does not automatically authorize retraining or replacement. Delayed labels limit what is currently measurable.

<details>
<summary>Check your choice and reason</summary>

Verify units/schema and labels, inspect affected cases and counts, and check changes in routes or population. Use the agreed fallback if needed; compare any candidate fairly before promotion.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| batch | km | late |
| --- | --- | --- |
| historical | 19 | True |
| historical | 13 | True |
| historical | 14 | True |
| historical | 18 | True |
| historical | 12 | True |
| historical | 16 | True |
| historical | 17 | True |
| historical | 5 | False |

Showing the first 8 of 160 rows. The CSV has the full sample.

<!-- teaching-note:start -->
<!-- teaching-profile:monitoring -->
<!-- teaching-note:end -->
