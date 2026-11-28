"""Choose a cutoff for alerts using validation orders."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    confusion_matrix,
    precision_recall_curve,
)

folder = Path(__file__).resolve().parent
data = pd.read_csv(folder / "sample.csv")
inputs = ["distance_km", "weight_kg", "rush_hour", "vehicle_load"]
train = data[data["split"] == "train"]
validation = data[data["split"] == "validation"]
test = data[data["split"] == "test"]
assert data["order_id"].is_unique
minimum_recall = pd.read_csv(folder / "new_inputs.csv")["min_recall"].item()
if not 0 < minimum_recall <= 1:
    raise SystemExit("Enter a minimum recall greater than 0 and at most 1.")

# 1. Teach a risk model on training orders. Compare against a no-alert rule.
model = LogisticRegression(max_iter=1000).fit(train[inputs], train["urgent"])
val_risk = model.predict_proba(validation[inputs])[:, 1]
prevalence = validation["urgent"].mean()
print(
    f"Validation urgent share: {prevalence:.1%}. Always silent accuracy: {1 - prevalence:.1%}; recall: 0%."
)

# 2. Use validation alone to choose the most precise cutoff that meets recall.
precision, recall, cutoffs = precision_recall_curve(validation["urgent"], val_risk)
choices = pd.DataFrame(
    {"Cutoff": cutoffs, "Precision": precision[:-1], "Recall": recall[:-1]}
)
eligible = choices[choices["Recall"] >= minimum_recall]
chosen = eligible.sort_values(["Precision", "Cutoff"], ascending=False).iloc[0]
cutoff = chosen["Cutoff"]
print(
    f"Validation choice: cutoff {cutoff:.3f}; precision {chosen['Precision']:.1%}; recall {chosen['Recall']:.1%}."
)

# 3. Freeze the cutoff and read the effect on the separate test orders.
risk = model.predict_proba(test[inputs])[:, 1]
rows = []
for name, threshold in [("Default", 0.5), ("Chosen on validation", cutoff)]:
    tn, fp, fn, tp = confusion_matrix(
        test["urgent"], risk >= threshold, labels=[0, 1]
    ).ravel()
    rows.append([name, threshold, tp, fn, fp, tp / max(1, tp + fp), tp / (tp + fn)])
summary = pd.DataFrame(
    rows,
    columns=[
        "Rule",
        "Cutoff",
        "Urgent caught",
        "Urgent missed",
        "False alarms",
        "Precision",
        "Recall",
    ],
)
print(summary.round(3).to_string(index=False))
print(
    f"Validation average precision: {average_precision_score(validation['urgent'], val_risk):.3f}"
)

# 4. Open the chart and find the chosen validation trade-off.
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.plot(recall, precision, color="#165eab", label="Validation model")
ax.axhline(prevalence, color="#637891", linestyle="--", label="Urgent share baseline")
ax.scatter(
    chosen["Recall"],
    chosen["Precision"],
    s=90,
    color="#a94914",
    label="Selected cutoff",
)
ax.set(
    xlabel="Recall: share of urgent orders found",
    ylabel="Precision: share of alerts truly urgent",
    title="Pick a trade-off before looking at the test",
)
ax.legend()
fig.savefig(folder / "precision-recall.png", dpi=200)
plt.close(fig)
