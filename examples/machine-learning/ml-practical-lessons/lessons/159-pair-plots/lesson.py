"""
Pair Plots

View several pairs of input columns at once.

Run: python lesson.py
Try changing distance from 2 to 6 in sample.csv. Compare the new output.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including distance, route_distance, weight.
data = pd.read_csv(input_path)


# 2. Print the result next to the input values so you can compare them.
print(data.agg(["mean", "median", "skew"]).round(2))
correlation = data.corr()
print("Distance overlap:", round(correlation.loc["distance", "route_distance"], 2))
# 3. Plot the values so you can see how they compare.
fig, axes = plt.subplots(2, 2, figsize=(9, 6))
sns.histplot(data=data, x="weight", ax=axes[0, 0])
sns.scatterplot(data=data, x="distance", y="minutes", ax=axes[0, 1])
sns.boxplot(data=data, x="weight", ax=axes[1, 0])
sns.heatmap(correlation, annot=True, vmin=-1, vmax=1, ax=axes[1, 1])
fig.tight_layout()
sns.pairplot(data[["distance", "weight", "minutes"]], diag_kind="hist")
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()
