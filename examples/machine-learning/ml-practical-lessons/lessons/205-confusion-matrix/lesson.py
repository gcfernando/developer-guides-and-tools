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

# 2. At the default cutoff, count each kind of right answer and mistake.
cutoff = float(pd.read_csv(folder / "new_inputs.csv")["cutoff"].iloc[0])
if not 0 <= cutoff <= 1:
    raise SystemExit("Set cutoff to a number from 0 to 1.")
predicted = risk >= cutoff
counts = confusion_matrix(test["answer"], predicted, labels=[0, 1])
table = pd.DataFrame(
    counts,
    index=["Actual regular", "Actual urgent"],
    columns=["Predicted regular", "Predicted urgent"],
)
print(table.to_string())
print(f"Missed urgent orders: {counts[1, 0]}. False alarms: {counts[0, 1]}.")

# 3. Save a labeled chart so you can locate the same cell visually.
fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
ax.imshow(counts, cmap="Blues")
ax.set(
    xticks=[0, 1],
    yticks=[0, 1],
    xticklabels=table.columns,
    yticklabels=table.index,
    title=f"Order decisions at cutoff {cutoff:g}",
)
for row in range(2):
    for col in range(2):
        ax.text(
            col,
            row,
            counts[row, col],
            ha="center",
            va="center",
            fontsize=17,
            color="white" if counts[row, col] >= counts.max() / 2 else "#172740",
        )
fig.savefig(folder / "confusion-matrix.png", dpi=200)
plt.close(fig)
