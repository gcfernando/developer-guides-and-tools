# Capstone: From delivery CSV to local model service

**Lesson 447 · Core**

## Your goal

Train, validate, test, and save a model. Send local requests and monitor later labeled deliveries.

## Before you start

Complete preparation, fair checks, baseline, API and monitoring.

Use the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.

## The idea in simple words

A checked workflow connects an input contract to learning, choice, evaluation, saved preparation and later use.

**Why and when.** Explain the guided workflow before attempting the independent project.

**A worked example to follow.** Split whole dates, compare Ridge with a training-median baseline, save the winner, validate requests, then compare a later labeled batch. Missing weights use the saved training preparation.

**Input and output.** The supplied sample fields are `shipment_id`, `delivery_date`, `distance_km`, `weight_kg`, `zone`, `actual_minutes`. In that field order, one original row is:

```text
D00001 | 2025-01-01 | 51.86 | (missing) | North | 89.1
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer. The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.

## Guess first

A valid request is accepted but West-zone errors rise. Does input validation prove continued usefulness? Write a reason before running or opening the answer.

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
Train: 430. Validation: 140. Test: 150.
Training median validation MAE: 22.36 minutes.
Ridge validation MAE: 2.98 minutes.
Selected: Ridge. Final test MAE: 2.80 minutes.
Saved delivery_model.joblib and model-info.json. Load the file you generated in this folder.

Local service results
15 km, North: 200 {'predicted_minutes': 32.3, 'model': 'Ridge'}
45 km, South: 200 {'predicted_minutes': 81.4, 'model': 'Ridge'}
65 km, West: 200 {'predicted_minutes': 108.2, 'model': 'Ridge'}
90 km, North: 422 {'detail': "That distance is outside the model's training range."}
-4 km, West: 422 {'detail': 'Enter a nonnegative distance.'}
```

[See the complete expected output](expected-output.txt). Explain one row aloud. A matching number is a check of the calculation, not proof of real-world quality.

## Change one thing

Change the 90 km request to 60 km. Run python send_requests.py to use your saved model. That request should receive 200 and an estimate.

Open the named CSV in a plain text editor. Keep its column names and commas. Save the same file name before running again. If you invent a request by changing its inputs, clear its old measured answer. Only score it after you have a real outcome for that new case.

## If you get stuck

If a file is missing, list the files with `dir` or `ls` and enter the folder holding the script. If a column or value is wrong, compare it with a fresh extracted CSV. Use a new folder to start over; keep your edited copy if useful. Use Setup for package or terminal errors.

## Explain the result

**Common mistakes and limits.** Synthetic results do not prove real-service quality. Valid inputs, accuracy, operational readiness and permission to deploy are separate questions.

<details markdown="1">
<summary>Check your choice and reason</summary>

No. Inspect measured outcomes, counts and source changes. Apply the agreed fallback and compare any replacement fairly before promotion.

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.

## 📋 Data dictionary

| File or field | Meaning |
| --- | --- |
| sample.csv | 720 invented, completed deliveries in date order, split by whole dates into 430 training, 140 validation, and 150 test orders. |
| later_batch.csv | 180 later deliveries with measured outcomes. Use them for monitoring after the final test. |
| new_inputs.csv | Example requests, including a blank weight, invalid distance, and unknown zone. |
| shipment_id | Unique delivery identifier. It is used to check records, and stays out of the model. |
| delivery_date | Date used to split and monitor shipments. The model does not receive this field. |
| distance_km | Input distance in kilometers. The service checks the training range. |
| weight_kg | Input in kilograms. A blank weight is handled by the training median in the Ridge pipeline. |
| zone | North, South, or West. The service rejects unrecognized values. |
| actual_minutes | Measured delivery time. It is provided for training and scoring only. |

## 🚚 Try the live service on this computer

1. Run `python lesson.py` to create the model and run the example requests using a local test client.
2. Start the app with `python -m uvicorn service:create_app --factory --host 127.0.0.1 --port 8000`. Leave that terminal open.
3. In a browser open [local interactive API docs](http://127.0.0.1:8000/docs). Open POST /predict, select **Try it out**, enter the JSON below, and select **Execute**.

```json
{"distance_km": 15, "weight_kg": 3, "zone": "North"}
```

You should see status 200 and about 32.3 minutes. Change 15 to 90 to get 422. Stop the server with Ctrl+C after practice. Run `python monitor.py` to inspect the later batch again without training.

For CSV requests without retraining, edit `new_inputs.csv` and run `python send_requests.py`. To perform only the training step, run `python fit_delivery_model.py`.

The saved artifact includes `model-info.json` with the columns, training distance limits, allowed zones, test result, and package versions. Use the Joblib file you generated yourself. This capstone uses made-up data and a local service.

## 🧾 Score your work

| Points | What to show |
| --- | --- |
| 2 | Explain each column and why the ID, date, and actual time stay out of API inputs. |
| 2 | Show the chronological split and why it keeps later orders out of model selection. |
| 2 | Name the validation winner and report the final test MAE in minutes. |
| 2 | Demonstrate an accepted request and a rejected request, and explain each response. |
| 2 | Compare the later batch with the test and explain why West deserves a closer look. |

The alert calls for investigation. Verify measurements and routing changes, then compare any replacement on a separate later batch before updating the service.

<!-- teaching-note:start -->
<!-- teaching-profile:capstone -->
<!-- teaching-note:end -->
