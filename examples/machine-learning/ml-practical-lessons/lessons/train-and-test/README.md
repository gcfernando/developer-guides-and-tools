# 🚚 Train, save, and test a delivery model

## Learn and apply the saved-model workflow

**Why and when.** Saving keeps the training preparation and selected model available for later inputs. Use it when repeated requests should apply one fitted rule rather than retrain for each customer.

**Ready check.** Explain why an unknown measured time must not be filled with the model's own guess and then counted as a correct test answer.

**Worked flow.** The first script fits from training rows, compares with a median baseline on validation and checks the chosen procedure on separate test rows. Its saved artifact contains the fitted preparation. The second script reads distance_km, weight_kg and zone from a new CSV and predicts minutes. A supplied actual_minutes is used only to score a genuinely completed trip.

**Code to inspect.** In `train_delivery_model.py`, find the three `split` filters and the validation comparison. In `test_delivery_model.py`, find the artifact load and `predict` call. Neither a new request nor an empty actual_minutes field should refit the training median.

**Mistakes to avoid.** Do not fit a new scaler, category list or fill value on the request CSV. Do not load an untrusted Joblib file. A physically possible long route can still exceed the model's checked evidence; this small example is not a production service policy.

**Apply it.** Change a request distance but leave its old measured time unchanged. Why would a printed error then be misleading? Clear the old answer before running.

<details>
<summary>Answer and reason</summary>

The old measured time described the original completed trip, not the invented request. A prediction needs inputs only. Its error can be measured only after a real outcome for that same case is recorded. Reuse the saved fit without pretending a request edit creates new ground truth.

</details>

Read the main learning path before this exercise. You need to know training, validation and test rows, missing values and category inputs. Keep the same active course environment for every command.

**In simple words:** training learns and saves a rule. Prediction opens that saved rule and uses it for a new request. Changing a request does not require learning again.

**Guess first:** If a new weight is blank, should the fill rule use the training weights or learn from that new request? Write your answer first. It should reuse the training rule.

Follow the steps below one at a time. Save a changed CSV before rerunning. Clear an old measured time when you invent a new request. If you get stuck, compare with a fresh copy and use the main Setup guide.


In this extracted folder, run `python -m pip install -r requirements.txt` once.

1. Run `python train_delivery_model.py`. It reads [training_deliveries.csv](training_deliveries.csv), chooses a model using the validation rows, checks it using the test rows, and saves `delivery_model.joblib`.
2. Open [new_deliveries.csv](new_deliveries.csv). Add a short route, a long route, or a route with a blank weight. Use kilometers and kilograms. A blank `actual_minutes` is fine if the delivery hasn't happened yet.
3. Run `python test_delivery_model.py`. It loads the saved model and prints a table. If you enter measured delivery times it also prints their errors.
4. Try another set of deliveries by editing only `new_deliveries.csv` and running the test script again.

| distance_km | weight_kg | zone | actual_minutes |
| --- | --- | --- | --- |
| 5 | 2 | North | 23 |
| 8 | 3 | South | 34 |
| 11 |  | North | 36 |
| 6 | 1 | West |  |

## ✅ Expected result

After training, look for the saved model filename. When you run the test script, look for one prediction per row in new_deliveries.csv and errors only where a measured time exists.

## 🧪 Try one change

For the first row (the 5 km route), clear `weight_kg` and `actual_minutes`, save the CSV, and rerun only the test script. The saved training rule fills the missing weight and returns an estimate. The changed request has no measured answer, so its error stays blank. Check that the printed average uses only rows with measured times. The supplied 11 km row already has a blank weight; leaving that row alone would not test a change.

## 📊 Read the visual

![Train and save. Run the training script on completed deliveries. → Change the request. Enter a different distance, weight or zone in the new CSV. → Run only the test. Load the saved model and read its estimates.](train-save-test-steps.png)

**👀 Read the visual.** The saved model keeps the rules learned from the training CSV.

**👉 What to do.** After the first run, change **new_deliveries.csv** and rerun only the test script.
