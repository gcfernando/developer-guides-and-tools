# Make useful project choices

[Learning path](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/LEARNING-PATH.html)

A working script is one part of a project. A useful project also needs a clear decision, suitable data and a person who will act on the result.

## 1. Fill in a project brief

Write one short answer for each row before building a model.

| Question | Your answer |
| --- | --- |
| Who needs help? | |
| What decision will they make? | |
| What answer do we want: a number, a known name, or a group? | |
| What facts will we know at that moment? | |
| When will the true answer become known? | |
| What do people do now? | |
| Would a fixed rule or report be enough? | |
| What is a simple baseline? | |
| What counts as a useful improvement? | |
| Who checks the result and owns the next action? | |

Keep fields that arrive after the decision out of prediction inputs. For example, call length is unknown before a call starts. A model choosing whom to call cannot use that call's final length.

## 2. Check where data came from

Data is a set of recorded facts. Clean-looking facts can still miss important people or cases.

1. Name the source and the date range.
2. Say what one row means. Is it one delivery, one customer or one measurement?
3. Check IDs. Two copies of the same shipment are different from two shipments with equal weights.
4. List who or what is missing. Do you have night deliveries? Rural routes? New customers?
5. Define each answer. Does “late” mean over 30 minutes or after a promised time? Use one rule.
6. Check a few labels with the source. If two people disagree, record the disagreement and agree on the rule.
7. Choose a test that matches the future job. A historical sample does not automatically represent a new place or later year.

## 3. Plan care for people and data

Use invented data in the first exercises. For a real project, ask the data owner:

- May we use these fields for this purpose?
- Which fields are actually needed?
- Who may open the data and saved model?
- How long should we keep each file? Who removes it when that time ends?
- Could a wrong answer harm someone? Which groups might get more mistakes?
- When must a person review a decision?
- Can an affected person ask for a correction?

Removing a contact column is a useful data-minimization example. It does not prove that a project meets GDPR, HIPAA or any other rule. Get the relevant requirements from the data owner and qualified support. The exercises named after those rules teach only one small sharing step.

## 4. Connect a score to a decision

Suppose one missed urgent order costs 20 units of staff time. One false alarm costs 2 units. A validation result has 4 misses and 10 false alarms.

`cost = 4 × 20 + 10 × 2 = 100 units`

These are practice costs, not prices from a real company. Choose your own agreed costs for a real project. Also check how many alerts the team can handle. A low-cost cutoff on paper may be unusable if no one can review the alerts.

Use validation rows to compare cutoffs. Write down your choice and reason before looking at final test results.

## 5. Read results honestly

Report the number of examples beside each score. Read several large mistakes. Compare groups that matter to the job. A group with three examples needs more evidence than one with three thousand.

Correlation means values move together. It does not show why. Feature importance shows what a fitted model used in a particular check. It does not show what will happen if you change that feature in the world.

## 6. Write a small model card

A **model card** is a readable note about a model. Fill in these fields:

| Field | What to record |
| --- | --- |
| Purpose | The decision this model supports. |
| Owner | The person who checks it and handles problems. |
| Inputs | Names, meanings, units and when they are known. |
| Data | Source, permission, date range and missing cases. |
| Split | How training, validation and test rows were kept apart. |
| Baseline | The simple rule and how it performed. |
| Result | Counts, errors, group checks and large mistakes. |
| Limits | Cases where the model should not be used. |
| Human review | When a person must decide. |
| Files | Script, data version, saved model and package versions. |
| Fallback | What to do when a request is invalid or the model is unavailable. |
| Next check | What is monitored, when and by whom. |

Give the files and this note to a classmate. Ask them to run the project and explain its limits. Record what was unclear.

## 7. Respond to worse later results

An alert means “investigate”. It does not prove the model needs retraining.

1. Keep the current model version and record the alert time.
2. Check whether fields, units or labels changed.
3. Inspect the affected cases and groups.
4. Decide whether to pause use or use the fallback. Name the person responsible.
5. If needed, gather new confirmed examples and train a candidate.
6. Compare the candidate and current model on the same separate later rows.
7. Record the decision to keep or replace the model. Keep a way to return to the previous version.

## 8. Know this course's scope

## Work through a brief before writing your own

A library wants to estimate loan duration at checkout. The decision is when to send a reminder. Available inputs include book format, loan type and the agreed due date. The future actual return date is the answer source, not an available predictor. A baseline might always use the middle duration among earlier completed training loans. Choose validation/check dates to match later use. Pending loans need a separate status; their unknown duration is not zero.

**Your task.** Draft the model-card fields for this case. Explain a privacy limit, an error measure, a fallback and the person who responds when later errors rise. Then propose a reason an ordinary due-date rule might be sufficient.

<details markdown="1">
<summary>One reasoned answer</summary>

Use only approved fields needed for the reminder decision; do not expose personal borrowing histories unnecessarily. Read absolute errors in days and inspect large misses and pending-loan coverage. Keep an ordinary due-date reminder as a possible fallback, with a named librarian reviewing data/label changes and results. If the decision is simply “send on the agreed date”, a fixed rule already expresses the policy and no learned estimate is needed. Each card field should connect to that decision rather than become paperwork without an action.

</details>

## What the current course covers

This course focuses on predicting numbers, known categories and groups from data. Generative AI creates content such as text or pictures. A pretrained model has already learned from other data. Retrieval finds information to use as context. These ideas can be combined, but they need their own evaluation. A good delivery prediction does not prove that a chatbot gives correct answers.
