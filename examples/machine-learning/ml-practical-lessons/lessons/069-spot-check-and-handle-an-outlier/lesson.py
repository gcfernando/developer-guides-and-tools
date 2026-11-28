"""Review the 90 kg entry for parcel 5. Run with python lesson.py."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

folder = Path(__file__).resolve().parent

# 1. Open the delivery log. Keep the last parcel for a fair model check.
deliveries = pd.read_csv(folder / "sample.csv")
training = deliveries.iloc[:-1].copy()
check = deliveries.iloc[[-1]]
parcel_under_review = 5
is_parcel_5 = training["parcel"].eq(parcel_under_review)
recorded_kg = training.loc[is_parcel_5, "weight_kg"].item()

# 2. Learn the review limits from the middle half of the training weights.
lower_quarter = training["weight_kg"].quantile(0.25)
upper_quarter = training["weight_kg"].quantile(0.75)
middle_spread = upper_quarter - lower_quarter
lower_limit = lower_quarter - 1.5 * middle_spread
upper_limit = upper_quarter + 1.5 * middle_spread
flagged = training.loc[
    ~training["weight_kg"].between(lower_limit, upper_limit), ["parcel", "weight_kg"]
]
print(f"Training review range: {lower_limit:g} to {upper_limit:g} kg.")
print("Training records outside that range")
print(flagged.to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.scatter(deliveries["parcel"], deliveries["weight_kg"], color="#165eab")
ax.scatter([parcel_under_review], [recorded_kg], marker="D", color="#a94914", s=95)
ax.axhline(upper_limit, color="#165eab", linestyle="--", label="Upper review limit")
ax.set(xlabel="Parcel ID", ylabel="Recorded weight (kg)", title="Compare recorded weights")
ax.legend()
fig.savefig(folder / "review-weights.png", dpi=180)
plt.close(fig)

# 3. Look up parcel 5 on the original weighing slip.
# A blank cell, missing row or missing file leaves the weight unverified.
slip_file = folder / "weighing_slip.csv"
verified_kg = None
if slip_file.exists() and slip_file.stat().st_size:
    slip = pd.read_csv(slip_file)
    weights = slip.loc[slip["parcel"].eq(parcel_under_review), "verified_weight_kg"]
    if len(weights) == 1:
        weight = pd.to_numeric(weights, errors="coerce").item()
        if pd.notna(weight) and 0 < weight < float("inf"):
            verified_kg = weight

# 4. Follow the slip. A flag by itself cannot tell us the right weight.
reviewed = training.copy()
if verified_kg is None:
    decision = "FLAG"
    # Set the unverified row aside in this exercise until someone reweighs it.
    reviewed = reviewed.loc[~is_parcel_5]
    explanation = "Parcel 5 needs a source check. Set it aside for this model run."
elif verified_kg == recorded_kg:
    decision = "KEEP"
    explanation = f"The slip confirms {recorded_kg:g} kg. Keep the recorded weight."
else:
    decision = "CORRECT"
    reviewed["weight_kg"] = reviewed["weight_kg"].astype(float)
    reviewed.loc[is_parcel_5, "weight_kg"] = verified_kg
    explanation = f"The slip confirms {verified_kg:g} kg. Change {recorded_kg:g} kg to {verified_kg:g} kg."

print(f"\nDecision: {decision}")
print(explanation)

# 5. Ask both models about the same reserved parcel and compare with its actual time.
columns = ["weight_kg"]
actual = check["minutes"].item()
results = []
for name, rows in [("Original records", training), ("After source review", reviewed)]:
    model = LinearRegression().fit(rows[columns], rows["minutes"])
    estimate = model.predict(check[columns]).item()
    results.append([name, estimate, actual])

comparison = pd.DataFrame(results, columns=["Training data", "Predicted minutes", "Actual minutes"])
print("\nCheck parcel 8")
print(comparison.round(1).to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 3.7), layout="constrained")
bars = ax.barh(comparison["Training data"], comparison["Predicted minutes"],
              color=["#a94914", "#096f69"])
ax.bar_label(bars, fmt="%.1f", padding=5)
ax.axvline(actual, color="#172740", linestyle="--", label=f"Actual: {actual:g} min")
ax.set(xlabel="Predicted minutes", xlim=(0, max(actual, *comparison["Predicted minutes"]) * 1.30))
ax.legend()
fig.savefig(folder / "compare-estimates.png", dpi=180)
plt.close(fig)
print("Open review-weights.png and compare-estimates.png in this folder.")
