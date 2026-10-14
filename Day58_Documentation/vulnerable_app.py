from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

USERS = {
    "alice": {"role": "user", "bio": "Hello! I am Alice."},
    "bob": {"role": "user", "bio": "Hey there, I'm Bob."},
    "admin": {
        "role": "administrator",
        "bio": "Top Secret Admin Panel: Flag{Access_Denied_123}"
    }
}

class AccessControlHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)

        if parsed_path.path != "/profile":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"Day 58: Broken Access Control Lab (Secured)"
            )
            return

        target_user = query.get("user", [""])[0]
        logged_in_user = self.headers.get("X-Session-User", "")

        if logged_in_user not in USERS:
            status = 401
            message = "Access Denied: Authentication Required"

        elif target_user not in USERS:
            status = 404
            message = "User not found"

        elif (
            logged_in_user != target_user
            and USERS[logged_in_user]["role"] != "administrator"
        ):
            status = 403
            message = "Access Denied: Unauthorized Resource Access"

        else:
            status = 200
            profile = USERS[target_user]
            message = (
                f"<html><body><h1>Profile: {target_user}</h1>"
                f"<p>Role: {profile['role']}</p>"
                f"<p>Bio: {profile['bio']}</p></body></html>"
            )

        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == "__main__":
    server = HTTPServer(
        ("127.0.0.1", 8000), AccessControlHandler
    )
    print("Day 58 Secure Lab running at http://127.0.0.1:8000")
    server.serve_forever()
