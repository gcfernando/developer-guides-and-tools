"""
Image embeddings

Summarize a drawing with two numeric measurements and use them to predict its direction.

Run: python lesson.py
Try changing direction from Upright to Sideways in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


def picture(direction, position):
    pixels = np.zeros((6, 6))
    if direction == "Sideways":
        pixels[position, 1:5] = 1
    else:
        pixels[1:5, position] = 1
    return pixels


def embedding(pixels):
    rows, columns = np.where(pixels > 0)
    return [float(np.std(rows)), float(np.std(columns))]


# 1. Read the CSV and check its inputs, including direction, position.
records = pd.read_csv(input_path)
labels = records["direction"].tolist()
images = [
    picture(row.direction, row.position) for row in records.itertuples(index=False)
]
training = [embedding(image) for image in images]
# 2. Read the new CSV rows, then apply the rules from the sample.
new_records = pd.read_csv(new_path)
new_images = [
    picture(row.direction, row.position) for row in new_records.itertuples(index=False)
]
new_image = new_images[0]
new_vector = embedding(new_image)


# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model = KNeighborsClassifier(n_neighbors=1).fit(training, labels)
guess = model.predict([new_vector])[0]
results = pd.DataFrame(
    [*training, new_vector], columns=["Vertical spread", "Horizontal spread"]
).round(2)
results["Label or prediction"] = [*labels, str(guess) + " (predicted)"]
print(results.to_string(index=False))

# 4. Plot the values so you can see how they compare.
fig, axes = plt.subplots(1, 3, figsize=(7.6, 3.2))
for ax, pixels, name in zip(
    axes,
    [images[0], images[2], new_image],
    ["Sideways training row", "Upright training row", f"New: {guess}"],
):
    ax.imshow(pixels, cmap="Blues", vmin=0, vmax=1)
    ax.set_title(name)
    ax.set_axis_off()
fig.tight_layout()
for chart_number in plt.get_fignums():
    plt.figure(chart_number).savefig(
        f"chart-{chart_number}.png", dpi=150, bbox_inches="tight"
    )
plt.show()
print(
    "Predicted direction for each new drawing:",
    model.predict([embedding(image) for image in new_images]).tolist(),
)
