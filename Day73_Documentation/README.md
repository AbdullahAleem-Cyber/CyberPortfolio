# Day 73: Post-Exploitation & Session Management with Metasploit

## Overview
Advanced into the post-exploitation phase of our Network Penetration Testing module. Learned how to manage active compromise sessions, switch between background tasks, and execute foundational post-exploitation enumeration commands within the Metasploit Framework.

## Key Technical Concepts & Workflow

### 1. Session Management
- **`sessions -l`**: Lists all active exploitation sessions established with target machines.
- **`sessions -i <id>`**: Connects directly into an active background session to execute commands.
- **`background`**: Safely detaches from an active session and returns control to the main `msfconsole` prompt.

### 2. Post-Exploitation Enumeration
- **Privilege & Identity Verification (`getuid`):** Determines the security context and user account under which the payload is executing.
- **System Reconnaissance (`sysinfo`):** Gathers OS architecture, hostname, and kernel details of the compromised host.

## Terminal Commands Executed

```bash
msfconsole -q
sessions -l
sessions -i 1
sysinfo
getuid
background
