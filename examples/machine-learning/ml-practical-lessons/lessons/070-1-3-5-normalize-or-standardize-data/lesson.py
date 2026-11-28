"""
1.3.5 Normalize or Standardize Data

Learn a scale from training deliveries and reuse it on new rows.

Run: python lesson.py
In new_inputs.csv, try 5 km and 2 kg, then try 12 km and 4 kg. Read the scaled values and predicted minutes in the same row.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
deliveries = pd.read_csv(input_path)


# iloc counts rows by position. The first four teach the scaler and model.
# 2. Set aside the check rows before the model learns.
training = deliveries.iloc[:4]
checking = deliveries.iloc[4:]
inputs = ["distance_km", "weight_kg"]
scaler = MinMaxScaler()
# 3. Learn the conversion on the training inputs before applying it to a new row.
scaled_training = scaler.fit_transform(training[inputs])
training_table = training[inputs].reset_index(drop=True)
training_table[["scaled_distance", "scaled_weight"]] = scaled_training.round(2)
print("Training rows before and after scaling")
print(training_table.to_string(index=False))


model = LinearRegression()
# 4. Teach the model from the training inputs and delivery time in minutes.
model.fit(scaled_training, training["delivery_minutes"])


# 5. Apply the fitted model to the new CSV rows and print a result for each row.
new_delivery = pd.read_csv(new_path)
scaled_new = scaler.transform(new_delivery)
new_time = model.predict(scaled_new)
# 6. Compare predictions with the measured answers in the check rows.
check_times = model.predict(scaler.transform(checking[inputs]))
known_results = checking[inputs].copy()
known_results["actual_minutes"] = checking["delivery_minutes"]
known_results["predicted_minutes"] = check_times.round(1)
print("\nCheck the predictions against actual deliveries")
print(known_results.to_string(index=False))

new_delivery[["scaled_distance", "scaled_weight"]] = scaled_new.round(2)
new_delivery["predicted_minutes"] = new_time.round(1)
print("\nNew deliveries and their predicted minutes")
print(new_delivery.to_string(index=False))
