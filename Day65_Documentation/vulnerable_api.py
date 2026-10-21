from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json
import time

# In-memory rate limiting tracker: {client_ip: [timestamp1, timestamp2, ...]}
REQUEST_HISTORY = {}
RATE_LIMIT_MAX = 3      # Maximum allowed requests
RATE_LIMIT_WINDOW = 10  # Time window in seconds

class RateLimitHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        client_ip = self.client_address[0]
        current_time = time.time()
        
        if parsed_path.path == "/api/v1/search":
            # Initialize or clean up request history for this IP
            if client_ip not in REQUEST_HISTORY:
                REQUEST_HISTORY[client_ip] = []
            
            # Filter out timestamps outside the current time window
            REQUEST_HISTORY[client_ip] = [t for t in REQUEST_HISTORY[client_ip] if current_time - t < RATE_LIMIT_WINDOW]
            
            # SECURE (Rate Limiting Check): Block if threshold is exceeded
            if len(REQUEST_HISTORY[client_ip]) >= RATE_LIMIT_MAX:
                self.send_response(429) # HTTP 429 Too Many Requests
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Rate Limit Exceeded: Too many requests. Please try again later."}).encode())
                return
            
            # Record current request timestamp
            REQUEST_HISTORY[client_ip].append(current_time)
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "success", "data": "Search results retrieved successfully."}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Day 65: Lack of Resources Lab (Secured)"}).encode())

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), RateLimitHandler)
    print("Day 65 Secure API Lab running at http://127.0.0.1:8000")
    server.serve_forever()
