# Test set

**Lesson 182 · Practice**

## Your goal

Check the chosen model once using its untouched test rows.

## Before you start

Name inputs and answers; count urgent and regular orders.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Training learns, validation chooses, and test checks the frozen choice. A split defines which new-case question is being tested.

**Why and when.** Set aside suitable check rows before any data-based preparation or model selection.

**A worked example to follow.** The 70/20/10 recipe uses 70 orders for fitting, 20 for choosing tree depth and 10 for testing. Balanced accuracy averages recall within each class: if 8/10 urgent and 18/20 regular are correct, it is (0.8 + 0.9) ÷ 2 = 0.85. This is a reading aid, not the script’s measured result.

**Input and output.** The supplied sample fields are `shipment_id`, `distance_km`, `weight_kg`, `urgent`. In that field order, one original row is:

```text
D001 | 2.78 | 6.47 | False
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A tree catches 4 of 5 urgent orders and correctly leaves 9 of 10 regular orders unflagged. Calculate balanced accuracy. May you choose its depth from final test answers? Write a reason before running or opening the answer.

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
Shared shipment IDs across splits: 0
       Set  Rows  Urgent  Urgent (%)
  Training    70      14        20.0
Validation    20       4        20.0
      Test    10       2        20.0

Validation scores by tree depth
 Depth  Balanced accuracy
     1              0.500
     2              0.500
     3              0.562
Look for Test. Count missed urgent cases after the depth has been chosen.
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Copy one training CSV row below itself. The script should stop before splitting. Delete the copy and rerun.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A percentage ratio does not establish independence. Keep repeated shipment identity together. Stratification preserves class shares; it does not fix time or customer leakage.

<details>
<summary>Check your choice and reason</summary>

The average of 0.8 and 0.9 is 0.85. Choose depth on validation or inside training cross-validation, then use the final test once for the chosen procedure.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:split -->
<!-- teaching-note:end -->
