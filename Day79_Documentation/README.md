# Day 79: Active Directory Fundamentals & Domain Enumeration

## Overview
Started learning Active Directory (AD) basics and domain enumeration concepts as part of the Network Penetration Testing and Post-Exploitation module.

## Key Concepts Learned

### 1. Active Directory Basics
- **Domain:** A group of users, computers, and devices managed under shared central rules.
- **Domain Controller (DC):** The central server that handles authentication and stores directory information.
- **Groups & Privileges:** Collections of accounts (such as standard users or administrators) that control access levels.

### 2. Domain Enumeration
- **Purpose:** Mapping users, groups, hosts, and services in an authorized environment to understand network structure and security risks.
- **Privacy & Safety:** Keep all practice inside authorized labs and avoid exposing sensitive credentials or private data in public notes.

## Example Command (Authorized Lab)

```bash
cd ~/CyberPortfolio/Day79_Documentation
nmap -p 88,389,445 --open 192.168.1.0/24
