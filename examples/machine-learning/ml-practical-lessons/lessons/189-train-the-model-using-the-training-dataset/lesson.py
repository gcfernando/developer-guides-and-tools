"""
Train the model using the training dataset

Give models the same inputs and known answers before comparing their errors.

Run: python lesson.py
Change an input and its known answer consistently in sample.csv. Rerun the comparison and check what changes.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the practice deliveries. Use km for distance and kg for parcel weight.
table = pd.read_csv(input_path)
X = table[["km", "kg"]]


y = table["answer"]
folds = StratifiedKFold(3, shuffle=True, random_state=7)
models = [
    DummyClassifier(),
    LogisticRegression(),
    DecisionTreeClassifier(max_depth=3, random_state=7),
    RandomForestClassifier(n_estimators=30, random_state=7),
    SVC(),
]
# 2. Compare the printed output with the original values.
for estimator in models:
    # A pipeline keeps preparation and prediction together in the right order.
    model = make_pipeline(StandardScaler(), estimator)
    scores = cross_val_score(model, X, y, scoring="f1", cv=folds)
    print(type(estimator).__name__, round(scores.mean(), 3))
