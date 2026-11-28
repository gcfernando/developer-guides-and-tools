"""
Identify missing values

Find which weights or delivery zones are missing and read the affected rows.

Run: python lesson.py
Leave one weight_kg cell blank or put ? in zone in sample.csv. See which column’s count changes.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV. Treat a question mark like a blank cell.
data = pd.read_csv(input_path, na_values=["?"])


# 2. Count missing values by column. Then print the rows you need to review.
missing = data.isna()
counts = missing.sum().rename("Missing cells").rename_axis("Column").reset_index()
print(counts.to_string(index=False))
print("\nRows to review")
print(
    data.loc[missing.any(axis=1), ["distance_km", "weight_kg", "zone"]].to_string(
        index=False
    )
)
