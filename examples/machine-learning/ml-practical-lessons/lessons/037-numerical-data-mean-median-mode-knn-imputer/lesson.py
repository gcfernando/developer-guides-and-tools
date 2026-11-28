"""
Numerical Data: Mean, Median, Mode, KNN Imputer

Compare four ways of filling the same missing weight and see how each changes the prediction.

Run: python lesson.py
Leave weight_kg blank for a new distance and compare what each method fills in.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
data = pd.read_csv(input_path, na_values=["?"])


# 2. Set aside the check rows before the model learns.
training = data.iloc[:4]
inputs = ["distance_km", "weight_kg"]
# 3. Read the new CSV rows, then apply the rules from the sample.
new_parcel = pd.read_csv(new_path).loc[:, inputs]
# This column contains measured times for comparison. It stays outside the model inputs.
actual_minutes = pd.read_csv(new_path)["actual_minutes"].to_numpy()


methods = [
    ("Mean", SimpleImputer(strategy="mean")),
    ("Median", SimpleImputer(strategy="median")),
    ("Most frequent (mode)", SimpleImputer(strategy="most_frequent")),
]
rows = []
# 4. Give each method the same practice data so you can compare the results.
for name, imputer in methods:
    filled_training = imputer.fit_transform(training[inputs])
    filled_parcel = imputer.transform(new_parcel)
    model = LinearRegression().fit(filled_training, training["delivery_minutes"])
    rows.append([name, filled_parcel[:, 1], model.predict(filled_parcel)])


scaler = StandardScaler()
# 5. Learn the conversion on the training inputs before applying it to a new row.
scaled_training = scaler.fit_transform(training[inputs])
knn = KNNImputer(n_neighbors=2)
# Learn the needed values here. New rows use transform with these saved values.
filled_training = knn.fit_transform(scaled_training)
filled_parcel = knn.transform(scaler.transform(new_parcel))
model = LinearRegression().fit(filled_training, training["delivery_minutes"])
# Column 0 is first. Column 1 is the second column.
filled_weight = scaler.inverse_transform(filled_parcel)[:, 1]
rows.append(["KNN (two neighbors)", filled_weight, model.predict(filled_parcel)])
results = []
for method, weights, predictions in rows:
    for i, (weight, prediction) in enumerate(zip(weights, predictions)):
        results.append([i + 1, method, weight, prediction, actual_minutes[i]])
table = pd.DataFrame(
    results,
    columns=[
        "New row",
        "Method",
        "Filled kg",
        "Prediction in minutes",
        "Actual minutes",
    ],
)
print(table.round(2).to_string(index=False, na_rep="—"))
