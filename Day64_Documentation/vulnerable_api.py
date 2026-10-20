from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json

USERS_DB = {
    "1": {
        "username": "alice",
        "email": "alice@cyber.local",
        "password_hash": "e10adc3949ba59abbe56e057f20f883e",
        "internal_salary": "$95,000",
        "ssn": "000-12-3456"
    }
}

class ExcessiveDataHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        if parsed_path.path == "/api/v1/profile":
            user_id = query.get("id", [""])[0]
            
            if user_id in USERS_DB:
                record = USERS_DB[user_id]
                # SECURE: Explicitly serialize/filter response to include ONLY non-sensitive public fields
                safe_response = {
                    "username": record["username"],
                    "email": record["email"]
                }
                self.wfile.write(json.dumps(safe_response).encode())
            else:
                self.wfile.write(json.dumps({"error": "User not found"}).encode())
        else:
            self.wfile.write(json.dumps({"message": "Day 64: Excessive Data Exposure Lab (Secured)"}).encode())

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), ExcessiveDataHandler)
    print("Day 64 Secure API Lab running at http://127.0.0.1:8000")
    server.serve_forever()
