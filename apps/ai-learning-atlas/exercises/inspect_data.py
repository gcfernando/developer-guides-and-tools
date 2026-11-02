"""Inspect synthetic data without downloading a package."""
import csv
import json
from pathlib import Path


def profile(path):
    with Path(path).open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        rows = list(reader)
        fields = reader.fieldnames or []
    signatures = [tuple(row.get(field, "") for field in fields) for row in rows]
    return {
        "rows": len(rows),
        "columns": len(fields),
        "missing": {field: sum(not row.get(field) for row in rows) for field in fields},
        "duplicate_rows": len(signatures) - len(set(signatures)),
    }


if __name__ == "__main__":
    print(json.dumps(profile(Path(__file__).with_name("customers.csv")), indent=2))
