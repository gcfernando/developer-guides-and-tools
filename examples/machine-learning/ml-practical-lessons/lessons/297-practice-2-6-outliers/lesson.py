"""
Outliers

Look for unusual measurements in the invented wine measurements and see which rows need checking.

Run: python lesson.py
Change an input in new_inputs.csv. Compare the predictions with the held-out check above.
"""

from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler
from sklearn.preprocessing import LabelEncoder

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the example records from sample.csv. The table uses the dataset fields shown below.
data = pd.read_csv(input_path)


numeric = ["alcohol", "citric_acid", "sulphates"]
categorical = []
features = numeric + categorical
# 2. Set aside the check rows before the model learns.
training_rows = data.iloc[:-2]
train = training_rows.dropna(subset=["quality"])
hold = data.iloc[-2:]
# 3. Find blanks in the rows you are about to use.
missing_counts = training_rows[features + ["quality"]].isna().sum()
print("Missing cells before filling or removing rows:", missing_counts.to_dict())

measurements = training_rows[["alcohol", "citric_acid", "sulphates"]].select_dtypes(
    "number"
)
# 4. Find where the middle values sit, then compare the remaining rows with those limits.
q1 = measurements.quantile(0.25)
q3 = measurements.quantile(0.75)
spread = q3 - q1
flags = measurements.lt(q1 - 1.5 * spread) | measurements.gt(q3 + 1.5 * spread)
outliers = pd.DataFrame(
    {"Field": measurements.columns, "Rows to review": flags.sum().values}
)
print(outliers.to_string(index=False))
flagged = measurements.where(flags).dropna(how="all")
print("Flagged original rows:", (flagged.index + 1).tolist())


# An unfamiliar category can still pass through the encoder.
# Numeric inputs and categories need different preparation. This gives each group its own rules.
prep = ColumnTransformer(
    [
        (
            "numeric",
            make_pipeline(SimpleImputer(strategy="median"), StandardScaler()),
            numeric,
        ),
        (
            "category",
            make_pipeline(
                SimpleImputer(strategy="constant", fill_value="Unknown"),
                OneHotEncoder(handle_unknown="ignore"),
            ),
            categorical,
        ),
    ]
)
# A pipeline keeps preparation and prediction together in the right order.
model = make_pipeline(prep, LinearRegression())
# 5. Fit the model on the prepared training rows. Keep it for the checks below.
model.fit(train[features], train["quality"])
results = pd.DataFrame(
    {
        "Original row": hold.index + 1,
        "Actual answer": hold["quality"].values,
        "Prediction": model.predict(hold[features]).round(1),
    }
)
print(results.to_string(index=False))


quality_labels = LabelEncoder().fit(["lower", "higher"])
rating = quality_labels.transform(
    train["quality"].ge(6).map({True: "higher", False: "lower"})
)
classifier = make_pipeline(
    SimpleImputer(strategy="median"), MinMaxScaler(), LogisticRegression()
)
classifier.fit(train[numeric], rating)
print(
    "Class predictions:",
    quality_labels.inverse_transform(classifier.predict(hold[numeric])).tolist(),
)


# 6. Apply the fitted model to the new CSV rows and print a result for each row.
fresh_rows = pd.read_csv(new_path)
print(
    fresh_rows.assign(prediction=model.predict(fresh_rows[features])).to_string(
        index=False
    )
)
