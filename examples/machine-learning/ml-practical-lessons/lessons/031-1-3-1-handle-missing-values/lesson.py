"""
1.3.1 Handle Missing Values

Count missing entries and locate the delivery rows you need to review.

Run: python lesson.py
Try changing distance_km from 2 to 6 in sample.csv. Compare the new output.
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
