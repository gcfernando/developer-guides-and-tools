"""
Your first prediction

Predict how long a 4 km delivery will take, then check the model against two trips with known times.

Run: python lesson.py
Change 4 to 8 in new_inputs.csv, then run this script again.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including distance_km, minutes.
deliveries = pd.read_csv(input_path)
# 2. Print the result next to the input values so you can compare them.
print("One completed delivery")
print(deliveries.head(1).to_string(index=False))


# 3. Set aside the check rows before the model learns.
training = deliveries.iloc[:3]
model = LinearRegression()
# 4. Teach the model from the training inputs and delivery time in minutes.
model.fit(training[["distance_km"]], training["minutes"])


checking = deliveries.iloc[3:]
# 5. Compare predictions with the measured answers in the check rows.
check_minutes = model.predict(checking[["distance_km"]])
checking_results = checking.copy()
checking_results["predicted_minutes"] = check_minutes.round(1)
print("\nCompare the recorded and predicted minutes")
print(checking_results.to_string(index=False))

# 6. Apply the fitted model to the new CSV rows and print a result for each row.
new_delivery = pd.read_csv(new_path)
new_minutes = model.predict(new_delivery[["distance_km"]])
results = new_delivery.copy()
results["Predicted time (min)"] = new_minutes.round(1)
print("\nNew delivery estimates")
print(results.to_string(index=False))
