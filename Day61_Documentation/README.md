# Day 61: Insufficient Logging & Monitoring Exploitation & Remediation

## Overview
Explored Insufficient Logging and Monitoring vulnerabilities (OWASP Top 10) by executing unmonitored administrative actions that leave no forensic trail, followed by securing the application with structured security audit logging.

## Execution Steps & Vulnerability Proof

1. *Unmonitored Action Exploitation:*
   - Command: curl -i "http://127.0.0.1:8000/admin/delete?file=system.conf"
   - Result: Critical system action performed successfully without generating server-side event logs or alerting defenders.

2. *Remediation & Audit Logging:*
   - Integrated python logging routines to record timestamps, client IP addresses, endpoints, and requested parameters into security_audit.log.
   - Defense Verification: Retested requests and verified real-time audit trail generation.

## Key Takeaways
- Without robust logging and monitoring, attackers can operate undetected inside systems for extended periods.
- Comprehensive security logs must capture critical events (logins, failed authentications, and privileged modifications) to feed SIEM and incident response pipelines.
