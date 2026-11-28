"""
Handle Near-Duplicates

Compare near-identical names and use the order ID before combining records.

Run: python lesson.py
Try changing order_id from A to B in sample.csv. Compare the new output.
"""

from pathlib import Path
from difflib import SequenceMatcher
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including order_id, name, minutes.
data = pd.read_csv(input_path)


# 2. Give different spellings of the same value one consistent form.
data["name_key"] = data["name"].str.lower().str.split().str.join(" ")
score = SequenceMatcher(None, data.loc[0, "name_key"], data.loc[2, "name_key"]).ratio()
print("Similar names:", round(score, 2))
confirmed = data.drop_duplicates(subset=["order_id", "name_key", "minutes"])
print("Confirmed distinct orders:", confirmed["order_id"].tolist())
