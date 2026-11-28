"""
Label Propagation

Pass labels from known points to nearby unknown points.

Run: python lesson.py
Edit x or y in new_inputs.csv. These rows are kept separate from the rows with masked labels and the labeled check rows.
"""

from pathlib import Path
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.semi_supervised import LabelPropagation

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


# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(StandardScaler(), LabelPropagation(kernel="knn", n_neighbors=6))
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model.fit(train, partial)
print("Holdout accuracy:", round(model.score(hold, answers), 3))
# 4. Apply the fitted model to the new CSV rows and print a result for each row.
print(
    "Predictions from new feature rows:",
    model.predict(pd.read_csv(new_path)[["x", "y"]].to_numpy()).tolist(),
)
