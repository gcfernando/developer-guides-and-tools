# ROC Curve

**Lesson 206 · Practice**

## Your goal

Compare catches and false alarms at two fixed practice cutoffs.

## Before you start

Explain a false alarm, urgent recall and a score cutoff.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

ROC plots the share of urgent cases caught against the share of regular cases falsely alerted across cutoffs. AUC summarizes ranking.

**Why and when.** Use it for ranking comparisons; inspect precision-recall and counts when the positive event is rare.

**A worked example to follow.** Lowering a cutoff may catch more urgent orders and create more false alarms. The lesson’s two cutoff points are reading practice on fixed check rows, not an invitation to optimize an app on its final test.

**Input and output.** The supplied sample fields are `distance`, `weight`, `answer`. In that field order, one original row is:

```text
37 | 5 | 1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Can changing a cutoff improve ranking AUC without changing the model’s scores? Write a reason before running or opening the answer.

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
 Cutoff  Urgent caught  Urgent missed  False alarms  Urgent recall  False alarm rate
   0.25             18              0             2          1.000             0.167
   0.75             17              1             1          0.944             0.083
AUC-ROC: 0.991
Here the test cutoffs are fixed for teaching. Choose an app cutoff on validation data.
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Replace 0.75 with 0.5. Compare detections and false alarms with the first row. These are practice cutoffs on the test set.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** AUC is not probability calibration or a chosen operating cutoff. A good ranking can still yield an unusable number of alerts.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. It changes the decisions at one operating point; ranking scores stay the same. Choose that decision rule using validation and practical constraints.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

### What this particular check asks

This example keeps exact distance-and-weight combinations out of its test training rows. That is a deliberately stricter, special question. Independent orders may have the same measurements. Equal numbers alone do not prove leakage. Use shipment identity and the intended future job to choose a normal split; see lesson 442.



<!-- teaching-note:start -->
<!-- teaching-profile:roc -->
<!-- teaching-note:end -->
