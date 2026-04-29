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


## Phase 2 — Remediation and System Restoration

## Questions / Findings to Verify
