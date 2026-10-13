from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO users "
        "(id, username, password) "
        "VALUES (1, 'admin', 'SuperSecretPass123')"
    )

    conn.commit()
    conn.close()


class SQLiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if parsed_path.path == "/login":
            username = query.get("user", [""])[0]
            password = query.get("pass", [""])[0]

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            # For local training only
            sql_query = (
                f"SELECT * FROM users "
                f"WHERE username = ? AND password = ?"
            )

            try:
                cursor.execute(sql_query, (username,password))
                user = cursor.fetchone()

                if user:
                    message = "Login Successful!"
                else:
                    message = "Login Failed: Invalid Credentials"

                self.wfile.write(
                    f"<html><body><h1>{message}</h1></body></html>".encode()
                )

            except sqlite3.Error:
                self.wfile.write(
                    b"<html><body><h1>Database Error</h1></body></html>"
                )

            finally:
                conn.close()

        else:
            self.wfile.write(
                b"<html><body><h1>Day 57: SQL Injection Lab</h1></body></html>"
            )
if __name__ == "__main__":
    init_db()
    server = HTTPServer(("127.0.0.1", 8000), SQLiHandler)
    print("Day 57 Lab running at http://127.0.0.1:8000")
    server.serve_forever()
