# Normalization

**Lesson 314 · Practice**

## Your goal

Put the pixels on a common scale before using the hand-drawn digit shapes in a model.

## Before you start

Finish the main preparation and checking modules.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

These are small invented practice datasets. Their old famous-dataset headings are historical labels. Use training rows to learn preparation and keep the check rows separate.

## Guess first

Do two correct examples prove that the model will work for a real population? Write your answer before running the script.

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
First raw sketch: ['###', '#.#', '#.#', '#.#', '###']
Blank images to inspect: 0
Model-input shape: (10, 64)
Pixel range: 0.0 1.0
Targets: ['0', '7']
Predictions: ['0', '7']
First one-hot label: [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
New labels: ['0', '7']
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Edit new_inputs.csv. Within a picture, # is an on pixel, a dot is an off pixel, and / starts the next row.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. They show the calculation. Check more suitable data and describe what is missing.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| split | pixel_rows | label |
| --- | --- | --- |
| train | ###/#.#/#.#/#.#/### | 0 |
| train | .#./##./.#./.#./### | 1 |
| train | ###/..#/###/#../### | 2 |
| train | ###/..#/.##/..#/### | 3 |
| train | #.#/#.#/###/..#/..# | 4 |
| train | ###/#../###/..#/### | 5 |
| train | ###/#../###/#.#/### | 6 |
| train | ###/..#/..#/.#./.#. | 7 |

Showing the first 8 of 12 rows. The CSV has the full sample.

## 📩 Supplied new inputs

| pixel_rows |
| --- |
| ###/#.#/#.#/#.#/##. |
| ###/..#/.##/.#./.#. |
