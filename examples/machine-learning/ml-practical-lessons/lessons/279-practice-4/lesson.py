"""
Practice

Use sepal and petal measurements from invented flower measurements to estimate flower type.

Run: python lesson.py
Change an input in new_inputs.csv. Compare the predictions with the held-out check above.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the example records from sample.csv. The table uses the dataset fields shown below.
data = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
train, hold = data.iloc[:6], data.iloc[6:]
fields = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
# 3. Find where the middle values sit, then compare the remaining rows with those limits.
q1 = train[fields].quantile(0.25)
q3 = train[fields].quantile(0.75)
spread = q3 - q1
flags = train[fields].lt(q1 - 1.5 * spread) | train[fields].gt(q3 + 1.5 * spread)
print("Flower measurements to review:", flags.sum().to_dict())
# 4. Plot the values so you can see how they compare.
sns.pairplot(train, vars=fields, hue="species", diag_kind="hist")
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()
labels = LabelEncoder().fit(train["species"])
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=1))
# 5. Teach the model from the training inputs and the known flower type.
model.fit(train[fields], labels.transform(train["species"]))
print("Actual:", hold["species"].tolist())
print("Predicted:", labels.inverse_transform(model.predict(hold[fields])).tolist())


# 6. Apply the fitted model to the new CSV rows and print a result for each row.
fresh_rows = pd.read_csv(new_path)
print(
    fresh_rows.assign(
        prediction=labels.inverse_transform(model.predict(fresh_rows[fields]))
    ).to_string(index=False)
)
