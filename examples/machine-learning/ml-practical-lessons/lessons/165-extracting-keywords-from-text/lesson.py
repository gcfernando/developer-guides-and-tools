"""
Extracting keywords from text

Mark whether a support message contains the word urgent.

Run: python lesson.py
Edit the input values in new_inputs.csv and compare the displayed predictions.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including birth, message, review.
data = pd.read_csv(input_path)


# 2. Turn a date and a message into numerical inputs.
def make_features(frame):
    born = pd.to_datetime(frame["birth"], format="%Y-%m-%d").dt
    cutoff = pd.Timestamp("2025-04-01")
    birthday_ahead = (born.month > cutoff.month) | (
        (born.month == cutoff.month) & (born.day > cutoff.day)
    )
    age = cutoff.year - born.year - birthday_ahead.astype(int)
    urgent = frame["message"].str.contains(r"\burgent\b", case=False).astype(int)
    return pd.DataFrame({"age": age, "urgent": urgent})


features = make_features(data)
print(features.to_string(index=False))
# 3. Teach the model from the training inputs and whether the message needs review.
model = LogisticRegression().fit(features.iloc[:4], data["review"].iloc[:4])
print("Held-out prediction:", model.predict(features.iloc[4:]).tolist())


# 4. Apply the fitted model to the new CSV rows and print a result for each row.
rows = pd.read_csv(new_path)
predictions = model.predict(make_features(rows)).round(2)
print(rows.assign(prediction=list(predictions)).to_string(index=False))
