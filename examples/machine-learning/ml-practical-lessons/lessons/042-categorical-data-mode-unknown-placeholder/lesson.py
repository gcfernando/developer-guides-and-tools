"""
Categorical Data: Mode, "Unknown" placeholder

Try the most common delivery zone and an explicit Unknown label for the same blank cell.

Run: python lesson.py
Change zone in new_inputs.csv, for example from ? to north. Compare the printed rows.
"""

from pathlib import Path
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including zone, minutes.
data = pd.read_csv(input_path, na_values=["?"])


# 2. Set aside the check rows before the model learns.
training = data.iloc[:4]
check = data.iloc[4:]
rows = []
# 3. Read the new CSV rows, then apply the rules from the sample.
# 4. Give each method the same practice data so you can compare the results.
for label, strategy in [("Mode", "most_frequent"), ("Explicit Unknown", "constant")]:
    fill = SimpleImputer(strategy=strategy, fill_value="Unknown")
    # An unfamiliar category can still pass through the encoder.
    encode = OneHotEncoder(handle_unknown="ignore")
    # A pipeline keeps preparation and prediction together in the right order.
    model = make_pipeline(fill, encode, LinearRegression())
    model.fit(training[["zone"]], training["minutes"])
    filled = fill.transform(check[["zone"]]).ravel()
    predicted = model.predict(check[["zone"]])
    # These are inputs someone can type into the app after training.
    fresh = pd.read_csv(new_path, na_values=["?"])
    print(
        label,
        fresh.assign(
            filled=fill.transform(fresh[["zone"]]).ravel(),
            minutes=model.predict(fresh[["zone"]]).round(2),
        ).to_string(index=False),
    )
    for index, (zone, minutes) in enumerate(zip(filled, predicted)):
        rows.append(
            [label, index + 5, zone, check.iloc[index]["minutes"], round(minutes, 1)]
        )
results = pd.DataFrame(
    rows,
    columns=[
        "Method",
        "Check row",
        "Zone sent to encoder",
        "Actual time (min)",
        "Predicted time (min)",
    ],
)
print(results.to_string(index=False))
