"""
Self-Training

Use confident guesses as extra training labels and compare with the known check rows.

Run: python lesson.py
Edit x or y in new_inputs.csv. These rows are kept separate from the rows with masked labels and the labeled check rows.
"""

from pathlib import Path
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.semi_supervised import SelfTrainingClassifier

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


# 3. Identify the labeled training rows for the baseline.
known = partial != -1
# A pipeline keeps preparation and prediction together in the right order.
baseline = make_pipeline(StandardScaler(), LogisticRegression()).fit(
    train[known], partial[known]
)
learner = SelfTrainingClassifier(LogisticRegression(), threshold=0.8)
# 4. Fit the model on the prepared training rows. Keep it for the checks below.
model = make_pipeline(StandardScaler(), learner).fit(train, partial)
print("Added pseudo-labels:", int(((learner.transduction_ != -1) & ~known).sum()))
print(
    "Labeled-only / self-training:",
    round(baseline.score(hold, answers), 3),
    round(model.score(hold, answers), 3),
)
# 5. Apply the fitted model to the new CSV rows and print a result for each row.
print(
    "New guesses:", model.predict(pd.read_csv(new_path)[["x", "y"]].to_numpy()).tolist()
)
