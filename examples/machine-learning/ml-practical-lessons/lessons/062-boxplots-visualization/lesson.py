"""
Boxplots & Visualization

Find a weight far from the others on a boxplot.

Run: python lesson.py
Compare 80 kg with 8 kg. Change or add a measured weight in sample.csv, then look for the flag and the boxplot.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including weight_kg.
weight = pd.read_csv(input_path)["weight_kg"]


# 2. Find where the middle values sit, then compare the remaining rows with those limits.
q1, q3 = weight.quantile([0.25, 0.75])
iqr = q3 - q1
spread = weight.std(ddof=0)
# Constant weights produce no z-score flags in this exercise.
z = (weight - weight.mean()) / spread if spread > 0 else weight * 0.0
flags = pd.DataFrame(
    {
        "weight_kg": weight,
        "Z-score": z.abs() > 3,
        "IQR": ~weight.between(q1 - 1.5 * iqr, q3 + 1.5 * iqr),
    }
)
print(flags.loc[flags["Z-score"] | flags["IQR"]].to_string(index=False))
# 3. Plot the values so you can see how they compare.
plt.boxplot(weight)
plt.ylabel("Weight in kg")
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()
