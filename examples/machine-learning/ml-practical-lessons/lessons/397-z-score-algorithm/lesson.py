"""
Z-score Algorithm

Check how many standard deviations a parcel weight lies from the training average.

Run: python lesson.py
Edit the rows in new_inputs.csv. Compare a typical case with an unusually heavy parcel. A flag means check the original record.
"""

from pathlib import Path
import numpy as np
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including weight_kg.
training = pd.read_csv(input_path)["weight_kg"].to_numpy()


# 2. Read the new CSV rows, then apply the rules from the sample.
new = pd.read_csv(new_path)["weight_kg"].to_numpy()
# 3. Measure each new weight in training standard deviations from the mean.
spread = training.std(ddof=0)
if not np.isfinite(spread) or spread == 0:
    raise SystemExit("Z-scores need valid training weights with a nonzero spread.")
z = (new - training.mean()) / spread
print("Z-scores:", z.round(2).tolist())
print("Flagged:", (abs(z) > 3).tolist())
