"""
Track metadata

Record where a file came from, how large it is and what its columns contain.

Run: python lesson.py
Try changing order_id from 1 to 2 in sample.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd
import numpy as np
from PIL import Image
import imageio.v3 as iio

input_path = Path(__file__).resolve().with_name("sample.csv")


folder = Path("collection_demo")
folder.mkdir(exist_ok=True)

# 1. Read the CSV and check its inputs, including order_id, minutes, contact.
rows = pd.read_csv(input_path)
shared_columns = ["order_id", "minutes"]
csv_path = folder / "deliveries.csv"
rows[shared_columns].to_csv(csv_path, index=False, lineterminator="\n")

(folder / "message.txt").write_text("Package arrived", encoding="utf-8")
image = Image.new("RGB", (16, 16), "skyblue")
image.save(folder / "image_fixture.png")
frames = np.stack(
    [np.asarray(image), np.asarray(image.transpose(Image.Transpose.FLIP_LEFT_RIGHT))]
)


iio.imwrite(folder / "video_fixture.mp4", frames, fps=2)
manifest = pd.DataFrame(
    {
        "record_id": [1, 2, 3],
        "file_type": ["text", "image", "video"],
        "path": ["message.txt", "image_fixture.png", "video_fixture.mp4"],
    }
)
manifest["collected"] = manifest["path"].map(lambda name: (folder / name).exists())
manifest.to_csv(folder / "manifest.csv", index=False)
metadata = {
    "source": "original sample",
    "method": "created in Python",
    "bytes": csv_path.stat().st_size,
    "types": rows[shared_columns].dtypes.astype(str).to_dict(),
}
# 2. Print the result next to the input values so you can compare them.
print(metadata)
print(manifest[["file_type", "collected"]].to_string(index=False))
with Image.open(folder / "image_fixture.png") as picture:
    print("Image width and height:", picture.size)
print(
    "Video frames read:", len(iio.imread(folder / "video_fixture.mp4", plugin="FFMPEG"))
)
assert manifest["collected"].all()
assert "contact" not in pd.read_csv(csv_path)
