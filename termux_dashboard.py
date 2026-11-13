#!/data/data/com.termux/files/usr/bin/env python3
"""
RobDoeAI-Core // Termux Native Terminal Dashboard & Telemetry
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
"""

import os
import json
import time
import subprocess

def get_memory_info():
    try:
        with open("/proc/meminfo", "r") as f:
            lines = f.readlines()
            mem_info = {}
            for line in lines:
                parts = line.split(":")
                if len(parts) == 2:
                    mem_info[parts[0].strip()] = parts[1].strip()
            total = mem_info.get("MemTotal", "Unknown")
            free = mem_info.get("MemAvailable", mem_info.get("MemFree", "Unknown"))
            return f"Total: {total} | Available: {free}"
    except Exception:
        return "Unavailable"

def render_dashboard():
    print("=" * 74)
    print(" [TERMUX NATIVE] ROBDOEAI-CORE LOCAL TELEMETRY DASHBOARD")
    print("=" * 74)
    
    uptime_str = subprocess.run(["uptime"], capture_output=True, text=True).stdout.strip()
    disk_free = subprocess.run(["df", "-h", "/data/data/com.termux/files/home"], capture_output=True, text=True).stdout
    git_branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()
    git_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
    
    dashboard_data = {
        "system": "RobDoeAI-Core // Termux Dashboard",
        "operator": "root@robdoe.com",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "uptime": uptime_str,
        "memory": get_memory_info(),
        "git_branch": git_branch,
        "dirty_files": len(git_status.splitlines()) if git_status else 0,
        "status": "TERMINAL_ENVIRONMENT_OPTIMIZED"
    }

    with open("termux_dashboard_state.json", "w") as f:
        json.dump(dashboard_data, f, indent=2)

    print(f" [+] Active Branch  : {git_branch}")
    print(f" [+] System Uptime  : {uptime_str}")
    print(f" [+] Memory Status  : {dashboard_data['memory']}")
    print(f" [+] Working Tree   : {'Clean' if dashboard_data['dirty_files'] == 0 else f'{dashboard_data[\"dirty_files\"]} files modified'}")
    print("-" * 74)
    print(" [+] Disk Usage (Home):")
    print(disk_free.strip())
    print("=" * 74)

if __name__ == "__main__":
    render_dashboard()
