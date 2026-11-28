# Spot overfitting with a validation curve

**Lesson 443 · Core**

## Your goal

Vary model complexity, read the training and validation errors, and test the selected setting once.

## Before you start

Read training and validation errors in the same units.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Overfitting helps the training fit while harming performance on separate relevant cases.

**Why and when.** Use validation to select complexity before a final test.

**A worked example to follow.** Depth varies while training and validation errors are printed together. A deep tree can nearly memorize training while losing to a shallower tree on validation.

**Input and output.** The supplied sample fields are `distance_km`, `actual_minutes`, `split`. In that field order, one original row is:

```text
6.97 | 26.5 | train
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Depth 25 wins training; depth 3 wins validation. Which proceeds to final assessment? Write a reason before running or opening the answer.

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
 Depth  Training MAE  Validation MAE
     1          5.44            4.79
     2          3.68            3.24
     3          2.75            2.99
     5          1.92            3.57
    10          0.14            4.21
    25          0.01            4.30
Selected depth: 3. Test MAE: 3.91 minutes.
Open validation-curve.png. The vertical gap measures how differently the two sets behaved.
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Add a deeper tree to new_inputs.csv. Compare its training and validation errors with the shallower tree before checking the winner.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A gap concerns these samples, not every future case. Repeated choices using test results consume that test.

<details>
<summary>Check your choice and reason</summary>

Depth 3 on that evidence. Freeze the procedure, then report separate test errors, counts and limitations.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:overfitting -->
<!-- teaching-note:end -->
