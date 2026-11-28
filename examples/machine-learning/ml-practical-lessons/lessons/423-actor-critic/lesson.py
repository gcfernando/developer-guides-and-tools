"""
Actor-Critic

Use one part to choose actions and another to estimate how good they are.

Run: python lesson.py
Swap the two reward chances in sample.csv. Rerun and see which button each method prefers.
"""

from pathlib import Path
import numpy as np
import pandas as pd

input_path = Path(__file__).resolve().with_name("sample.csv")


rng = np.random.default_rng(7)

# 1. Read the CSV and check its inputs, including button, chance_of_reward.
buttons = pd.read_csv(input_path)
reward_chance = buttons["chance_of_reward"].to_numpy()


# 2. Compare the printed output with the original values.
for method in ["Policy gradient", "Actor-Critic"]:
    logits = np.zeros(2)
    critic = 0.0
    for _ in range(500):
        probabilities = np.exp(logits - logits.max())
        probabilities /= probabilities.sum()
        action = rng.choice(2, p=probabilities)
        reward = float(rng.random() < reward_chance[action])
        gradient = np.eye(2)[action] - probabilities
        advantage = reward
        if method == "Actor-Critic":
            advantage = reward - critic
            critic += 0.05 * advantage
        logits += 0.08 * advantage * gradient
    print(method, "chosen button:", int(logits.argmax()))
    if method == "Actor-Critic":
        print("Estimated policy value:", round(critic, 2))
