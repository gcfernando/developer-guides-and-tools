# Turn ordered names into numbers (OrdinalEncoder)

**Lesson 076 · Practice**

## Your goal

Turn Low, Medium and High into ordered numbers before predicting a review action.

## Before you start

Explain why low, medium and high have an order.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Ordinal encoding records an explicit order between input categories. Label encoding gives identifiers to answer classes.

**Why and when.** Use an order only when the field meaning supports it. The model may also impose a spacing assumption on those numbers.

**A worked example to follow.** Low, Medium, High become 0, 1, 2 in this exercise. LabelEncoder separately turns the wait/review answers into class IDs and reverses predictions to readable names.

**Input and output.** The supplied sample fields are `priority`, `action`. In that field order, one original row is:

```text
Low | wait
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Could North, South and West be ordered 0, 1, 2 because a terminal prints them that way? Write a reason before running or opening the answer.

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
Priority codes: [0.0, 1.0, 2.0]
Held-out label: ['review']
priority action
     Low   wait
  Medium review
    High review
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing priority from Low to High in new_inputs.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Codes 0, 1, 2 do not prove that the gap between low and medium equals the gap between medium and high. Unordered colours need a different representation.

<details>
<summary>Check your choice and reason</summary>

No. Alphabetical or display order is not a real scale. Use separate columns or another justified categorical representation.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:ordinal -->
<!-- teaching-note:end -->
