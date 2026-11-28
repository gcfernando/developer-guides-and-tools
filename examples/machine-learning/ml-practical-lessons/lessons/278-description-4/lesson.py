"""
Description

Inspect the columns in the invented flower measurements and see what each row represents.

Run: python lesson.py
Add another original example in sample.csv. Rerun to check that its columns and row count make sense.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the example records from sample.csv. The table uses the dataset fields shown below.
records = pd.read_csv(input_path)
# 2. Print the result next to the input values so you can compare them.
print("PDF reference: UCI Iris Dataset")


fields = pd.DataFrame(
    {"Column": records.columns, "Type": records.dtypes.astype(str).to_numpy()}
)
print("Origin of this CSV: original synthetic practice rows")
print("Rows:", len(records))
print(fields.to_string(index=False))
print(records.head(3).to_string(index=False))
