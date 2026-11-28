"""
Missing values

Find missing entries in the invented app listings and see how the example prepares them for a model.

Run: python lesson.py
Try changing price to $5 in new_inputs.csv. You can also compare the filled values or missing counts for the blank cells already in the sample.
"""

from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the example records from sample.csv. The table uses the dataset fields shown below.
data = pd.read_csv(input_path)


data["price"] = pd.to_numeric(data["price"].str.replace("$", "", regex=False))
data["installs"] = pd.to_numeric(data["installs"].str.replace(r"[,\+]", "", regex=True))
data["category"] = data["category"].fillna("unknown")
data["price_band"] = data["price"].gt(0).map({True: "paid", False: "free"})
data["rating_band"] = pd.cut(data["rating"], [0, 4, 5], labels=["at_most_4", "above_4"])
data["rating_band"] = data["rating_band"].astype(object).fillna("unknown")
# 2. Set aside the check rows before the model learns.
train, hold = data.iloc[:-1], data.iloc[-1:]
print("Missing ratings:", train["rating"].isna().sum())
print(
    train.nlargest(2, "installs")[["name", "price", "installs"]].to_string(index=False)
)
# An unfamiliar category can still pass through the encoder.
features = ColumnTransformer(
    [
        ("numeric", SimpleImputer(strategy="median"), ["price", "rating"]),
        (
            "category",
            OneHotEncoder(handle_unknown="ignore"),
            ["category", "price_band", "rating_band"],
        ),
    ]
)
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model = make_pipeline(features, LinearRegression()).fit(train, train["installs"])
print("Holdout forecast:", model.predict(hold).round(0).tolist())


# 4. Apply the fitted model to the new CSV rows and print a result for each row.
fresh_rows = pd.read_csv(new_path)
fresh_rows["price"] = pd.to_numeric(
    fresh_rows["price"].str.replace("$", "", regex=False)
)
fresh_rows["category"] = fresh_rows["category"].fillna("unknown")
fresh_rows["price_band"] = fresh_rows["price"].gt(0).map({True: "paid", False: "free"})
fresh_rows["rating_band"] = pd.cut(
    fresh_rows["rating"], [0, 4, 5], labels=["at_most_4", "above_4"]
)
fresh_rows["rating_band"] = fresh_rows["rating_band"].astype(object).fillna("unknown")
print(
    fresh_rows.assign(predicted_installs=model.predict(fresh_rows).round()).to_string(
        index=False
    )
)
