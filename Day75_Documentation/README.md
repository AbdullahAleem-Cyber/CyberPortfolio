# Day 75: Automated Enumeration & Persistence Mechanisms

## Overview
Executed hands-on practical labs covering automated privilege escalation auditing with **LinPEAS** and establishing access persistence via **Cron Jobs** on Linux systems.

## Practical Execution & Workflow

### 1. Automated Enumeration with LinPEAS
- **Execution Workflow:** Downloaded, made executable, and ran `linpeas.sh` locally.
- **Output Analysis:** Analyzed the color-coded output, noting how **Red/Yellow** highlights instantly expose critical misconfigurations, insecure file permissions, and potential privilege escalation vectors.

### 2. Persistence Implementation via Cron Jobs
- **Scheduled Task Creation:** Configured a test `@reboot` crontab entry (`crontab -e`) to automatically execute background tasks upon system startup.
- **Verification:** Verified the persistent task successfully using `crontab -l`.

## Terminal Commands Executed

```bash
wget [https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh](https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh)
chmod +x linpeas.sh
./linpeas.sh
crontab -e
crontab -l
