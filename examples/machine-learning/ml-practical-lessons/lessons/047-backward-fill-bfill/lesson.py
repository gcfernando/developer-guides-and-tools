"""
Backward Fill (bfill)

Use the next recorded count to repair a gap in historical data.

Run: python lesson.py
Change the measured value after the gap. Watch that change flow one day backward in the historical table.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including day, requests.
data = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
train = data.iloc[:4].sort_values("day").copy()
train["forward"] = train["requests"].ffill()
train["backward"] = train["requests"].bfill()
print(train[["day", "requests", "forward", "backward"]].to_string(index=False))
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model = LinearRegression().fit(train[["day"]], train["backward"])
print("Day 5 forecast:", model.predict(data.iloc[4:][["day"]]).round(1).tolist())


# 4. Apply the fitted model to the new CSV rows and print a result for each row.
rows = pd.read_csv(new_path)
predictions = model.predict(rows[["day"]]).round(2)
print(rows.assign(prediction=list(predictions)).to_string(index=False))
