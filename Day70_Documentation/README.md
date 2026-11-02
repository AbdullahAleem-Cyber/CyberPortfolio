# Day 70: Automated Vulnerability Scanning & Exploit Mapping

## Overview
Transitioned into vulnerability analysis and exploit correlation. Learned how to leverage Nmap NSE vulnerability scripts and offline exploit databases (`searchsploit`) to map discovered software versions to public Common Vulnerabilities and Exposures (CVEs).

## Execution Steps & Technical Proof

1. **Automated Vulnerability Scripting:**
   - Command: `nmap -p 80 --script vuln 127.0.0.1`
   - Result: Audited active HTTP endpoints for known script-based vulnerability signatures.

2. **Exploit Database Correlation:**
   - Command: `searchsploit apache 2.4`
   - Result: Queried offline Exploit-DB records to locate proof-of-concept (PoC) scripts and remote code execution vectors.

## Key Takeaways
- Precise service version detection allows security professionals to quickly cross-reference software stacks with known vulnerabilities.
- Reviewing local PoC exploit code via `searchsploit` helps analysts understand attack mechanisms safely without relying on automated execution blindfolded.
