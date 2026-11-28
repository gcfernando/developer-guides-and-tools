"""
Handle missing dates using interpolation

Estimate a missing time-series reading from the readings on either side.

Run: python lesson.py
In sample.csv, change orders for 2025-02-03 from 16 to 18. The February 2 estimate becomes 14.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including day, orders.
data = pd.read_csv(input_path, parse_dates=["day"])
if data["day"].duplicated().any():
    raise SystemExit("Keep one reading per date for this exercise. Restore the original CSV if needed.")
daily = data.set_index("day")["orders"].asfreq("D")
# 2. Print the result next to the input values so you can compare them.
print(
    pd.DataFrame({"observed": daily, "interpolated": daily.interpolate(method="time")})
)
