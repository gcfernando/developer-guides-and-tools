# Remove

**Lesson 066 · Practice**

## Your goal

Remove an impossible negative parcel weight before fitting a model.

## Before you start

Sort numbers. The middle half is the values between the lower and upper quarters.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

An outlier is an unusual value. A flag says check it. It does not say it is wrong. Use the source to keep, correct or set it aside.

## Guess first

Does an outlier flag prove a recording error? Write your answer before running the script.

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
Confirmed errors removed: 1
remove only
 weight_used_by_model  original_weight_kg  predicted_minutes  actual_minutes
                  7.0                 7.0               28.1              32
remove and clip
 weight_used_by_model  original_weight_kg  predicted_minutes  actual_minutes
                  7.0                 7.0               44.3              32
remove and log
 weight_used_by_model  original_weight_kg  predicted_minutes  actual_minutes
             2.079442                 7.0               38.8              32
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing weight_kg from 1 to 2 in sample.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. A very heavy parcel can be real. Ask for a source check.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| weight_kg | minutes |
| --- | --- |
| 1 | 18 |
| -45 | 18 |
| 2 | 21 |
| 3 | 23 |
| 5 | 28 |
| 40 | 72 |
| 7 | 32 |
