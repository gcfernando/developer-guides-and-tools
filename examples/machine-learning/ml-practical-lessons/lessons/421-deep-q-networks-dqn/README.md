# Deep Q Networks (DQN)

**Lesson 421 · Practice**

## Your goal

Teach a small neural network to score left and right moves.

## Before you start

Complete the network bridge and one Q update.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

DQN uses a neural network to approximate action values instead of a separate table entry for each state.

**Why and when.** Study its mechanics on the track before a larger control task.

**A worked example to follow.** A one-hot state yields left/right values. Replay stores transitions; a target copy supplies later values. A terminal mask stops future value being added after the goal.

**Input and output.** The supplied sample fields are `state`, `action`, `next_state`, `reward`, `done`. In that field order, one original row is:

```text
0 | 0 | 0 | -0.02 | False
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Find the state/action inputs, follow the transition and reward calculation, then inspect the policy, action values or planned move this particular script produces. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Why does a terminal goal target contain no next-state value? Write a reason before running or opening the answer.

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
Replay transitions: 8
DQN policy: [1, 1, 1, 1]
Moves for test starts: [1, 1, 1]
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing start from 0 to 3 in new_inputs.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** This complete tiny replay batch does not establish robust control, safe exploration or image understanding.

<details markdown="1">
<summary>Check your choice and reason</summary>

The episode ended, so no later action rewards follow within that return.

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

<!-- extra-lab:start -->
## Trace one update before a network

Read the [network bridge](../../ELECTIVES.md#a-bridge-before-networks-trace-one-learning-step) before the larger training loop. The complete [network_bridge.py](network_bridge.py) needs only Python:

```bash
python network_bridge.py
```

Its [recorded output](network-expected-output.txt) follows one input, a weighted sum, a squared mistake, and a change to the weight and bias. It does not measure performance on separate examples. In that practice file change `learning_rate = 0.1` to `learning_rate = 1.0`, save, and run again. This row's loss rises from 1 to 81: a larger step can make learning worse. Restore 0.1 afterward. Complete the array-shape paper task in Extra topics before reading frame or token tensors.
<!-- extra-lab:end -->


<!-- teaching-note:start -->
<!-- teaching-profile:dqn -->
<!-- teaching-note:end -->
