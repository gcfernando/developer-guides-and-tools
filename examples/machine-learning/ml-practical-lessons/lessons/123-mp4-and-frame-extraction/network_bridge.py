"""Trace one weighted sum and one learning update using only basic Python.

Run: python network_bridge.py
This is one linear neuron and one invented training row, not a language model.
"""


def run_bridge():
    distance = 2.0
    measured_minutes = 3.0
    weight = 1.0
    bias = 0.0
    learning_rate = 0.1
    # 1. A weighted sum produces the current estimate.
    before = weight * distance + bias
    error = before - measured_minutes
    loss_before = error ** 2
    # 2. For this squared-error rule, these gradients describe local change.
    weight_gradient = 2 * error * distance
    bias_gradient = 2 * error
    # 3. Move a small step opposite the gradients.
    weight = weight - learning_rate * weight_gradient
    bias = bias - learning_rate * bias_gradient
    after = weight * distance + bias
    loss_after = (after - measured_minutes) ** 2
    print(f"Input: {distance:g}. Measured training answer: {measured_minutes:g}.")
    print(f"Before: prediction {before:.2f}; squared-error loss {loss_before:.2f}.")
    print(f"Gradients: weight {weight_gradient:.2f}; bias {bias_gradient:.2f}.")
    print(f"After: weight {weight:.2f}; bias {bias:.2f}; prediction {after:.2f}.")
    print(f"After: squared-error loss {loss_after:.2f}.")
    print("Only this training row was checked. No separate prediction quality was measured.")
    print("The chosen values make this one update exact; other data/rates need not do so.")


if __name__ == "__main__":
    run_bridge()
