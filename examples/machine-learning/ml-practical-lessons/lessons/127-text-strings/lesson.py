"""
Text (strings)

Clean short text strings and turn their word counts into model inputs.

Run: python lesson.py
Change message in new_inputs.csv, for example from WHERE IS MY PARCEL!!! to The package never arrived.. Compare the printed rows.
"""

from pathlib import Path
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the support messages and their known categories.
messages = pd.read_csv(input_path)


# 2. Keep the same lowercase and punctuation rules for training and new messages.
def clean_message(text):
    lower = text.lower()
    words = re.sub(r"[^\w\s]|_", " ", lower)
    return " ".join(words.split())


before_after = pd.DataFrame(
    {
        "Original message": [messages.iloc[0]["message"]],
        "Cleaned message": [clean_message(messages.iloc[0]["message"])],
    }
)
print(before_after.to_string(index=False))


# 3. Set aside the check rows before the model learns.
training = messages.iloc[:6]
checking = messages.iloc[6:]
counts = CountVectorizer(preprocessor=clean_message)
# Learn the needed values here. New rows use transform with these saved values.
word_counts = counts.fit_transform(training["message"])
# 4. Teach the model from the training inputs and the known message category.
model = LogisticRegression().fit(word_counts, training["category"])
print("Check actual / predicted:", checking["category"].tolist(),
      model.predict(counts.transform(checking["message"])).tolist())


# 5. Apply the fitted model to the new CSV rows and print a result for each row.
raw_messages = pd.read_csv(new_path)["message"].tolist()
predictions = model.predict(counts.transform(raw_messages))
results = pd.DataFrame(
    {
        "Raw message": raw_messages,
        "Clean message": [clean_message(text) for text in raw_messages],
        "Prediction": predictions,
    }
)
print(results.to_string(index=False))
