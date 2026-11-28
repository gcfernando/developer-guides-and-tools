"""
Tokenization & Lemmatization

Split sentences into words and bring a few word variants back to the same form.

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


lemmas = {
    "parcels": "parcel",
    "packages": "package",
    "charged": "charge",
    "charges": "charge",
}


# 2. Split text into words, then look up each word’s usual form.
def tokenize_and_lemmatize(text):
    words = re.findall(r"[a-z]+", text.lower())
    return [lemmas.get(word, word) for word in words]


print("Tokens:", tokenize_and_lemmatize("Late PARCELS and two charges!"))
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(
    CountVectorizer(tokenizer=tokenize_and_lemmatize, token_pattern=None),
    LogisticRegression(),
)

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
