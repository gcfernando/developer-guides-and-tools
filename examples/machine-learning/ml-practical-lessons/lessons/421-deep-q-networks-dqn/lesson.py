"""
Deep Q Networks (DQN)

Teach a small neural network to score left and right moves.

Run: python lesson.py
Try changing start from 0 to 3 in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
from copy import deepcopy
import torch
from torch import nn
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the track rules. Each row describes one move and its reward.
rules = pd.read_csv(input_path).set_index(["state", "action"])


# 2. Read what happens after this move from the track table.
def step(state, action):
    row = rules.loc[(state, action)]
    return int(row["next_state"]), float(row["reward"]), bool(row["done"])


torch.manual_seed(7)
torch.set_num_threads(1)
action_value = nn.Sequential(nn.Linear(5, 12), nn.ReLU(), nn.Linear(12, 2))
target_network = deepcopy(action_value)
optimizer = torch.optim.Adam(action_value.parameters(), lr=0.025)
states = torch.tensor([0, 0, 1, 1, 2, 2, 3, 3])
actions = torch.tensor([0, 1] * 4)
observations = [step(s, a) for s, a in zip(states.tolist(), actions.tolist())]


new_states, rewards, terminal = zip(*observations)
one_hot = torch.eye(5)
for update in range(190):
    prediction = action_value(one_hot[states]).gather(1, actions[:, None]).squeeze(1)
    with torch.no_grad():
        future = target_network(one_hot[list(new_states)]).max(dim=1).values
        goal = torch.tensor(rewards) + 0.95 * future * (~torch.tensor(terminal))
    loss = nn.functional.smooth_l1_loss(prediction, goal)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if update % 10 == 0:
        target_network.load_state_dict(action_value.state_dict())

print("Replay transitions:", len(observations))
print("DQN policy:", action_value(one_hot[:4]).argmax(dim=1).tolist())
# 3. Read the new CSV rows, then apply the rules from the sample.
starts = pd.read_csv(new_path)["start"].tolist()
print("Moves for test starts:", action_value(one_hot[starts]).argmax(dim=1).tolist())
