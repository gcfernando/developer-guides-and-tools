"""
Q-Learning

Build a table of expected rewards for each cell and move.

Run: python lesson.py
Change a starting cell (0–3) in new_inputs.csv. Read the saved-in-memory policy’s preferred move, 0 left or 1 right.
"""

from pathlib import Path
import numpy as np
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the track rules. Each row describes one move and its reward.
rules = pd.read_csv(input_path).set_index(["state", "action"])


# 2. Read what happens after this move from the track table.
def step(state, action):
    row = rules.loc[(state, action)]
    return int(row["next_state"]), float(row["reward"]), bool(row["done"])


rng = np.random.default_rng(7)
q = np.zeros((5, 2))
for _ in range(350):
    state = 0
    for _ in range(20):
        action = int(rng.integers(2)) if rng.random() < 0.2 else int(q[state].argmax())
        next_state, reward, done = step(state, action)
        target = reward if done else reward + 0.95 * q[next_state].max()
        q[state, action] += 0.2 * (target - q[state, action])
        state = next_state
        if done:
            break
print("Best actions (0 left, 1 right):", q[:4].argmax(axis=1).tolist())
print("State values:", q[:4].max(axis=1).round(2).tolist())
# 3. Read the new CSV rows, then apply the rules from the sample.
starts = pd.read_csv(new_path)["start"].to_numpy()
print("Moves for test starts:", q[starts].argmax(axis=1).tolist())
