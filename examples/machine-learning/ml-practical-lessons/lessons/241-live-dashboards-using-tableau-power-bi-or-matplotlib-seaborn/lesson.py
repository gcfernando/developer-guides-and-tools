"""
Live dashboards using Tableau, Power BI, or Matplotlib/Seaborn

Create a local dashboard and use the companion lessons to prepare BI imports.

Run: python lesson.py
Change Correct from 16 to 18 in the Afternoon row. Accuracy should rise to 90% and the alert should disappear.
"""

from pathlib import Path
import pandas as pd
from streamlit.testing.v1 import AppTest

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the labeled batches so you can compare the model’s results over time.
report = pd.read_csv(input_path)
if report.empty or not {"Batch", "Correct", "Checked"}.issubset(report.columns):
    raise SystemExit("Keep at least one row with Batch, Correct and Checked columns.")
if (
    report[["Correct", "Checked"]].isna().any().any()
    or (report["Checked"] <= 0).any()
    or (report["Correct"] < 0).any()
    or (report["Correct"] > report["Checked"]).any()
):
    raise SystemExit(
        "Checked must be positive, and Correct must be between zero and Checked."
    )
report["Accuracy"] = report["Correct"] / report["Checked"]
report.to_csv("monitoring.csv", index=False)


dashboard = """
import pandas as pd
import streamlit as st

st.title("Delivery model checks")

@st.fragment(run_every="5s")
def show_latest():
    history = pd.read_csv("monitoring.csv")
    latest = history.iloc[-1]["Accuracy"]
    st.metric("Latest labeled accuracy", f"{latest:.0%}")
    st.line_chart(history.set_index("Batch")["Accuracy"])
    if latest < .85:
        st.warning("Accuracy is below 85%. Review the latest batch.")

show_latest()
"""
Path("monitoring_dashboard.py").write_text(dashboard, encoding="utf-8")
view = AppTest.from_string(dashboard).run()
assert not view.exception
results = pd.DataFrame(
    {
        "Dashboard field": [
            "Latest labeled accuracy",
            "Alert threshold",
            "Alert visible",
        ],
        "Value": [view.metric[0].value, "85%", bool(view.warning)],
    }
)
# 2. Print the result next to the input values so you can compare them.
print(results.to_string(index=False))
