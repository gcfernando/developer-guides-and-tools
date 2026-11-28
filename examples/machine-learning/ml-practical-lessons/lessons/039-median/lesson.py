"""
Median

Fill an empty weight with the middle training weight after sorting.

Run: python lesson.py
Change a distance in new_inputs.csv and clear actual_minutes on that row. The old actual time does not belong to an invented request.
"""

from pathlib import Path
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
data = pd.read_csv(input_path, na_values=["?"])


# 2. Set aside the check rows before the model learns.
training = data.iloc[:4]
inputs = ["distance_km", "weight_kg"]
# 3. Apply the conversion learned from training to each new row.
new_parcel = pd.read_csv(new_path).loc[:, inputs]
# Keep any measured time for the comparison table.
actual_minutes = pd.read_csv(new_path)["actual_minutes"].to_numpy()


# Learn the median weight from the training rows.
imputer = SimpleImputer(strategy="median")
# Learn the needed values here. New rows use transform with these saved values.
filled_training = imputer.fit_transform(training[inputs])

# Fit a delivery model with the completed training rows.
# 4. Teach the model from the training inputs and delivery time in minutes.
model = LinearRegression().fit(filled_training, training["delivery_minutes"])

# Fill missing weights in the new rows the same way.
filled_parcels = imputer.transform(new_parcel)
results = new_parcel.copy()
# Column 0 is first. Column 1 is the second column.
results["filled_weight_kg"] = filled_parcels[:, 1]
results["predicted_minutes"] = model.predict(filled_parcels).round(2)
results["actual_minutes"] = actual_minutes
print(results.to_string(index=False, na_rep="—"))
