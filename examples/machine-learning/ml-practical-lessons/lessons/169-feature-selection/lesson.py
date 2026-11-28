"""
Feature Selection

Choose useful input columns, then see how the choice affects predictions.

Run: python lesson.py
Try changing id from 0 to 2 in sample.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including id, minutes, duplicate_minutes.
data = pd.read_csv(input_path)


# 2. Give each method the same practice data so you can compare the results.
for name, statistic in [("ANOVA", f_classif), ("Chi-square", chi2)]:
    # ANOVA uses a continuous measurement. Chi-square uses an indicator here.
    fields = ["minutes", "keyword"] if name == "ANOVA" else ["keyword"]
    features = data[fields]
    selector = SelectKBest(statistic, k=1)
    # A pipeline keeps preparation and prediction together in the right order.
    model = make_pipeline(selector, LogisticRegression())
    # Counting from the start of the table sets aside the same rows every run.
    model.fit(features.iloc[:6], data["review"].iloc[:6])
    print(name, "selected:", features.columns[selector.get_support()].tolist())
    print("Held-out labels:", model.predict(features.iloc[6:]).tolist())
