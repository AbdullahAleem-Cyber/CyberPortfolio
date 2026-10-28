# Day 68: Network Reconnaissance & Service Enumeration with Nmap

## Overview
Transitioned into *Network Penetration Testing*, focusing on active reconnaissance, TCP SYN port scanning (-sS), and service version fingerprinting (-sV) using Nmap in a Kali Linux environment against a locally hosted service.

## Execution Steps & Methodology

1. *Local Service Deployment:*
   - Hosted a Python HTTP server on port 8000 (python3 -m http.server 8000 --bind 127.0.0.1) to simulate a live listening network service.

2. *Stealth Port Scanning & Service Fingerprinting:*
   - Command: sudo nmap -sS -sV -p 8000 127.0.0.1
   - Result: Successfully bypassed closed ports, identified port 8000 as open, and accurately fingerprinted the service banner (SimpleHTTPServer 0.6).

## Key Takeaways
- Nmap service version detection (-sV) probes open ports to elicit service protocols and exact version numbers.
- Combining SYN scanning with version fingerprinting provides a complete tactical map of target infrastructure during the initial phase of a penetration test.
