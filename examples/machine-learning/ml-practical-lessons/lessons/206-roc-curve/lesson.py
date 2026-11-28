from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

folder = Path(__file__).resolve().parent
data = pd.read_csv(folder / "sample.csv")
inputs = ["distance", "weight"]

# 1. Set the test rows aside before fitting the classifier.
training, test = train_test_split(
    data, test_size=0.25, stratify=data["answer"], random_state=7
)

# Keep the test orders. Training may use only distance-and-weight pairs absent from test.
# Special check for this example: test on exact input combinations absent from training.
# Equal values alone do not mean copied records. This check asks a narrower question
# than predicting independent orders from the same setting. See lesson 442.
test_pairs = pd.MultiIndex.from_frame(test[inputs])
training_pairs = pd.MultiIndex.from_frame(training[inputs])
training = training.loc[~training_pairs.isin(test_pairs)]
assert not pd.MultiIndex.from_frame(training[inputs]).isin(test_pairs).any()

# Give the classifier the two input columns and their known urgency labels.
model = LogisticRegression().fit(training[inputs], training["answer"])
risk = model.predict_proba(test[inputs])[:, 1]

from sklearn.metrics import roc_curve, roc_auc_score

# 2. Check the same test orders at both supplied cutoffs.
cutoffs = pd.read_csv(folder / "new_inputs.csv")["cutoff"]
if not cutoffs.between(0, 1).all():
    raise SystemExit("Cutoffs must be numbers from 0 to 1.")
results = []
for cutoff in cutoffs:
    tn, fp, fn, tp = confusion_matrix(
        test["answer"], risk >= cutoff, labels=[0, 1]
    ).ravel()
    results.append([cutoff, tp, fn, fp, tp / (tp + fn), fp / (fp + tn)])
table = pd.DataFrame(
    results,
    columns=[
        "Cutoff",
        "Urgent caught",
        "Urgent missed",
        "False alarms",
        "Urgent recall",
        "False alarm rate",
    ],
)
print(table.round(3).to_string(index=False))
print("AUC-ROC:", round(roc_auc_score(test["answer"], risk), 3))
print(
    "Here the test cutoffs are fixed for teaching. Choose an app cutoff on validation data."
)

# 3. Mark those two choices on the curve.
false_alarm_rate, recall, _ = roc_curve(test["answer"], risk)
fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
ax.plot(false_alarm_rate, recall, color="#165eab", label="All cutoffs")
ax.plot([0, 1], [0, 1], linestyle="--", color="#637891", label="Chance ranking")
for row in table.itertuples(index=False, name=None):
    cutoff, _, _, _, true_rate, false_rate = row
    ax.scatter(false_rate, true_rate, s=65, color="#a94914")
    ax.annotate(
        f"{cutoff:g}",
        (false_rate, true_rate),
        xytext=(7, -12),
        textcoords="offset points",
    )
ax.set(
    xlabel="False alarm rate",
    ylabel="Urgent-order recall",
    title="Trade-off at two cutoffs",
)
ax.legend(loc="lower right")
fig.savefig(folder / "roc-cutoffs.png", dpi=200)
plt.close(fig)
