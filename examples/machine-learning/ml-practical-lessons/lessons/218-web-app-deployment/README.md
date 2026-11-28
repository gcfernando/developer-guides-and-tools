# Web app deployment

**Lesson 218 · Practice**

## Your goal

Send a request from a small web page and show the estimate.

## Before you start

Explain an input field, a request and a response.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A form collects inputs and displays the service response. It is another way to use the same model contract.

**Why and when.** Use it to let a person make a controlled local request after the prediction code works.

**A worked example to follow.** Enter a distance, select Predict and read returned minutes. The endpoint must still validate a negative or missing value, even if the browser provides a numeric input control.

**Input and output.** The supplied sample fields are `distance_km`, `minutes`. In that field order, one original row is:

```text
1 | 12
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

If someone bypasses the form and sends a negative number directly, should the endpoint accept it because the form normally blocks it? Write a reason before running or opening the answer.

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

**Common mistakes and limits.** A working server test is not a tested browser layout. The practice app is local; it does not establish deployment security or production reliability.

<details>
<summary>Check your choice and reason</summary>

No. Validate at the service boundary and return a clear problem. Show an understandable message in the form as well.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

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

<!-- teaching-note:start -->
<!-- teaching-profile:web_form -->
<!-- teaching-note:end -->
