"""
One-Class SVM

Learn a boundary around typical parcels and check which new ones fall outside.

Run: python lesson.py
Edit the rows in new_inputs.csv. Compare a typical case with an unusually heavy parcel. A flag means check the original record.
"""

from pathlib import Path
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including minutes, kg.
regular = pd.read_csv(input_path)[["minutes", "kg"]].to_numpy()


# 2. Read the new CSV rows, then apply the rules from the sample.
new = pd.read_csv(new_path)[["minutes", "kg"]].to_numpy()
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model = make_pipeline(StandardScaler(), OneClassSVM(nu=0.15)).fit(regular)
print("Example training shipments:", regular[:3].round(2).tolist())
print("Typical / unusually large:", model.predict(new).tolist())
