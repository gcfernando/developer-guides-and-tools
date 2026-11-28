"""Predict delivery times from new_deliveries.csv.

1. Train once with: python train_delivery_model.py
2. Edit the rows in new_deliveries.csv and save it.
3. Run this file again each time: python test_delivery_model.py
"""

from pathlib import Path

import joblib
import pandas as pd

folder = Path(__file__).resolve().parent
input_columns = ["distance_km", "weight_kg", "zone"]


def main():
    # 1. Open the model created by the training script.
    model_path = folder / "delivery_model.joblib"
    if not model_path.exists():
        raise SystemExit("Run python train_delivery_model.py first.")
    # Load the file you trained here, or another artifact from a source you trust.
    model = joblib.load(model_path)

    # 2. Read your new deliveries. Keep distance in km and weight in kg.
    # Leave weight blank when unknown. Keep a zone name in every row.
    csv_path = folder / "new_deliveries.csv"
    if not csv_path.is_file():
        raise SystemExit("Put new_deliveries.csv next to this Python file.")
    deliveries = pd.read_csv(csv_path)
    if deliveries.empty:
        raise SystemExit("Add at least one delivery to new_deliveries.csv.")

    # 3. Ask for an estimate. The supplied practice model fills a blank
    # weight using the middle weight it learned during training.
    predictions = model.predict(deliveries[input_columns])
    results = deliveries[input_columns].copy()
    results["predicted_minutes"] = predictions.round(2)

    # 4. If you recorded a real time, show how far off the guess was.
    if "actual_minutes" in deliveries.columns:
        actual = deliveries["actual_minutes"]
        errors = (actual - predictions).abs()
        results["actual_minutes"] = actual
        results["error_minutes"] = errors.round(2)
        if errors.notna().any():
            print(f"Average error where the actual time is known: {errors.mean():.2f} minutes.")

    # 5. Read the table. A dash marks an unknown value.
    print(results.to_string(index=False, na_rep="—"))


if __name__ == "__main__":
    main()
