# Day 66: Broken Function Level Authorization in APIs (OWASP API Top 10 - API5)

## Overview
Explored API Function Level Authorization vulnerabilities by accessing hidden administrative endpoints without proper role verification, followed by securing the API with strict Role-Based Access Control (RBAC) header validation.

## Execution Steps & Vulnerability Proof

1. **Unauthorized Function Execution:**
   - Command: `curl -i "http://127.0.0.1:8000/api/v1/admin/users"`
   - Result: Successfully executed sensitive administrative functions without holding administrative privileges.

2. **Remediation & RBAC Enforcement:**
   - Integrated header-based role checking (`X-User-Role`) to ensure only verified administrators can invoke sensitive management endpoints.
   - Defense Verification: Retested requests and confirmed unprivileged queries receive an HTTP `403 Forbidden` response.

## Key Takeaways
- Complex access control policies with different role hierarchies often result in flaws where administrative functions are left exposed to lower-privileged users.
- Every API endpoint handling administrative or privileged actions must explicitly validate the user's role and permissions on the server side.
