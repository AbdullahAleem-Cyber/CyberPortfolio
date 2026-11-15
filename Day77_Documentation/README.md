# Day 77: Lateral Movement & Pass-the-Hash (PtH)

## Overview
Advanced into enterprise network pivoting and lateral movement within the Network Penetration Testing and Post-Exploitation module. Learned how captured password hashes are weaponized to authenticate across multiple systems without cracking them.

## Key Technical Concepts & Workflow

### 1. Network Pivoting & Lateral Movement
- **Definition:** The methodology of moving from a compromised initial foothold to other hosts within an internal network infrastructure.
- **Objective:** Reaching critical assets such as file servers, domain controllers, or internal management portals.

### 2. Pass-the-Hash (PtH) Attack Mechanics
- **Authentication Protocol Flaw:** Exploits how NTLM authentication relies on password hashes rather than requiring plain-text passwords.
- **Hash Injection:** Using tools to pass a captured user hash directly to network services (like SMB or WinRM) to gain remote administrative sessions.

## Terminal Commands Executed

```bash
cd ~/CyberPortfolio/Day77_Documentation
# Example conceptual workflow for network scanning and lateral movement enumeration
nmap -p 445 --script smb-os-discovery 192.168.1.0/24
