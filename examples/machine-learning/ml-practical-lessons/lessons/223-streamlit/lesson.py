"""
Streamlit

Fill in a Streamlit form and see the delivery estimate change.

Run: python lesson.py
Enter distances of 5, 10 and 15 km with positive weights. The script fills out the sample form for each row.
"""

from pathlib import Path
from streamlit.testing.v1 import AppTest
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the training data for the form and fit a model in the local Streamlit app.
# 2. Teach the model from the training inputs and delivery time in minutes.
app = """
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

fields = ["distance_km", "weight_kg"]
training = pd.read_csv(r"__TRAINING_CSV__")
model = LinearRegression().fit(training[fields], training["delivery_minutes"])
st.title("Delivery time")
km = st.number_input("Distance in km", min_value=0.0, value=5.0)
kg = st.number_input("Weight in kg", min_value=0.1, value=2.0)
row = pd.DataFrame([[km, kg]], columns=fields)
st.write(f"Prediction: {model.predict(row)[0]:.1f} minutes")
"""
test = AppTest.from_string(
    app.replace('r"__TRAINING_CSV__"', repr(str(input_path)))
).run()
assert len(test.exception) == 0
print(test.markdown[0].value)

# 3. Send each new CSV row to the app and read the response.
for request in pd.read_csv(new_path).itertuples(index=False):
    test.number_input[0].set_value(float(request.distance_km))
    test.number_input[1].set_value(float(request.weight_kg))
    test.run()
    assert not test.exception
    print(request.distance_km, request.weight_kg, test.markdown[0].value)
