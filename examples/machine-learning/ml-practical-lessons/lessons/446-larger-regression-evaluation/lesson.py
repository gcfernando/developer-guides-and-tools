"""Check delivery errors on future trips and find where the model struggles."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder

folder = Path(__file__).resolve().parent
data = pd.read_csv(folder / "sample.csv", parse_dates=["delivery_date"]).sort_values(
    "delivery_date"
)
settings = pd.read_csv(folder / "new_inputs.csv").iloc[0]
assert data["shipment_id"].is_unique
inputs = ["distance_km", "weight_kg", "zone"]

# 1. Learn on the earlier days. Reserve the later days for testing.
cut = data["delivery_date"].iloc[int(len(data) * 0.75)]
train = data[data["delivery_date"] < cut]
test = data[data["delivery_date"] >= cut].copy()
assert train["delivery_date"].max() < test["delivery_date"].min()

# 2. Compare a model with a baseline that always guesses the median training time.
prepare = ColumnTransformer(
    [
        ("number", SimpleImputer(strategy="median"), inputs[:2]),
        ("zone", OneHotEncoder(handle_unknown="ignore"), ["zone"]),
    ]
)
model = make_pipeline(prepare, LinearRegression()).fit(
    train[inputs], train["actual_minutes"]
)
baseline = DummyRegressor(strategy="median").fit(
    train[["distance_km"]], train["actual_minutes"]
)
test["model"] = model.predict(test[inputs])
test["baseline"] = baseline.predict(test[["distance_km"]])
print(f"Test deliveries: {len(test)}. First test day: {cut.date()}.")
whole = []
for name in ("baseline", "model"):
    truth, pred = test["actual_minutes"], test[name]
    whole.append(
        [
            name,
            mean_absolute_error(truth, pred),
            root_mean_squared_error(truth, pred),
            r2_score(truth, pred),
        ]
    )
print(
    pd.DataFrame(whole, columns=["Method", "MAE (min)", "RMSE (min)", "R squared"])
    .round(2)
    .to_string(index=False)
)

# 3. Put each held-out error in its route, weight, and zone group.
test["route"] = pd.cut(
    test["distance_km"],
    [0, settings["short_route_max_km"], settings["long_route_min_km"], np.inf],
    labels=["Short", "Medium", "Long"],
    include_lowest=True,
).astype("object")
test["weight"] = np.where(
    test["weight_kg"].isna(),
    "Missing",
    np.where(test["weight_kg"] <= settings["light_parcel_max_kg"], "Light", "Heavy"),
)
test["model_error"] = (test["actual_minutes"] - test["model"]).abs()
test["baseline_error"] = (test["actual_minutes"] - test["baseline"]).abs()
for field in ("route", "weight", "zone"):
    print(f"\nBy {field}")
    summary = test.groupby(field, dropna=False).agg(
        orders=("shipment_id", "count"),
        model_mae=("model_error", "mean"),
        baseline_mae=("baseline_error", "mean"),
    )
    print(summary.round(2).to_string())
print("Look at the order count before drawing a conclusion about a group.")
