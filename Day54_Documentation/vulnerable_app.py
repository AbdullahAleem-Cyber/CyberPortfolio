from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import os

BASE_DIR = os.path.abspath(".")

class PathTraversalHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        if parsed_path.path == "/file":
            filename = query.get("name", [""])[0]

            # SECURE: Prevent traversal outside BASE_DIR
            requested_path = os.path.abspath(os.path.join(BASE_DIR, filename))

            if requested_path.startswith(BASE_DIR) and os.path.exists(requested_path) and os.path.isfile(requested_path):
                with open(requested_path, "r") as f:
                    self.wfile.write(f.read().encode())
            else:
                self.wfile.write(b"Access Denied: Invalid File Path")
        else:
            self.wfile.write(b"Day 54: Path Traversal Security Lab (Secured)")

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), PathTraversalHandler)
    print("Day 54 Secure Lab running at http://127.0.0.1:8000")
    server.serve_forever()
