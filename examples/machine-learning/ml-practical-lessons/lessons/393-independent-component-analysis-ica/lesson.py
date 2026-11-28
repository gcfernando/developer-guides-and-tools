"""
Independent Component Analysis (ICA)

Use independent component analysis to separate patterns mixed across the measured columns.

Run: python lesson.py
Change a measurement in new_inputs.csv. The fitted scaler and algorithm process each row.
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import FastICA

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including long, wide, score.
data = pd.read_csv(input_path)


scaler = StandardScaler()
# 2. Learn the conversion on the training inputs before applying it to a new row.
scaled = scaler.fit_transform(data[["long", "wide", "score"]])
model = FastICA(n_components=2, max_iter=1000, random_state=7)
# Learn the needed values here. New rows use transform with these saved values.
projected = model.fit_transform(scaled)
print("Output shape:", projected.shape)
print("First two rows:", projected[:2].round(2).tolist())


# 3. Apply the conversion learned from training to each new row.
fresh = pd.read_csv(new_path)
for values, result in zip(
    fresh.to_numpy(), model.transform(scaler.transform(fresh)).round(2)
):
    print(values, "->", result)
