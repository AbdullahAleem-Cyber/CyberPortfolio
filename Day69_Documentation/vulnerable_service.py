from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SecureBannerHandler(BaseHTTPRequestHandler):

    server_version = "SecureServer"
    sys_version = ""

    def version_string(self):
        return "SecureServer"

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {
            "status": "success",
            "message": "Welcome to the Day 69 Secured Service Lab"
        }

        self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), SecureBannerHandler)
    print("Day 69 Secure Lab running at http://127.0.0.1:8000")
    server.serve_forever()

