# AWS, Google Cloud, or Heroku

**Lesson 224 · Reference**

## Your goal

Practice a local request check, then use the deployment notes for your platform.

## Before you start

Run the local Flask or FastAPI request example first.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

Hosting runs an application on another service’s computers. Packaging and access rules are separate from the prediction calculation.

**Why and when.** Use an approved learning account only after local request checks and a cost/removal plan.

**A worked example to follow.** These scripts inspect a local request contract. The companion service notes describe preparing files for a selected platform; they do not mean the platform was deployed or tested.

**Input and output.** The supplied sample fields are `distance_km`, `weight_kg`. In that field order, one original row is:

```text
5 | 2
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Trace the named source fields into the printed table, file or request result. Check names and counts before interpreting what the program reports. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A script prints expected HTTP 200. Does that prove a hosted endpoint was called successfully? Write a reason before running or opening the answer.

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
 distance_km  weight_kg  valid  expected_status
           5          2   True              200
          15          6   True              200
          -2          4  False              422
           5          0  False              422
Platform to explore: AWS, Google Cloud, or Heroku
These are expected responses from a local contract check.
Use the FastAPI lesson to send real requests to a local test client.
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing distance_km from 5 to -2 in sample.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Keep credentials out of code and avoid uploading private data. Platform instructions and costs change. Preserve the prediction route, dependencies and input contract when adapting the module.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. It is a local expected-contract result. Deployment evidence requires the actual approved service, a request to its endpoint and recorded response, with costs and cleanup checked.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| distance_km | weight_kg |
| --- | --- |
| 5 | 2 |
| 15 | 6 |
| -2 | 4 |
| 5 | 0 |


See [External services](EXTERNAL-SERVICES.md) for the platform steps.

<!-- teaching-note:start -->
<!-- teaching-profile:hosting -->
<!-- teaching-note:end -->
