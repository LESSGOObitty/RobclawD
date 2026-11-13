import time
import subprocess
import os

INTERVAL_SECONDS = 3600  # Run every hour

def run_task(script_path, name):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [*] Running periodic {name}...")
    try:
        subprocess.run(["python3", script_path], check=True)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [+] {name} completed successfully.")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [!] Error running {name}: {e}")

if __name__ == "__main__":
    print("[+] RobclawD Background Cron Daemon started.")
    while True:
        run_task(os.path.expanduser("~/workspace/scripts/audit_manifest.py"), "Merkle Audit & Sync")
        run_task(os.path.expanduser("~/workspace/scripts/git_guardian.py"), "Git Guardian Sync")
        time.sleep(INTERVAL_SECONDS)
