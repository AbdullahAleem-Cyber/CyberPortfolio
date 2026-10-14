# Day 58: Broken Access Control Exploitation & Remediation

## Overview
Explored Broken Access Control and IDOR (Insecure Direct Object Reference) vulnerabilities (OWASP Top 10) by bypassing authorization logic to view restricted user profiles, followed by implementing strict role-based and session-based access controls.

## Execution Steps & Vulnerability Proof

1. *Access Control Exploitation (IDOR):*
   - Command: curl -i "http://127.0.0.1:8000/profile?user=admin"
   - Result: Successfully retrieved confidential administrator profile data without session verification.

2. *Remediation & Authorization Validation:*
   - Implemented strict session header verification (X-Session-User) ensuring users can only read records matching their active session or administrator privileges.
   - Defense Verification: curl -i -H "X-Session-User: alice" "http://127.0.0.1:8000/profile?user=admin"
   - Response: Access Denied: Unauthorized Resource Access.

## Key Takeaways
- Failing to verify user permissions for every object or route request leads to serious privilege escalation and data exposure.
- Robust access controls require central authorization checks matching user session identities against requested resources.
