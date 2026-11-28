"""
K-Means Classifier

Find clusters first, then use known labels to name each cluster.

Run: python lesson.py
Try changing x from 1.5 to 4 in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including x, y, label.
rows = pd.read_csv(input_path)
training = rows[["x", "y"]].to_numpy()


labels = rows["label"].to_numpy()
clusterer = KMeans(n_clusters=2, n_init=10, random_state=7).fit(training)
# 2. Match each cluster to the most common known label among its training rows.
mapping = {}
for cluster in range(2):
    values, counts = np.unique(labels[clusterer.labels_ == cluster], return_counts=True)
    mapping[cluster] = values[counts.argmax()]
# 3. Apply the fitted model to the new CSV rows and print a result for each row.
new_groups = clusterer.predict(pd.read_csv(new_path)[["x", "y"]].to_numpy())
print("Cluster IDs:", new_groups.tolist())
print("Mapped class predictions:", [mapping[group] for group in new_groups])
