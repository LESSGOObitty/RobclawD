import os
import subprocess
import shutil
import json
from datetime import datetime

def get_battery():
    try:
        res = subprocess.run(["termux-battery-status"], capture_output=True, text=True, check=True)
        data = json.loads(res.stdout)
        return f"{data.get('percentage', 'N/A')}% ({data.get('status', 'N/A')})"
    except Exception:
        return "N/A (termux-api unavailable)"

def get_storage():
    total, used, free = shutil.disk_usage(os.path.expanduser("~/workspace"))
    return f"Used: {used // (2**20)} MB | Free: {free // (2**20)} MB ({free * 100 / total:.1f}% free)"

def get_tmux_sessions():
    try:
        res = subprocess.run(["tmux", "ls"], capture_output=True, text=True, check=True)
        return res.stdout.strip().split("\n")
    except Exception:
        return ["No active tmux sessions"]

def main():
    print("\n" + "="*50)
    print(f" 🛡️  ROBCLAWD NODE PULSE | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50)
    print(f" • Device Battery : {get_battery()}")
    print(f" • Workspace Disk : {get_storage()}")
    print(f" • Tmux Sessions  :")
    for session in get_tmux_sessions():
        print(f"     - {session}")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
