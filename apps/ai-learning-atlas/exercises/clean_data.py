"""Reference extension: inspect the hints and attempt the challenge first."""
import csv
from pathlib import Path


def clean(rows):
    """Return unique non-conflicting records and conflicts for manual review.

    Keep missing fields as supplied. Quarantine every distinct version of a
    conflicting ID; choosing the first version would silently pick a winner.
    """
    by_id = {}
    for row in rows:
        key = row.get("customer_id", "").strip()
        if not key:
            raise ValueError("customer_id is required")
        bucket = by_id.setdefault(key, [])
        if row not in bucket:
            bucket.append(dict(row))
    accepted, conflicts = [], []
    for bucket in by_id.values():
        (accepted if len(bucket) == 1 else conflicts).extend(bucket)
    return accepted, conflicts


if __name__ == "__main__":
    with Path(__file__).with_name("customers.csv").open(encoding="utf-8", newline="") as stream:
        accepted, conflicts = clean(list(csv.DictReader(stream)))
    print("Accepted:", len(accepted), "Conflicting versions:", len(conflicts))
