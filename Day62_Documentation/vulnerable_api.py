from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json

API_USERS = {
    "1": {"token": "token-alice-123", "username": "alice", "email": "alice@cyber.local", "credit_card": "4111-2222-3333-4444"},
    "2": {"token": "token-bob-456", "username": "bob", "email": "bob@cyber.local", "credit_card": "5555-6666-777-8888"},
    "3": {"token": "token-admin-789", "username": "admin", "email": "admin@cyber.local", "credit_card": "9999-0000-1111-2222"}
}

class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        if parsed_path.path == "/api/v1/user":
            target_id = query.get("id", [""])[0]
            auth_header = self.headers.get("Authorization", "")
            
            # Extract token from "Bearer <token>"
            token = auth_header.split(" ")[1] if "Bearer " in auth_header else ""
            
            # Identify which user owns this token
            current_user_id = None
            for uid, data in API_USERS.items():
                if data["token"] == token:
                    current_user_id = uid
                    break
            
            # SECURE (BOLA Mitigation): Ensure the user can only access their own object record unless they are admin
            if current_user_id and (current_user_id == target_id or API_USERS[current_user_id]["username"] == "admin"):
                if target_id in API_USERS:
                    user_record = API_USERS[target_id].copy()
                    del user_record["token"] # Strip sensitive auth tokens from response
                    self.wfile.write(json.dumps(user_record).encode())
                else:
                    self.wfile.write(json.dumps({"error": "User not found"}).encode())
            else:
                self.wfile.write(json.dumps({"error": "Access Denied: BOLA Prevention - Unauthorized Object Access"}).encode())
        else:
            self.wfile.write(json.dumps({"message": "Day 62: API Security Lab (Secured)"}).encode())

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), APIHandler)
    print("Day 62 Secure API Lab running at http://127.0.0.1:8000")
    server.serve_forever()
