"""
BERT

Use a tiny BERT model to inspect how token vectors become one message vector.

Run: python lesson.py
Replace one message in new_inputs.csv. Include one delivery message and one billing message.
"""

from pathlib import Path
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import torch
from transformers import BertConfig, BertModel, BertTokenizer

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the support messages and their known categories.
messages = pd.read_csv(input_path)


torch.manual_seed(42)
# 2. Set aside the check rows before the model learns.
train, hold = messages.iloc[:6], messages.iloc[6:]
tokenize = CountVectorizer().build_analyzer()
words = sorted({word for text in train["message"] for word in tokenize(text)})
vocabulary = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"] + words
Path("tiny_vocab.txt").write_text("\n".join(vocabulary) + "\n", encoding="utf-8")
tokenizer = BertTokenizer(vocab_file="tiny_vocab.txt", do_lower_case=True)


bert = BertModel(
    BertConfig(
        vocab_size=len(tokenizer),
        hidden_size=16,
        num_hidden_layers=1,
        num_attention_heads=2,
        intermediate_size=32,
    )
).eval()


def vectors(texts):
    batch = tokenizer(texts.tolist(), padding=True, return_tensors="pt")
    with torch.no_grad():
        states = bert(**batch).last_hidden_state
    mask = batch["attention_mask"].unsqueeze(-1)
    return ((states * mask).sum(1) / mask.sum(1)).numpy()


train_vectors = vectors(train["message"])
# 3. Teach the model from the training inputs and the known message category.
model = LogisticRegression().fit(train_vectors, train["category"])
print("Training matrix:", train_vectors.shape)
print("Held-out predictions:", model.predict(vectors(hold["message"])).tolist())


# 4. Apply the fitted model to the new CSV rows and print a result for each row.
fresh = pd.read_csv(new_path)
fresh["predicted"] = model.predict(vectors(fresh["message"]))
print(fresh.to_string(index=False))
