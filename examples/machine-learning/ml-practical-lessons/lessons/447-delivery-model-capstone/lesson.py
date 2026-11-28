"""Run every capstone step once."""

from fit_delivery_model import train_model
from monitor import monitor
from send_requests import try_requests

# 1. Train, choose, and save the model.
train_model()

# 2. Use the saved model to respond to the example request CSV.
try_requests()

# 3. Compare errors on a later, labeled delivery batch.
monitor()
