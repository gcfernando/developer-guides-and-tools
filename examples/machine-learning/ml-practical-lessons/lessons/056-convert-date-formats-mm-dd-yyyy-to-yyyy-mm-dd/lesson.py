"""
Convert date formats (MM/DD/YYYY to YYYY-MM-DD)

Read US-style and ISO dates and convert both to YYYY-MM-DD.

Run: python lesson.py
Try changing ship_date from 01/07/2025 to 2025-01-10 in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including ship_date, weight, unit.
data = pd.read_csv(input_path)


# 2. Put the date, unit, and zone rules in one place so fresh rows go through the same cleanup.
def clean(frame):
    us_dates = pd.to_datetime(frame["ship_date"], format="%m/%d/%Y", errors="coerce")
    iso_dates = pd.to_datetime(frame["ship_date"], format="%Y-%m-%d", errors="coerce")
    dates = us_dates.fillna(iso_dates)
    units = frame["unit"].str.strip().str.lower()
    kilograms = frame["weight"] * units.map(
        {"kg": 1, "lb": 0.45359237, "lbs": 0.45359237}
    )
    zone = frame["zone"].str.strip().str.lower()
    if (
        dates.isna().any()
        or kilograms.isna().any()
        or not zone.isin(["north", "south"]).all()
    ):
        raise ValueError("Check for an unreadable date, weight, unit, or zone.")
    return pd.DataFrame(
        {
            "date": dates.dt.strftime("%Y-%m-%d"),
            "weight_kg": kilograms,
            "zone": zone,
            "weekday": dates.dt.dayofweek,
            "is_south": zone.eq("south").astype(int),
        }
    )


cleaned = clean(data)
before_after = pd.DataFrame(
    {
        "Original date": data["ship_date"],
        "Standard date": cleaned["date"],
        "Original weight": data["weight"].astype(str) + " " + data["unit"],
        "Weight (kg)": cleaned["weight_kg"].round(2),
        "Original zone": data["zone"].str.strip(),
        "Standard zone": cleaned["zone"],
        "South flag": cleaned["is_south"],
    }
)


inputs = ["weight_kg", "weekday", "is_south"]
# 3. Set aside the check rows before the model learns.
training = cleaned.iloc[:4]
# 4. Teach the model from the training inputs and delivery time in minutes.
model = LinearRegression().fit(training[inputs], data.iloc[:4]["minutes"])
last_shipment = clean(data.iloc[4:])[inputs]
predicted = model.predict(last_shipment)[0]
results = pd.DataFrame(
    {
        "Shipment": ["Check row 5"],
        "Actual time (min)": [data.iloc[4]["minutes"]],
        "Predicted time (min)": [round(predicted, 1)],
    }
)
print(before_after.to_string(index=False))
print(results.to_string(index=False))


# 5. Apply the fitted model to the new CSV rows and print a result for each row.
rows = pd.read_csv(new_path)
changed = clean(rows)
changed["predicted_minutes"] = model.predict(changed[inputs]).round(2)
print(changed.to_string(index=False))
