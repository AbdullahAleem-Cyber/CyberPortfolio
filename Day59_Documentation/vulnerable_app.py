from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import os

class MisconfigHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        self.send_response(200)
        # SECURE: Generic Server header to prevent version fingerprinting
        self.send_header("Server", "Webserver")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        if parsed_path.path == "/config":
            # SECURE: Block access to sensitive configuration backup files
            self.wfile.write(b"<html><body><h1>403 Forbidden: Access to configuration files is restricted.</h1></body></html>")
        elif parsed_path.path == "/debug":
            # SECURE: Generic error message without leaking internal database logic or stack traces
            self.wfile.write(b"<html><body><h1>500 Internal Server Error</h1><p>An unexpected error occurred. Please try again later.</p></body></html>")
        else:
            self.wfile.write(b"<html><body><h1>Day 59: Security Misconfiguration Lab (Secured)</h1></body></html>")

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), MisconfigHandler)
    print("Day 59 Secure Lab running at http://127.0.0.1:8000")
    server.serve_forever()
EOF
