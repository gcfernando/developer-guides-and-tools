"""
Fill missing values with mode

Fill an unknown signup flag with the most common training value before making a prediction.

Run: python lesson.py
Try Yes, 0 and an unknown value in new_inputs.csv.
"""

from pathlib import Path
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including signed_up, clicked.
data = pd.read_csv(input_path)


# 2. Give different spellings of the same value one consistent form.
known = {"yes": 1, "true": 1, "1": 1, "no": 0, "false": 0, "0": 0}
data["flag"] = data["signed_up"].str.strip().str.lower().map(known)
print(data[["signed_up", "flag"]].to_string(index=False))
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(SimpleImputer(strategy="most_frequent"), LogisticRegression())
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model.fit(data.iloc[:5][["flag"]], data.iloc[:5]["clicked"])
print("Imputed value:", model[0].transform(data.iloc[5:][["flag"]]).ravel().tolist())
print("Prediction:", model.predict(data.iloc[5:][["flag"]]).tolist())

# 4. Apply the fitted model to the new CSV rows and print a result for each row.
fresh = pd.read_csv(new_path)
fresh["flag"] = fresh["signed_up"].str.strip().str.lower().map(known)
fresh["prediction"] = model.predict(fresh[["flag"]])
print(fresh.to_string(index=False))
