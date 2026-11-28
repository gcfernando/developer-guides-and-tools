"""
Tune hyperparameters

Try different Ridge settings and compare how search methods find them.

Run: python lesson.py
Edit new_inputs.csv and rerun the script. Change an input and its known answer consistently in sample.csv. Rerun the comparison and check what changes.
"""

from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import norm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.linear_model import Ridge
from sklearn.model_selection import (
    GridSearchCV,
    KFold,
    RandomizedSearchCV,
    cross_val_score,
)

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including input_1, input_2, input_3.
table = pd.read_csv(input_path)
X = table[["input_1", "input_2", "input_3"]].to_numpy()


y = table["answer"]
folds = KFold(3, shuffle=True, random_state=7)
metric = "neg_mean_absolute_error"
grid = GridSearchCV(Ridge(), {"alpha": [0.01, 0.1, 1, 10]}, cv=folds, scoring=metric)
random = RandomizedSearchCV(
    Ridge(),
    {"alpha": np.logspace(-2, 1, 20)},
    n_iter=4,
    cv=folds,
    scoring=metric,
    random_state=7,
)
# 2. Give each method the same practice data so you can compare the results.
for search in [grid, random]:
    search.fit(X, y)
    print(
        type(search).__name__,
        round(search.best_params_["alpha"], 3),
        "MAE",
        round(-search.best_score_, 3),
    )


# Explore untried values using a Gaussian process and expected improvement.
options = np.linspace(-2, 1, 16).reshape(-1, 1)
tried = [0, 8, 15]


def score(index):
    model = Ridge(alpha=10 ** options[index, 0])
    return cross_val_score(model, X, y, cv=folds, scoring=metric).mean()


values = [score(index) for index in tried]
for _ in range(4):
    surrogate = GaussianProcessRegressor(kernel=RBF(0.7), alpha=0.001, optimizer=None)
    surrogate.fit(options[tried], values)
    means, stds = surrogate.predict(options, return_std=True)
    gain = means - max(values)
    ratio = gain / np.maximum(stds, 1e-12)
    improvement = gain * norm.cdf(ratio) + stds * norm.pdf(ratio)
    improvement[tried] = -np.inf
    next_index = int(improvement.argmax())
    tried.append(next_index)
    values.append(score(next_index))
best = int(np.argmax(values))
print(
    "Bayesian", round(10 ** options[tried[best], 0], 3), "MAE", round(-values[best], 3)
)
chosen_model = Ridge(alpha=10 ** options[tried[best], 0]).fit(X, y)
# 3. Apply the fitted model to the new CSV rows and print a result for each row.
new_rows = pd.read_csv(new_path)
print(
    new_rows.assign(
        prediction=chosen_model.predict(new_rows.to_numpy()).round(2)
    ).to_string(index=False)
)
