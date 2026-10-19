# Day 63: Broken User Authentication in APIs (OWASP API Top 10 - API2)

## Overview
Explored API Broken Authentication vulnerabilities by exploiting weak, predictable session tokens to impersonate administrative users, followed by securing the API with cryptographically secure random token generation (secrets module).

## Execution Steps & Vulnerability Proof

1. *Token Guessing & Spoofing:*
   - Command: curl -i -H "Authorization: Bearer token_admin_3" "http://127.0.0.1:8000/api/v1/dashboard"
   - Result: Successfully bypassed authentication by guessing sequential token patterns to impersonate the admin user.

2. *Remediation & Secure Token Generation:*
   - Replaced weak tokens with high-entropy cryptographic hex tokens generated via Python's secrets.token_hex(32).
   - Defense Verification: Retested the spoofed token against the secured endpoint and received an unauthorized rejection.

## Key Takeaways
- API authentication tokens must never be predictable, sequential, or based on user attributes.
- Utilizing strong, cryptographically secure random number generators (CSPRNG) ensures tokens cannot be guessed or brute-forced.
