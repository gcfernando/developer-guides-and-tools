"""
Geocoding APIs

Try a local address lookup and see how it handles an address outside its small list.

Run: python lesson.py
Change address in new_inputs.csv, for example from North Depot to Unknown Depot. Compare the printed rows.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the weights in kilograms and the delivery times in minutes.
rows = pd.read_csv(input_path)


places = pd.DataFrame(
    {
        "address": ["North Depot", "South Depot", "River Depot"],
        "latitude": [59.35, 59.28, 59.31],
        "longitude": [18.06, 18.02, 18.14],
    }
)
train = rows.merge(places, on="address", how="left").dropna()
fields = ["latitude", "longitude", "weight_kg"]


# 2. Teach the model from the training inputs and delivery time in minutes.
model = LinearRegression().fit(train[fields], train["minutes"])
# 3. Read the new CSV rows, then apply the rules from the sample.
fresh = pd.read_csv(new_path).merge(places, on="address", how="left")
# 4. Separate addresses with coordinates from those that need review.
known = fresh["latitude"].notna()
fresh["estimated_minutes"] = float("nan")
if known.any():
    fresh.loc[known, "estimated_minutes"] = model.predict(
        fresh.loc[known, fields]
    ).round(1)
print(fresh.to_string(index=False, na_rep="address needs review"))
