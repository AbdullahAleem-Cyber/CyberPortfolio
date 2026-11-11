# Day 74: Privilege Escalation Fundamentals & Advanced Meterpreter Interaction

## Overview
Advanced further into the post-exploitation module by studying local privilege escalation vectors and practicing advanced Meterpreter capabilities, including file system manipulation, process migration, and system enumeration.

## Key Technical Concepts & Workflow

### 1. Advanced Meterpreter Commands
- **`migrate <PID>`**: Moves the meterpreter payload into another running process (e.g., `explorer.exe` or `svchost.exe`) to stabilize the session and evade detection.
- **`download / upload`**: Facilitates exfiltration of sensitive target files or deployment of post-exploitation tooling.
- **`ps`**: Audits active operating system processes to identify high-privilege services or target migration candidates.

### 2. Privilege Escalation Vectors
- **SUID/SGID Binaries:** Executables that temporarily elevate user privileges to match the file owner upon execution.
- **Sudo Misconfigurations (`sudo -l`):** Identifying commands a low-privileged user is permitted to execute as root.

## Terminal Commands Executed

```bash
# Inside Meterpreter Session
sysinfo
getuid
ps
migrate 1234
pwd
ls
