"""
Label Encoding (For Ordered Categories)

Turn Low, Medium and High into ordered numbers before predicting a review action.

Run: python lesson.py
Try changing priority from Low to High in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including priority, action.
data = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
train, hold = data.iloc[:6], data.iloc[6:]
labels = LabelEncoder().fit(train["action"])
ordinal = OrdinalEncoder(categories=[["Low", "Medium", "High"]])
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(ordinal, LogisticRegression())
# 3. Teach the model which review action matches each ordered priority.
model.fit(train[["priority"]], labels.transform(train["action"]))
print(
    "Priority codes:",
    ordinal.transform(train.iloc[[0, 2, 4]][["priority"]]).ravel().tolist(),
)
print(
    "Held-out label:",
    labels.inverse_transform(model.predict(hold[["priority"]])).tolist(),
)


# 4. Apply the fitted model to the new CSV rows and print a result for each row.
fresh = pd.read_csv(new_path)
fresh["action"] = labels.inverse_transform(model.predict(fresh[["priority"]]))
print(fresh.to_string(index=False))
