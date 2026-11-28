"""
AWS, Google Cloud, or Heroku

Practice a local request check, then use the deployment notes for your platform.

Run: python lesson.py
Try changing distance_km from 5 to -2 in sample.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
requests = pd.read_csv(input_path)


requests["valid"] = requests["distance_km"].ge(0) & requests["weight_kg"].gt(0)


# Treat these as example status codes for an API contract.
requests["expected_status"] = requests["valid"].map({True: 200, False: 422})
# 2. Print the result next to the input values so you can compare them.
print(requests.to_string(index=False))
print("Platform to explore: AWS, Google Cloud, or Heroku")
print("These are expected responses from a local contract check.")
print("Use the FastAPI lesson to send real requests to a local test client.")
