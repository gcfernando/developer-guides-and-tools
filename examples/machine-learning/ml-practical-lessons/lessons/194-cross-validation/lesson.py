"""
Cross-validation

Take turns holding different deliveries back and compare the error on each group.

Run: python lesson.py
Change the recorded time for one completed delivery. See which three-group check changes its error.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the delivery table. Distance is in km, and weight is in kg.
deliveries = pd.read_csv(input_path)


folds = KFold(3, shuffle=True, random_state=7)
X = deliveries[["distance_km", "weight_kg"]]
# 2. Take turns keeping one group back for a check. Read each group’s average error in minutes.
errors = -cross_val_score(
    LinearRegression(),
    X,
    deliveries["delivery_minutes"],
    scoring="neg_mean_absolute_error",
    cv=folds,
)
results = []
for fold_number, (training, checking) in enumerate(folds.split(X), start=1):
    results.append([fold_number, len(training), len(checking), errors[fold_number - 1]])
table = pd.DataFrame(
    results,
    columns=["Fold", "Rows to learn", "Rows to check", "Average error in minutes"],
)
print(table.round(2).to_string(index=False))
