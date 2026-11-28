"""
REST API or integrate with mobile/web apps

Turn CSV rows into JSON request bodies a web or mobile app would send.

Run: python lesson.py
Try changing distance_km from 5 to 14 in sample.csv. Compare the new output.
"""

from pathlib import Path
import json
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
for row in pd.read_csv(input_path).to_dict("records"):
    # A client would send this JSON body to POST /predict.
    request_body = json.dumps(row)
    print("POST /predict", request_body)
    assert set(json.loads(request_body)) == {"distance_km", "weight_kg"}
