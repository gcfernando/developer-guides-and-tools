"""
Handling Strategies

Compare deleting a confirmed error, clipping a value and applying a log.

Run: python lesson.py
Try changing weight_kg from 1 to 2 in sample.csv. Compare the new output.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the weights in kilograms and the delivery times in minutes.
data = pd.read_csv(input_path)


valid = data.loc[data["weight_kg"] >= 0]
# 2. Set aside the check rows before the model learns.
train, hold = valid.iloc[:-1], valid.iloc[-1:]
print("Confirmed errors removed:", len(data) - len(valid))

weights = train[["weight_kg"]].astype(float)
new = hold[["weight_kg"]].astype(float)
lower = weights["weight_kg"].quantile(0.1)
upper = weights["weight_kg"].quantile(0.8)


# 3. Give each method the same practice data so you can compare the results.
for name, train_x, test_x in [
    ("remove only", weights, new),
    (
        "remove and clip",
        weights.clip(lower=lower, upper=upper),
        new.clip(lower=lower, upper=upper),
    ),
    ("remove and log", np.log1p(weights), np.log1p(new)),
]:
    model = LinearRegression().fit(train_x, train["minutes"])
    preview = test_x.copy()
    preview.columns = ["weight_used_by_model"]
    preview["original_weight_kg"] = new["weight_kg"]
    preview["predicted_minutes"] = model.predict(test_x).round(1)
    preview["actual_minutes"] = hold["minutes"]
    print(name)
    print(preview.to_string(index=False))
