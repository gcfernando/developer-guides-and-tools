"""Try new CSV rows with the model already saved in this folder."""

from pathlib import Path

import pandas as pd
from fastapi.testclient import TestClient
from service import create_app

folder = Path(__file__).resolve().parent


def try_requests():
    # Turn missing weights into JSON null. The saved pipeline fills them from training.
    rows = pd.read_csv(folder / "new_inputs.csv").astype(object)
    rows = rows.where(rows.notna(), None)
    print("\nLocal service results")
    with TestClient(create_app()) as client:
        for order in rows.to_dict(orient="records"):
            reply = client.post("/predict", json=order)
            print(
                f"{order['distance_km']} km, {order['zone']}: {reply.status_code} {reply.json()}"
            )


if __name__ == "__main__":
    if not (folder / "delivery_model.joblib").is_file():
        raise SystemExit("Run python fit_delivery_model.py first.")
    try_requests()
