# Understand the domain knowledge related to the data

**Lesson 008 · Practice**

## Your goal

Write down what the data means, including its units and what you know before predicting.

## Before you start

Name a person who needs to make a decision.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A project brief states the decision, wanted answer, available inputs, useful score and practical limits.

**Why and when.** Write the brief before choosing an algorithm. It can reveal that a report or ordinary rule is enough.

**A worked example to follow.** A shop wants a delivery estimate before dispatch. Distance is available then; the finished delivery time is not. Minutes of error answer this question more directly than a percentage of correct category names.

**Input and output.** The supplied sample fields are `use_case`, `objective`, `metric`, `domain_check`, `constraint`. In that field order, one original row is:

```text
Estimate delivery time | regression | RMSE | Distance is in km | One laptop
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Trace the named source fields into the printed table, file or request result. Check names and counts before interpreting what the program reports. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

For a rule giving free delivery above 50 currency units, write the decision and decide whether training is needed. Then change the question to estimated arrival time. Write a reason before running or opening the answer.

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
              use_case                          domain_check
Estimate delivery time                     Distance is in km
Route support messages              Negation changes meaning
        Group shoppers Income and scores use different units
First decision: Estimate delivery time
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Add one task to sample.csv with a decision, objective, metric, domain check and constraint. Look for it in the printed table.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** A convenient score is not automatically a useful business goal. State units, when fields arrive, and who acts on the result.

<details>
<summary>Check your choice and reason</summary>

Free delivery follows an agreed threshold, so no learned model is needed. Arrival time may need examples; compare it with a simple existing estimate and choose an acceptable error in minutes.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Sample data

| use_case | objective | metric | domain_check | constraint |
| --- | --- | --- | --- | --- |
| Estimate delivery time | regression | RMSE | Distance is in km | One laptop |
| Route support messages | classification | F1 | Negation changes meaning | Review missed items |
| Group shoppers | clustering | Silhouette | Income and scores use different units | Groups must be interpretable |

<!-- teaching-note:start -->
<!-- teaching-profile:project_brief -->
<!-- teaching-note:end -->
