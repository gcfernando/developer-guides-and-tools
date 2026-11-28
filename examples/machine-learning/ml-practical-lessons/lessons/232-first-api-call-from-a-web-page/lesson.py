"""
First API call from a web page

Send a distance to a local model from a web page and read the response.

Run: python lesson.py
Try changing km from 4 to 12 in new_inputs.csv. Compare the new output.
"""

from pathlib import Path
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field
from sklearn.linear_model import LinearRegression

input_path = Path(__file__).resolve().with_name("sample.csv")
new_path = Path(__file__).resolve().with_name("new_inputs.csv")


# 1. Read the CSV and check its inputs, including distance_km, minutes.
data = pd.read_csv(input_path)
# 2. Teach the model from the training inputs and delivery time in minutes.
model = LinearRegression().fit(data[["distance_km"]], data["minutes"])
# Create the local API. The route below receives inputs and returns an estimate.
app = FastAPI()


class Delivery(BaseModel):
    km: float = Field(ge=0)


@app.get("/", response_class=HTMLResponse)
def page():
    return """<label>Distance in km <input id="km" type="number" value="4" min="0"></label>
<button id="predict">Predict</button><p id="answer" role="status"></p>
<script>
document.getElementById("predict").onclick = async () => {
  const km = Number(document.getElementById("km").value);
  if (!document.getElementById("km").value.trim()) {
    document.getElementById("answer").textContent = "Enter a distance.";
    return;
  }
  const response = await fetch("/predict", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({km})
  });
  const result = await response.json();
  document.getElementById("answer").textContent = response.ok
    ? result.minutes + " minutes" : "Please enter a nonnegative distance.";
};
</script>"""


@app.post("/predict")
def predict(delivery: Delivery):
    parcel = pd.DataFrame({"distance_km": [delivery.km]})
    minutes = model.predict(parcel)[0]
    return {"minutes": round(float(minutes), 1)}


if __name__ == "__main__":
    client = TestClient(app)
    page_status = client.get("/").status_code
    # 3. Send each new CSV row to the app and read the response.
    request_rows = pd.read_csv(new_path)
    response = client.post("/predict", json={"km": float(request_rows.iloc[0]["km"])})
    results = pd.DataFrame(
        [
            ["Open the page", page_status, None],
            [
                f"Predict {request_rows.iloc[0]['km']:g} km",
                response.status_code,
                response.json().get("minutes"),
            ],
        ],
        columns=["Action", "HTTP status", "Predicted minutes"],
    )
    print(results.to_string(index=False))
    print("Response:", response.json())
    for km in request_rows["km"].iloc[1:]:
        reply = client.post("/predict", json={"km": float(km)})
        print(km, reply.status_code, reply.json())
