"""
Scheduled model checks

Reuse the same model check for each batch and see which one raises an alert.

Run: python lesson.py
Try changing distance from 1 to 3 in sample.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the labeled batches so you can compare the model’s results over time.
batches = pd.read_csv(input_path)


def batch(name):
    return batches[batches["batch"] == name]


history = batch("History")
current = LinearRegression().fit(history[["distance"]], history["minutes"])


def check_batch(day, records):
    # Counting from the start of the table sets aside the same rows every run.
    training = records.iloc[:4]
    checking = records.iloc[4:]
    candidate = LinearRegression().fit(training[["distance"]], training["minutes"])
    actual = checking["minutes"]
    old_error = mean_absolute_error(actual, current.predict(checking[["distance"]]))
    new_error = mean_absolute_error(actual, candidate.predict(checking[["distance"]]))
    decision = "Review candidate" if new_error < old_error else "Keep current model"
    return [day, round(old_error, 1), round(new_error, 1), decision]


results = pd.DataFrame(
    [check_batch("Monday", batch("Monday")), check_batch("Tuesday", batch("Tuesday"))],
    columns=["Check", "Current error (min)", "Candidate error (min)", "Decision"],
)
results.to_csv(Path("scheduled_checks.csv"), index=False)
# 2. Print the result next to the input values so you can compare them.
print(results.to_string(index=False))
