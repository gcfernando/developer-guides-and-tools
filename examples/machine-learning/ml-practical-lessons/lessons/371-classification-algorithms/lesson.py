"""
Classification Algorithms

Use known late or on-time answers to predict a category for a new delivery.

Run: python lesson.py
Change km or kg in new_inputs.csv. The model is trained on sample.csv. The new rows only receive predictions.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the practice deliveries. Use km for distance and kg for parcel weight.
deliveries = pd.read_csv(input_path)

# 2. Set aside the check rows before the model learns.
train, test = train_test_split(
    deliveries, test_size=0.25, stratify=deliveries["late"], random_state=7
)
inputs = ["km", "kg"]

# Keep matching distance-and-weight pairs out of the final model check.
# Special check for this example: test on exact input combinations absent from training.
# Equal values alone do not mean copied records. This check asks a narrower question
# than predicting independent orders from the same setting. See lesson 442.
test_pairs = pd.MultiIndex.from_frame(test[inputs])
training_pairs = pd.MultiIndex.from_frame(train[inputs])
train = train.loc[~training_pairs.isin(test_pairs)]
assert not pd.MultiIndex.from_frame(train[inputs]).isin(test_pairs).any()


model = LogisticRegression()
# 3. Teach the model from the training inputs and whether the delivery was late.
model.fit(train[inputs], train["late"])
print("Accuracy:", round(model.score(test[inputs], test["late"]), 3))
# Counting from the start of the table sets aside the same rows every run.
print("Predicted:", model.predict(test.iloc[:4][inputs]).tolist())
print("Actual:", test.iloc[:4]["late"].tolist())
# 4. Apply the fitted model to the new CSV rows and print a result for each row.
new = pd.read_csv(new_path)
new["predicted_late"] = model.predict(new[inputs])
print(new.to_string(index=False))
