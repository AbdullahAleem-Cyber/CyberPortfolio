from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json

class FunctionAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        if parsed_path.path == "/api/v1/admin/users":
            # Extract role header to enforce RBAC
            user_role = self.headers.get("X-User-Role", "guest")
            
            # SECURE (Function-Level Authorization Check): Restrict access strictly to administrators
            if user_role != "admin":
                self.send_response(403) # HTTP 403 Forbidden
                self.wfile.write(json.dumps({"error": "Access Denied: Administrative privileges required."}).encode())
                return
            
            admin_data = {
                "status": "success",
                "privileged_action": "User database dump",
                "users": [{"id": 1, "role": "admin"}, {"id": 2, "role": "user"}]
            }
            self.wfile.write(json.dumps(admin_data).encode())
        else:
            self.wfile.write(json.dumps({"message": "Day 66: Broken Function Level Authorization Lab (Secured)"}).encode())

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), FunctionAuthHandler)
    print("Day 66 Secure API Lab running at http://127.0.0.1:8000")
    server.serve_forever()
