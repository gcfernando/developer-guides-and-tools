# Practice before looking at the answer

[Learning path](LEARNING-PATH.md) · [Word list](GLOSSARY.md)

Use paper first. Then use Python if you chose that route. Say why you chose an answer. If you guessed, read the short answer and try a similar question tomorrow.

## 1. A prediction

Old trips follow `minutes = 10 + 2 × distance`. Guess the time for 5 km. Which part is the input? Do you need the actual time to make a new guess?

<details><summary>Answer and reason</summary>

20 minutes. Distance is the input. You do not need the new trip's actual time to predict. You need it later to measure the error. This is a made-up exact rule; real trips vary.

</details>

## 2. A useful project

A store always gives free delivery for orders over 50 currency units. Must it train a model to decide who gets free delivery? What if it wants to guess a delivery time instead?

<details><summary>Answer and reason</summary>

The free-delivery rule is already known. A normal rule is enough. Delivery time is less certain and may need a learned pattern, if enough useful examples exist. Decide whether the result helps a real decision before building a model.

</details>

## 3. A fair check

You will use the model next month. Would you check it on random past rows or on later dates? A customer has many orders. If you need to handle completely new customers, may that customer's orders be in both training and test?

<details><summary>Answer and reason</summary>

Use later dates for the future-use question. For completely new customers, keep each customer's orders together. Two independent orders can have equal distance and weight; that alone does not make them the same order. Check identity and source, not only equal numbers.

</details>

## 4. Find and fix data problems

You see `weight = 10`, `unit = lb`. The model expects kg. Another row has a blank weight. A third has 90 kg. Which is a known conversion? Which needs a learned fill value? Which needs a source check?

<details><summary>Answer and reason</summary>

Convert 10 lb with the fixed pounds-to-kilograms rule: about 4.54 kg. A blank may use a fill value learned from training, if that is suitable for the task. The 90 kg value needs a source check before changing it. A large value can be valid. Zero and missing are different.

</details>

## Review after module 4

Close your notes. Write a project question, name its input and answer, choose its fair check, and name one possible data problem. Ask a friend to read your explanation. They should not need to know Python to understand it.

## 5. Prepare a new row

Training weights are 1, 2, 4, 5 and 8 kg. A new request has no weight. What is the middle training weight? Should you add the request to training before finding that value? Why might missingness itself matter?

<details><summary>Answer and reason</summary>

The middle value, or median, is 4 kg. Use the value learned from training. Do not refit the fill rule on each request. Missing weights may come from one broken scale or one kind of order, so investigate the pattern. A fill is a useful guess, not a recovered measurement.

</details>

For a category, make columns such as North and South. North becomes `1, 0`. South becomes `0, 1`. A new name is not automatically a known zone. Decide whether to reject it, ask for help, or use a tested fallback.

## 6. A simple baseline

A **baseline** is a simple rule used for comparison. Training times are 12, 14, 16, 20 and 22 minutes. The middle is 16. Guess 16 for every validation trip.

| Actual validation time | Baseline guess | Size of mistake |
| --- | --- | --- |
| 18 | 16 | 2 |
| 24 | 16 | 8 |

The average mistake is `(2 + 8) ÷ 2 = 5` minutes. This is **mean absolute error**, or **MAE**. Absolute means ignore the sign when measuring the size.

**Your task:** A trained model guesses 19 and 22 for those same trips. What is its MAE? Which result is better on these two rows? Can two rows prove it is better for everyone?

<details><summary>Answer and reason</summary>

The mistake sizes are 1 and 2 minutes. MAE is 1.5 minutes. That is better on these rows. Two rows are too few to make a strong general claim. Use more separate rows that match the future job.

</details>

Now make your own three-row table. Leave the mistake column blank. Fill it by hand. Then use the train-and-test lesson to compare a baseline and a model in code.

## 7. Spot memorizing

Model A has training MAE 0 and validation MAE 9. Model B has training MAE 3 and validation MAE 4. Which would you choose before the final test? What is the model-setting name in the tree-depth lesson?

<details><summary>Answer and reason</summary>

Choose B on this validation evidence. A may have memorized training details. That is called overfitting. Tree depth is a setting that controls how many levels of decisions a tree can make. Do not choose using the final test answers.

</details>

## 8. Read errors and uncertainty

### A setting is a choice, not a magic number

Ridge is a straight-line model with a penalty on large learned weights. Its `alpha` setting controls that penalty. Imagine comparing three fits on the same training and validation rows:

| Fit | What changes | What to check |
| --- | --- | --- |
| No penalty | Weights are free to fit the training pattern. | Does the rule make large mistakes elsewhere? |
| Small penalty | Weights are pulled towards zero a little. | Does validation error improve? |
| Large penalty | Weights are pulled towards zero more. | Has the model become too simple? |

These rows explain choices, not measured results. Run the Ridge lesson to see its prediction scores. To inspect learned input weights in lesson 362, add `print(model.coef_)` just after its `model.fit` line. These are training weights, not validation scores. Scale affects a penalty: expressing distance in metres gives a different coefficient from kilometres. Keep units clear and compare preparation choices within validation. Do not change units merely to get a smaller-looking weight.

### Read the size and direction of a mistake

Actual time is 30 minutes. The prediction is 24. The **residual**, or signed error, is `actual − prediction = 6`. It is positive because the model guessed too little.

