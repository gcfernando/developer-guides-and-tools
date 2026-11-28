"""
Normalization (Min-Max Scaling)

Scale known distances, then see what happens when training covers 1–50 km and someone enters 90 km.

Run: python lesson.py
Try 5 km with 2 kg and 12 km with 4 kg in new_inputs.csv. Then use the separate saved-model exercise to try a 90 km route.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the delivery log. Each row has a distance, a weight and an actual time.
deliveries = pd.read_csv(input_path)


# iloc counts rows by position. The first four teach the scaler and model.
# 2. Take the first four trips for training. Save the last two to check the model.
training = deliveries.iloc[:4]
checking = deliveries.iloc[4:]
inputs = ["distance_km", "weight_kg"]
scaler = MinMaxScaler()
# 3. Find the smallest and largest training values for each input, then scale the training rows.
scaled_training = scaler.fit_transform(training[inputs])
training_table = training[inputs].reset_index(drop=True)
training_table[["scaled_distance", "scaled_weight"]] = scaled_training.round(2)
print("Training rows before and after scaling")
print(training_table.to_string(index=False))


model = LinearRegression()
# 4. Teach the model using the scaled distance and weight. Leave the answers in minutes.
model.fit(scaled_training, training["delivery_minutes"])


# 5. Check the model against the measured delivery times.
check_times = model.predict(scaler.transform(checking[inputs]))
known_results = checking[inputs].copy()
known_results["actual_minutes"] = checking["delivery_minutes"]
known_results["predicted_minutes"] = check_times.round(1)
print("\nCheck the predictions against actual deliveries")
print(known_results.to_string(index=False))

# 6. Reuse the fitted scaler for the new trips. Print the raw inputs, scaled inputs and predicted minutes together.
new_delivery = pd.read_csv(new_path)
scaled_new = scaler.transform(new_delivery[inputs])
new_time = model.predict(scaled_new)

new_delivery[["scaled_distance", "scaled_weight"]] = scaled_new.round(2)
new_delivery["predicted_minutes"] = new_time.round(1)
print("\nNew deliveries and their predicted minutes")
print(new_delivery.to_string(index=False))
