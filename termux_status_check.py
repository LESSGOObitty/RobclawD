#!/data/data/com.termux/files/usr/bin/env python3
import os
import json
import time
import subprocess

def system_status():
    print("=" * 74)
    print(" [TERMUX] LIVE COMMAND TERMINAL ENVIRONMENT CHECK")
    print("=" * 74)
    
    uname = os.uname()
    uptime = subprocess.run(["uptime"], capture_output=True, text=True).stdout.strip()
    git_status = subprocess.run(["git", "status", "-s"], capture_output=True, text=True).stdout.strip()
    
    status = {
        "system": "RobDoeAI-Core // Termux Environment Status",
        "operator": "root@robdoe.com",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "os_release": f"{uname.sysname} {uname.release} {uname.machine}",
        "uptime_output": uptime,
        "git_dirty_files": len(git_status.splitlines()) if git_status else 0,
        "status": "TERMUX_COMMAND_LINE_READY"
    }
    
    with open("termux_status.json", "w") as f:
        json.dump(status, f, indent=2)

    print(f" [+] OS Kernel    : {status['os_release']}")
    print(f" [+] System Uptime: {uptime}")
    print(f" [+] Git Working  : {'Clean' if status['git_dirty_files'] == 0 else 'Unstaged modifications present'}")
    print("=" * 74)

if __name__ == "__main__":
    system_status()
