"""
t-Distributed Stochastic Neighbor Embedding (t-SNE)

Draw similar rows near one another in a two-dimensional plot.

Run: python lesson.py
Add or edit a row in sample.csv, then rerun to refit. This method works on the whole group of rows.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including long, wide, score.
data = pd.read_csv(input_path)


# 2. Learn the conversion on the training inputs before applying it to a new row.
scaled = StandardScaler().fit_transform(data[["long", "wide", "score"]])
# Scale the full table before re-fitting the example to all of these rows.
projected = TSNE(
    n_components=2, perplexity=3, init="random", random_state=7
).fit_transform(scaled)
# 3. Plot the values so you can see how they compare.
plt.scatter(projected[:, 0], projected[:, 1])
plt.title("t-SNE of original measurements")
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()
print("Output shape:", projected.shape)
print("First two rows:", projected[:2].round(2).tolist())
