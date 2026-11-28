"""
Multivariate Regression

Predict delivery minutes and fuel use for each new delivery.

Run: python lesson.py
Enter another distance and weight. Read the separate columns for estimated minutes and fuel litres.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
deliveries = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
train, hold = deliveries.iloc[:4], deliveries.iloc[4:]
# 3. Teach the model from the training inputs and delivery time in minutes.
simple = LinearRegression().fit(train[["distance_km"]], train["delivery_minutes"])
print("Simple predictions:", simple.predict(hold[["distance_km"]]).round(1).tolist())
features = ["distance_km", "weight_kg"]
multiple = LinearRegression().fit(train[features], train["delivery_minutes"])
print(
    "Multiple-predictor predictions:",
    multiple.predict(hold[features]).round(1).tolist(),
)
two_targets = train[["delivery_minutes"]].assign(
    fuel_litres=0.15 * train["distance_km"] + 0.05 * train["weight_kg"]
)
model = LinearRegression().fit(train[features], two_targets)
print("Two outcomes per row:", model.predict(hold[features]).round(2).tolist())


# 4. Apply the fitted model to the new CSV rows and print a result for each row.
rows = pd.read_csv(new_path)
predictions = model.predict(rows[features]).round(2)
rows[["predicted_minutes", "predicted_fuel_litres"]] = predictions
print(rows.to_string(index=False))
