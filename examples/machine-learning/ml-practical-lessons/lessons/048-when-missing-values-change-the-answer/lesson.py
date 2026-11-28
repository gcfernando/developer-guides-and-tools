"""
When missing values change the answer

See how losing the slower trips can make the average delivery time look too low.

Run: python lesson.py
Try changing True time from 12 to 16 in sample.csv. Compare the new output.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the CSV and check its inputs, including Route, True time, Recorded time.
data = pd.read_csv(input_path)


results = pd.DataFrame(
    {
        "Average uses": ["All six times", "Recorded times only"],
        "Average time (min)": [data["True time"].mean(), data["Recorded time"].mean()],
    }
)
# 2. Print the result next to the input values so you can compare them.
print(results.to_string(index=False))


# 3. Plot the values so you can see how they compare.
fig, ax = plt.subplots(figsize=(7, 3.5))
bars = ax.bar(
    results["Average uses"], results["Average time (min)"], color=["#226899", "#b86920"]
)
ax.bar_label(bars, fmt="%.1f", padding=4)
ax.set(
    ylabel="Average delivery time (min)",
    title="Missing slow trips change the average",
    ylim=(0, 30),
)
fig.tight_layout()
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()
