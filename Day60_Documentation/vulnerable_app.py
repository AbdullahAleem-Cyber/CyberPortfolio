from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

SECURE_LIB_VERSION = "2.0.0 (Patched)"

class ComponentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if parsed_path.path == "/version":
            response = (
                "<html><body><h1>"
                f"Component Status: {SECURE_LIB_VERSION}"
                "</h1></body></html>"
            )
            self.wfile.write(response.encode())
        else:
            self.wfile.write(
                b"<html><body><h1>"
                b"Day 60: Components Lab (Secured Simulation)"
                b"</h1></body></html>"
            )

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), ComponentHandler)
    print("Day 60 Secure Lab running at http://127.0.0.1:8000")
    server.serve_forever()
