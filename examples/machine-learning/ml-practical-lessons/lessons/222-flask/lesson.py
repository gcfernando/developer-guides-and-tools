"""
Flask

Send the same delivery fields to a Flask route and read the JSON reply.

Run: python lesson.py
Try changing distance_km from 5 to -2 in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd
from flask import Flask, request
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
deliveries = pd.read_csv(input_path)


fields = ["distance_km", "weight_kg"]
# 2. Teach the model from the training inputs and delivery time in minutes.
model = LinearRegression().fit(deliveries[fields], deliveries["delivery_minutes"])
app = Flask(__name__)


@app.post("/predict")
def predict():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return {"error": "Send a JSON object."}, 400
    try:
        distance, weight = float(data["distance_km"]), float(data["weight_kg"])
    except (KeyError, TypeError, ValueError):
        return {"error": "Send numeric distance_km and weight_kg."}, 400
    import math

    if (
        not math.isfinite(distance)
        or not math.isfinite(weight)
        or distance < 0
        or weight <= 0
    ):
        return {
            "error": "Distance must be finite and nonnegative and weight positive."
        }, 400
    row = pd.DataFrame([[distance, weight]], columns=fields)
    return {"minutes": round(float(model.predict(row)[0]), 1)}


response = app.test_client().post("/predict", json={"distance_km": 5, "weight_kg": 2})
print(response.status_code, response.json)


# 3. Send each new CSV row to the app and read the response.
for payload in pd.read_csv(new_path).to_dict("records"):
    result = app.test_client().post("/predict", json=payload)
    print(payload, result.status_code, result.get_json())
