"""
Log transformation

Take a log of large sensor readings before predicting cost.

Run: python lesson.py
Try a signal reading of 3, 15, or 40 in new_inputs.csv. Compare the predicted cost for each row.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the sensor readings and their measured costs.
data = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
training = data.iloc[:7]
checking = data.iloc[7:]

transform = FunctionTransformer(np.log1p)
name = "Log Transformation"
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(transform, LinearRegression())
# 3. Teach the model from the training inputs and the recorded cost.
model.fit(training[["signal"]], training["cost"])
# Counting from the start of the table sets aside the same rows every run.
first_two = np.asarray(transform.transform(training[["signal"]].iloc[:2])).round(2)
guesses = model.predict(checking[["signal"]]).round(1)
print(name, "first two training rows:", first_two.tolist())
print("Actual costs:", checking["cost"].tolist())
print("Predicted costs:", guesses.tolist())
# 4. Apply the fitted model to the new CSV rows and print a result for each row.
fresh = pd.read_csv(new_path)
print(
    fresh.assign(predicted_cost=model.predict(fresh[["signal"]]).round(2)).to_string(
        index=False
    )
)
