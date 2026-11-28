# A new table to try yourself

**Why this project is different.** Earlier lessons supply complete runnable demonstrations. Here `starter.py` is a complete file-inspection script, while your fitting work is deliberately unfinished practice. The task is to choose and explain the missing workflow yourself. Do not mistake an inspection-only script for a trained classifier.

**Trace the contract.** Training and validation include inputs and wine_type answers; test_inputs has only inputs and row_id. Your prediction file supplies one predicted_type per row ID. The checker compares it with separately held answers. A successful format check establishes coverage and valid codes; accuracy still needs interpretation and limits.

**New-case check.** If an ID sorts between two training IDs, should that ID become a useful chemical measurement? No: it is a row name. Use the 13 recorded measurement fields and preserve the ID only for matching predictions back to cases.

These files support the independent project in the main course folder.

- `training.csv`: rows and known answers for learning.
- `validation.csv`: separate rows and known answers for choosing.
- `test_inputs.csv`: final rows without answers.
- `data_dictionary.csv`: meanings of the fields.
- `starter.py`: reads the files and shows their sizes. Add your own model steps in a copy.
- `instructor/test_answers.csv`: final answers. Do not use them while choosing.
- `instructor/check_predictions.py`: checks your final prediction file.
- `SOURCE.md`: where the data came from, how this copy was changed and its licence.

Open a terminal here after activating the course environment. Run `python starter.py`. Follow `INDEPENDENT-PROJECT.html` in the main course folder for the task.
