"""
Learn the Model

Build a small transition table from observed moves and use it to plan.

Run: python lesson.py
Edit start in new_inputs.csv. The script builds a lookup from the observed moves and uses it to plan.
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


observations = {
    (state, action): step(state, action) for state in range(4) for action in range(2)
}


def learned(state, action):
    return observations[(state, action)]


def best_value(state, remaining, transition):
    if remaining == 0 or state == 4:
        return 0
    return max(action_return(state, action, remaining, transition) for action in [0, 1])


def action_return(state, action, remaining, transition):
    next_state, reward, done = transition(state, action)
    return (
        reward
        if done
        else reward + 0.95 * best_value(next_state, remaining - 1, transition)
    )


for name, transition in [("learn-the-model", learned)]:
    values = [action_return(0, action, 6, transition) for action in [0, 1]]
    print(name, "first-action values:", [round(value, 2) for value in values])
    print("Best action:", max([0, 1], key=values.__getitem__))
# 3. Read the new CSV rows, then apply the rules from the sample.
for start in pd.read_csv(new_path)["start"]:
    possibilities = [action_return(int(start), action, 6, learned) for action in [0, 1]]
    print(f"Start {start}, planned values: {possibilities}")
