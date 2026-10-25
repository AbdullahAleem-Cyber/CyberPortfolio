# Day 67: Unsafe Consumption of APIs (OWASP API Top 10 - API10)

## Overview
Explored API Unsafe Consumption vulnerabilities by analyzing risks associated with blindly trusting data returned from external third-party microservices or APIs, followed by securing the application with strict schema validation and response sanitization.

## Execution Steps & Vulnerability Proof

1. **Unsafe External Data Processing:**
   - Command: `curl -i "http://127.0.0.1:8000/api/v1/sync"`
   - Result: Processed external payload fields directly without checking types, exposing backend systems to risks if upstream services are compromised.

2. **Remediation & Schema Validation:**
   - Implemented strict whitelist validation on incoming fields (`status`) and stripped all unverified dynamic callback properties.
   - Defense Verification: Retested synchronization and verified safe, sanitized output handling.

## Key Takeaways
- Applications must never implicitly trust data received from external APIs or third-party integrations.
- Always treat external API responses as untrusted user input by enforcing strict schema validation, type checking, and sanitization before processing.
