# Day 52: HTTP Request Inspection & Burp Suite Proxying

## Overview
Built a local Python HTTP service to practice client-server HTTP communication, request parameter manipulation, and traffic interception using Burp Suite Community Edition.

## Execution Steps & Commands

1. Local Target Server Setup:
   - Script: app.py
   - Endpoint: http://127.0.0.1:8000/ping?host=<parameter>

2. Parameter Testing with cURL:
   - Command: curl -i "http://127.0.0.1:8000/ping?host=hello"
   - Response: HTTP/1.0 200 OK

3. Burp Suite Proxy Interception:
   - Configured proxy listener on 127.0.0.1:8080.
   - Intercepted request structure:
     GET /ping?host=hello HTTP/1.1
     Host: 127.0.0.1:8000

## Key Findings
- Verified how GET parameters transmit data to web backend services.
- Confirmed Burp Suite proxy interception for inspecting and modifying HTTP headers before server execution.
