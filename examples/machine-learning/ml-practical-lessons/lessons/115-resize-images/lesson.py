"""
Resize images

Resize training and test pictures to the same dimensions.

Run: python lesson.py
Edit the red, green, and blue numbers (0–255) in new_inputs.csv to predict dark or light.
"""

from pathlib import Path
import numpy as np
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


def pixels(color):
    image = Image.new("RGB", (6, 6), color)
    gray = image.convert("L").resize((4, 4))
    return np.asarray(gray, dtype=float).reshape(-1) / 255


# 1. Read the CSV and check its inputs, including red, green, blue.
training = pd.read_csv(input_path)
channels = ["red", "green", "blue"]
colors = list(training[channels].itertuples(index=False, name=None))
features = np.array([pixels(color) for color in colors])
# 2. Fit the model on the prepared training rows. Keep it for the checks below.
model = KNeighborsClassifier(n_neighbors=1).fit(features, training["label"])
print("Image matrix becomes one row:", features.shape)
print("First normalized pixels:", features[0, :4].round(3).tolist())
# 3. Apply the fitted model to the new CSV rows and print a result for each row.
print(
    "New picture:",
    model.predict(
        [
            pixels(color)
            for color in pd.read_csv(new_path)[channels].itertuples(
                index=False, name=None
            )
        ]
    ).tolist(),
)
