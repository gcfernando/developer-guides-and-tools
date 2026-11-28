"""
Extract XML fields

Read relevant fields from an XML record and compare them with the tabular version.

Run: python lesson.py
Change address in sample.csv, for example from Depot North to Depot South. Compare the printed rows.
"""

from pathlib import Path
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from xml.etree import ElementTree

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the weights in kilograms and the delivery times in minutes.
shipments = pd.read_csv(input_path)
records = []
for row in shipments.itertuples(index=False):
    parcel = {} if pd.isna(row.weight_kg) else {"kg": row.weight_kg}
    records.append({"address": row.address, "parcel": parcel, "minutes": row.minutes})
rows = pd.json_normalize(records)
geo = {"Depot North": (59.35, 18.05), "Depot South": (59.28, 18.02)}
coordinates = rows["address"].map(geo)
rows["latitude"] = coordinates.str[0]
rows["longitude"] = coordinates.str[1]
# 2. Print the result next to the input values so you can compare them.
print(rows.to_string(index=False))
assert rows["latitude"].dropna().between(-90, 90).all()
assert rows["longitude"].dropna().between(-180, 180).all()

xml = ElementTree.fromstring("<parcel><kg>2</kg></parcel>")
print("XML weight:", float(xml.findtext("kg")))
fields = ["parcel.kg", "latitude"]
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(SimpleImputer(strategy="median"), LinearRegression())
# 3. Teach the model from the training inputs and delivery time in minutes.
model.fit(rows.iloc[:3][fields], rows.iloc[:3]["minutes"])
print("Held-out estimate:", model.predict(rows.iloc[3:][fields]).round(1).tolist())
