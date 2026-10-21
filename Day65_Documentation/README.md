# Day 65: Lack of Resources & Rate Limiting in APIs (OWASP API Top 10 - API4)

## Overview
Explored API Resource and Rate Limiting vulnerabilities by flooding unthrottled endpoints with automated requests, followed by securing the API with IP-based rate limiting and tracking windows.

## Execution Steps & Vulnerability Proof

1. *Request Flooding & Unthrottled Access:*
   - Command: for i in {1..10}; do curl -i "http://127.0.0.1:8000/api/v1/search"; done
   - Result: Successfully executed continuous rapid requests without restriction or server-side throttling.

2. *Remediation & Rate Limiting Enforcement:*
   - Implemented tracking logic to monitor request frequencies per client IP within sliding time windows.
   - Defense Verification: Retested rapid loops and verified that requests exceeding the threshold received an HTTP 429 Too Many Requests response.

## Key Takeaways
- Failing to implement rate limiting leaves APIs vulnerable to Denial of Service (DoS), brute-force attacks, and automated scraping.
- Robust API architectures enforce strict rate limits, payload size limits, and concurrency controls per user or IP.
