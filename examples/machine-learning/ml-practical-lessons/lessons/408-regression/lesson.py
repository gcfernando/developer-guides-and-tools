"""
Regression

Train a model with a few known numbers, then use its confident estimates to add practice rows.

Run: python lesson.py
Change the input in new_inputs.csv. The model supplies an estimated numeric value.
"""

from pathlib import Path
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including input, answer.
rows = pd.read_csv(input_path)
x = rows[["input"]].to_numpy()


y = rows["answer"].to_numpy()
# 2. Set aside the check rows before the model learns.
train, hold = x[:10], x[10:]
# 3. Keep half the training answers and compare guesses from two regressors.
known = np.arange(len(train)) % 2 == 0
one = LinearRegression().fit(train[known], y[:10][known])
two = Ridge().fit(train[known], y[:10][known])
unlabeled = train[~known]
a, b = one.predict(unlabeled), two.predict(unlabeled)
accept = np.abs(a - b) < 1
# 4. Fit the model on the prepared training rows. Keep it for the checks below.
model = LinearRegression().fit(
    np.vstack([train[known], unlabeled[accept]]),
    np.r_[y[:10][known], (a[accept] + b[accept]) / 2],
)
print("Added values:", int(accept.sum()))
print(
    "Holdout MAE, before / after:",
    round(mean_absolute_error(y[10:], one.predict(hold)), 2),
    round(mean_absolute_error(y[10:], model.predict(hold)), 2),
)
# 5. Apply the fitted model to the new CSV rows and print a result for each row.
print(
    "Fresh estimates:",
    model.predict(pd.read_csv(new_path)[["input"]].to_numpy()).round(2).tolist(),
)
