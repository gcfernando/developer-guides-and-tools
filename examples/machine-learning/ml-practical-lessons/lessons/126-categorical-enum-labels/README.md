# Category (enum, labels)

**Lesson 126 · Practice**

## Your goal

Turn category names into separate 0-or-1 columns for a model.

## Before you start

Tell a category name from a measured amount.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

One-hot encoding gives each known category a separate 0-or-1 column. It avoids inventing an order between names.

**Why and when.** Use it for a modest set of unordered names when the chosen model requires numeric inputs.

**A worked example to follow.** This script explicitly declares the column order Red, Blue, Green. Green becomes 0, 0, 1. Fit the encoder using training inputs, then transform check rows and new requests with that same encoder. The order and number of columns stay fixed.

**Input and output.** The supplied sample fields are `color`, `orders`. In that field order, one original row is:

```text
Red | 20
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Encode Blue on paper. A new request says Yellow. Add a Yellow column only to that request, or keep the saved three-column schema? Explain what the service must decide. Write a reason before running or opening the answer.

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
Check actual / predicted: [23] [21.0]
Original color  Red  Blue  Green
           Red    1     0      0
          Blue    0     1      0
         Green    0     0      1
        Purple    0     0      0
 color  Red  Blue  Green  Predicted orders
   Red    1     0      0              21.0
  Blue    0     1      0              13.0
Purple    0     0      0              16.5
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In new_inputs.csv, enter Red, Blue and an unfamiliar color such as Purple. See the encoded columns and predicted orders for each one.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Purple becomes 0, 0, 0 here because handle_unknown is ignore. That is an allowed representation, not evidence about Purple-specific demand. Do not fit a separate encoder on new requests. Thousands of categories may need a different, validated approach.

<details markdown="1">
<summary>Check your choice and reason</summary>

Blue is 0, 1, 0. Keep the saved schema; changing only the request columns breaks the model contract. This demonstration maps Yellow to all zeros. A real service must explicitly reject, review or use a tested fallback for unfamiliar names.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

### A new category

Purple becomes all zeros in this example. The model has no Purple-specific evidence. A real service may reject a new name or use a tested fallback. An encoded row is not proof that its prediction is reliable.

## 📋 Sample data

| color | orders |
| --- | --- |
| Red | 20 |
| Blue | 12 |
| Green | 15 |
| Red | 22 |
| Blue | 14 |
| Green | 16 |
| Red | 23 |

## 📩 Supplied new inputs

| color |
| --- |
| Red |
| Blue |
| Purple |

<!-- teaching-note:start -->
<!-- teaching-profile:one_hot -->
<!-- teaching-note:end -->
