"""
MP4 and frame extraction

Save sample frames as MP4 and read the frames back for a model.

Run: python lesson.py
Try changing direction from 1 to 0 in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import imageio.v3 as iio
import numpy as np
import torch
from torch import nn
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


torch.manual_seed(7)
torch.set_num_threads(1)


# 1. Build a short sequence of frames showing one direction of travel.
def clip(direction, row):
    frames = np.zeros((4, 1, 6, 6), dtype="float32")
    columns = [1, 2, 3, 4] if direction == 1 else [4, 3, 2, 1]
    for frame, column in enumerate(columns):
        frames[frame, 0, row, column] = 1
    return frames


# 2. Read the CSV and check its inputs, including direction, row.
training = pd.read_csv(input_path)
train = torch.tensor(
    np.stack([clip(row.direction, row.row) for row in training.itertuples(index=False)])
)


labels = torch.tensor(training["direction"].tolist())
conv = nn.Sequential(nn.Conv2d(1, 2, 3, padding=1), nn.ReLU(), nn.Flatten())
lstm = nn.LSTM(72, 12, batch_first=True)
classifier = nn.Linear(12, 2)
optimizer = torch.optim.Adam(
    list(conv.parameters()) + list(lstm.parameters()) + list(classifier.parameters()),
    lr=0.03,
)


def predict_logits(clips):
    batches, frames = clips.shape[:2]
    features = conv(clips.flatten(0, 1)).reshape(batches, frames, 72)
    sequence, _ = lstm(features)
    return classifier(sequence[:, -1])


for _ in range(65):
    loss = nn.functional.cross_entropy(predict_logits(train), labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Write and read one original video, then restore its grayscale model shape.
# 3. Apply the fitted model to the new CSV rows and print a result for each row.
new_rows = pd.read_csv(new_path)
first = new_rows.iloc[0]
gray = (255 * clip(int(first["direction"]), int(first["row"]))[:, 0]).astype("uint8")
rgb = np.repeat(gray[..., None], 3, axis=3)
iio.imwrite("dot.mp4", rgb, fps=4, macro_block_size=2)
decoded = iio.imread("dot.mp4", plugin="FFMPEG")
new = torch.from_numpy(decoded[..., 0].astype("float32") / 255)[None, :, None]
print("Clips × frames × channels × height × width:", tuple(train.shape))
print("Decoded MP4 direction:", predict_logits(new).argmax(1).tolist())
extra = torch.tensor(
    np.stack([clip(r.direction, r.row) for r in new_rows.itertuples(index=False)])
)
print("Directions for all new clips:", predict_logits(extra).argmax(1).tolist())
