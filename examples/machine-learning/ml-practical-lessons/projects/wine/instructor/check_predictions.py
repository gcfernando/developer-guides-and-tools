"""Check a frozen prediction file once. Do not use this result to choose a model."""

from pathlib import Path
import sys

import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix


def check(path):
    guesses = pd.read_csv(path)
    expected = pd.read_csv(Path(__file__).resolve().with_name("test_answers.csv"))
    if set(guesses.columns) != {"row_id", "predicted_type"}:
        raise SystemExit("Use exactly row_id and predicted_type as column names.")
    if guesses["row_id"].isna().any() or not guesses["row_id"].is_unique:
        raise SystemExit("Keep each row ID exactly once. Do not leave an ID blank.")
    if set(guesses["row_id"]) != set(expected["row_id"]):
        raise SystemExit("Predict every test row exactly once, with no extra row IDs.")
    if not guesses["predicted_type"].isin([0, 1, 2]).all():
        raise SystemExit("Each predicted_type must be 0, 1 or 2.")
    checked = expected.merge(guesses, on="row_id", validate="one_to_one")
    truth, predicted = checked["wine_type"], checked["predicted_type"]
    counts = confusion_matrix(truth, predicted, labels=[0, 1, 2])
    print("Final test rows:", len(checked))
    print("Correct predictions:", int((truth == predicted).sum()))
    print(f"Accuracy: {accuracy_score(truth, predicted):.1%}")
    print("Rows are actual types. Columns are predicted types, in order 0, 1, 2.")
    print(pd.DataFrame(counts, index=[0, 1, 2], columns=[0, 1, 2]).to_string())
    print("Explain mistakes and limits. Do not use this final score for more model choices.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Run: python instructor/check_predictions.py predictions.csv")
    check(Path(sys.argv[1]))
