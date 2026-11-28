# Choose the right data split

**Lesson 442 · Core**

## Your goal

Compare random, customer-grouped, and chronological splits on the same delivery data.

## Before you start

Explain training and test roles.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

## The idea in simple words

Choose a split for the question, not for its best-looking score. Random rows, new customers and later dates are different questions.

## Guess first

Which split tests new customers? Write your answer before running the script.

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

<details>
<summary>Read the answer after trying</summary>

Keep customer groups separate.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.
