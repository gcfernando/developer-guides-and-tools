"""
Frequently occurring items

Add a shopping basket and see which item pairs remain common.

Run: python lesson.py
Add or change a basket in sample.csv. Use | between items. The printed support is the share of baskets that contain the item set.
"""

from pathlib import Path
import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth
from mlxtend.preprocessing import TransactionEncoder

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the baskets. A vertical bar separates the items in each basket.
baskets = pd.read_csv(input_path)["items"].str.split("|").tolist()


encoder = TransactionEncoder().fit(baskets)
rows = pd.DataFrame(encoder.transform(baskets), columns=encoder.columns_)
for method in [apriori, fpgrowth]:
    found = method(rows, min_support=0.4, use_colnames=True)
    pairs = found[found["itemsets"].map(len) == 2]
    print(
        method.__name__,
        sorted(
            (tuple(sorted(items)), float(support))
            for items, support in zip(pairs["itemsets"], pairs["support"])
        ),
    )
support_pair = (
    rows.reindex(columns=["milk", "bread"], fill_value=False).all(axis=1).mean()
)
milk_count = rows.get("milk", pd.Series(False, index=rows.index)).mean()
# 2. Compare the printed output with the original values.
if milk_count:
    print("Milk to bread confidence:", round(support_pair / milk_count, 2))
