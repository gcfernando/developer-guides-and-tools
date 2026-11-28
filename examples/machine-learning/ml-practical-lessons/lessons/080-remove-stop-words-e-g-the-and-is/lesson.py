"""
Remove stop words (e.g., "the", "and", "is")

Drop selected common words such as the and is, then test a delivery or billing message.

Run: python lesson.py
Replace one message in new_inputs.csv. Include one delivery message and one billing message.
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


stop_words = ["the", "and", "is"]
vectorizer = CountVectorizer(stop_words=stop_words)
example = "The parcel is not here and I am waiting!"
# 2. Print the result next to the input values so you can compare them.
print("Before:", CountVectorizer().build_analyzer()(example))
print("After:", vectorizer.build_analyzer()(example))
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(vectorizer, LogisticRegression())

# 3. Set aside the check rows before the model learns.
train = messages.iloc[:6]
test = messages.iloc[6:]
# 4. Teach the model from the training inputs and the known message category.
model.fit(train["message"], train["category"])
print("Actual:", test["category"].tolist())
print("Predicted:", model.predict(test["message"]).tolist())


# 5. Apply the fitted model to the new CSV rows and print a result for each row.
fresh = pd.read_csv(new_path)
fresh["predicted"] = model.predict(fresh["message"])
print(fresh.to_string(index=False))
