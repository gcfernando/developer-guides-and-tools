# Image pixels for a nearest-neighbour model

**Lesson 117 · Practice**

## Your goal

Turn a tiny picture into numbers, then predict light or dark with KNN. This is not a CNN.

## Before you start

Draw a small grid and label row and column positions.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A digital picture stores pixel values. Resize changes its grid size; grayscale changes colour representation; flatten arranges values in a row.

**Why and when.** Prepare all images with the same rules for a pixel-based model. Keep spatial dimensions for models that use neighborhoods.

**A worked example to follow.** This exercise makes a 6-by-6 RGB image, converts brightness to a 4-by-4 grid and flattens it into 16 values divided by 255. A nearest-neighbour classifier compares those numeric rows; it is not a CNN.

**Input and output.** The supplied sample fields are `red`, `green`, `blue`, `label`. In that field order, one original row is:

```text
15 | 15 | 15 | dark
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A 4-by-4 grayscale grid becomes how many values after flattening? Could a new 5-by-5 row be sent to the same 16-input model? Write a reason before running or opening the answer.

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
Image matrix becomes one row: (4, 16)
First normalized pixels: [0.059, 0.059, 0.059, 0.059]
New picture: ['light', 'dark', 'light']
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit the red, green, and blue numbers (0–255) in new_inputs.csv to predict dark or light.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Grayscale can discard useful colour information. Resizing and flattening are different operations. A uniform-colour toy image is far simpler than an everyday photograph.

<details>
<summary>Check your choice and reason</summary>

It becomes 16 values. Apply the saved resizing/preparation rule first; the model expects the same input count and ordering.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| red | green | blue | label |
| --- | --- | --- | --- |
| 15 | 15 | 15 | dark |
| 30 | 30 | 30 | dark |
| 220 | 220 | 220 | light |
| 240 | 240 | 240 | light |

## 📩 Supplied new inputs

| red | green | blue |
| --- | --- | --- |
| 210 | 210 | 210 |
| 8 | 8 | 8 |
| 255 | 230 | 210 |

<!-- teaching-note:start -->
<!-- teaching-profile:pixels -->
<!-- teaching-note:end -->
