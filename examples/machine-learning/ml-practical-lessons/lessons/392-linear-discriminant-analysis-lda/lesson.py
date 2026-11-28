"""
Linear Discriminant Analysis (LDA)

Use known group labels to build a smaller set of measurements that separates the groups.

Run: python lesson.py
Change long, wide or score in one new row. Compare the resulting projection with the training projections.
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including long, wide, score.
data = pd.read_csv(input_path)


scaler = StandardScaler()
# 2. Learn the conversion on the training inputs before applying it to a new row.
scaled = scaler.fit_transform(data[["long", "wide", "score"]])
model = LinearDiscriminantAnalysis(n_components=1)
# Learn the needed values here. New rows use transform with these saved values.
projected = model.fit_transform(scaled, data["group"])
print("Training class predictions:", model.predict(scaled).tolist())
print("Output shape:", projected.shape)
print("First two rows:", projected[:2].round(2).tolist())


# 3. Apply the conversion learned from training to each new row.
fresh = pd.read_csv(new_path)
for values, result in zip(
    fresh.to_numpy(), model.transform(scaler.transform(fresh)).round(2)
):
    print(values, "->", result)
