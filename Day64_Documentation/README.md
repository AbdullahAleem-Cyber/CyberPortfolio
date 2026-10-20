# Day 64: Excessive Data Exposure in APIs (OWASP API Top 10 - API3)

## Overview
Explored API Excessive Data Exposure vulnerabilities by inspecting raw JSON payloads that leaked internal sensitive properties (`password_hash`, `internal_salary`, `ssn`), followed by securing the endpoint with explicit response filtering and serialization.

## Execution Steps & Vulnerability Proof

1. **Excessive Data Extraction:**
   - Command: `curl -i "http://127.0.0.1:8000/api/v1/profile?id=1"`
   - Result: Captured raw response containing confidential backend fields that should never leave the server.

2. **Remediation & Explicit Filtering:**
   - Implemented server-side response serialization to construct safe dictionaries containing only authorized public properties.
   - Defense Verification: Retested the endpoint and confirmed sensitive database fields are fully stripped.

## Key Takeaways
- Never rely on client-side code to filter or hide sensitive data returned by API endpoints.
- Always apply explicit response models and serializers to filter out internal properties before transmitting JSON data.
