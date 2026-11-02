"""Local teaching fixture: a deterministic FAQ service, not a language model.

Run from this directory with Python 3.10+: python assistant.py
The service binds only to this computer. Stop with Ctrl+C.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

DOCUMENTS = [
    {"id": "public-hours", "owner": "public", "question": "hours", "answer": "Open 09:00–17:00."},
    {"id": "alice-note", "owner": "alice", "question": "project", "answer": "Alice's synthetic project is Atlas."},
    {"id": "bob-note", "owner": "bob", "question": "project", "answer": "Bob's synthetic project is Beacon."},
]


def answer(question, user="guest", documents=None):
    """Return a source-backed exact match from permitted synthetic records."""
    if not isinstance(question, str) or not question.strip() or len(question) > 200:
        raise ValueError("question must contain 1–200 non-blank characters")
    query = question.strip().casefold()
    records = DOCUMENTS if documents is None else documents
    permitted = [record for record in records if record["owner"] in ("public", user)]
    for record in permitted:
        if record["question"].casefold() == query:
            return {"answer": record["answer"], "source": record["id"]}
    return {"answer": "Not found in permitted sources.", "source": None}


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/ask":
            self.send_error(404)
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 4096:
                raise ValueError("request must contain 1–4096 bytes")
            payload = json.loads(self.rfile.read(size))
            if not isinstance(payload, dict):
                raise ValueError("request must be a JSON object")
            # Identity is fixed by the server. Never trust a user field in the request.
            result = answer(payload.get("question"), user="guest")
            status = 200
        except (ValueError, UnicodeDecodeError) as error:
            result, status = {"error": str(error)}, 400
        encoded = json.dumps(result).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, *args):
        pass  # Keep synthetic question content out of request logs.


if __name__ == "__main__":
    print("Local fixture at http://127.0.0.1:8765/ask — stop with Ctrl+C")
    HTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
