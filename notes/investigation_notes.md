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

### Hacker User Directory Analysis

Command: ls -la /home/hacker
Result: Only default shell configuration files present

Observation:
No suspicious files, scripts, or hidden backdoors found in the hacker user's home directory

Meaning:
The account appears to be newly created with no active usage. This suggests it may have been established as a persistence mechanism for future unauthorized access.

### FTP User Access Control Check vulnerbility

Command: cat /etc/vsftpd.userlist
Result: File not found

Observation:
No user access control list is configured for FTP

Meaning:
FTP access is not restricted by a user list. Combined with the lack of encryption, this increases the risk of unauthorized access using any valid system account.

### FTP Service Misconfig Vulnerbility

Command: ps aux | grep ftp
Result: vsftpd process running as root

Observation:
FTP service is actively running on the system

Meaning:
The system is currently exposing an active FTP service. Combined with lack of encryption and access controls, this represents a security risk.

### FTP Local User Access

Command: cat /etc/vsftpd.conf | grep -i local_enable
Result: local_enable=YES

Observation:
Local system users are allowed to authenticate via FTP

Meaning:
Any valid system account can access the FTP service. Without a user restriction list, this increases the attack surface if credentials are compromised.

The vsftpd FTP service was identified as active and potentially insecure.

Actions taken:
- Stopped the service using: systemctl stop vsftpd
- Disabled the service using: systemctl disable vsftpd

Result:
- Service is no longer running
- Service will not start on system reboot
- System exposure via FTP has been mitigated

 ## A suspicious user account named 'hacker' was identified.

The account has:
- A valid shell (/bin/bash)
- A home directory (/home/hacker)

No login activity was found using the `last` command, suggesting:
- The account may have been created for persistence
- Or used through non-interactive methods 

## Phase 2 – Remediation and System Restoration


Based on the findings from Phase 1, remediation actions were taken to remove unauthorized access and reduce potential attack vectors.



Actions performed:

Stopped the FTP service to eliminate active exposure:

systemctl stop vsftpd

Disabled the FTP service to prevent it from starting on reboot:

systemctl disable vsftpd

Identified and removed the unauthorized user account:

sudo userdel -r hacker

Verified that the user account and associated home directory were removed

Checked for active processes related to the unauthorized user:

ps aux | grep hacker

Inspected cron directories for persistence mechanisms:

sudo ls -la /var/spool/cron/crontabs/

Reviewed login history for suspicious activity:

last



All remediation actions were validated to ensure no remaining traces of the unauthorized user or active attack vectors.



Result:

Unauthorized user account successfully removed

FTP service disabled, reducing system exposure

No evidence of active processes or persistence mechanisms

System restored to a secure operational state


