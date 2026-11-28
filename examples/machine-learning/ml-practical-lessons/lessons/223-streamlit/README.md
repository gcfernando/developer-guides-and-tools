# Streamlit

**Lesson 223 · Practice**

## Your goal

Fill in a Streamlit form and see the delivery estimate change.

## Before you start

Train and save a model. Know an input and a prediction.

Use the [main learning path](../../LEARNING-PATH.md) if you have not learned this yet. For extra topics, read [the extra-topic guide](../../ELECTIVES.md). In the repository, these links open the course guides. If you downloaded a ZIP, open README.html for the browser links. Keep the extracted lesson folder directly inside the complete course folder.

## The idea in simple words

A request gives inputs to a program. A response gives its answer or a clear problem. An HTTP status is a short result code. Local tests do not publish a server.

## Guess first

Should a negative distance receive a normal estimate? Write your answer before running the script.

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
Prediction: 27.5 minutes
5 2 Prediction: 27.5 minutes
10 4 Prediction: 43.0 minutes
15 1 Prediction: 38.5 minutes
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Enter distances of 5, 10 and 15 km with positive weights. The script fills out the sample form for each row.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Reject it with a clear explanation. A valid-looking value can still be outside the tested range.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.

### Open the form yourself

Run `python -m streamlit run delivery_app.py`. Open the local address printed in the terminal. Enter a distance and weight. Stop with Ctrl+C. The supplied file resolves its own CSV path.


## 📋 Sample data

| distance_km | weight_kg | delivery_minutes |
| --- | --- | --- |
| 2 | 1 | 19 |
| 4 | 3 | 30 |
| 6 | 2 | 29 |
| 8 | 4 | 40 |

## 📩 Supplied new inputs

| distance_km | weight_kg |
| --- | --- |
| 5 | 2 |
| 10 | 4 |
| 15 | 1 |
