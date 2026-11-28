# Practice

**Lesson 328 · Practice**

## Your goal

Predict subscription before the call using available customer facts, such as balance and job. Inspect current-call duration only as a descriptive field; it is unavailable to this predictor.

## Before you start

Read the named fields and explain the preparation taught earlier.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A complete practice pipeline connects input preparation with a fit and a separate check.

**Why and when.** Use this bank campaign records exercise to trace one row through the supplied workflow.

**A worked example to follow.** The bank campaign records exercise uses age, balance, job, marital, education and prior. Its output is subscribed. Current-call duration is unavailable before calling and stays outside prediction inputs. Find one kept-back row and compare its prediction with its recorded answer where a confirmed answer exists.

**Input and output.** The supplied sample fields are `age`, `balance`, `duration`, `job`, `marital`, `education`, `prior`, `subscribed`. In that field order, one original row is:

```text
21 | 500 | 60 | student | single | school | none | no
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

Write a three-line handoff for the bank campaign records: input contract, result meaning, and one reason the result may fail on new cases. Write a reason before running or opening the answer.

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
Balance / duration range: {'balance': {'min': 300, 'max': 12000}, 'duration': {'min': 35, 'max': 650}}
Training-only descriptive duration scale: [-0.86, -0.63, -0.19, 0.88, -0.97, 1.77]
Missing cells before filling or removing rows: {'age': 0, 'balance': 0, 'job': 1, 'marital': 1, 'education': 0, 'prior': 0, 'subscribed': 0}
   Field  Rows to review
 balance               0
duration               0
Flagged original rows: []
 Original row Actual answer Prediction
            7            no         no
            8           yes        yes
 age  balance  duration     job marital education   prior prediction
  21      500        60 student  single    school    none         no
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change an input in new_inputs.csv. Compare the predictions with the held-out check above.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** The tiny invented table illustrates mechanics. Two correct predictions, a cluster assignment or a familiar benchmark name does not establish real-world performance.

<details>
<summary>Check your choice and reason</summary>

Name age, balance, job, marital, education and prior; explain subscribed in the appropriate unit or category; state a specific missing population, recording problem or representation limit. Use more suitable independent data before making a general claim.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| age | balance | duration | job | marital | education | prior | subscribed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 21 | 500 | 60 | student | single | school | none | no |
| 36 | 1200 | 110 | admin | married | degree | none | no |
| 44 | 4200 | 210 | manager | married | degree | success | yes |
| 51 | 6500 | 450 | owner | married | graduate | success | yes |
| 28 | 300 | 35 | — | single | school | none | no |
| 60 | 12000 | 650 | owner | — | graduate | success | yes |
| 30 | 700 | 40 | admin | single | degree | none | no |
| 49 | 5000 | 220 | manager | married | degree | success | yes |

## 📩 Supplied new inputs

| age | balance | duration | job | marital | education | prior |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | 500 | 60 | student | single | school | none |
| 49 | 5000 | 220 | manager | married | degree | success |
| 44 | 4200 | 210 | manager | married | degree | success |

<!-- teaching-note:start -->
<!-- teaching-profile:dataset_328 -->
<!-- teaching-note:end -->
