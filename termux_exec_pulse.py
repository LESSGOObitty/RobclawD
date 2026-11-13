#!/data/data/com.termux/files/usr/bin/env python3
"""
RobDoeAI-Core // Termux Native Execution Pulse (Syntax-Safe Patch)
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
"""

import os
import json
import time
import subprocess

def execute_pulse():
    print("=" * 74)
    print(" [TERMUX PULSE] EXECUTING LOCAL COMMAND SUITE & VERIFYING GIT TREE")
    print("=" * 74)

    git_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
    commit_count = subprocess.run(["git", "rev-list", "--count", "HEAD"], capture_output=True, text=True).stdout.strip()
    active_branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()

    dirty_count = len(git_status.splitlines()) if git_status else 0
    tree_msg = "Clean" if dirty_count == 0 else f"{dirty_count} modified files"

    pulse_data = {
        "system": "RobDoeAI-Core // Termux Execution Pulse",
        "operator": "root@robdoe.com",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "active_branch": active_branch,
        "total_commits": commit_count,
        "dirty_files": dirty_count,
        "status": "TERMUX_PULSE_VERIFIED"
    }

    with open("termux_pulse_state.json", "w") as f:
        json.dump(pulse_data, f, indent=2)

    print(f" [+] Active Branch  : {active_branch}")
    print(f" [+] Total Commits  : {commit_count}")
    print(f" [+] Working Tree   : {tree_msg}")
    print(f" [+] Pulse State    : termux_pulse_state.json updated")
    print("=" * 74)

if __name__ == "__main__":
    execute_pulse()
