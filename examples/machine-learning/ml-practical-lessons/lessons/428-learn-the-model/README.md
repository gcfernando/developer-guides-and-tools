# Learn the Model

**Lesson 428 · Practice**

## Your goal

Build a small transition table from observed moves and use it to plan.

## Before you start

Read transitions and distinguish observations from given rules.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Model-based planning uses a supplied or learned representation of action consequences.

**Why and when.** Plan when transition predictions and their uncertainty are appropriate for the decision.

**A worked example to follow.** The lesson compares a given deterministic rule with a lookup learned from one observation per state/action pair, then looks ahead through possible moves.

**Input and output.** The supplied sample fields are `state`, `action`, `next_state`, `reward`, `done`. In that field order, one original row is:

```text
0 | 0 | 0 | -0.02 | False
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Find the state/action inputs, follow the transition and reward calculation, then inspect the policy, action values or planned move this particular script produces. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A move sometimes slips left and sometimes right. Store its first result as a certain rule? Write a reason before running or opening the answer.

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
learn-the-model first-action values: [0.74, 0.8]
Best action: 1
Start 0, planned values: [0.7403087499999998, 0.8003249999999998]
Start 1, planned values: [0.7403087499999998, 0.8634999999999999]
Start 3, planned values: [0.8634999999999999, 1.0]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit start in new_inputs.csv. The script builds a lookup from the observed moves and uses it to plan.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** One observation per pair suffices only for this deterministic toy. It does not establish probabilities for an uncertain task.

<details>
<summary>Check your choice and reason</summary>

No. Gather observations and represent transition uncertainty, then evaluate the planner under those outcomes.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| state | action | next_state | reward | done |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | -0.02 | False |
| 0 | 1 | 1 | -0.02 | False |
| 1 | 0 | 0 | -0.02 | False |
| 1 | 1 | 2 | -0.02 | False |
| 2 | 0 | 1 | -0.02 | False |
| 2 | 1 | 3 | -0.02 | False |
| 3 | 0 | 2 | -0.02 | False |
| 3 | 1 | 4 | 1.0 | True |

## 📩 Supplied new inputs

| start |
| --- |
| 0 |
| 1 |
| 3 |

<!-- teaching-note:start -->
<!-- teaching-profile:model_based -->
<!-- teaching-note:end -->
