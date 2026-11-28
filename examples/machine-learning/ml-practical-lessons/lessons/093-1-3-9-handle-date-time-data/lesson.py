"""
1.3.9 Handle Date/Time Data

Read written dates and timestamps so Python can use them consistently.

Run: python lesson.py
Change raw_date in sample.csv, for example from 02/03/2025 to invalid. Compare the printed rows.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the raw date strings, including different formats and an invalid value.
raw = pd.read_csv(input_path, dtype=str)["raw_date"]


single = pd.to_datetime(raw, format="%m/%d/%Y", errors="coerce")
iso = pd.to_datetime(raw, format="%Y-%m-%d", errors="coerce")
parsed = single.fillna(iso)
seconds = pd.to_numeric(raw, errors="coerce")
unix = pd.to_datetime(seconds, unit="s", errors="coerce", utc=True).dt.tz_localize(None)
parsed = parsed.fillna(unix)
# 2. Print the result next to the input values so you can compare them.
print(parsed.dt.strftime("%Y-%m-%d").fillna("invalid date").tolist())
