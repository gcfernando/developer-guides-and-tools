"""Use a later labeled batch to decide whether to investigate the model."""

from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_absolute_error
from service import read_artifact

FOLDER = Path(__file__).resolve().parent


def monitor():
    # This offline check scores all later records to measure drift and errors.
    # The public-facing service can still decline a new request outside its range.
    model, info = read_artifact()
    later = pd.read_csv(FOLDER / "later_batch.csv", parse_dates=["delivery_date"])
    assert later["shipment_id"].is_unique
    assert later["delivery_date"].min() > pd.Timestamp(info["test_last_date"])
    predicted = model.predict(later[info["input_columns"]])
    later["absolute_error"] = (later["actual_minutes"] - predicted).abs()
    report = later.groupby("zone").agg(
        orders=("shipment_id", "size"), mae=("absolute_error", "mean")
    )
    print("\nLater MAE by zone")
    print(report.round(2).to_string())
    error = mean_absolute_error(later["actual_minutes"], predicted)
    delta = error - info["test_mae_minutes"]
    print(f"Later batch: {len(later)} orders, MAE {error:.2f} minutes.")
    print(f"Change from final test: {delta:+.2f} minutes.")
    decision = "INVESTIGATE" if delta > 2 else "KEEP WATCHING"
    print(
        f"Decision: {decision}. The practice alert triggers above a 2-minute increase."
    )


if __name__ == "__main__":
    monitor()
