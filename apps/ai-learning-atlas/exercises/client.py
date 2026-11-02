"""Run after starting assistant.py in another terminal."""
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

request = Request(
    "http://127.0.0.1:8765/ask",
    data=json.dumps({"question": "hours"}).encode(),
    headers={"Content-Type": "application/json"},
)
try:
    with urlopen(request, timeout=2) as response:
        print(json.load(response))
except HTTPError as error:
    print("Request rejected:", error.code)
except URLError:
    print("Service unavailable. Start assistant.py and retry; do not invent an answer.")
