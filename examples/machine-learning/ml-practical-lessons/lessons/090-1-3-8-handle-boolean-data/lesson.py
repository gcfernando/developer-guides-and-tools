"""
1.3.8 Handle Boolean Data

Make mixed yes/no entries consistent before a model uses them.

Run: python lesson.py
Change signed_up in sample.csv, for example from Yes to true. Compare the printed rows.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including signed_up.
data = pd.read_csv(input_path)
# 2. Give different spellings of the same value one consistent form.
mapping = {"yes": 1, "true": 1, "1": 1, "no": 0, "false": 0, "0": 0}
data["flag"] = data["signed_up"].str.strip().str.lower().map(mapping)
print(data.to_string(index=False))
