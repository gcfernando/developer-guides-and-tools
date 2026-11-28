# Check whether predicted probabilities are reliable

**Lesson 445 · Practice**

## Your goal

Train a calibration model using validation rows and compare probability quality on a separate test set.

## Before you start

Read probabilities and group outcome fractions.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Calibration asks whether similar predicted chances correspond to similar observed event rates.

**Why and when.** Check it when probability values inform decisions, alongside ranking and counts.

**A worked example to follow.** Train the base forest, fit a sigmoid adjustment on separate validation rows, then compare test probabilities. Brier score averages squared probability errors; it reflects more than calibration alone.

**Input and output.** The supplied sample fields are `order_id`, `distance_km`, `weight_kg`, `rush_hour`, `vehicle_load`, `urgent`, `split`. In that field order, one original row is:

```text
R00000 | 76.01 | 14.8 | 0 | 10 | 1 | train
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Does a 0.7 average predicted chance guarantee seven successes in the next ten cases? Write a reason before running or opening the answer.

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
Raw forest test Brier score: 0.1081
Adjusted forest test Brier score: 0.1083
Lower Brier score is better on this probability check. Changing bins changes the visual, not the score.
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change bins from 5 to 10. Compare the chart’s grouping. The Brier scores should stay the same.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** More chart bins change grouping, not the underlying Brier score. Small bins are uncertain and adjustment need not improve a particular test.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Assess rates across suitable groups with counts and uncertainty, not promises for one small batch.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:calibration -->
<!-- teaching-note:end -->
