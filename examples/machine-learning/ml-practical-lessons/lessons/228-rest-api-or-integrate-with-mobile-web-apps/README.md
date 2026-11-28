# REST API or integrate with mobile/web apps

**Lesson 228 · Practice**

## Your goal

Turn CSV rows into JSON request bodies a web or mobile app would send.

## Before you start

Train a small model and identify its required input names and units.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A prediction service accepts a request, validates inputs and returns an estimate or a clear error.

**Why and when.** Use a service when another program needs the saved model. Test locally before considering hosting.

**A worked example to follow.** A request supplies distance_km and weight_kg; the response contains minutes. A negative distance should be rejected rather than quietly producing a normal estimate. HTTP status reports success or the kind of failure.

**Input and output.** The supplied sample fields are `distance_km`, `weight_kg`. In that field order, one original row is:

```text
5 | 2
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A client sends metres in a field named distance_km. Will a numeric type check detect the mistake? What belongs in the input contract? Write a reason before running or opening the answer.

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
POST /predict {"distance_km": 5, "weight_kg": 2}
POST /predict {"distance_km": 10, "weight_kg": 3}
POST /predict {"distance_km": 14, "weight_kg": 4}
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing distance_km from 5 to 14 in sample.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Local test-client calls do not deploy a public server. Valid types do not establish in-scope ranges or reliable predictions. Load only model files you created or trust.

<details>
<summary>Check your choice and reason</summary>

Not necessarily. Record units, names, ranges, missing-value rules and unfamiliar-category policy, and test examples that violate them.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| distance_km | weight_kg |
| --- | --- |
| 5 | 2 |
| 10 | 3 |
| 14 | 4 |

<!-- teaching-note:start -->
<!-- teaching-profile:service -->
<!-- teaching-note:end -->
