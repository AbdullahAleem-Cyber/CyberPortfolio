# Day 62: API Endpoint Enumeration & BOLA (Broken Object Level Authorization)

## Overview
Explored API Security vulnerabilities (OWASP API Top 10 - API1: Broken Object Level Authorization) by abusing sequential user ID parameters to enumerate and extract sensitive records, followed by implementing strict token-to-object ownership validation.

## Execution Steps & Vulnerability Proof

1. *BOLA Exploitation & ID Enumeration:*
   - Command: curl -i "http://127.0.0.1:8000/api/v1/user?id=3"
   - Result: Successfully retrieved confidential administrative records by manipulating the numerical object identifier.

2. *Remediation & Authorization Validation:*
   - Integrated Bearer token mapping to validate that the requesting user's session matches the requested object identifier.
   - Defense Verification: curl -i -H "Authorization: Bearer token-alice-123" "http://127.0.0.1:8000/api/v1/user?id=3"
   - Response: {"error": "Access Denied: BOLA Prevention - Unauthorized Object Access"}.

## Key Takeaways
- APIs frequently expose endpoints that handle object identifiers directly, making them prime targets for BOLA if authorization checks are missing.
- Every API endpoint handling object references must validate that the logged-in user has explicit permissions to access the requested resource.
