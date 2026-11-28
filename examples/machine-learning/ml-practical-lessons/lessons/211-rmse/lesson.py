"""
RMSE

Use RMSE to give bigger errors more weight.

Run: python lesson.py
Edit the input values in new_inputs.csv and compare the displayed predictions.
"""

from pathlib import Path
import pandas as pd

print(
    "Worked calculation: two test deliveries. Use lesson 446 for a larger evaluation."
)
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
deliveries = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
train, test = deliveries.iloc[:4], deliveries.iloc[4:]
features = ["distance_km", "weight_kg"]
# 3. Teach the model from the training inputs and delivery time in minutes.
model = LinearRegression().fit(train[features], train["delivery_minutes"])
actual = test["delivery_minutes"]
predicted = model.predict(test[features])


error_rows = pd.DataFrame(
    {
        "Actual (min)": actual.to_numpy(),
        "Prediction (min)": predicted,
        "Actual minus prediction (min)": actual.to_numpy() - predicted,
    }
).round(1)
print("Typical error in minutes, with extra weight on large misses.")
print(round(root_mean_squared_error(actual, predicted), 3))


# 4. Apply the fitted model to the new CSV rows and print a result for each row.
rows = pd.read_csv(new_path)
predictions = model.predict(rows[features]).round(2)
print(rows.assign(prediction=list(predictions)).to_string(index=False))
