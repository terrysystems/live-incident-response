# Investigation Notes

## Initial System State

## Phase 1 — Reconnaissance and Evidence Collection
### User Identification

Command: whoami
Result: sysadmin
Meaning: Logged in as system administrator account

### System Identification

Command: hostname
Result: 4geeks-server
Meaning: Confirmed target system name

### Running Processes

Command: ps aux
Result: Multiple system processes observed including systemd, apache2, wazuh agent, and python processes

Observation:
No immediately obvious malicious processes detected

Meaning:
Further investigation required to identify subtle or hidden threats

### Network Activity

Command: ss -tulnp
Result: Open ports detected on 80 (HTTP), 21 (FTP), and 22 (SSH)

Observation:
FTP service (port 21) is active, which is less commonly used and may present a security risk

Meaning:
Potential attack surface identified, requires further investigation

### FTP Service Identification

Command: ps aux | grep ftp
Result: vsftpd service running (/usr/sbin/vsftpd /etc/vsftpd.conf)

Observation:
FTP service confirmed active and listening on port 21

Meaning:
FTP service identified as a potential entry point or attack surface, requires further investigation

### First Vulnerbility in FTP

Command: cat /etc/vsftpd.conf
Result: SSL disabled (ssl_enable=NO)

Observation:
FTP service is running without encryption

Meaning:
Credentials and data are transmitted in plain text, making the service vulnerable to interception. This represents a potential security risk and possible attack vector.

### User Enumeration

Command: cat /etc/passwd
Result: Multiple system users identified

Observation:
Three users have interactive login shells:
- sysadmin
- reports
- hacker

Meaning:
These accounts are capable of logging into the system. The presence of a user named "hacker" is suspicious and may indicate unauthorized access or a compromised account.

### Login Activity Analysis

Command: last
Result: Login history reviewed

Observation:
- sysadmin is currently logged in
- reports user had prior login activity
- no login activity found for user "hacker"

Meaning:
The "reports" account appears to be actively used.
The absence of login history for the "hacker" account is suspicious, suggesting it may have been recently created or intended for unauthorized access.
### User Privilege Check

Command: id hacker
Result: uid=1002(hacker) gid=1002(hacker) groups=1002(hacker)

Observation:
User "hacker" does not belong to any privileged groups (e.g., sudo)

Meaning:
The account does not currently have elevated privileges. However, its presence remains suspicious and could be used for unauthorized access or future privilege escalation.


### Sysadmin Privilege Check

Command: id sysadmin
Result: User belongs to sudo group

Observation:
The sysadmin account has administrative privileges

Meaning:
This account has full control over the system and can execute privileged commands. It is a high-value target for attackers and critical for system management.

## Phase 2 — Remediation and System Restoration

## Questions / Findings to Verify
