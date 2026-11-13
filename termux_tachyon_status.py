#!/data/data/com.termux/files/usr/bin/env python3
"""
RobDoeAI-Core // Termux Tachyon Status & Repository Verification
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
"""

import os
import json
import time
import subprocess

def check_tachyon_status():
    print("=" * 74)
    print(" [TERMUX] VERIFYING TACHYONIC MANIFOLD & REPOSITORY GIT TELEMETRY")
    print("=" * 74)

    git_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
    commit_count = subprocess.run(["git", "rev-list", "--count", "HEAD"], capture_output=True, text=True).stdout.strip()
    active_branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()

    dirty_count = len(git_status.splitlines()) if git_status else 0
    tree_msg = "Clean" if dirty_count == 0 else f"{dirty_count} modified files"

    status_data = {
        "system": "RobDoeAI-Core // Termux Tachyon Status",
        "operator": "root@robdoe.com",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "active_branch": active_branch,
        "total_commits": commit_count,
        "invariant_anchor": 932808725,
        "dirty_files": dirty_count,
        "status": "TACHYON_FIELD_SECURE"
    }

    with open("termux_tachyon_status.json", "w") as f:
        json.dump(status_data, f, indent=2)

    print(f" [+] Active Branch  : {active_branch}")
    print(f" [+] Total Commits  : {commit_count}")
    print(f" [+] Invariant Base : {status_data['invariant_anchor']}")
    print(f" [+] Working Tree   : {tree_msg}")
    print(f" [+] State Saved To : termux_tachyon_status.json")
    print("=" * 74)

if __name__ == "__main__":
    check_tachyon_status()
