"""
FastAPI

Send valid and invalid deliveries to a FastAPI route and read the response.

Run: python lesson.py
Try changing distance_km from 5 to -2 in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd
from fastapi import FastAPI
from fastapi.testclient import TestClient
from joblib import dump, load
from pydantic import BaseModel, Field
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
deliveries = pd.read_csv(input_path)


fields = ["distance_km", "weight_kg"]
dump(
    LinearRegression().fit(deliveries[fields], deliveries["delivery_minutes"]),
    "delivery.joblib",
)
model = load("delivery.joblib")
# Create the local API. The route below receives inputs and returns an estimate.
app = FastAPI()


class Delivery(BaseModel):
    distance_km: float = Field(ge=0)
    weight_kg: float = Field(gt=0)


@app.post("/predict")
def predict(data: Delivery):
    features = pd.DataFrame([data.model_dump()], columns=fields)
    return {"minutes": round(float(model.predict(features)[0]), 1)}


client = TestClient(app)
# 2. Send a practice request and read the response code and body.
response = client.post("/predict", json={"distance_km": 5, "weight_kg": 2})
print(response.status_code, response.json())
invalid = client.post("/predict", json={"distance_km": -5, "weight_kg": 2})
print("Invalid distance:", invalid.status_code)


# 3. Send each new CSV row to the app and read the response.
for payload in pd.read_csv(new_path).to_dict("records"):
    result = client.post("/predict", json=payload)
    print(payload, result.status_code, result.json())
