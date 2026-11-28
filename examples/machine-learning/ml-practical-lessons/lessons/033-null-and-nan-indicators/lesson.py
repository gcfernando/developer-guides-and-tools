"""
Null and NaN indicators

Use pandas to count blank cells and question marks as missing.

Run: python lesson.py
Enter a blank cell and a question mark in sample.csv. Check that both appear in the missing count.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
data = pd.read_csv(input_path, na_values=["?"])


# 2. Find blanks in the rows you are about to use.
missing = data.isna()
counts = missing.sum().rename("Missing cells").rename_axis("Column").reset_index()
print(counts.to_string(index=False))
print("\nRows to review")
print(
    data.loc[missing.any(axis=1), ["distance_km", "weight_kg", "zone"]].to_string(
        index=False
    )
)
