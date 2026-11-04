# Day 71: Exploitation & Payload Delivery with Metasploit Framework (MSFconsole)

## Overview
Advanced into the active infrastructure exploitation module by working directly with the **Metasploit Framework (`msfconsole`)** on Kali Linux. Explored auxiliary scanner modules, searched for verified service exploits, inspected module metadata, and configured target parameters against vulnerable network service signatures.

## Key Technical Workflow & Commands

### 1. Framework Initialization & Metadata Inspection
- **Command:** `msfconsole -q`
- **Version Verified:** `Metasploit Framework 6.4.50-dev`
- **Objective:** Launched the Metasploit interface in quiet mode to streamline interaction and avoid banner delays.

### 2. Auxiliary Module Searching & Inspection
- **Command:** `search type:auxiliary ftp`
- **Result:** Filtered and enumerated active FTP scanner and gatherer modules.
- **Module Info:** Inspected specific module details using `info auxiliary/scanner/ftp/ftp_version`.

### 3. Exploitation Module Selection & Parameter Configuration
- **Module Loaded:** `use exploit/unix/ftp/vsftpd_234_backdoor`
- **Default Payload:** `cmd/unix/interact`
- **Parameter Inspection:** Executed `show options` to analyze required target parameters:
  - `RHOSTS`: Target IP address(es) to hit.
  - `RPORT`: Target port (defaulted to TCP port 21).

## Terminal Commands Executed

```bash
msfconsole -q
version
search type:auxiliary ftp
info auxiliary/scanner/ftp/ftp_version
info -d auxiliary/scanner/ftp/ftp_version
info exploit/unix/ftp/vsftpd_234_backdoor
use exploit/unix/ftp/vsftpd_234_backdoor
show options
