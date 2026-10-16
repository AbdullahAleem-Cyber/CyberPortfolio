# Day 60: Vulnerable & Outdated Components Exploitation & Remediation

## Overview
Explored the risks of Using Components with Known Vulnerabilities (OWASP Top 10) by identifying outdated software dependencies exposing known CVE vectors, followed by securing the application through dependency patching and version upgrades.

## Execution Steps & Vulnerability Proof

1. *Component Fingerprinting:*
   - Command: curl -i "http://127.0.0.1:8000/version"
   - Result: Exposed outdated library version (1.0.1) susceptible to remote exploit matching.

2. *Remediation & Dependency Patching:*
   - Upgraded component architecture to the secure patched version (2.0.0).
   - Defense Verification: curl -i "http://127.0.0.1:8000/version"
   - Response: Confirmed execution runs on secure patched libraries.

## Key Takeaways
- Using unmaintained or outdated third-party libraries introduces major supply-chain vulnerabilities.
- Regular Software Bill of Materials (SBOM) audits and automated dependency scanning (e.g., pip audit, npm audit) are essential to maintaining application hygiene.
