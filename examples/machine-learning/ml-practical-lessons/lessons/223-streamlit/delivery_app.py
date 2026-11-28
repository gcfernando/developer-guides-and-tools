import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

fields = ["distance_km", "weight_kg"]
from pathlib import Path
training = pd.read_csv(Path(__file__).resolve().with_name("sample.csv"))
model = LinearRegression().fit(training[fields], training["delivery_minutes"])
st.title("Delivery time")
km = st.number_input("Distance in km", min_value=0.0, value=5.0)
kg = st.number_input("Weight in kg", min_value=0.1, value=2.0)
row = pd.DataFrame([[km, kg]], columns=fields)
st.write(f"Prediction: {model.predict(row)[0]:.1f} minutes")
