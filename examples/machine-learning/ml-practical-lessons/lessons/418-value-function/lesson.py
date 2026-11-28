"""
Value Function

Add future rewards with more weight on the rewards that come sooner.

Run: python lesson.py
Try changing start from 0 to 3 in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the track rules. Each row describes one move and its reward.
rules = pd.read_csv(input_path).set_index(["state", "action"])


# 2. Read what happens after this move from the track table.
def step(state, action):
    row = rules.loc[(state, action)]
    return int(row["next_state"]), float(row["reward"]), bool(row["done"])


# 3. Read the new CSV rows, then apply the rules from the sample.
starts = pd.read_csv(new_path)["start"]
state = int(starts.iloc[0])


discounted = 0
moves = []
for turn in range(4):
    action = 1  # The policy chooses right.
    next_state, reward, done = step(state, action)
    moves.append([turn + 1, state, "Right", next_state, reward])
    discounted += 0.95**turn * reward
    state = next_state
    if done:
        break
results = pd.DataFrame(
    moves, columns=["Move", "From cell", "Action", "To cell", "Reward"]
)
print(results.to_string(index=False))
print("Discounted return:", round(discounted, 3))
for start in starts.iloc[1:]:
    next_state, reward, done = step(int(start), 1)
    print(f"From cell {start} move right to {next_state}, reward = {reward}")
