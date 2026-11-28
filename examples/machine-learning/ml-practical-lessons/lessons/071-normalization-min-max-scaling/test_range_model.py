"""Test new distances without retraining the model."""

from pathlib import Path

import joblib
import pandas as pd

folder = Path(__file__).resolve().parent
inputs = ["distance_km"]

# 1. Open the file you created by running train_range_model.py.
model_file = folder / "range_model.joblib"
if not model_file.is_file():
    raise SystemExit("Run python train_range_model.py first.")
# Load the file you trained here, or another artifact from a source you trust.
delivery_model = joblib.load(model_file)
scaler = delivery_model.named_steps["minmaxscaler"]

# 2. Read the distances someone entered. You can edit this CSV and rerun.
requests = pd.read_csv(folder / "range_requests.csv")
distance = pd.to_numeric(requests["distance_km"], errors="coerce")
valid = distance.notna() & distance.ge(0) & distance.lt(float("inf"))
lowest = scaler.data_min_[0]
highest = scaler.data_max_[0]
within_training_range = valid & distance.between(lowest, highest)
print(f"Training range: {lowest:g} to {highest:g} km")

# 3. Show what the scaler and the toy model do with all valid distances.
# 90 km is a valid distance and will scale above 1.
requests["scaled_distance"] = float("nan")
requests["demo_minutes"] = float("nan")
if valid.any():
    valid_inputs = distance.loc[valid].to_frame("distance_km")
    requests.loc[valid, "scaled_distance"] = scaler.transform(valid_inputs).ravel()
    requests.loc[valid, "demo_minutes"] = delivery_model.predict(valid_inputs)

# 4. Show what a delivery app could return if it serves this range only.
requests["app_minutes"] = requests["demo_minutes"].where(within_training_range)
requests["app_message"] = "Estimate ready"
requests.loc[~valid, "app_message"] = "Enter a finite, nonnegative distance."
requests.loc[valid & ~within_training_range, "app_message"] = (
    f"Outside training range ({lowest:g}–{highest:g} km)"
)
print(
    requests.to_string(
        index=False,
        na_rep="—",
        formatters={
            "scaled_distance": "{:.4f}".format,
            "demo_minutes": "{:.1f}".format,
            "app_minutes": "{:.1f}".format,
        },
    )
)
