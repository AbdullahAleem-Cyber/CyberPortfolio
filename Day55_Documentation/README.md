# Day 55: Server-Side Request Forgery (SSRF) Exploitation & Remediation

## Overview
Explored Server-Side Request Forgery (SSRF) vulnerabilities (OWASP Top 10) by forcing a backend application to query internal loopback addresses, followed by implementing strict domain whitelisting and internal IP address blocking.

## Execution Steps & Vulnerability Proof

1. *SSRF Exploitation:*
   - Command: curl -i "http://127.0.0.1:8000/fetch?url=http://127.0.0.1:8000/"
   - Result: Forced the server to make an HTTP request to its own local loopback port, exposing internal service output.

2. *Remediation & IP Filtering:*
   - Implemented domain whitelisting (ALLOWED_DOMAINS) and checked resolved IPs via socket and ipaddress libraries to block loopback, private, and link-local ranges.
   - Defense Verification: curl -i "http://127.0.0.1:8000/fetch?url=http://127.0.0.1:8000/"
   - Response: Access Denied: Restricted Destination URL.

## Key Takeaways
- Allowing unvalidated user-supplied URLs in backend HTTP requests leads to SSRF, enabling internal network reconnaissance and service abuse.
- Mitigations require strict destination domain whitelisting and validation of resolved IP addresses against private or loopback spaces.
