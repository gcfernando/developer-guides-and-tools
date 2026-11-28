"""
2.12. Fashion MNIST

Use pixels in each drawing from hand-drawn clothing shapes to estimate clothing type.

Run: python lesson.py
Edit new_inputs.csv. Within a picture, # is an on pixel, a dot is an off pixel, and / starts the next row.
"""

from pathlib import Path
import numpy as np
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the small drawings and their labels. Each slash separates two rows of pixels.
pictures = pd.read_csv(input_path, dtype={"label": str})
training = [
    (row.pixel_rows.split("/"), row.label)
    for row in pictures.itertuples()
    if row.split == "train"
]
hold = [
    (row.pixel_rows.split("/"), row.label)
    for row in pictures.itertuples()
    if row.split == "check"
]


# 2. Resize each picture and turn it into the same number of pixel values.
def prepare(pattern):
    pixels = np.array(
        [[255 if dot == "#" else 0 for dot in row] for row in pattern], dtype="uint8"
    )
    enlarged = Image.fromarray(pixels).resize((8, 8), Image.Resampling.NEAREST)
    return np.asarray(enlarged, dtype=float).reshape(-1) / 255


print("First raw sketch:", training[0][0])


print(
    "Blank images to inspect:",
    sum(not any("#" in line for line in grid) for grid, _ in training),
)
features = np.array([prepare(sketch) for sketch, _ in training])
labels = [label for _, label in training]
# 3. Fit the model on the prepared training rows. Keep it for the checks below.
model = KNeighborsClassifier(n_neighbors=1).fit(features, labels)
print("Model-input shape:", features.shape)
print("Pixel range:", features.min(), features.max())
print("Targets:", [label for _, label in hold])
print("Predictions:", model.predict([prepare(sketch) for sketch, _ in hold]).tolist())
encoder = OneHotEncoder(sparse_output=False)
# Learn the needed values here. New rows use transform with these saved values.
print(
    "First one-hot label:",
    encoder.fit_transform(np.array(labels).reshape(-1, 1))[0].tolist(),
)
# 4. Apply the fitted model to the new CSV rows and print a result for each row.
new_pictures = pd.read_csv(new_path)["pixel_rows"]
print(
    "New labels:",
    model.predict([prepare(grid.split("/")) for grid in new_pictures]).tolist(),
)
