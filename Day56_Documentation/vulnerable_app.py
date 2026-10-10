from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import html


class XSSHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if parsed.path == "/search":
            keyword = query.get("q", [""])[0]
            safe_keyword = html.escape(keyword)

            response = (
                f"<html><body>"
                f"<h1>Search Results for: {safe_keyword}</h1>"
                f"</body></html>"
            )
            self.wfile.write(response.encode())
        else:
            self.wfile.write(
                b"<html><body><h1>Day 56 Secure XSS Lab</h1>"
                b"<form action='/search'>"
                b"<input name='q'>"
                b"<input type='submit' value='Search'>"
                b"</form></body></html>"
            )


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), XSSHandler)
    print("Day 56 Secure Lab running at http://127.0.0.1:8000")
    server.serve_forever()
