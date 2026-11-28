# Image embeddings

**Lesson 114 · Practice**

## Your goal

Summarize a drawing with two numeric measurements and use them to predict its direction.

## Before you start

Draw a small grid. Each cell is a pixel value.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

Resize makes pictures the same size. Flatten puts the grid in a row. This KNN example compares pixel values; it does not train a CNN.

## Guess first

Do flattening and resizing mean the same thing? Write your answer before running the script.

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

<details>
<summary>Read the answer after trying</summary>

No. Resizing changes the grid size. Flattening changes how its values are arranged.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


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
