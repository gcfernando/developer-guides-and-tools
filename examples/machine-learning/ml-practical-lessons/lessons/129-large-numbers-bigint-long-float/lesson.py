"""
Large Numbers (BigInt, Long Float)

Read large values and display them in a shorter format.

Run: python lesson.py
Try changing event_id from 123456789012345 to 123456789012347 in sample.csv. Compare the new output.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including event_id, visits, server_cost.
data = pd.read_csv(input_path, dtype={"event_id": "string"})


# 2. Print the result next to the input values so you can compare them.
print("First ID:", data.loc[0, "event_id"])
print("Traffic display:", [f"{value:.3e}" for value in data["visits"]])
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(FunctionTransformer(np.log1p), LinearRegression())
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model.fit(data.iloc[:3][["visits"]], data.iloc[:3]["server_cost"])
print(
    "Numeric log features:",
    model[0].transform(data[["visits"]]).round(2)["visits"].tolist(),
)
print(
    "Held-out cost estimate:",
    model.predict(data.iloc[3:][["visits"]]).round(1).tolist(),
)
