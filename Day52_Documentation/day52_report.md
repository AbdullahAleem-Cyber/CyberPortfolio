Day 52 - HTTP Request and Burp Suite Practice

Today I practiced sending HTTP requests with curl.

Target:
http://127.0.0.1:8000/ping?host=hello

127.0.0.1 refers to the local machine.

The server returned:
HTTP/1.0 200 OK

I also used Burp Suite to intercept the HTTP request.

Burp showed the request as:
GET /ping?host=hello HTTP/1.1

Host: 127.0.0.1:8000

This helped me understand how a client sends an HTTP request
to a web server and how Burp Suite can intercept and inspect
the request.
