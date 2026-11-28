"""
Year

Pull the year out of each order date.

Run: python lesson.py
Try 2025-02-05 09:00 and 2026-01-12 08:30 in new_inputs.csv. Keep the YYYY-MM-DD HH:MM format.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the timestamp and recorded order count for each row.
data = pd.read_csv(input_path)


# 2. Read each timestamp once and pull out the parts the model can use.
def date_features(values):
    dt = pd.to_datetime(values, format="%Y-%m-%d %H:%M", errors="raise").dt
    return pd.DataFrame(
        {
            "Year": dt.year,
            "Month": dt.month,
            "Day": dt.day,
            "Weekday": dt.dayofweek,
            "Hour": dt.hour,
        }
    )


features = date_features(data["timestamp"])
print(features.to_string(index=False))
use = ["Year"]
# 3. Teach the model from the training inputs and the recorded order count.
model = LinearRegression().fit(features[use], data["orders"])

# 4. Apply the fitted model to the new CSV rows and print a result for each row.
fresh_dates = pd.read_csv(new_path)
fresh_features = date_features(fresh_dates["timestamp"])
fresh_dates[use] = fresh_features[use]
fresh_dates["estimated_orders"] = model.predict(fresh_features[use]).round(1)
print(fresh_dates.to_string(index=False))
