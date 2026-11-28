# Q-Learning

**Lesson 420 · Practice**

## Your goal

Build a table of expected rewards for each cell and move.

## Before you start

Explain state, action and discounted return.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Q-learning updates a table of action values from observed transitions and later estimated values.

**Why and when.** Use a small table when states/actions are manageable and interaction is appropriate.

**A worked example to follow.** The agent explores sometimes, otherwise choosing its largest value. It updates the observed entry; a terminal goal adds no next-action value.

**Input and output.** The supplied sample fields are `state`, `action`, `next_state`, `reward`, `done`. In that field order, one original row is:

```text
0 | 0 | 0 | -0.02 | False
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Find the state/action inputs, follow the transition and reward calculation, then inspect the policy, action values or planned move this particular script produces. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

If all values start at zero and the agent never explores, what can remain untested? Write a reason before running or opening the answer.

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
Best actions (0 left, 1 right): [1, 1, 1, 1]
State values: [0.8, 0.86, 0.93, 1.0]
Moves for test starts: [1, 1, 1]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change a starting cell (0–3) in new_inputs.csv. Read the saved-in-memory policy’s preferred move, 0 left or 1 right.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Early greedy choices can prevent discovery. Learning depends on exploration and sufficient suitable experience.

<details>
<summary>Check your choice and reason</summary>

Moves not selected by initial tie-breaking can remain untested. Inspect experience coverage and evaluate the policy.

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
<!-- teaching-profile:q_learning -->
<!-- teaching-note:end -->
