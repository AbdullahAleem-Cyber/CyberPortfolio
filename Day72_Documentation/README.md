# Day 72: Payload Configuration & Exploit Execution with Metasploit

## Overview
Advanced further into the Network Penetration Testing module by focusing on payload mechanics, local listener configurations (`LHOST`, `LPORT`), and the fundamentals of executing remote code execution (RCE) vectors safely within a controlled lab environment.

## Key Technical Concepts & Workflow

### 1. Understanding Payloads
- **Reverse Shells:** The target system connects back to the attacker's machine. Highly effective for bypassing inbound firewall rules.
- **Bind Shells:** The target opens a listening port on itself, and the attacker connects directly to it (vulnerable to inbound filtering).

### 2. Parameter Configuration
- **Target Parameters:** `RHOSTS` (Target IP) and `RPORT` (Target Port).
- **Listener Parameters:** `LHOST` (Attacker/Kali IP) and `LPORT` (Listening Port for incoming callback connections).

## Terminal Commands Executed

```bash
msfconsole -q
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 192.168.x.x
show payloads
set LHOST 192.168.x.y
show options
