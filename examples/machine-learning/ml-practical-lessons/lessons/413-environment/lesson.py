"""
Environment

Read the track rules that decide what happens after each move.

Run: python lesson.py
Try changing start from 0 to 2 in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the track rules. Each row describes one move and its reward.
track = pd.read_csv(input_path).set_index(["state", "action"])
# 2. Read the new CSV rows, then apply the rules from the sample.
cases = pd.read_csv(new_path)


records = []
for case in cases.itertuples(index=False):
    turn = track.loc[(case.start, case.action)]
    direction = "left" if case.action == 0 else "right"
    records.append(
        [case.start, direction, turn["next_state"], turn["reward"], turn["done"]]
    )


print("The CSV describes the track. Each row says what happens after a move.")
result = pd.DataFrame(
    records, columns=["Start", "Action", "Next cell", "Reward", "At goal"]
)
print(result.to_string(index=False))
