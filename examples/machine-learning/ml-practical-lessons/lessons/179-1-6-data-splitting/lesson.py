"""Keep urgent orders represented and prevent repeated records crossing a split."""

from pathlib import Path
from itertools import combinations

import pandas as pd
from sklearn.metrics import balanced_accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

folder = Path(__file__).resolve().parent
POINT = "Trace how the three sets have different jobs."
inputs = ["distance_km", "weight_kg"]
orders = pd.read_csv(folder / "sample.csv")

# 1. Stop if one shipment ID appears twice. Separate shipments may have equal inputs.
if orders["shipment_id"].duplicated().any():
    raise SystemExit(
        "Remove the copy or keep both records in the same group before splitting."
    )

# 2. Keep urgent and regular orders in each set. Set the test rows aside first.
test_share = 0.1
learning, test = train_test_split(
    orders, test_size=test_share, stratify=orders["urgent"], random_state=7
)
if test_share == 0.1:
    train, validation = train_test_split(
        learning, test_size=2 / 9, stratify=learning["urgent"], random_state=17
    )
    groups = {"Training": train, "Validation": validation, "Test": test}
else:
    train = learning
    groups = {"Training": train, "Test": test}

for left, right in combinations(groups.values(), 2):
    assert set(left["shipment_id"]).isdisjoint(right["shipment_id"])
print("Shared shipment IDs across splits: 0")
table = pd.DataFrame(
    [
        {
            "Set": name,
            "Rows": len(part),
            "Urgent": int(part["urgent"].sum()),
            "Urgent (%)": 100 * part["urgent"].mean(),
        }
        for name, part in groups.items()
    ]
)
print(table.to_string(index=False))

# 3. On a three-way split, compare settings on validation and keep the best one.
depth = 2
if test_share == 0.1:
    scores = []
    for candidate_depth in (1, 2, 3):
        candidate = DecisionTreeClassifier(max_depth=candidate_depth, random_state=7)
        candidate.fit(train[inputs], train["urgent"])
        score = balanced_accuracy_score(
            validation["urgent"], candidate.predict(validation[inputs])
        )
        scores.append((candidate_depth, score))
    depth = max(scores, key=lambda pair: pair[1])[0]
    print("\nValidation scores by tree depth")
    print(
        pd.DataFrame(scores, columns=["Depth", "Balanced accuracy"])
        .round(3)
        .to_string(index=False)
    )

# 4. Fit the chosen tree, then count its mistakes on the reserved test orders.
model = DecisionTreeClassifier(max_depth=depth, random_state=7)
model.fit(train[inputs], train["urgent"])
tn, fp, fn, tp = confusion_matrix(
    test["urgent"], model.predict(test[inputs]), labels=[False, True]
).ravel()
print(f"{POINT}\nChosen depth: {depth}")
print(
    f"Test: {tp} urgent caught, {fn} urgent missed, {fp} false alarms, {tn} regular correct."
)
print(
    f"The test contains only {tp + fn} urgent orders. A single missed order changes recall a lot."
)

# 5. Try new inputs. Their guesses are separate from the scored test rows.
fresh = pd.read_csv(folder / "new_inputs.csv")
fresh["predicted_urgent"] = model.predict(fresh[inputs])
print(fresh.to_string(index=False))