Compare two lists of mistake sizes:

| Case | Mistake sizes | MAE |
| --- | --- | --- |
| A | 2, 2, 2, 2, 2 | 2 |
| B | 0, 0, 0, 0, 10 | 2 |

**Your task:** Why might a business prefer A, even though the averages match?

<details><summary>Answer and reason</summary>

B has one large miss. That might break a promise to a customer. Read the average, number of cases, largest mistakes and the share within an agreed limit. RMSE is another score that gives large mistakes more weight. For errors 2 and 4, it is the square root of `(4 + 16) ÷ 2`, about 3.16 minutes. MAE for those two is 3 minutes.

</details>

To see small-sample uncertainty, suppose the first two mistake sizes are 1 and 1. Their average is 1. Add a third mistake of 10. The average becomes 4. A few rows can change a score a lot. This arithmetic illustrates uncertainty; it is not a confidence interval.

For a larger exercise, split validation rows into several groups and print each group's size and MAE. Do not use this to keep changing your final test. Repeated model choices need validation, and a final report needs a fresh check.

## Review after module 8

Without notes, calculate a median, an absolute error and an MAE. Explain why the best training score can lose on new rows. Then inspect one delivery group in lesson 446. Report its number of orders next to its error.

## 9. Count category mistakes

There are 10 urgent orders. A model raises 8 alerts. Six alerts are truly urgent. Answer these questions:

1. How many alerts are false alarms?
2. How many urgent orders were missed?
3. What share of alerts was right? This is **precision**.
4. What share of real urgent orders was found? This is **recall**.

<details><summary>Answers and reasons</summary>

Two false alarms: `8 − 6`. Four missed urgent orders: `10 − 6`. Precision is `6 ÷ 8 = 75%`. Recall is `6 ÷ 10 = 60%`. The denominators answer different questions. Write the counts before the ratios.

</details>

A **cutoff** turns a model score into an alert. Lowering it usually raises more alerts. The model's scores have not changed; the decision rule has changed. A score of 0.7 is not a promise. Calibration asks whether groups with a stated chance have outcomes at about that rate.

## 10. Explain without claiming a cause

A model uses umbrella sales to predict rainy days. Does selling more umbrellas cause rain? If shuffling a column makes the model worse, what have you learned?

<details><summary>Answer and reason</summary>

Sales do not establish a cause of rain. They can be a clue associated with weather. Shuffling shows that the fitted model relied on that column in this check. It does not prove changing that fact will change the outcome.

</details>

## 11. Save and request

You trained and saved a model. You change a new request from 4 km to 8 km. Must you train again? Should a −4 km request receive a normal estimate?

<details><summary>Answer and reason</summary>

No retraining is needed for a new request. Reuse the saved preparation and model. A negative delivery distance is invalid and should get a clear error. An unfamiliar but possible long distance needs a stated service policy too; possible does not mean tested.

</details>

## 12. Respond to an alert

Later errors rise in the West zone. Write three actions before replacing the model.

<details><summary>One useful answer</summary>

Check the measurements and labels. Ask whether routes or recording rules changed. Inspect West examples and their count. Use a safe fallback if predictions can cause harm. Train a candidate only after deciding what changed, and compare it on a separate later batch. Record who makes the decision.

</details>

## Review after module 12

A support team can review only 20 alerts a day. A new cutoff would raise 100. Explain why recall alone cannot choose the cutoff. Write a short note for a manager: result, evidence, limits and next action. Then continue to the guided and independent projects.

## 13. Finish a partly completed encoding task

Training has zone names North and South. The saved encoder uses columns `[North, South]`. Complete the blank entries before viewing the reason.

| Request | North | South | What needs a decision? |
| --- | --- | --- | --- |
| South | ? | ? | A known category |
| North | ? | ? | A known category |
| East | ? | ? | An unfamiliar name |

<details>
<summary>Hint</summary>

Each known name activates its own column. Do not invent a new input column only at prediction time. The unfamiliar-name behavior must be specified separately.

</details>

<details>
<summary>Answer and reason</summary>

South is `0, 1`; North is `1, 0`. Under the lesson's `handle_unknown="ignore"` policy, East is `0, 0`. Other policies can reject or explicitly represent unknowns. Zero indicators do not establish how the model should behave for East. Keep the fitted schema and evaluate the chosen service policy.

</details>

## 14. Choose the method in an unfamiliar case

A library records book format as paperback, hardback or audio. Another field is reservation priority low, medium or high. One recorded loan lasted 800 days. A reader's final return date is unknown when predicting the loan duration.

Write an input-preparation plan. Explain the representation for each category field, what to investigate about the long loan, which information is unavailable at prediction time, and a fair way to check later loans. Do not start by choosing a complex algorithm.

<details>
<summary>One reasoned plan</summary>

Book format has no inherent numeric ranking; a fixed one-hot representation is a suitable candidate. Priority has a stated order, but integer gaps impose an additional assumption for some models. Investigate the 800-day source record and library rules before keeping, correcting or flagging it. The future return date is unavailable as an input for duration prediction. Learn preparation on earlier training loans, choose using validation and check separate later completed loans against a simple baseline. State who is missing from the records and which outcomes are still pending.

</details>

Try this case again after a few days without the answer. Then try the independent Wine project. Recognition of a familiar delivery number is easier than applying the rule to a new setting; record both separately.
