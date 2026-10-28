"""Serve an existing Jekyll build locally with its configured base path."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
BASE = "/developer-guides-and-tools"

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/", BASE]:
            self.send_response(302)
            self.send_header("Location", BASE + "/")
            self.end_headers()
            return
        if not self.path.startswith(BASE + "/"):
            self.send_error(404)
            return
        self.path = self.path[len(BASE):]
        super().do_GET()

    def list_directory(self, path):
        self.send_error(404, "No published index for this path")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    site = ROOT / "_site"
    if not site.is_dir():
        parser.error("Build Jekyll before starting the preview")
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(Handler, directory=str(site)))
    print(f"Preview: http://127.0.0.1:{args.port}{BASE}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
