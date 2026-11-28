# Flattening

**Lesson 347 · Practice**

## Your goal

Flatten one clothing drawing and reconstruct the original pixel grid.

## Before you start

Read the named fields and explain the preparation taught earlier.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Flattening arranges an existing grid into a one-dimensional sequence.

**Why and when.** Use it for an estimator expecting one feature row per image.

**A worked example to follow.** The clothing drawings exercise uses pixel_rows. Its output is label. A 5-by-5 grid becomes 25 values. C order reads rows first; F order reads columns first.

**Input and output.** The supplied sample fields are `split`, `pixel_rows`, `label`. In that field order, one original row is:

```text
train | .###./#####/#.#.#/..#../.###. | T-shirt
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Switch the traversal order, then reconstruct using that same order. Should the original grid be recovered? Write a reason before running or opening the answer.

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
Original shape: (5, 5). Flattened shape: (25,).
First ten values: [0, 255, 255, 255, 0, 255, 255, 255, 255, 255]
Recovered the original grid: True
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change order from C to F. The first ten entries should change while the recovered grid remains the same.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Training and prediction must use the same traversal order. Flattening removes explicit spatial arrangement from the input shape.

<details markdown="1">
<summary>Check your choice and reason</summary>

Yes. Matching flatten and reshape orders recover the grid. Mixing the orders can rearrange pixels and corrupt the representation.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:dataset_347 -->
<!-- teaching-note:end -->
