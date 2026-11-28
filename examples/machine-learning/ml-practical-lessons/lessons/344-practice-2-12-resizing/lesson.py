"""Resizing a hand-drawn clothing picture."""

from pathlib import Path
import numpy as np
import pandas as pd
from PIL import Image

folder = Path(__file__).resolve().parent
pictures = pd.read_csv(folder / "sample.csv")
options = pd.read_csv(folder / "new_inputs.csv")

# 1. Read the first drawing and turn lit pixels into 255, with 0 for dark pixels.
lines = pictures.loc[0, "pixel_rows"].split("/")
original = np.array(
    [[255 if letter == "#" else 0 for letter in line] for line in lines], dtype="uint8"
)

# 2. Apply the same input setting you can change in the CSV.

side = int(options.loc[0, "side"])
resized = np.asarray(
    Image.fromarray(original).resize((side, side), Image.Resampling.NEAREST)
)
print(f"Original picture: {original.shape[1]} columns by {original.shape[0]} rows.")
print(f"Resized picture: {resized.shape[1]} columns by {resized.shape[0]} rows.")
print(f"Pixel count: {original.size} before, {resized.size} after.")
