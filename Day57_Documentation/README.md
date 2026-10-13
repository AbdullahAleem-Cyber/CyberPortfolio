# Day 57: SQL Injection (SQLi) Exploitation & Remediation

## Overview
Explored SQL Injection (SQLi) vulnerabilities (OWASP Top 10) by injecting malicious SQL control characters into unvalidated login parameters to bypass authentication, followed by securing the database layer using parameterized queries.

## Execution Steps & Vulnerability Proof

1. *Authentication Bypass Exploitation:*
   - Command: curl -i "http://127.0.0.1:8000/login?user=admin' OR '1'='1&pass=anything"
   - Result: Injected string logic forced the SQL WHERE clause to evaluate to true, granting unauthorized admin access.

2. *Remediation & Parameterized Queries:*
   - Replaced string formatting with SQLite parameterized placeholders (?).
   - Defense Verification: curl -i "http://127.0.0.1:8000/login?user=admin' OR '1'='1&pass=anything"
   - Response: Login Failed: Invalid Credentials.

## Key Takeaways
- Direct string concatenation in database queries allows attackers to manipulate query structures and bypass security controls.
- Parameterized queries (prepared statements) separate code from data, completely eliminating SQL injection vectors.
