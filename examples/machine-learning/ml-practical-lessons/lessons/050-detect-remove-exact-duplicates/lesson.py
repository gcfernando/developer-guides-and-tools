"""
Detect & Remove Exact Duplicates

Keep one copy of each exact row before training on distance and time.

Run: python lesson.py
Edit the input values in new_inputs.csv and compare the displayed predictions.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including order_id, km, minutes.
data = pd.read_csv(input_path)


# 2. Print the result next to the input values so you can compare them.
print("Repeated rows:", data.duplicated().sum())
# 3. Apply the confirmed correction before teaching the model.
data = data.drop_duplicates(keep="first")
assert data["order_id"].is_unique
# 4. Set aside the check rows before the model learns.
train, test = data.iloc[:-1], data.iloc[-1:]
# 5. Teach the model from the training inputs and delivery time in minutes.
model = LinearRegression().fit(train[["km"]], train["minutes"])
print("D prediction:", model.predict(test[["km"]]).round(1).tolist())


# 6. Apply the fitted model to the new CSV rows and print a result for each row.
rows = pd.read_csv(new_path)
predictions = model.predict(rows[["km"]]).round(2)
print(rows.assign(prediction=list(predictions)).to_string(index=False))
