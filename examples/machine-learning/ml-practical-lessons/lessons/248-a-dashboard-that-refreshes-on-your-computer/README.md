# A dashboard that refreshes on your computer

**Lesson 248 · Practice**

## Your goal

Run a local dashboard that reads the latest accuracy file.

## Before you start

Read a model score and wait for actual outcomes.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

Monitoring watches later inputs and results. Drift means change over time. A change is a reason to investigate, not an automatic instruction to replace a model.

## Guess first

Can we measure new accuracy before the true answers arrive? Write your answer before running the script.

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
        Dashboard field Value
Latest labeled accuracy   80%
        Alert threshold   85%
          Alert visible  True
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

In the Afternoon row, change Correct from 16 to 18. You should see 90% and Alert visible: False.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Record predictions and wait for outcomes.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.


## 📋 Sample data

| Batch | Correct | Checked |
| --- | --- | --- |
| Morning | 18 | 20 |
| Midday | 14 | 20 |
| Afternoon | 16 | 20 |

## Open the dashboard

1. Run `python lesson.py` to build the dashboard and its monitoring CSV.
2. Run `python -m streamlit run monitoring_dashboard.py` in the same folder. Open the local address printed in the terminal.
3. Change `sample.csv` and rerun `python lesson.py` from a second terminal in the same folder. The open dashboard reads the new accuracy.
