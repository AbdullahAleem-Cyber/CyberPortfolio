from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json
import secrets

USERS = {
    "alice": {"password": "password123", "token": None},
    "bob": {"password": "password123", "token": None},
    "admin": {"password": "adminpassword", "token": None}
}

class AuthAPIHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        if self.path == "/api/v1/login":
            username = params.get("username", [""])[0]
            password = params.get("password", [""])[0]
            
            if username in USERS and USERS[username]["password"] == password:
                # SECURE: Generate a cryptographically secure, random token using secrets module
                secure_token = secrets.token_hex(32)
                USERS[username]["token"] = secure_token
                response = {"status": "success", "token": secure_token}
                self.wfile.write(json.dumps(response).encode())
            else:
                self.wfile.write(json.dumps({"error": "Invalid credentials"}).encode())
        else:
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        if parsed_path.path == "/api/v1/dashboard":
            auth_header = self.headers.get("Authorization", "")
            token = auth_header.split(" ")[1] if "Bearer " in auth_header else ""
            
            logged_in_user = None
            for user, data in USERS.items():
                if data["token"] and data["token"] == token:
                    logged_in_user = user
                    break
            
            if logged_in_user:
                self.wfile.write(json.dumps({"message": f"Welcome to the secure dashboard, {logged_in_user}!"}).encode())
            else:
                self.wfile.write(json.dumps({"error": "Unauthorized: Invalid cryptographic token"}).encode())
        else:
            self.wfile.write(json.dumps({"message": "Day 63: Broken Authentication API Lab (Secured)"}).encode())

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), AuthAPIHandler)
    print("Day 63 Secure API Lab running at http://127.0.0.1:8000")
    server.serve_forever()
