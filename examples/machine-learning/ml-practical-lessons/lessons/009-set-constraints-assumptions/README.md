# Set constraints & assumptions

**Lesson 009 · Core**

## Your goal

Record the time, hardware and accuracy limits that affect your project.

## Before you start

Name the person and decision the result should help.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

A project needs a useful question before it needs a model. A fixed rule may be enough. A score must match the decision.

## Guess first

Do we always need machine learning? Write your answer before running the script.

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
              use_case                   constraint
Estimate delivery time                   One laptop
Route support messages          Review missed items
        Group shoppers Groups must be interpretable
First decision: Estimate delivery time
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Add one task to sample.csv with a decision, objective, metric, domain check and constraint. Look for it in the printed table.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Use a known rule or report if it answers the question well enough.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| use_case | objective | metric | domain_check | constraint |
| --- | --- | --- | --- | --- |
| Estimate delivery time | regression | RMSE | Distance is in km | One laptop |
| Route support messages | classification | F1 | Negation changes meaning | Review missed items |
| Group shoppers | clustering | Silhouette | Income and scores use different units | Groups must be interpretable |
