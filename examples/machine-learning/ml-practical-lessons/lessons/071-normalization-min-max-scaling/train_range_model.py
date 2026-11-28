"""Train and save the model for deliveries from 1 to 50 km."""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler

folder = Path(__file__).resolve().parent
inputs = ["distance_km"]

# 1. Read completed deliveries. Each distance has a measured time in minutes.
training = pd.read_csv(folder / "range_training.csv")
checking = pd.read_csv(folder / "range_check.csv")

# 2. Teach the scaler and the model using only the training rows.
# The pipeline keeps them together, so the same scaler is used every time.
delivery_model = make_pipeline(MinMaxScaler(), LinearRegression())
delivery_model.fit(training[inputs], training["actual_minutes"])

# 3. Use separate completed trips to check the model's estimates.
checking["predicted_minutes"] = delivery_model.predict(checking[inputs]).round(1)
print("Check rows with known times")
print(checking.to_string(index=False))

# 4. Save everything needed for later predictions.
model_file = folder / "range_model.joblib"
joblib.dump(delivery_model, model_file)
print(f"Saved {model_file.name}. Next, run python test_range_model.py.")
