"""
Co-Training

Let models trained on different input columns teach each other from unlabeled rows.

Run: python lesson.py
Edit x or y in new_inputs.csv. These rows are kept separate from the rows with masked labels and the labeled check rows.
"""

from pathlib import Path
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.linear_model import LogisticRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including x, y, label.
rows = pd.read_csv(input_path)
X = rows[["x", "y"]].to_numpy()
y = rows["label"].to_numpy()
# 2. Set aside the check rows before the model learns.
train, hold, labels, answers = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=7
)
partial = np.full(len(labels), -1)
for category in [0, 1]:
    kept = np.flatnonzero(labels == category)[:4]
    partial[kept] = category
print(
    "Labeled / unlabeled training rows:",
    int((partial != -1).sum()),
    int((partial == -1).sum()),
)


views = [train[:, :1], train[:, 1:]]
hold_views = [hold[:, :1], hold[:, 1:]]
sets = [partial.copy(), partial.copy()]


# 3. Have the two classifiers exchange confident labels on unlabeled training rows.
for _ in range(3):
    choices = []
    for values, labels in zip(views, sets):
        known = labels != -1
        fit = LogisticRegression().fit(values[known], labels[known])
        probabilities = fit.predict_proba(values)
        confidence = probabilities.max(axis=1)
        candidates = np.argsort(-confidence)
        chosen = candidates[
            (labels[candidates] == -1) & (confidence[candidates] >= 0.8)
        ][:4]
        choices.append((chosen, fit.classes_[probabilities[chosen].argmax(axis=1)]))
    for labels, (chosen, guesses) in zip(sets[::-1], choices):
        missing = labels[chosen] == -1
        labels[chosen[missing]] = guesses[missing]

predicted = []
for values, checks, labels in zip(views, hold_views, sets):
    known = labels != -1
    fit = LogisticRegression().fit(values[known], labels[known])
    predicted.append(fit.predict_proba(checks))
print("Labels per view:", [int((labels != -1).sum()) for labels in sets])
print(
    "Holdout accuracy:",
    round((np.mean(predicted, axis=0).argmax(axis=1) == answers).mean(), 3),
)
# 4. Apply the fitted model to the new CSV rows and print a result for each row.
new_rows = pd.read_csv(new_path)
new_probabilities = []
for column, values, labels in zip(["x", "y"], views, sets):
    known = labels != -1
    model = LogisticRegression().fit(values[known], labels[known])
    new_probabilities.append(model.predict_proba(new_rows[[column]].to_numpy()))
print("New guesses:", np.mean(new_probabilities, axis=0).argmax(axis=1).tolist())
