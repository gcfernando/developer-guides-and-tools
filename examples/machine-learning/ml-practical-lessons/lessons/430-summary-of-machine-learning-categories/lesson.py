"""Work out which learning category fits the information you have."""

from pathlib import Path
import pandas as pd

folder = Path(__file__).resolve().parent
practice = pd.read_csv(folder / "sample.csv")
new = pd.read_csv(folder / "new_inputs.csv")
categories = {
    "known answers": "Supervised",
    "no answers": "Unsupervised",
    "some answers": "Semi-supervised",
    "rewards": "Reinforcement",
}


# 1. Read the kind of feedback available. Match it to one of the four categories.
def show(rows):
    selection = (
        rows["feedback"].map(categories).fillna("Check which feedback is available")
    )
    print(
        rows.assign(learning_category=selection)[
            ["problem", "feedback", "learning_category"]
        ].to_string(index=False)
    )


print("Worked examples")
show(practice)
print("\nYour examples")
show(new)
