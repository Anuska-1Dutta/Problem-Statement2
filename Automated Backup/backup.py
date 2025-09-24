#!/usr/bin/env python3
import os
import tarfile
import datetime
import subprocess

# Settings
SOURCE_DIR = r"C:\Users\anusk\OneDrive\Desktop\MyData"
BACKUP_DIR = r"C:\Users\anusk\OneDrive\Desktop\Backup"
REMOTE_SERVER = "anusk@192.168.29.51:/mnt/c/Users/anusk/OneDrive/Desktop/Backup"  # remote server

# Log file
LOG_FILE = "backup.log"

def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")
    print(message)

def create_backup():
    try:
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)

        # Backup filename with timestamp
        backup_filename = os.path.join(
            BACKUP_DIR,
            f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"
        )

        # Create tar.gz archive
        with tarfile.open(backup_filename, "w:gz") as tar:
            tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))

        log_message(f"Backup created successfully: {backup_filename}")
        return backup_filename
    except Exception as e:
        log_message(f"ERROR creating backup: {str(e)}")
        return None

def upload_backup(backup_file):
    try:
        result = subprocess.run(
            ["scp", backup_file, REMOTE_SERVER],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            log_message(f"Backup uploaded successfully to {REMOTE_SERVER}")
        else:
            log_message(f"ERROR uploading backup: {result.stderr}")
    except Exception as e:
        log_message(f"ERROR during upload: {str(e)}")

if __name__ == "__main__":
    backup_file = create_backup()
    if backup_file:
        upload_backup(backup_file)