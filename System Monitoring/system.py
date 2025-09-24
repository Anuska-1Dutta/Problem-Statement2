#!/usr/bin/env python3
import psutil
import datetime

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Log file
LOG_FILE = "system_health.log"

def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")
    print(message)

def check_system_health():
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"ALERT: High CPU usage detected: {cpu_usage}%")

    # Memory Usage
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        log_message(f"ALERT: High Memory usage detected: {memory_usage}%")

    # Disk Usage
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        log_message(f"ALERT: High Disk usage detected: {disk_usage}%")

    # Running Processes
    process_count = len(psutil.pids())
    log_message(f"INFO: Running processes: {process_count}")

if __name__ == "__main__":
    check_system_health()