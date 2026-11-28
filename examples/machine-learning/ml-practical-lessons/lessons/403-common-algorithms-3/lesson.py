"""
Common Algorithms

Try one way to use both labeled and unlabeled rows before predicting new cases.

Run: python lesson.py
Change x and y in new_inputs.csv. Keep four blank-label rows in sample.csv if editing the training example.
"""

from pathlib import Path
from itertools import product
import numpy as np
from sklearn.svm import SVC
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including x, y, label.
rows = pd.read_csv(input_path)
known_rows = rows["label"].notna()
known_x = rows.loc[known_rows, ["x", "y"]].to_numpy()


known_y = rows.loc[known_rows, "label"].astype(int).to_numpy()
unknown_x = rows.loc[~known_rows, ["x", "y"]].to_numpy()
if set(known_y) != {-1, 1} or len(unknown_x) != 4:
    raise SystemExit("Keep both known labels, -1 and 1, and exactly four blank labels in sample.csv.")
X = np.vstack([known_x, unknown_x])
weights = np.r_[np.ones(len(known_x)), np.full(len(unknown_x), 0.25)]
best_loss = float("inf")
# 2. Try balanced guesses for the unknown labels and keep the lowest-loss fit.
for guess in product([-1, 1], repeat=len(unknown_x)):
    if sum(guess) != 0:
        continue  # This toy problem assumes balanced unlabeled classes.
    y = np.r_[known_y, guess]
    candidate = SVC(kernel="linear", C=1).fit(X, y, sample_weight=weights)
    hinge = np.maximum(0, 1 - y * candidate.decision_function(X))
    loss = 0.5 * np.square(candidate.coef_).sum() + weights @ hinge
    if loss < best_loss:
        best_loss, chosen, model = loss, guess, candidate
print("Chosen training pseudo-labels:", chosen)
# 3. Apply the fitted model to the new CSV rows and print a result for each row.
print(
    "Predictions for new rows:",
    model.predict(pd.read_csv(new_path)[["x", "y"]].to_numpy()).tolist(),
)
