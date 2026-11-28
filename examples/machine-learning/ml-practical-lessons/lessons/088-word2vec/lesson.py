"""
Word2Vec

Learn small word vectors from practice messages and average them to represent a new message.

Run: python lesson.py
Replace one message in new_inputs.csv. Include one delivery message and one billing message.
"""

from pathlib import Path
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import numpy as np
from gensim.models import Word2Vec

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the support messages and their known categories.
messages = pd.read_csv(input_path)


# 2. Set aside the check rows before the model learns.
train, hold = messages.iloc[:6], messages.iloc[6:]
tokens = CountVectorizer().build_analyzer()
embedding = Word2Vec(
    [tokens(text) for text in train["message"]],
    vector_size=8,
    min_count=1,
    workers=1,
    seed=7,
)


def encode(text):
    vectors = [embedding.wv[word] for word in tokens(text) if word in embedding.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(8)


train_vectors = np.vstack([encode(text) for text in train["message"]])
hold_vectors = np.vstack([encode(text) for text in hold["message"]])
# 3. Teach the model from the training inputs and the known message category.
model = LogisticRegression().fit(train_vectors, train["category"])
print("Training matrix:", train_vectors.shape)
print("Held-out predictions:", model.predict(hold_vectors).tolist())


# 4. Apply the fitted model to the new CSV rows and print a result for each row.
fresh = pd.read_csv(new_path)
fresh["predicted"] = model.predict(
    np.vstack([encode(text) for text in fresh["message"]])
)
print(fresh.to_string(index=False))
