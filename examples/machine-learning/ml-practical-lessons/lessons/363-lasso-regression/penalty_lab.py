"""Compare penalty settings using validation, then check one frozen choice.

Run: python penalty_lab.py
Reads the supplied sample.csv. Writes coefficient-check.csv for the lesson chart.
The special grouped split keeps identical input pairs together. This tests new
input combinations, rather than implying equal measurements are duplicates.
"""
from pathlib import Path
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

FOLDER = Path(__file__).resolve().parent
INPUTS = ["km", "kg"]


def run_lab():
    data = pd.read_csv(FOLDER / "sample.csv")
    groups = pd.MultiIndex.from_frame(data[INPUTS]).factorize()[0]
    # 1. Reserve a final group check. Its answers do not select a setting.
    split = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=7)
    learn_positions, test_positions = next(split.split(data, groups=groups))
    learning, test = data.iloc[learn_positions], data.iloc[test_positions]
    # 2. Keep separate groups for choosing alpha inside the learning portion.
    choose = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=11)
    train_pos, val_pos = next(choose.split(learning, groups=groups[learn_positions]))
    train, validation = learning.iloc[train_pos], learning.iloc[val_pos]
    print(f"Rows: training {len(train)}, validation {len(validation)}, test {len(test)}.")
    print("The split asks about new distance/weight combinations.")
    rows, fitted = [], {}
    candidates = [("No penalty", 0.0, LinearRegression())]
    for method in (Ridge, Lasso):
        for alpha in (0.01, 0.1, 1.0, 10.0, 100.0):
            candidates.append((method.__name__, alpha, method(alpha=alpha, max_iter=10000)))
    for method, alpha, estimator in candidates:
        # 3. The scaler learns only the training mean and spread.
        model = make_pipeline(StandardScaler(), estimator)
        model.fit(train[INPUTS], train["minutes"])
        validation_mae = mean_absolute_error(
            validation["minutes"], model.predict(validation[INPUTS])
        )
        # Coefficients now refer to a one-training-SD change, in minutes.
        km_weight, kg_weight = model[-1].coef_
        rows.append([method, alpha, km_weight, kg_weight, validation_mae])
        fitted[method, alpha] = model
    result = pd.DataFrame(rows, columns=[
        "method", "alpha", "km_coefficient", "kg_coefficient", "validation_mae_minutes"
    ])
    result.to_csv(FOLDER / "coefficient-check.csv", index=False)
    print("Coefficients: minutes per one training-standard-deviation input increase.")
    print(result.round(3).to_string(index=False))
    # 4. Choose from validation only, then inspect the final test once.
    best = result.sort_values(["validation_mae_minutes", "method", "alpha"]).iloc[0]
    winner = fitted[best["method"], best["alpha"]]
    test_mae = mean_absolute_error(test["minutes"], winner.predict(test[INPUTS]))
    print(f"Validation choice: {best['method']}, alpha {best['alpha']:g}.")
    print(f"Frozen-choice test MAE: {test_mae:.3f} minutes.")
    print("A smaller coefficient is not automatically a better validation result.")
    print("A zero coefficient does not prove that the field never matters.")
    return result


if __name__ == "__main__":
    run_lab()
