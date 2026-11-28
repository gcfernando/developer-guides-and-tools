# Choose a cutoff for rare urgent orders

**Lesson 444 · Core**

## Your goal

Compare precision and recall and pick an alert cutoff on validation orders before testing.

## Before you start

Finish lesson 205 and the error-count practice.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

Choose a cutoff on validation orders. More caught urgent orders may bring more false alarms. Team capacity and costs matter.

## Guess first

Does changing the cutoff retrain the model? Write your answer before running the script.

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
Validation urgent share: 17.1%. Always silent accuracy: 82.9%; recall: 0%.
Validation choice: cutoff 0.192; precision 40.0%; recall 70.1%.
                Rule  Cutoff  Urgent caught  Urgent missed  False alarms  Precision  Recall
             Default   0.500             38            105            26      0.594   0.266
Chosen on validation   0.192            104             39           199      0.343   0.727
Validation average precision: 0.504
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change min_recall from 0.70 to 0.85. Check why the new cutoff is lower and how the alert counts change. Pick a target on validation only.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. It changes which scores raise alerts.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.
