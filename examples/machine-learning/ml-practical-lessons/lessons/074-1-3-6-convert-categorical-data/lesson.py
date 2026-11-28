"""
1.3.6 Convert Categorical Data

Turn labels such as color into numerical columns a model can read.

Run: python lesson.py
In new_inputs.csv, enter Red, Blue and an unfamiliar color such as Purple. See the encoded columns and predicted orders for each one.
"""

from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including color, orders.
products = pd.read_csv(input_path)
# 2. Set aside the check rows before the model learns.
training = products.iloc[:6]
checking = products.iloc[6:]


# An unfamiliar category can still pass through the encoder.
encoder = OneHotEncoder(
    categories=[["Red", "Blue", "Green"]], handle_unknown="ignore", sparse_output=False
)
# 3. Learn the conversion on the training inputs before applying it to a new row.
training_bits = encoder.fit_transform(training[["color"]])
colors = pd.DataFrame({"color": ["Red", "Blue", "Green", "Purple"]})
bits = encoder.transform(colors).astype(int)
encoding_table = pd.DataFrame(bits, columns=["Red", "Blue", "Green"])
encoding_table.insert(0, "Original color", colors["color"])


# 4. Teach the model from the training inputs and the recorded order count.
model = LinearRegression().fit(training_bits, training["orders"])
print("Check actual / predicted:", checking["orders"].tolist(),
      model.predict(encoder.transform(checking[["color"]])).round(1).tolist())
# 5. Apply the fitted model to the new CSV rows and print a result for each row.
test_colors = pd.read_csv(new_path)
fresh_bits = encoder.transform(test_colors)
estimates = model.predict(fresh_bits)
results = test_colors.copy()
results[["Red", "Blue", "Green"]] = fresh_bits.astype(int)
results["Predicted orders"] = estimates.round(1)
print(encoding_table.to_string(index=False))
print(results.to_string(index=False))
