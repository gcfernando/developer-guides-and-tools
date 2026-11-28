"""
Tableau

Turn batch counts into a CSV that Tableau can plot.

Run: python lesson.py
Try changing Batch from Morning to Afternoon in sample.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the labeled batches so you can compare the model’s results over time.
history = pd.read_csv(input_path)
if (history["Checked"] <= 0).any() or (history["Correct"] > history["Checked"]).any():
    raise ValueError("Checked must be positive and at least as large as Correct.")


history["Accuracy"] = (history["Correct"] / history["Checked"]).round(3)


history.to_csv("dashboard_import.csv", index=False)
# 2. Print the result next to the input values so you can compare them.
print(history.to_string(index=False))
print("In Tableau, open dashboard_import.csv, then chart Accuracy by Batch.")
print("Edit the sample, rerun Python, then refresh the imported file.")
