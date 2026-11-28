"""Train a delivery-time model with training_deliveries.csv.

Run once: python train_delivery_model.py
Then run: python test_delivery_model.py
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder

# Keep the CSV and saved model next to this Python file.
folder = Path(__file__).resolve().parent
input_columns = ["distance_km", "weight_kg", "zone"]


def main():
    # 1. Read the CSV. Each row is one completed delivery.
    csv_path = folder / "training_deliveries.csv"
    if not csv_path.is_file():
        raise SystemExit("Put training_deliveries.csv next to this Python file.")
    data = pd.read_csv(csv_path)

    # 2. Give each group a job.
    # Train = teach. Validation = choose. Test = check the chosen model.
    train = data[data["split"] == "train"]
    validation = data[data["split"] == "validation"]
    test = data[data["split"] == "test"]
    print(f"Rows to teach: {len(train)}. To choose: {len(validation)}. To check: {len(test)}.")

    # 3. Prepare the inputs. Learn the median weight and zone names
    # only from the training rows. An unfamiliar zone can still be predicted.
    prepare = ColumnTransformer([
        ("weight", SimpleImputer(strategy="median"), ["weight_kg"]),
        ("zone", OneHotEncoder(handle_unknown="ignore"), ["zone"]),
        ("distance", "passthrough", ["distance_km"]),
    ])

    # 4. Teach the model with the inputs and their actual delivery times.
    model = make_pipeline(prepare, LinearRegression())
    model.fit(train[input_columns], train["actual_minutes"])

    # 5. Choose on the validation rows. The baseline is a simple guess:
    # use the middle training time for every delivery.
    baseline = DummyRegressor(strategy="median")
    baseline.fit(train[input_columns], train["actual_minutes"])
    actual = validation["actual_minutes"]
    baseline_error = mean_absolute_error(actual, baseline.predict(validation[input_columns]))
    model_error = mean_absolute_error(actual, model.predict(validation[input_columns]))
    print(f"Average validation error: model {model_error:.2f} min, baseline {baseline_error:.2f} min.")
    if model_error < baseline_error:
        print("Chosen model: linear regression.")
    else:
        print("Chosen model: median baseline.")
        model = baseline

    # 6. Check the chosen model on the rows we kept for the end.
    predictions = model.predict(test[input_columns])
    test_error = mean_absolute_error(test["actual_minutes"], predictions)
    print(f"Average error on the final test rows: {test_error:.2f} minutes.")

    # 7. Save the chosen model and any preparation it learned.
    model_path = folder / "delivery_model.joblib"
    joblib.dump(model, model_path)
    print(f"Saved {model_path.name}. Next run: python test_delivery_model.py")


if __name__ == "__main__":
    main()
