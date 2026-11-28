# Visualization Techniques

**Lesson 240 · Practice**

## Your goal

Use a local dashboard to read the latest accuracy and see an alert.

## Before you start

Divide correct predictions by checked predictions.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A dashboard presents recorded monitoring results; refreshing a view does not retrain a model.

**Why and when.** Use a dashboard to help an owner notice a change and decide what to inspect.

**A worked example to follow.** Sixteen correct out of twenty is 80%, below the example’s 85% alert line. Eighteen out of twenty is 90%. The local display reloads monitoring data; Tableau and Power BI require the documented import/refresh steps.

**Input and output.** The supplied sample fields are `Batch`, `Correct`, `Checked`. In that field order, one original row is:

```text
Morning | 18 | 20
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Trace the named source fields into the printed table, file or request result. Check names and counts before interpreting what the program reports. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

The display refreshes every five seconds but outcomes arrive tomorrow. Can today’s newest accuracy be measured every five seconds? Write a reason before running or opening the answer.

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
        Dashboard field Value
Latest labeled accuracy   80%
        Alert threshold   85%
          Alert visible  True
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In the Afternoon row, change Correct from 16 to 18. You should see 90% and Alert visible: False.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Show counts, units, period and refresh time. A green display or a small batch is not proof of reliability; do not calculate new accuracy without outcomes.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Only the view refreshes. Clearly mark which batches have confirmed outcomes and the age of the latest measured result.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| Batch | Correct | Checked |
| --- | --- | --- |
| Morning | 18 | 20 |
| Midday | 14 | 20 |
| Afternoon | 16 | 20 |

## Open the dashboard

1. Run `python lesson.py` to build the dashboard and its monitoring CSV.
2. Run `python -m streamlit run monitoring_dashboard.py` in the same folder. Open the local address printed in the terminal.
3. Change `sample.csv` and rerun `python lesson.py` from a second terminal in the same folder. The open dashboard reads the new accuracy.

<!-- teaching-note:start -->
<!-- teaching-profile:dashboard -->
<!-- teaching-note:end -->
