"""
Convert Text to Numerical Representation

Compare plain word counts and weighted word counts for short messages.

Run: python lesson.py
Change message in new_inputs.csv, for example from The parcel is late! to WHERE ARE MY PACKAGES?. Compare the printed rows.
"""

from pathlib import Path
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the support messages and their known categories.
messages = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
train, hold = messages.iloc[:6], messages.iloc[6:]
# 3. Read the new CSV rows, then apply the rules from the sample.
# 4. Give each method the same practice data so you can compare the results.
for vectorizer in [CountVectorizer(), TfidfVectorizer()]:
    # A pipeline keeps preparation and prediction together in the right order.
    model = make_pipeline(vectorizer, LogisticRegression())
    model.fit(train["message"], train["category"])
    parcel = vectorizer.vocabulary_["parcel"]
    # Counting from the start of the table sets aside the same rows every run.
    value = vectorizer.transform(train["message"].iloc[:1])[0, parcel]
    print(
        type(vectorizer).__name__,
        "parcel feature:",
        round(value, 2),
        "predictions:",
        model.predict(hold["message"]).tolist(),
    )
    # These are inputs someone can type into the app after training.
    fresh = pd.read_csv(new_path)
    print(
        fresh.assign(predicted=model.predict(fresh["message"])).to_string(index=False)
    )
