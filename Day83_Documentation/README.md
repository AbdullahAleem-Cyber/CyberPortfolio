# Day 83: Delegation & Lateral Movement Concepts in Active Directory

## Overview
Continued the Active Directory learning track by exploring how delegation works across services, how lateral movement connects systems across a network, and how defenders reduce risk in authorized environments.

## Key Concepts Learned

### 1. Delegation in Active Directory
- **Purpose:** Allows a service or host to act on behalf of an authenticated user when interacting with other domain resources.
- **Security Risk & Control:** Over-broad delegation settings can create unintended escalation paths if an intermediate service is compromised, making tight scoping essential.

### 2. Lateral Movement & Defensive Hardening
- **Lateral Movement:** Moving across internal systems and accounts after an initial foothold toward higher-value targets.
- **Defensive Controls:** Restrict delegation scope, enforce least privilege and account separation, monitor cross-host authentication, and keep public documentation privacy-safe.

## Key Takeaways
- Over-trusted delegation and overly broad cross-system access increase the blast radius of a compromised host.
- Scoped permissions, clean identity boundaries, and monitoring help contain lateral movement.
