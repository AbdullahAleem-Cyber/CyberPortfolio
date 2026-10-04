# Day 51: Web Application Reconnaissance & Content Discovery

## Overview
Executed web surface discovery, web server fingerprinting, and directory endpoint fuzzing against an HTTP service hosted on port 8000.

## Tools Executed & Workflows
1. *Gobuster (Directory Brute-forcing):*
   - Syntax: gobuster dir -u http://localhost:8000 -w /usr/share/wordlists/dirb/common.txt
   - Outcome: Identified local directories and endpoints (/.cache/, /.config/, /Downloads/, /Music/).

2. *Nikto (Web Application Fingerprinting):*
   - Syntax: nikto -h http://localhost:8000
   - Outcome: Extracted server banner signatures (Python/3.13.2), audited HTTP response headers, and verified directory listing status.

3. *FFUF (Parameter & Directory Fuzzing):*
   - Syntax: ffuf -w /usr/share/wordlists/dirb/common.txt -u http://localhost:8000/FUZZ
   - Outcome: Fuzzed endpoints with status code filtering (200 OK, 301 Moved Permanently).

## Key Takeaways & Defense
- *Forced Browsing Mitigation:* Disable directory indexing across web configuration settings.
- *Access Controls:* Restrict unlinked development files and administrative directories via strict Access Control Lists (ACLs).
