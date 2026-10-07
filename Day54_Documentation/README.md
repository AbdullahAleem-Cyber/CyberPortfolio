# Day 54: Path Traversal Exploitation & Input Sanitization

## Overview
Analyzed Directory Traversal vulnerabilities (OWASP Top 10) by exploiting unvalidated path concatenation to read sensitive system files (/etc/passwd), followed by securing the endpoint using absolute path canonicalization (os.path.abspath).

## Execution Steps & Vulnerability Proof

1. *Path Traversal Exploitation:*
   - Command: curl -i "http://127.0.0.1:8000/file?name=../../../../etc/passwd"
   - Result: Escaped application working directory and extracted system user records from /etc/passwd.

2. *Remediation & Path Canonicalization:*
   - Implemented os.path.abspath verification to enforce access restrictions strictly within BASE_DIR.
   - Defense Verification: curl -i "http://127.0.0.1:8000/file?name=../../../../etc/passwd"
   - Response: HTTP/1.0 200 OK with body output Access Denied: Invalid File Path.

## Key Takeaways
- Direct string concatenation of user-controlled input into file paths exposes backend file systems to unauthorized read operations.
- Input validation via strict directory canonicalization (whitelisting base paths) completely mitigates path traversal attacks.
