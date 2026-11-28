# 80%-20% (Train-Test)

**Lesson 184 · Practice**

## Your goal

Train with 80% of the rows and check the model with the remaining 20%.

## Before you start

Understand the three row roles from Start here.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

Training teaches. Validation chooses. Test checks the final choice. Match the split to future use. Equal input numbers do not alone prove copied observations.

## Guess first

May you choose tree depth using the final test answers? Write your answer before running the script.

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
Training    80      16        20.0
    Test    20       4        20.0
Look for 80 training orders and 20 test orders. The tree depth is fixed before testing.
Chosen depth: 2
Test: 4 urgent caught, 0 urgent missed, 1 false alarms, 15 regular correct.
The test contains only 4 urgent orders. A single missed order changes recall a lot.
 distance_km  weight_kg  predicted_urgent
           5          2             False
          39          4             False
          47          3             False
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Copy one training CSV row below itself. The script should stop before splitting. Delete the copy and rerun.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Use validation. Keep the final test for the frozen choice.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.
