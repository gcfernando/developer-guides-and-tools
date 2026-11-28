# Normal distribution

**Lesson 144 · Practice**

## Your goal

Map readings to a bell-shaped scale based on their ranks.

## Before you start

Sort numbers and explain rank.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A quantile transformation maps training ranks to a chosen output distribution.

**Why and when.** Use it when a model benefits from the changed spacing and the distortion is acceptable.

**A worked example to follow.** Training readings can be mapped across a uniform scale or a normal-shaped scale. The distances between original readings change; new rows use the saved training mapping.

**Input and output.** The supplied sample fields are `signal`, `cost`. In that field order, one original row is:

```text
1 | 10
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

If two different readings are close in rank but far apart in original units, will rank scaling preserve that large physical gap? Write a reason before running or opening the answer.

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
normal first two training rows: [[-5.2], [-1.11]]
Actual costs: [23, 48]
Predicted costs: [31.7, 38.5]
 signal  predicted_cost
      3           26.38
     15           33.36
     40           36.88
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try a signal reading of 3, 15, or 40 in new_inputs.csv. Compare the predicted cost for each row.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** The method does not recover a true normal-generating process. Ties and values beyond the training range need inspection; an inverse can only reflect the fitted mapping.

<details>
<summary>Check your choice and reason</summary>

Not necessarily. It changes spacing based on ranks. Keep original units available for interpretation and validate whether losing gap information helps the task.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| signal | cost |
| --- | --- |
| 1 | 10 |
| 5 | 18 |
| 12 | 25 |
| 20 | 31 |
| 35 | 41 |
| 80 | 53 |
| 160 | 64 |
| 10 | 23 |

Showing the first 8 of 9 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| signal |
| --- |
| 3 |
| 15 |
| 40 |

<!-- teaching-note:start -->
<!-- teaching-profile:quantile -->
<!-- teaching-note:end -->
