# Web app integration

**Lesson 231 · Practice**

## Your goal

Pass a distance from a small web page to an API route.

## Before you start

Train and save a model. Know an input and a prediction.

Use the [main learning path](../LEARNING-PATH.html) if you have not learned this yet. For extra topics, read [the extra-topic guide](../ELECTIVES.html). These links work when this folder is extracted directly into the complete course folder.

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
       Action  HTTP status  Predicted minutes
Open the page          200                NaN
 Predict 4 km          200               18.0
Response: {'minutes': 18.0}
8 200 {'minutes': 26.0}
12 200 {'minutes': 34.0}
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Try changing km from 4 to 12 in new_inputs.csv. Compare the new output.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

<details>
<summary>Read the answer after trying</summary>

No. Reject it with a clear explanation. A valid-looking value can still be outside the tested range.

</details>

You can move on when you can explain the goal, the changed value and why the result did or did not change. Then return to the next box in the main learning path.

### Open the page yourself

Run `python -m uvicorn lesson:app --host 127.0.0.1 --port 8000`. Keep that terminal open. Open `http://127.0.0.1:8000` in your browser. Enter 4 and select Predict. Stop with Ctrl+C. If port 8000 is busy, use `--port 8001` and open port 8001 instead.


## 📋 Sample data

| distance_km | minutes |
| --- | --- |
| 1 | 12 |
| 2 | 14 |
| 3 | 16 |

## 📩 Supplied new inputs

| km |
| --- |
| 4 |
| 8 |
| 12 |

## Open the form on your computer

1. In the lesson folder run `python -m uvicorn lesson:app`.
2. Open [the local form](http://127.0.0.1:8000) in your browser.
3. Enter 4 km or 12 km and click **Predict**. Press **Ctrl+C** in the terminal when you finish.
