# Build a model for a new table

[Learning path](LEARNING-PATH.md) · [Project choices](PROJECT-CHOICES.md)

Finish the guided delivery project first. This task checks whether you can use the ideas on a different table. There is no complete model script to copy.

## Your question

Can chemical measurements help predict one of three wine types in a small historical dataset?

This is a real teaching benchmark, not the invented drink table in the workbook. It has 178 rows and 13 measured inputs. You do not need to taste or handle wine. The task is about numbers in a table.

The source is [UCI Wine](https://archive.ics.uci.edu/dataset/109/wine), by Stefan Aeberhard and M. Forina. This copy comes from scikit-learn. The files include attribution and the data licence. Source units are not supplied for every field, so do not invent them.

## 1. Open the files

Open `projects/wine`. Its README explains the files. With the active course environment, run:

```bash
python starter.py
```

It prints row counts and field names. It does not train a model for you.

## 2. Write a brief

Use the questions in Project choices. State the target, possible inputs and a simple baseline. The three target values are names, not a low-to-high ranking. Do not use row ID as an input.

Explain a limit: this historical sample does not establish performance on all wines, new countries or a future instrument. The file split is for a classroom comparison of similar recorded samples. It does not test future dates or unseen producers.

## 3. Inspect and plan

1. Read `data_dictionary.csv`.
2. Inspect missing values and numeric ranges in `training.csv`.
3. Choose a simple baseline and one candidate model.
4. Decide whether the candidate needs scaling.
5. Write which values will be learned from training only.

## 4. Fill in the missing work

Before writing the whole procedure, complete these smaller decisions. They give structure without supplying a model solution:

1. From training only, count examples per wine type. Write what an always-most-common-type baseline would predict.
2. Write the input-column list without row_id or wine_type. Explain which operation learns any scale or fill value.
3. Sketch a two-row result table: baseline and candidate, with the same validation metric and counts.
4. Write one reason to keep the baseline even if a candidate has an impressive training score.

<details>
<summary>Check the decisions, then close this hint</summary>

The most common training type defines the constant baseline; it does not come from test answers. Preparation fits on training inputs. Both procedures receive the same validation cases and metric. Training performance alone can reward memorization; a usable candidate needs separate evidence and practical justification. The supplied starter intentionally stops before model fitting: this part is your independent exercise, not a complete implementation to copy.

</details>

Copy `starter.py` to `my_model.py`. Keep your own notes. Add the steps yourself:

- Read training inputs and their targets.
- Train a baseline and your candidate.
- Compare them on `validation.csv` with the same metric.
- Inspect counts and mistakes for each target type.
- Choose one model. Save your choice and reason before using the final check.

Use the glossary, earlier small lessons or a hint from a teacher if needed. Do not open the instructor answer file to choose a model.

## 5. Make final predictions

Read `test_inputs.csv`. Save one guess per row to `predictions.csv`, with exactly these two columns:

```text
row_id,predicted_type
```

Keep each row ID exactly once. `predicted_type` must be 0, 1 or 2. Then run:

```bash
python instructor/check_predictions.py predictions.csv
```

The checker reads the separate answer file and prints the final counts and score. Do not use that score to keep changing your model. If you do, this test becomes part of choosing, and a new independent evaluation is needed.

## 6. Explain and hand over

Write a small model card. Include the data source, choice, baseline, validation comparison, final count table, mistakes and limits. Give your script and notes to another learner. They should be able to run it and explain why the model might fail elsewhere.

Use the five-area rubric in [Teaching](TEACHING.md#score-an-independent-project). The goal is a reasoned, repeatable result. A high score alone is not a pass if the model used the final answers while choosing.

## Ideas route

You can still complete the brief, identify the target and inputs, explain the split, calculate an accuracy from a teacher-supplied count table, and write the limitations. State that you assessed the project rather than built the Python model.
