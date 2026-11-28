"""
Monte Carlo Tree Search (MCTS)

Try several possible future move sequences before choosing a first move.

Run: python lesson.py
Change the ordinary move reward in sample.csv. Keep the goal and the list of state/action pairs. See whether the planner's first move changes.
"""

from pathlib import Path
import numpy as np
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the track rules. Each row describes one move and its reward.
rules = pd.read_csv(input_path).set_index(["state", "action"])


# 2. Read what happens after this move from the track table.
def step(state, action):
    row = rules.loc[(state, action)]
    return int(row["next_state"]), float(row["reward"]), bool(row["done"])


rng = np.random.default_rng(7)
visits = {}
returns = {}


for _ in range(240):
    state = 0
    node = ()
    path = []
    score = 0.0
    for depth in range(8):
        children = [node + (0,), node + (1,)]
        unvisited = [child for child in children if child not in visits]
        if unvisited:
            child = unvisited[int(rng.integers(len(unvisited)))]
        else:
            total = sum(visits[child] for child in children)
            child = max(
                children,
                key=lambda c: returns[c] / visits[c]
                + np.sqrt(2 * np.log(total) / visits[c]),
            )
        path.append(child)
        state, reward, done = step(state, child[-1])
        score += 0.95**depth * reward
        node = child
        if done:
            break
        if unvisited:
            for later in range(depth + 1, 8):
                state, reward, done = step(state, int(rng.integers(2)))
                score += 0.95**later * reward
                if done:
                    break
            break
    for child in path:
        visits[child] = visits.get(child, 0) + 1
        returns[child] = returns.get(child, 0.0) + score
print("First-step visits:", [visits[(a,)] for a in [0, 1]])
print("Recommended first action:", max([0, 1], key=lambda a: visits[(a,)]))
