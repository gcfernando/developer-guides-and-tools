"""
Remove

Drop a spare note column and remove rows missing a required distance or known time.

Run: python lesson.py
Leave distance_km blank on a practice row. Compare the number of usable rows and enter a new distance to predict.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including distance_km, note, minutes.
data = pd.read_csv(input_path)


# 2. Keep rows with both a usable input and a known answer.
reviewed = data.drop(columns="note").dropna(subset=["distance_km", "minutes"])
# 3. Set aside the check rows before the model learns.
train = reviewed.iloc[:-1]
# 4. Teach the model from the training inputs and delivery time in minutes.
model = LinearRegression().fit(train[["distance_km"]], train["minutes"])
print("Rows retained:", len(reviewed))
print(
    "Held-out prediction:",
    model.predict(reviewed.iloc[-1:][["distance_km"]]).round(1).tolist(),
)


# 5. Apply the fitted model to the new CSV rows and print a result for each row.
print(model.predict(pd.read_csv(new_path)[["distance_km"]]).round(1))
