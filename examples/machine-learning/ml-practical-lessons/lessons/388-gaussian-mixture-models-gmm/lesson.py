"""
Gaussian Mixture Models (GMM)

Give each shopper a probability of belonging to each group.

Run: python lesson.py
Change a measurement in new_inputs.csv. The fitted scaler and algorithm process each row.
"""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including age, income, spending.
data = pd.read_csv(input_path)


scaler = StandardScaler()
# 2. Learn the conversion on the training inputs before applying it to a new row.
values = scaler.fit_transform(data)
model = GaussianMixture(n_components=3, random_state=7)
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
group = model.fit_predict(values)
print("Labels:", group.tolist())
print(data.assign(group=group).groupby("group").mean().round(1).to_string())
print(
    "First membership probabilities:", model.predict_proba(values[:1]).round(2).tolist()
)


# 4. Apply the fitted model to the new CSV rows and print a result for each row.
fresh = pd.read_csv(new_path)
for values, result in zip(
    fresh.to_numpy(), model.predict_proba(scaler.transform(fresh)).round(2)
):
    print(values, "->", result)
