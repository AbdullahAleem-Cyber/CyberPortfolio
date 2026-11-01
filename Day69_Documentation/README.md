# Day 69: Network Reconnaissance - Service Enumeration & Banner Grabbing

## Overview
Explored network service enumeration and banner grabbing vulnerabilities by analyzing how verbose server headers leak sensitive software versions, followed by securing the server through header minimization and banner masking.

## Execution Steps & Vulnerability Proof

1. **Banner Grabbing & Information Disclosure:**
   - Command: `curl -i "http://127.0.0.1:8000/"`
   - Result: Inspected HTTP response headers (`Server`, `X-Powered-By`) which leaked exact, outdated component versions.

2. **Remediation & Header Hardening:**
   - Replaced explicit version signatures with generic, minimal strings (`SecureServer`).
   - Defense Verification: Retested headers via `cURL` and confirmed version concealment.

## Key Takeaways
- Leaking detailed software versions allows attackers to easily match targets against vulnerability databases (e.g., Exploit-DB).
- Hardening network services requires stripping unnecessary response headers and masking server signatures.
