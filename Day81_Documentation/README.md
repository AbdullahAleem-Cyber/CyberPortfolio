# Day 81: Practical Active Directory Enumeration & Attack Path Concepts

## Overview
Practiced safe local service checking and documented how user, group, computer, and service account relationships form attack paths in Active Directory environments.

## Key Concepts Learned

### 1. Enumeration Focus Areas
- **Accounts & Machines:** Identifying user accounts, service accounts, and domain computers to understand the environment.
- **Groups & Permissions:** Checking group memberships and access rights to spot high-privilege accounts or risky shortcuts.
- **Active Services:** Observing how network services communicate (such as Kerberos on port 88, LDAP on port 389, and SMB on port 445).

### 2. Attack Paths & Defensive Hardening
- **Attack Paths:** Connected chains of permissions or access relationships leading from lower-privilege accounts to higher-value targets.
- **Defensive Hardening:** Enforcing least privilege, removing unnecessary privileges, and keeping public notes free of sensitive or private data.

## Safe Local Check Run
```bash
cd ~/CyberPortfolio/Day81_Documentation
nmap -p 88,389,445 127.0.0.1
