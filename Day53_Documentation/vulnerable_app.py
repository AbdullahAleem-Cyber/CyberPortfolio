from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import ipaddress
import subprocess

class SecureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if parsed_path.path == "/ping":
            host = query.get("host", ["127.0.0.1"])[0]

            try:
                ipaddress.ip_address(host)

                result = subprocess.run(
                    ["ping", "-c", "1", host],
                    capture_output=True,
                    text=True
                )

                response = f"<html><body><h1>Ping Results</h1><pre>{result.stdout}</pre></body></html>"

            except ValueError:
                response = "<html><body><h1>Invalid IP address</h1></body></html>"

            self.wfile.write(response.encode())

        else:
            self.wfile.write(
                b"<html><body><h1>Day 53 Secure Lab</h1></body></html>"
            )

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), SecureHandler)
    print("Day 53 Secure Lab running at http://127.0.0.1:8000")
    server.serve_forever()
