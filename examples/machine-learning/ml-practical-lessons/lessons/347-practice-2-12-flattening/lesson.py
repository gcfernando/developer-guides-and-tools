"""Flattening a hand-drawn clothing picture."""

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

order = options.loc[0, "order"].upper()
if order not in {"C", "F"}:
    raise SystemExit("Use C for row order or F for column order.")
flat = original.ravel(order=order)
restored = flat.reshape(original.shape, order=order)
assert np.array_equal(original, restored)
print(f"Original shape: {original.shape}. Flattened shape: {flat.shape}.")
print("First ten values:", flat[:10].tolist())
print("Recovered the original grid:", np.array_equal(original, restored))
