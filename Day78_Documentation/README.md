# Day 78: Network Pivoting, Tunneling & Port Forwarding

## Overview
Advanced into enterprise internal network reconnaissance and pivoting within the Network Penetration Testing and Post-Exploitation module. Learned how to route traffic through compromised hosts to reach hidden subnets.

## Key Technical Concepts & Workflow

### 1. Network Pivoting & Tunneling
- **Definition:** The technique of using a compromised machine (the pivot host) as a gateway to access other internal networks that are normally firewalled from the external attacker.
- **Proxychains:** A tool that forces command-line applications (like `nmap`) to route network connections through proxy servers or tunnels (such as SOCKS4/SOCKS5).

## Terminal Commands Executed

```bash
cd ~/CyberPortfolio/Day78_Documentation
# Example proxychains configuration and tool execution workflow
proxychains nmap -sT -p 80 192.168.2.10
