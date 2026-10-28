# model_service.py – all ML logic for the house price app
from datetime import datetime
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

FEATURES = ["area_m2", "bedrooms", "age_years", "distance_km", "has_garden"]
TARGET = "price"
LIMITS = {"area_m2": (20, 400), "bedrooms": (0, 10), "age_years": (0, 200),
          "distance_km": (0, 100), "has_garden": (0, 1)}                 # allowed input ranges
MODEL_DIR = Path("models")
DATA_STORE = Path("data") / "all_training_data.csv"
HISTORY = MODEL_DIR / "history.csv"


def load_data(csv_path):
    """Read a CSV and keep only clean, useful rows."""
    df = pd.read_csv(csv_path)
    missing = [c for c in FEATURES + [TARGET] if c not in df.columns]
    if missing:
        raise ValueError(f"The file is missing these columns: {missing}")
    df = df.drop_duplicates()
    df = df.dropna(subset=[TARGET])                                    # no price → can't learn from it
    return df


def build_model():
    return make_pipeline(SimpleImputer(strategy="median"),
                         HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, random_state=0))


def evaluate(model, df):
    pred = model.predict(df[FEATURES])
    return {"mae": round(float(mean_absolute_error(df[TARGET], pred))), "r2": round(float(r2_score(df[TARGET], pred)), 3)}


def _next_version():
    existing = [int(p.stem.split("_v")[-1]) for p in MODEL_DIR.glob("house_model_v*.joblib")]
    return max(existing, default=0) + 1


def save_model(model, metrics, rows, note):
    """Save the model as the next version and add a line to the history."""
    MODEL_DIR.mkdir(exist_ok=True)
    version = _next_version()
    joblib.dump({"model": model, "features": FEATURES, "version": version}, MODEL_DIR / f"house_model_v{version}.joblib")
    line = pd.DataFrame([{"version": version, "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                          "rows_used": rows, "mae": metrics["mae"], "r2": metrics["r2"],
                          "note": note, "current": True}])
    old = pd.read_csv(HISTORY) if HISTORY.exists() else pd.DataFrame()
    if len(old):
        old["current"] = False                                          # only the newest is "current"
    pd.concat([old, line], ignore_index=True).to_csv(HISTORY, index=False)
    return version


def history():
    return pd.read_csv(HISTORY) if HISTORY.exists() else pd.DataFrame()


def current_version():
    h = history()
    return int(h.loc[h["current"], "version"].iloc[0]) if len(h) else None


def load_model(version=None):
    """Load a saved model. version=None → the current one."""
    version = version or current_version()
    if version is None:
        raise FileNotFoundError("No model saved yet – train one first.")
    bundle = joblib.load(MODEL_DIR / f"house_model_v{version}.joblib")
    return bundle["model"], bundle["version"]


def train_first_model(csv_path):
    """Train on one CSV, test on 20 % hidden rows, save as a new version."""
    df = load_data(csv_path)
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=0)
    model = build_model().fit(train_df[FEATURES], train_df[TARGET])
    metrics = evaluate(model, test_df)
    final = build_model().fit(df[FEATURES], df[TARGET])               # then learn from ALL rows
    DATA_STORE.parent.mkdir(exist_ok=True)
    df.to_csv(DATA_STORE, index=False)
    version = save_model(final, metrics, len(df), note=f"first model from {Path(csv_path).name}")
    return version, metrics


def check_inputs(values):
    clean = {}
    for name in FEATURES:
        if name not in values or str(values[name]).strip() == "":
            raise ValueError(f"Please fill in '{name}'.")
        number = float(values[name])
        low, high = LIMITS[name]
        if not low <= number <= high:
            raise ValueError(f"'{name}' must be between {low} and {high}.")
        clean[name] = number
    return clean


def predict_price(values, version=None):
    """values = {"area_m2": 100, "bedrooms": 3, ...} → (price, version used)."""
    model, used = load_model(version)
    row = pd.DataFrame([check_inputs(values)])[FEATURES]
    return float(model.predict(row)[0]), used


def update_with_new_data(new_csv_path, keep_years=None):
    """New data arrived: compare the current model with a retrained one on FRESH data, save the new version.
    keep_years=None → learn from ALL data;  keep_years=2 → only the 2 most recent sale years."""
    new = load_data(new_csv_path)
    new_train, new_check = train_test_split(new, test_size=0.3, random_state=0)   # new_check: unseen by both models
    current_model, current_v = load_model()
    old_metrics = evaluate(current_model, new_check)

    store = pd.read_csv(DATA_STORE)
    if len(new.merge(store, how="inner")) == len(new):
        raise ValueError("This file was already used for an update.")
    combined = pd.concat([store, new_train], ignore_index=True).drop_duplicates()
    # remove the "check" rows from the training data, so the new model is judged on rows it never saw
    check_rows = set(map(tuple, new_check.to_numpy()))
    combined = combined[[tuple(r) not in check_rows for r in combined[new_check.columns].to_numpy()]]
    if keep_years is not None:                                        # forget old prices if the market moved
        newest_year = combined["sold_year"].max()
        combined = combined[combined["sold_year"] > newest_year - keep_years]
    candidate = build_model().fit(combined[FEATURES], combined[TARGET])
    new_metrics = evaluate(candidate, new_check)

    final = build_model().fit(pd.concat([combined, new_check])[FEATURES], pd.concat([combined, new_check])[TARGET])
    pd.concat([store, new], ignore_index=True).drop_duplicates().to_csv(DATA_STORE, index=False)
    better = new_metrics["mae"] < old_metrics["mae"]
    version = save_model(final, new_metrics, len(combined) + len(new_check),
                         note=f"update with {Path(new_csv_path).name} (v{current_v} MAE on new data: {old_metrics['mae']})")
    if not better:
        rollback(current_v)                                           # keep the old one as current
    return {"old_version": current_v, "old_mae_on_new_data": old_metrics["mae"],
            "new_version": version, "new_mae_on_new_data": new_metrics["mae"], "promoted": better}


def rollback(version):
    """Make an older saved version the 'current' one again."""
    h = history()
    if version not in h["version"].tolist():
        raise ValueError(f"Version {version} does not exist.")
    h["current"] = h["version"] == version
    h.to_csv(HISTORY, index=False)
    return version
