"""
Outliers

Look for unusual measurements in the invented shopper records and see which rows need checking.

Run: python lesson.py
Change annual_income or score in new_inputs.csv. Compare the new cluster with scaling turned on and off.
"""

from pathlib import Path
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the example records from sample.csv. The table uses the dataset fields shown below.
data = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
train, hold = data.iloc[:-1], data.iloc[-1:]
numbers = ["age", "annual_income", "score"]
print(train[numbers].quantile([0.05, 0.95]).to_string())
# 3. Read the new CSV rows, then apply the rules from the sample.
# 4. Give each method the same practice data so you can compare the results.
for scale in ["passthrough", StandardScaler()]:
    # An unfamiliar category can still pass through the encoder.
    # Give numeric inputs and categories their own preparation rules.
    prep = ColumnTransformer(
        [
            (
                "numeric",
                make_pipeline(SimpleImputer(strategy="median"), scale),
                numbers,
            ),
            ("region", OneHotEncoder(handle_unknown="ignore"), ["region"]),
        ]
    )
    # A pipeline keeps preparation and prediction together in the right order.
    model = make_pipeline(prep, KMeans(n_clusters=3, n_init=10, random_state=7))
    group = model.fit_predict(train)
    print(
        str(scale), train.assign(group=group).groupby("group")[numbers].mean().round(1)
    )
    print("New group:", model.predict(hold).tolist())
    # These are inputs someone can type into the app after training.
    fresh_rows = pd.read_csv(new_path)
    print(fresh_rows.assign(cluster=model.predict(fresh_rows)).to_string(index=False))
