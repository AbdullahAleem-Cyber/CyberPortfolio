# Day 56: Cross-Site Scripting (XSS) Exploitation & Remediation

## Overview
Explored Reflected Cross-Site Scripting (XSS) vulnerabilities (OWASP Top 10) by injecting malicious JavaScript into unescaped web application parameters, followed by securing the endpoint using proper HTML output encoding (html.escape).

## Execution Steps & Vulnerability Proof

1. *Reflected XSS Exploitation:*
   - Command: curl -i "http://127.0.0.1:8000/search?q=<script>alert('XSS-Exploit')</script>"
   - Result: Injected script tags were rendered directly into the server response body without filtering.

2. *Remediation & Output Encoding:*
   - Implemented Python's html.escape() method to convert characters like < and > into safe HTML entities.
   - Defense Verification: curl -i "http://127.0.0.1:8000/search?q=<script>alert('XSS-Exploit')</script>"
   - Response Body: Rendered safe escaped text (&lt;script&gt;...), neutralizing execution.

## Key Takeaways
- Reflecting user-supplied input directly into web pages allows attackers to execute arbitrary JavaScript in victim browsers.
- Context-aware output encoding is the primary defense mechanism against XSS vulnerabilities.
