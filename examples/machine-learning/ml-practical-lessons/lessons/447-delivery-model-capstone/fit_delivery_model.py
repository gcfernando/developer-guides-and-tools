"""Train, choose, evaluate, and save the delivery model."""

import json
from importlib.metadata import version
from pathlib import Path
import platform

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder

FOLDER = Path(__file__).resolve().parent
FIELDS = ["distance_km", "weight_kg", "zone"]


def train_model():
    # 1. Use earlier dates to learn, later dates to choose, and the latest dates to test.
    data = pd.read_csv(
        FOLDER / "sample.csv", parse_dates=["delivery_date"]
    ).sort_values("delivery_date")
    if not data["shipment_id"].is_unique:
        raise SystemExit("Each shipment_id must appear once.")
    first_cut = data["delivery_date"].iloc[430]
    second_cut = data["delivery_date"].iloc[570]
    train = data[data["delivery_date"] < first_cut]
    validate = data[
        data["delivery_date"].between(first_cut, second_cut, inclusive="left")
    ]
    test = data[data["delivery_date"] >= second_cut]
    assert train["delivery_date"].max() < validate["delivery_date"].min()
    assert validate["delivery_date"].max() < test["delivery_date"].min()
    print(f"Train: {len(train)}. Validation: {len(validate)}. Test: {len(test)}.")

    # 2. Compare a median guess and a Ridge pipeline on exactly the same validation rows.
    prepare = ColumnTransformer(
        [
            ("number", SimpleImputer(strategy="median"), FIELDS[:2]),
            ("zone", OneHotEncoder(handle_unknown="ignore"), ["zone"]),
        ]
    )
    candidates = {
        "Training median": DummyRegressor(strategy="median"),
        "Ridge": make_pipeline(prepare, Ridge()),
    }
    validation_scores = {}
    for name, model in candidates.items():
        model.fit(train[FIELDS], train["actual_minutes"])
        score = mean_absolute_error(
            validate["actual_minutes"], model.predict(validate[FIELDS])
        )
        validation_scores[name] = score
        print(f"{name} validation MAE: {score:.2f} minutes.")
    winner = min(validation_scores, key=validation_scores.get)

    # 3. Evaluate the chosen model once. Save its fitted preprocessing with it.
    model = candidates[winner]
    test_error = mean_absolute_error(
        test["actual_minutes"], model.predict(test[FIELDS])
    )
    print(f"Selected: {winner}. Final test MAE: {test_error:.2f} minutes.")
    joblib.dump(model, FOLDER / "delivery_model.joblib")

    # 4. Write down the input contract and the versions needed to reload it.
    metadata = {
        "model": winner,
        "input_columns": FIELDS,
        "distance_min_km": float(train["distance_km"].min()),
        "distance_max_km": float(train["distance_km"].max()),
        "known_zones": sorted(train["zone"].unique().tolist()),
        "test_mae_minutes": test_error,
        "test_last_date": test["delivery_date"].max().date().isoformat(),
        "python": platform.python_version(),
        "packages": {
            p: version(p)
            for p in ("pandas", "numpy", "scikit-learn", "scipy", "joblib")
        },
    }
    (FOLDER / "model-info.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )
    print(
        "Saved delivery_model.joblib and model-info.json. Load the file you generated in this folder."
    )
    return metadata


if __name__ == "__main__":
    train_model()
