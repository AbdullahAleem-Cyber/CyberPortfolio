from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import urllib.parse
import urllib.request
import ipaddress
import socket

ALLOWED_DOMAINS = ["example.com", "httpbin.org"]

def is_internal_ip(hostname):
    try:
        ip_str = socket.gethostbyname(hostname)
        ip = ipaddress.ip_address(ip_str)
        return ip.is_loopback or ip.is_private or ip.is_link_local
    except Exception:
        return True

class SSRFHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if parsed_path.path == "/fetch":
            target_url = query.get("url", [""])[0]
            parsed_target = urllib.parse.urlparse(target_url)
            hostname = parsed_target.hostname

            if hostname and hostname in ALLOWED_DOMAINS and not is_internal_ip(hostname):
                try:
                    req = urllib.request.Request(
                        target_url,
                        headers={'User-Agent': 'Mozilla/5.0'}
                    )

                    with urllib.request.urlopen(req, timeout=3) as response:
                        content = response.read().decode(
                            'utf-8',
                            errors='ignore'
                        )

                    self.wfile.write(
                        f"<html><body><h1>Fetched Content:</h1>"
                        f"<pre>{content}</pre></body></html>".encode()
                    )

                except Exception as e:
                    self.wfile.write(
                        f"<html><body><h1>Error fetching URL:</h1>"
                        f"<p>{str(e)}</p></body></html>".encode()
                    )
            else:
                self.wfile.write(
                    b"<html><body><h1>Access Denied: "
                    b"Restricted Destination URL</h1></body></html>"
                )
        else:
            self.wfile.write(
                b"<html><body><h1>"
                b"Day 55: SSRF Security Lab (Secured)"
                b"</h1></body></html>"
            )

if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8000), SSRFHandler)
    print("Day 55 Secure Lab running at http://127.0.0.1:8000")
    server.serve_forever()
