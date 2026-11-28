# A new table to try yourself

**Why this project is different.** Earlier lessons supply complete runnable demonstrations. Here `starter.py` is a complete file-inspection script, while your fitting work is deliberately unfinished practice. The task is to choose and explain the missing workflow yourself. Do not mistake an inspection-only script for a trained classifier.

**Trace the contract.** Training and validation include inputs and wine_type answers; test_inputs has only inputs and row_id. Your prediction file supplies one predicted_type per row ID. The checker compares it with separately held answers. A successful format check establishes coverage and valid codes; accuracy still needs interpretation and limits.

**New-case check.** If an ID sorts between two training IDs, should that ID become a useful chemical measurement? No: it is a row name. Use the 13 recorded measurement fields and preserve the ID only for matching predictions back to cases.

These files support the [independent project assignment](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/INDEPENDENT-PROJECT.html) in the main course folder. Return to the [course overview](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/README.html) for setup and the guided lessons.

- [training.csv](training.csv): rows and known answers for learning.
- [validation.csv](validation.csv): separate rows and known answers for choosing.
- [test_inputs.csv](test_inputs.csv): final rows without answers.
- [data_dictionary.csv](data_dictionary.csv): meanings of the fields.
- [starter.py](starter.py): reads the files and shows their sizes. Add your own model steps in a copy.
- `instructor/test_answers.csv`: final answers. Do not use them while choosing.
- [instructor/check_predictions.py](instructor/check_predictions.py): checks your final prediction file.
- [Data source and licence](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/projects/wine/SOURCE.html): where the data came from, how this copy was changed and its licence. The [Markdown source](https://github.com/gcfernando/developer-guides-and-tools/blob/main/examples/machine-learning/ml-practical-lessons/projects/wine/SOURCE.md) is also available.

Open a terminal here after activating the course environment. Run `python starter.py`. Follow the [independent project assignment](https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/INDEPENDENT-PROJECT.html) for the task. The links above let you inspect individual files; use the complete local course folder to run the project.
