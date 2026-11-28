"""
DBSCAN

Look for dense groups of shoppers and flag isolated points as noise.

Run: python lesson.py
Add or edit a row in sample.csv, then rerun to refit. This method works on the whole group of rows.
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including age, income, spending.
data = pd.read_csv(input_path)


# Scale the full table before re-fitting the example to all of these rows.
values = StandardScaler().fit_transform(data)
model = DBSCAN(eps=0.7, min_samples=2)
# 2. Fit the model on the prepared training rows. Keep it for the checks below.
group = model.fit_predict(values)
print("Labels:", group.tolist())
print(data.assign(group=group).groupby("group").mean().round(1).to_string())
