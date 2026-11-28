# Choose the right data split

**Lesson 442 · Core**

## Your goal

Compare random, customer-grouped, and chronological splits on the same delivery data.

## Before you start

Read a held-back row and error in minutes.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A split defines the new-case question: comparable orders, unseen customers or later dates.

**Why and when.** Choose the question before inspecting which split produces the best score.

**A worked example to follow.** MAE averages mistake sizes: actual 30 versus prediction 27 is an absolute error of 3 minutes. The script prints shared shipment IDs, shared customer IDs and date order before MAE.

**Input and output.** The supplied sample fields are `shipment_id`, `customer_id`, `date`, `distance_km`, `weight_kg`, `actual_minutes`. In that field order, one original row is:

```text
S0000 | C001 | 2025-01-01 | 5.36 | 17.07 | 35.9
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A model must handle new customers next month. What checks can a random split miss? Write a reason before running or opening the answer.

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
    Plan  Test orders  Shared shipments  Shared customers  Test is entirely later  Test MAE (min)
  random          105                 0                63                   False            2.92
customer          105                 0                 0                   False            5.91
    time          105                 0                84                    True            2.50

Random: independent orders in the same setting. Customer: customers the model has never seen.
Time: later orders. Their customers may already be known. Pick the plan before comparing scores.
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Leave only customer in new_inputs.csv. Check that this plan keeps all rows for an unseen customer together.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** No shared shipment IDs is not sufficient for every job. Customer ID is deliberately included here to illustrate known versus unseen customers, not as a universal input recommendation.

<details markdown="1">
<summary>Check your choice and reason</summary>

Keep customers unseen for the new-customer question, and consider later-time evaluation for future use. Design combined evaluation for the actual job.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.



<!-- teaching-note:start -->
<!-- teaching-profile:split_choice -->
<!-- teaching-note:end -->
