# Choose a cutoff for rare urgent orders

**Lesson 444 · Core**

## Your goal

Compare precision and recall and pick an alert cutoff on validation orders before testing.

## Before you start

Calculate precision and recall from counts.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A cutoff converts fixed scores into actions, changing alerts without retraining the model.

**Why and when.** Choose it on validation using misses, false alarms, costs and capacity.

**A worked example to follow.** The script picks highest precision among candidates meeting minimum validation recall. This illustrates one constraint; it does not automatically enforce staffing capacity.

**Input and output.** The supplied sample fields are `order_id`, `distance_km`, `weight_kg`, `rush_hour`, `vehicle_load`, `urgent`, `split`. In that field order, one original row is:

```text
R00000 | 76.01 | 14.8 | 0 | 10 | 1 | train
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A rule creates 100 alerts daily but reviewers can handle 20. Is recall alone enough? Write a reason before running or opening the answer.

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

**Common mistakes and limits.** Lowering a cutoff can overwhelm reviewers. A validation recall target is not guaranteed on a new population.

<details>
<summary>Check your choice and reason</summary>

No. Check validation workload and costs against agreed capacity and decide a practical policy or fallback.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:threshold -->
<!-- teaching-note:end -->
