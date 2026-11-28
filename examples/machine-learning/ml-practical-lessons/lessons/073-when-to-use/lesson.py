"""
When to use?

Compare several transformations using the same rows and pick one based on validation error.

Run: python lesson.py
Try changing signal from 1 to 12 in sample.csv. Compare the new output.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    FunctionTransformer,
    KBinsDiscretizer,
    MinMaxScaler,
    PolynomialFeatures,
    PowerTransformer,
    QuantileTransformer,
    RobustScaler,
    StandardScaler,
)

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the sensor readings and their measured costs.
data = pd.read_csv(input_path)


methods = [
    ("Raw", "passthrough"),
    ("Min-Max Scaling", MinMaxScaler()),
    ("Z-Score Standardization", StandardScaler()),
    ("Log Transformation", FunctionTransformer(np.log1p)),
    ("Robust Scaling", RobustScaler()),
    ("Power Transformations", PowerTransformer(method="yeo-johnson")),
    ("Quantile Transformation", QuantileTransformer(n_quantiles=4)),
    ("Binning", KBinsDiscretizer(n_bins=3, encode="onehot-dense", strategy="uniform")),
    ("Polynomial Features", PolynomialFeatures(2, include_bias=False)),
]
folds = KFold(3, shuffle=True, random_state=7)
# 2. Compare the printed output with the original values.
for name, transform in methods:
    model = Pipeline([("transform", transform), ("regression", Ridge())])
    errors = -cross_val_score(
        model,
        data[["signal"]],
        data["cost"],
        cv=folds,
        scoring="neg_mean_absolute_error",
    )
    print(f"{name:27} MAE {errors.mean():.2f}")
