# Key Concepts

**Lesson 411 · Practice**

## Your goal

Connect the robot’s position, chosen move and reward using a short track.

## Before you start

Read state, action and reward on a track.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A policy chooses actions. Return adds rewards; a value function is an expected return under a policy.

**Why and when.** Use sequential reasoning when actions affect later situations.

**A worked example to follow.** The five-cell track gives −0.02 for ordinary moves and +1 at the goal. Discounting weights later rewards less. This script follows one fixed route, not a stochastic expectation.

**Input and output.** The supplied sample fields are `state`, `action`, `next_state`, `reward`, `done`. In that field order, one original row is:

```text
0 | 0 | 0 | -0.02 | False
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Find the state/action inputs, follow the transition and reward calculation, then inspect the policy, action values or planned move this particular script produces. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Can changing move rewards change the preferred policy on an unchanged track? Write a reason before running or opening the answer.

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
 Move  From cell Action  To cell  Reward
    1          0  Right        1   -0.02
    2          1  Right        2   -0.02
    3          2  Right        3   -0.02
    4          3  Right        4    1.00
Discounted return: 0.8
From cell 1 move right to 2, reward = -0.02
From cell 3 move right to 4, reward = 1.0
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing start from 0 to 3 in new_inputs.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** One rewarded move does not establish a reliable policy. A designed reward may miss the real goal.

<details markdown="1">
<summary>Check your choice and reason</summary>

Yes. Review reward meaning and evaluate behavior across suitable trials.

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
<!-- teaching-profile:rl_return -->
<!-- teaching-note:end -->
