"""
LightGBM

Use LightGBM to predict delivery time and read the held-out error.

Run: python lesson.py
Change km or kg in new_inputs.csv. The model is trained on sample.csv. The new rows only receive predictions.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from lightgbm import LGBMRegressor

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the practice deliveries. Use km for distance and kg for parcel weight.
deliveries = pd.read_csv(input_path)

# 2. Set aside the check rows before the model learns.
train, test = train_test_split(deliveries, test_size=0.25, random_state=7)
inputs = ["km", "kg"]

# Keep matching distance-and-weight pairs out of the final model check.
# Special check for this example: test on exact input combinations absent from training.
# Equal values alone do not mean copied records. This check asks a narrower question
# than predicting independent orders from the same setting. See lesson 442.
test_pairs = pd.MultiIndex.from_frame(test[inputs])
training_pairs = pd.MultiIndex.from_frame(train[inputs])
train = train.loc[~training_pairs.isin(test_pairs)]
assert not pd.MultiIndex.from_frame(train[inputs]).isin(test_pairs).any()


# 3. Read the new CSV rows, then apply the rules from the sample.
# 4. Give each method the same practice data so you can compare the results.
for model in [
    LGBMRegressor(
        n_estimators=30, min_child_samples=5, n_jobs=1, random_state=7, verbosity=-1
    )
]:
    model.fit(train[inputs], train["minutes"])
    predictions = model.predict(test[inputs])
    # These are inputs someone can type into the app after training.
    new = pd.read_csv(new_path)
    print("New inputs and predictions:")
    new["predicted_minutes"] = model.predict(new[inputs]).round(2)
    print(new.to_string(index=False))
    error = mean_absolute_error(test["minutes"], predictions)
    print(type(model).__name__, "MAE:", round(error, 2))
    print(
        "First actual / predicted:",
        round(test.iloc[0]["minutes"], 1),
        round(predictions[0], 1),
    )
