"""
Set constraints & assumptions

Record the time, hardware and accuracy limits that affect your project.

Run: python lesson.py
Add one task to sample.csv with a decision, objective, metric, domain check and constraint. Look for it in the printed table.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the project brief. Each row lists one example project.
brief = pd.read_csv(input_path)
# 2. Print the result next to the input values so you can compare them.
print(brief[["use_case", "constraint"]].to_string(index=False))
print("First decision:", brief.loc[0, "use_case"])
