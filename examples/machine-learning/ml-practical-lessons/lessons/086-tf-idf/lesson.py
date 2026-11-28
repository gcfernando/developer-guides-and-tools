"""
TF-IDF

Make words that stand out across messages count more than words that appear everywhere.

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
# 3. Learn the vocabulary and see how this vectorizer represents one word.
# 4. Use the same fitted vectorizer for the check and new messages.
for vectorizer in [TfidfVectorizer()]:
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
