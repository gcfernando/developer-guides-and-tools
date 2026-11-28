"""
Standardization (Z-score Scaling)

Measure distance and weight relative to their training averages, then estimate a new delivery time.

Run: python lesson.py
In new_inputs.csv, try 5 km and 2 kg, then try 12 km and 4 kg. Read the scaled values and predicted minutes in the same row.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the practice deliveries and their measured times.
deliveries = pd.read_csv(input_path)


# iloc counts rows by position. The first four teach the scaler and model.
# 2. Use the first four trips to learn and keep the last two for checking.
training = deliveries.iloc[:4]
checking = deliveries.iloc[4:]
inputs = ["distance_km", "weight_kg"]
scaler = StandardScaler()
# 3. Find the training average and spread for each input. Express each row in those units.
scaled_training = scaler.fit_transform(training[inputs])
training_table = training[inputs].reset_index(drop=True)
training_table[["scaled_distance", "scaled_weight"]] = scaled_training.round(2)
print("Training rows before and after scaling")
print(training_table.to_string(index=False))


model = LinearRegression()
# 4. Teach the model how the scaled inputs relate to the measured minutes.
model.fit(scaled_training, training["delivery_minutes"])


# 5. Read the new trips and scale them using the training values.
new_delivery = pd.read_csv(new_path)
scaled_new = scaler.transform(new_delivery[inputs])
new_time = model.predict(scaled_new)
# 6. Compare estimates with the two known times, then read the estimates for your new trips.
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
