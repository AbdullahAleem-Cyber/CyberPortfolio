from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json

class UnsafeConsumptionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        if parsed_path.path == "/api/v1/sync":
            # Mock external response
            external_mock_response = {
                "status": "active",
                "callback_action": "print('MOCK EXTERNAL EXECUTION: Unsafe Third-Party Data Processed')"
            }
            
            # SECURE (Schema Validation & Sanitization): Explicitly validate expected keys and types
            allowed_status = ["active", "inactive", "pending"]
            fetched_status = external_mock_response.get("status")
            
            if fetched_status not in allowed_status:
                self.wfile.write(json.dumps({"error": "Security Error: Invalid status received from external API"}).encode())
                return
            
            # Completely strip or ignore unverified dynamic execution fields (callback_action)
            safe_processed_data = {
                "status": fetched_status,
                "note": "External data sanitized and validated successfully against schema."
            }
            
            response = {
                "status": "success",
                "message": "Third-party API synced securely",
                "processed_data": safe_processed_data
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.wfile.write(json.dumps({"message": "Day 67: Unsafe Consumption of APIs Lab (Secured)"}).encode())

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), UnsafeConsumptionHandler)
    print("Day 67 Secure API Lab running at http://127.0.0.1:8000")
    server.serve_forever()
