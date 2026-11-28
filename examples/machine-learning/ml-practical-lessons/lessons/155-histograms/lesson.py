"""
Histograms

Count how often each range of weights occurs.

Run: python lesson.py
Change one weight or delivery time in sample.csv. Check how the chart responds to the new row.
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
fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(data=data, x="weight", ax=ax)
ax.set_title("How often does each parcel weight occur?")
fig.tight_layout()
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()
