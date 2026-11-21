# Day 80: Service Accounts, Kerberos Basics & Kerberoasting Concepts

## Overview
Learned how normal user accounts, service accounts, and Kerberos tickets work together in Active Directory, why weak service account passwords create risk (Kerberoasting concepts), and how defenders protect against these risks.

## Key Concepts Learned

### 1. Service Accounts & Kerberos Tickets
- **Service Accounts:** Accounts created for software programs or background services rather than individual human users.
- **Kerberos Tickets:** Digital tickets used in Active Directory so users can access services without sending raw passwords repeatedly.

### 2. Kerberoasting Concepts & Defensive Hardening
- **Risk of Weak Passwords:** Service tickets tied to service accounts can face offline password-guessing risk if a service account uses a weak or static password.
- **How Defenders Protect:** Use strong or automatically rotating passwords (such as Group Managed Service Accounts), limit permissions to what is truly needed (least privilege), and monitor activity.

## Key Takeaways
- High-privilege service accounts with weak passwords are a serious security weakness in Active Directory.
- Strong password habits, least privilege, and monitoring help keep domain accounts safe.
