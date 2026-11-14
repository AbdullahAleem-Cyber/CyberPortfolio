# Day 76: Credential Dumping & Password Hashing

## Overview
Completed hands-on learning on credential harvesting, hash extraction mechanics, and the necessity of root administrative privileges during post-exploitation assessments.

## Key Technical Concepts & Workflow

### 1. Root Privileges & File Permissions
- **Linux (`/etc/shadow`):** Examined how restricted file permissions prevent standard users from viewing encrypted password hashes, requiring root-level access (`sudo su`) to bypass "Permission denied" errors.
- **Windows (SAM / LSASS):** Explored local account hash storage and memory-resident credentials.

### 2. Password Hashing & Offline Cracking
- **One-Way Hashes:** Understood that cryptographic hashes cannot be directly decrypted or reversed.
- **Offline Cracking Mechanics:** Learned how tools like John the Ripper use dictionaries (wordlists) and trial-and-error to recover plain-text passwords from captured hashes.

## Terminal Commands Executed

```bash
whoami
sudo su
cat /etc/shadow
