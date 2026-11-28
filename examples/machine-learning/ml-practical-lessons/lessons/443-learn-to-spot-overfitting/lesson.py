"""Use a validation curve to see when a tree starts memorizing the practice deliveries."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

folder = Path(__file__).resolve().parent
data = pd.read_csv(folder / "sample.csv")
train = data[data["split"] == "train"]
validation = data[data["split"] == "validation"]
test = data[data["split"] == "test"]
depths = pd.read_csv(folder / "new_inputs.csv")["depth"].tolist()
inputs = ["distance_km"]

# 1. Fit a tree at each depth. Use the same validation orders each time.
scores = []
for depth in depths:
    model = DecisionTreeRegressor(max_depth=depth, random_state=7)
    model.fit(train[inputs], train["actual_minutes"])
    train_mae = mean_absolute_error(
        train["actual_minutes"], model.predict(train[inputs])
    )
    val_mae = mean_absolute_error(
        validation["actual_minutes"], model.predict(validation[inputs])
    )
    scores.append([depth, train_mae, val_mae])

# 2. Read the two lines. A lower training error can come with a higher validation error.
curve = pd.DataFrame(
    scores, columns=["Depth", "Training MAE", "Validation MAE"]
).sort_values("Depth")
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.plot(curve["Depth"], curve["Training MAE"], "o-", color="#165eab", label="Training")
ax.plot(
    curve["Depth"], curve["Validation MAE"], "s-", color="#a94914", label="Validation"
)
ax.set(
    xlabel="Maximum tree depth",
    ylabel="Mean absolute error (minutes)",
    title="Training error can keep falling while validation error rises",
)
ax.legend()
fig.savefig(folder / "validation-curve.png", dpi=200)
plt.close(fig)
print(curve.round(2).to_string(index=False))

# 3. Pick a depth on validation. Check that tree on the test rows once.
winner = int(curve.sort_values(["Validation MAE", "Depth"]).iloc[0]["Depth"])
final = DecisionTreeRegressor(max_depth=winner, random_state=7).fit(
    train[inputs], train["actual_minutes"]
)
error = mean_absolute_error(test["actual_minutes"], final.predict(test[inputs]))
print(f"Selected depth: {winner}. Test MAE: {error:.2f} minutes.")
print(
    "Open validation-curve.png. The vertical gap measures how differently the two sets behaved."
)
