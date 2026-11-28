# Image embeddings

**Lesson 114 · Practice**

## Your goal

Summarize a drawing with two numeric measurements and use them to predict its direction.

## Before you start

Find lit cells in rows and columns of a grid.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A feature vector can summarize a picture without passing every pixel.

**Why and when.** Use hand-built measurements when they preserve the information the task needs, and compare their failures with alternatives.

**A worked example to follow.** A sideways bar has horizontal spread and little vertical spread. An upright bar reverses that pattern. The lesson gives those two spread values to a nearest-neighbour model.

**Input and output.** The supplied sample fields are `direction`, `position`. In that field order, one original row is:

```text
Sideways | 1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Would these two spread values alone reliably distinguish a handwritten 6 from an 8? What test would reveal a weakness? Write a reason before running or opening the answer.

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
 Vertical spread  Horizontal spread Label or prediction
            0.00               1.12            Sideways
            0.00               1.12            Sideways
            1.12               0.00             Upright
            1.12               0.00             Upright
            1.12               0.00 Upright (predicted)
Predicted direction for each new drawing: ['Upright', 'Sideways']
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing direction from Upright to Sideways in new_inputs.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** These hand-built features do not prove that a neural image encoder was trained. Two different images can share the same summary and become indistinguishable.

<details markdown="1">
<summary>Check your choice and reason</summary>

Not necessarily. Find distinct drawings with similar spreads and compare their feature vectors and held-back predictions. A summary must be assessed for the actual task.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| direction | position |
| --- | --- |
| Sideways | 1 |
| Sideways | 3 |
| Upright | 1 |
| Upright | 3 |

## 📩 Supplied new inputs

| direction | position |
| --- | --- |
| Upright | 4 |
| Sideways | 2 |

<!-- teaching-note:start -->
<!-- teaching-profile:image_embedding -->
<!-- teaching-note:end -->
