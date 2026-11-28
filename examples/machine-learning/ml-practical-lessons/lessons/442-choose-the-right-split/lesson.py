"""Compare three ways to reserve deliveries for a fair test."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GroupShuffleSplit, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

folder = Path(__file__).resolve().parent
data = pd.read_csv(folder / "sample.csv", parse_dates=["date"]).sort_values("date")
assert data["shipment_id"].is_unique

# 1. Decide what kind of delivery the model will see after training.
random_train, random_test = train_test_split(data, test_size=0.25, random_state=7)
group = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=7)
train_indices, test_indices = next(group.split(data, groups=data["customer_id"]))
cut = data["date"].iloc[int(len(data) * 0.75)]
plans = {
    "random": (random_train, random_test),
    "customer": (data.iloc[train_indices], data.iloc[test_indices]),
    "time": (data[data["date"] < cut], data[data["date"] >= cut]),
}

# 2. Check exactly what the split keeps separate.
results = []
for plan in pd.read_csv(folder / "new_inputs.csv")["plan"]:
    if plan not in plans:
        raise SystemExit("Choose random, customer, or time.")
    train, test = plans[plan]
    shared_shipments = set(train["shipment_id"]) & set(test["shipment_id"])
    shared_customers = set(train["customer_id"]) & set(test["customer_id"])
    past_then_future = train["date"].max() < test["date"].min()
    assert not shared_shipments
    if plan == "customer":
        assert not shared_customers
    if plan == "time":
        assert past_then_future

    # 3. Fit preprocessing and the model only on the teaching rows.
    features = ["distance_km", "weight_kg", "customer_id"]
    prepare = ColumnTransformer(
        [
            ("numbers", StandardScaler(), features[:2]),
            ("customer", OneHotEncoder(handle_unknown="ignore"), ["customer_id"]),
        ]
    )
    model = make_pipeline(prepare, Ridge())
    model.fit(train[features], train["actual_minutes"])
    error = mean_absolute_error(test["actual_minutes"], model.predict(test[features]))
    results.append(
        [
            plan,
            len(test),
            len(shared_shipments),
            len(shared_customers),
            past_then_future,
            round(error, 2),
        ]
    )

table = pd.DataFrame(
    results,
    columns=[
        "Plan",
        "Test orders",
        "Shared shipments",
        "Shared customers",
        "Test is entirely later",
        "Test MAE (min)",
    ],
)
print(table.to_string(index=False))
print(
    "\nRandom: independent orders in the same setting. Customer: customers the model has never seen."
)
print(
    "Time: later orders. Their customers may already be known. Pick the plan before comparing scores."
)
