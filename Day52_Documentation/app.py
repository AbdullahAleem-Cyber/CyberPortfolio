from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class LabHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        if parsed.path == "/":
            message = """
            <html>
            <body>
                <h1>Day 52 Local Security Lab</h1>
                <p>Try the /ping endpoint.</p>
                <p>Example: /ping?host=127.0.0.1</p>
            </body>
            </html>
            """

        elif parsed.path == "/ping":
            host = params.get("host", [""])[0]

            message = f"""
            <html>
            <body>
                <h1>Ping Practice Endpoint</h1>
                <p>Received host: <b>{host}</b></p>
            </body>
            </html>
            """

        else:
            message = """
            <html>
            <body>
                <h1>404 - Not Found</h1>
            </body>
            </html>
            """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode())


server = HTTPServer(("127.0.0.1", 8000), LabHandler)

print("Day 52 lab running at http://127.0.0.1:8000")
server.serve_forever()

