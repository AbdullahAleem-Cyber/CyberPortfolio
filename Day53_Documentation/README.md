# Day 53: Command Injection Vulnerability & Input Sanitization

## Overview
Demonstrated OS command injection by passing shell operators (;&|) into unvalidated web parameters, followed by implementing strict IP validation to secure the backend application.

## Execution Steps & Vulnerability Proof

1. Vulnerable Target Execution:
   - Command: curl -i "http://127.0.0.1:8000/ping?host=127.0.0.1;whoami"
   - Result: Executed ping -c 1 127.0.0.1 and appended system execution for whoami, returning the current user (kali).

2. Remediation & Input Validation:
   - Implemented IP address parsing check (ipaddress.ip_address()) prior to command assembly.
   - Verified Defense: curl -i "http://127.0.0.1:8000/ping?host=127.0.0.1;whoami"
   - Response: HTTP/1.0 200 OK with body output <h1>Invalid IP address</h1>.

## Key Takeaways
- Unsanitized inputs appended directly to system calls allow arbitrary command execution.
- Strict input validation (whitelisting allowed characters or validating expected data types) completely prevents parameter-based injection attacks.
