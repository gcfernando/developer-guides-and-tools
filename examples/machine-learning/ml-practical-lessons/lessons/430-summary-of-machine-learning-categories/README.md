# Summary of Machine Learning Categories

**Lesson 430 · Practice**

## Your goal

Match a delivery problem to one of the four learning categories.

## Before you start

Name numbers, categories, groups and rewards.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Learning categories describe the available feedback and the learning task.

**Why and when.** Choose a workflow from the question rather than memorize every algorithm.

**A worked example to follow.** Known answers suggest supervised learning; unlabeled grouping is unsupervised; mixed labels can motivate semi-supervised methods; actions and rewards motivate reinforcement learning.

**Input and output.** The supplied sample fields are `problem`, `target`, `feedback`. In that field order, one original row is:

```text
Predict delivery time | minutes | known answers
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Trace the named source fields into the printed table, file or request result. Check names and counts before interpreting what the program reports. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A robot classifies pictures and learns routes from rewards. Must it have only one learning category? Write a reason before running or opening the answer.

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
Worked examples
                                      problem      feedback learning_category
                        Predict delivery time known answers        Supervised
          Group routes by distance and weight    no answers      Unsupervised
             Tag the remaining delivery notes  some answers   Semi-supervised
Learn which corridor reaches the loading door       rewards     Reinforcement

Your examples
                                problem      feedback learning_category
                 Predict package weight known answers        Supervised
           Find unusual delivery routes    no answers      Unsupervised
Classify photos with a few known labels  some answers   Semi-supervised
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change the first new example’s feedback to some answers. Its category should become Semi-supervised.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Numeric class IDs do not turn classification into regression. One product can combine tasks.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Its components have different feedback, outputs and evaluation.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:categories -->
<!-- teaching-note:end -->
