"""
Hierarchical Clustering

See which shoppers merge first by reading the clustering tree from bottom to top.

Run: python lesson.py
Add a shopper with age 32, income 40 and spending 57. Regenerate the tree and see which branch joins first.
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including age, income, spending.
data = pd.read_csv(input_path)


# Scale the full table before re-fitting the example to all of these rows.
values = StandardScaler().fit_transform(data)
model = AgglomerativeClustering(n_clusters=3)
# 2. Fit the model on the prepared training rows. Keep it for the checks below.
group = model.fit_predict(values)
print("Labels:", group.tolist())
print(data.assign(group=group).groupby("group").mean().round(1).to_string())


tree = linkage(values, method="ward")
# 3. Plot the values so you can see how they compare.
fig, ax = plt.subplots(figsize=(7, 4))
dendrogram(tree, labels=[f"Customer {i+1}" for i in range(len(data))], ax=ax)
ax.set(
    ylabel="Distance when groups join", title="Similar customers join near the bottom"
)
ax.tick_params(axis="x", labelrotation=35)
fig.tight_layout()
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()
