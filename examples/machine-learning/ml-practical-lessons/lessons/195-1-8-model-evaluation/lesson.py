"""
1.8. Model Evaluation

Measure prediction errors on check rows and read the chart that explains them.

Run: python lesson.py
Edit new_inputs.csv and rerun the script. Change an input and its known answer consistently in sample.csv. Rerun the comparison and check what changes.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import (
    StratifiedGroupKFold,
    cross_val_score,
    train_test_split,
)
from sklearn.base import clone

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including distance, weight, answer.
table = pd.read_csv(input_path)
X = table[["distance", "weight"]]


y = table["answer"]
# 2. Set aside the check rows before the model learns.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=7
)

# Each distance-and-weight pair belongs to just one side of the final check.
# Special check for this example: test on exact input combinations absent from training.
# Equal values alone do not mean copied records. This check asks a narrower question
# than predicting independent orders from the same setting. See lesson 442.
test_pairs = pd.MultiIndex.from_frame(X_test)
training_is_new = ~pd.MultiIndex.from_frame(X_train).isin(test_pairs)
X_train = X_train.loc[training_is_new]
y_train = y_train.loc[training_is_new]
assert not pd.MultiIndex.from_frame(X_train).isin(test_pairs).any()

# Keep matching pairs together when comparing models within the training rows.
groups = pd.MultiIndex.from_frame(X_train).factorize()[0]
folds = StratifiedGroupKFold(n_splits=3, shuffle=True, random_state=7)

candidates = [DummyClassifier(), LogisticRegression()]
# Compare the simple baseline and logistic model using training folds only.
model = max(
    candidates,
    key=lambda candidate: cross_val_score(
        candidate, X_train, y_train, groups=groups, cv=folds, scoring="f1"
    ).mean(),
)
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model.fit(X_train, y_train)
predictions = model.predict(X_test)
# Column 0 is first. Column 1 is the second column.
probability = model.predict_proba(X_test)[:, 1]
# 4. Check how often the model gets the known answers right on the rows you set aside.
scores = {
    "accuracy": accuracy_score(y_test, predictions),
    "precision": precision_score(y_test, predictions, zero_division=0),
    "recall": recall_score(y_test, predictions, zero_division=0),
    "F1": f1_score(y_test, predictions, zero_division=0),
    "AUC-ROC": roc_auc_score(y_test, probability),
}
print(pd.Series(scores).round(3).to_string())

# 5. Plot the values so you can see how they compare.
fig, ax = plt.subplots(figsize=(6.5, 3.6))
ConfusionMatrixDisplay.from_predictions(y_test, predictions, ax=ax, cmap="Blues")
ax.set_title("Which urgent orders did the model miss?")


fig.tight_layout()

fig, ax = plt.subplots(figsize=(6.5, 3.6))
RocCurveDisplay.from_predictions(y_test, probability, ax=ax, plot_chance_level=True)
ax.set_title("Urgent orders found versus false alarms")
fig.tight_layout()
# Use a separate grouped check inside training to measure importance.
importance_folds = StratifiedGroupKFold(n_splits=4, shuffle=True, random_state=9)
fit_rows, check_rows = next(importance_folds.split(X_train, y_train, groups))
fit_x, check_x = X_train.iloc[fit_rows], X_train.iloc[check_rows]
fit_y, check_y = y_train.iloc[fit_rows], y_train.iloc[check_rows]

importance = permutation_importance(
    clone(model).fit(fit_x, fit_y),
    check_x,
    check_y,
    scoring="f1",
    n_repeats=5,
    random_state=7,
)
fig, ax = plt.subplots(figsize=(6.5, 3.6))
pd.Series(importance.importances_mean, index=X.columns).plot.bar(
    ax=ax, color="#097a70", title="Which input helped the model most?"
)
ax.set_ylabel("Drop in F1 after shuffling")
ax.tick_params(axis="x", rotation=0)
fig.tight_layout()
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()

# 6. Apply the fitted model to the new CSV rows and print a result for each row.
fresh = pd.read_csv(new_path)
print(fresh.assign(predicted_urgent=model.predict(fresh)).to_string(index=False))
