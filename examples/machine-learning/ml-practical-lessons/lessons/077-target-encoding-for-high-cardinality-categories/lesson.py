"""
Target Encoding (For High-Cardinality Categories)

Summarize each supplier by its learned delay rate and try a supplier the model has never seen.

Run: python lesson.py
Enter S00 and a supplier name such as New Supplier. Compare their encoded values and estimated chances of delay.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import TargetEncoder

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including supplier, delayed.
data = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
train, hold = data.iloc[:60], data.iloc[60:]
print(data.head(5).to_string(index=False))
encoder = TargetEncoder(target_type="binary", cv=3, random_state=42)
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(encoder, LogisticRegression())
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model.fit(train[["supplier"]], train["delayed"])
print("Holdout predictions:", model.predict(hold[["supplier"]])[:6].tolist())
# 4. Apply the fitted model to the new CSV rows and print a result for each row.
new = pd.read_csv(new_path)
print("Encoded supplier values:", np.round(encoder.transform(new).ravel(), 2).tolist())
# Column 0 is first. Column 1 is the second column.
print("Delay probabilities:", model.predict_proba(new)[:, 1].round(2).tolist())
print(
    new.assign(delay_probability=model.predict_proba(new)[:, 1].round(2)).to_string(
        index=False
    )
)
