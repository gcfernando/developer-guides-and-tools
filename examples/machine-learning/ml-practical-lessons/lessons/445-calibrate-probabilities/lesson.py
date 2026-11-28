"""Compare raw probabilities with probabilities adjusted using validation answers."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.calibration import CalibratedClassifierCV, CalibrationDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.frozen import FrozenEstimator
from sklearn.metrics import brier_score_loss

folder = Path(__file__).resolve().parent
data = pd.read_csv(folder / "sample.csv")
inputs = ["distance_km", "weight_kg", "rush_hour", "vehicle_load"]
train = data[data["split"] == "train"]
calibration = data[data["split"] == "validation"]
test = data[data["split"] == "test"]
assert data["order_id"].is_unique
bins = int(pd.read_csv(folder / "new_inputs.csv")["bins"].item())
if not 2 <= bins <= 12:
    raise SystemExit("Pick between 2 and 12 bins.")

# 1. Fit the classifier on training orders and freeze it.
base = RandomForestClassifier(n_estimators=70, max_depth=8, random_state=7)
base.fit(train[inputs], train["urgent"])

# 2. Learn the probability adjustment from separate validation orders.
adjusted = CalibratedClassifierCV(FrozenEstimator(base), method="sigmoid")
adjusted.fit(calibration[inputs], calibration["urgent"])

# 3. Compare both probability columns on the same test orders.
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
for name, model in [("Raw forest", base), ("Adjusted forest", adjusted)]:
    risk = model.predict_proba(test[inputs])[:, 1]
    score = brier_score_loss(test["urgent"], risk)
    print(f"{name} test Brier score: {score:.4f}")
    CalibrationDisplay.from_predictions(
        test["urgent"], risk, n_bins=bins, strategy="quantile", name=name, ax=ax
    )
ax.set_title("Compare predicted probability with what happened")
fig.savefig(folder / "calibration.png", dpi=200)
plt.close(fig)
print(
    "Lower Brier score is better on this probability check. Changing bins changes the visual, not the score."
)
