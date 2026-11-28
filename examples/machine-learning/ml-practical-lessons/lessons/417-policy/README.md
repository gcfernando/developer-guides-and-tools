# Policy

**Lesson 417 · Practice**

## Your goal

Follow a simple rule for choosing moves and compare the resulting rewards.

## Before you start

Read the robot, reward and network notes in Extra topics.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

An agent chooses an action, sees a result and gets a reward. A policy is its action rule. Return adds rewards, often giving later rewards less weight.

## Guess first

Does one rewarded move prove a policy is reliable? Write your answer before running the script.

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
A policy is a rule for choosing a move. This rule chooses right until the goal.
 Start Action  Next cell  Reward  At goal
     0   left          0   -0.02    False
     0  right          1   -0.02    False
     2  right          3   -0.02    False
     3  right          4    1.00     True
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing start from 0 to 2 in new_inputs.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Check the whole policy over suitable trials.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


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

| start | action |
| --- | --- |
| 0 | 0 |
| 0 | 1 |
| 2 | 1 |
| 3 | 1 |
