"""
Fix typos and spelling variations

Map known spelling variants to a single category before encoding it.

Run: python lesson.py
Try changing record_id from 1 to 3 in sample.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including record_id, category.
data = pd.read_csv(input_path)


# 2. Give different spellings of the same value one consistent form.
spelling = {"male": "Male", "m": "Male", "female": "Female", "f": "Female"}
data["standard"] = data["category"].str.strip().str.casefold().map(spelling)
assert data["standard"].notna().all()
# An unfamiliar category can still pass through the encoder.
encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
encoder.fit(data.iloc[:3][["standard"]])
print(data[["category", "standard"]].to_string(index=False))
print("Held-out encoded row:", encoder.transform(data.iloc[3:][["standard"]]).tolist())
