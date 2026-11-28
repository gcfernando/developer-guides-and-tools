"""
Database storage

Store orders in a database table and retrieve them with SQL.

Run: python lesson.py
Add order_id 4 with zone west in sample.csv. Look for it in the database, API or page output.
"""

from pathlib import Path
import json
import sqlite3
import pandas as pd
from fastapi import FastAPI
from fastapi.testclient import TestClient
from html.parser import HTMLParser
from html import escape

input_path = Path(__file__).resolve().with_name("sample.csv")


# 1. Read the order IDs and the zone for each order.
file_rows = pd.read_csv(input_path)


with sqlite3.connect(":memory:") as db:
    file_rows.to_sql("orders", db, index=False)
    database_rows = pd.read_sql_query("SELECT * FROM orders", db)


app = FastAPI()


@app.get("/orders")
def orders():
    return {"items": file_rows.to_dict("records")}


# 2. Send a practice request and read the response code and body.
response = TestClient(app).get("/orders")
response.raise_for_status()
api_rows = pd.DataFrame(response.json()["items"])


class ZoneParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.zones = []

    def handle_starttag(self, tag, attrs):
        fields = dict(attrs)
        if tag == "li" and "data-zone" in fields:
            self.zones.append(fields["data-zone"])


parser = ZoneParser()
# Build this practice page from the CSV so changing a row also changes the page.

items = [
    f'<li data-zone="{escape(zone)}">{escape(zone)}</li>' for zone in file_rows["zone"]
]
parser.feed("<ul>" + "".join(items) + "</ul>")
print("Rows from the CSV and database:", len(file_rows), len(database_rows))
print("\nOrders returned by the local API")
print(api_rows.to_string(index=False))
print("Parsed HTML:", parser.zones)
