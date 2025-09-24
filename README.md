# Problem Statement 2: System Health Monitoring & Automated Backup

This repository contains two scripts developed as part of *Problem Statement 2*:

1. *System Health Monitoring Script* (system_monitor.sh)  
2. *Automated Backup Script* (backup.py)

---

1️⃣ System Health Monitoring Script

*File:* system_monitor.sh  
*Language:* Bash  

### Features:
- Monitors *CPU usage, **Memory usage, **Disk usage, and **Running processes*.
- Logs *alerts* when usage exceeds predefined thresholds.
- Records information in a *log file* with timestamps.
- Designed for macOS / Linux systems.

### Usage:
1. Open Terminal and navigate to the script folder:
   ```bash
   cd /path/to/script
##Make the script executable:

chmod +x system_monitor.sh
Run the script:

./system_monitor.sh
Configuration:

Update the following variables in backup.py:

# Folder to backup
SOURCE_DIR = r"C:\Users\anusk\OneDrive\Desktop\MyData"

# Local backup storage
BACKUP_DIR = r"C:\Users\anusk\OneDrive\Desktop\Backup"

# Remote server (optional)
REMOTE_SERVER = "user@remote_host:/path/to/remote/folder"
Usage:

Open VS Code terminal and navigate to the script folder:

cd "D:\Problem Statement2\Automated Backup"

Run the script:

python backup.py
