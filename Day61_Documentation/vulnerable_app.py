from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import datetime

def write_audit_log(client_ip, endpoint, action):
    # SECURE: Generate structured audit log entries for security monitoring and SIEM ingestion
    timestamp = datetime.datetime.utcnow().isoformat()
    log_entry = f"[{timestamp}] IP: {client_ip} | Endpoint: {endpoint} | Action: {action}\n"
    with open("security_audit.log", "a") as f:
        f.write(log_entry)
    print(f"[AUDIT LOGGED] {log_entry.strip()}")

class LoggingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        client_ip = self.client_address[0]
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        if parsed_path.path == "/admin/delete":
            target_file = query.get("file", [""])[0]
            # SECURE: Log critical administrative actions immediately
            write_audit_log(client_ip, parsed_path.path, f"Deleted file: {target_file}")
            self.wfile.write(f"<html><body><h1>Successfully deleted target: {target_file}</h1></body></html>".encode())
        else:
            self.wfile.write(b"<html><body><h1>Day 61: Insufficient Logging Lab (Secured)</h1></body></html>")

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), LoggingHandler)
    print("Day 61 Secure Lab running at http://127.0.0.1:8000")
    server.serve_forever()
