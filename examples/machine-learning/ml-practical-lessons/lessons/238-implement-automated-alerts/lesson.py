"""
Implement automated alerts

Raise a local alert if accuracy falls or the input data changes too much.

Run: python lesson.py
Try changing km from 19 to 14 in sample.csv. Compare the new output.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the labeled batches so you can compare the model’s results over time.
batches = pd.read_csv(input_path)


historical = batches[batches["batch"] == "historical"]


recent = batches[batches["batch"] == "recent"]
future = batches[batches["batch"] == "future"]
# 2. Teach the model from the training inputs and whether the delivery was late.
live = DecisionTreeClassifier(max_depth=2, random_state=7).fit(
    historical[["km"]], historical["late"]
)
reference = batches[batches["batch"] == "reference"]
baseline = live.score(reference[["km"]], reference["late"])
recent_score = live.score(recent[["km"]], recent["late"])
drift = recent["km"].median() - historical["km"].median()
print("Recent accuracy:", round(recent_score, 2), "median km change:", drift)
if recent_score < 0.8 or abs(drift) > 5:
    print("ALERT: investigate before promoting a candidate.")
candidate = DecisionTreeClassifier(max_depth=2, random_state=7).fit(
    recent[["km"]], recent["late"]
)


print(
    "Later batch, live / candidate:",
    live.score(future[["km"]], future["late"]),
    candidate.score(future[["km"]], future["late"]),
)

# 3. Plot the values so you can see how they compare.
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
sns.ecdfplot(data=historical, x="km", label="historical", ax=axes[0])
sns.ecdfplot(data=recent, x="km", label="recent", ax=axes[0])
axes[0].legend()
report = pd.DataFrame(
    {"batch": ["historical reference", "recent"], "accuracy": [baseline, recent_score]}
)
sns.barplot(data=report, x="batch", y="accuracy", ax=axes[1])
report.to_csv("monitoring.csv", index=False)
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()
