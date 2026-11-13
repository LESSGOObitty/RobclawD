#!/data/data/com.termux/files/usr/bin/env python3
"""
RobDoeAI-Core // Termux Native Equilibrium Telemetry (Syntax-Safe Patch)
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
"""

import os
import json
import time
import subprocess

def equilibrium_pulse():
    print("=" * 74)
    print(" [TERMUX] VERIFYING ABSOLUTE EQUILIBRIUM & REPOSITORY INTEGRITY")
    print("=" * 74)

    git_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
    commit_hash = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    active_branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()

    dirty_count = len(git_status.splitlines()) if git_status else 0
    tree_msg = "Clean" if dirty_count == 0 else f"{dirty_count} modified files"

    report = {
        "system": "RobDoeAI-Core // Termux Equilibrium",
        "operator": "root@robdoe.com",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "branch": active_branch,
        "head_commit": commit_hash,
        "invariant_anchor": 932808725,
        "dirty_files": dirty_count,
        "status": "ABSOLUTE_EQUILIBRIUM_ACTIVE"
    }

    with open("termux_equilibrium_state.json", "w") as f:
        json.dump(report, f, indent=2)

    print(f" [+] Active Branch  : {active_branch}")
    print(f" [+] HEAD Commit    : {commit_hash}")
    print(f" [+] Invariant Base : {report['invariant_anchor']}")
    print(f" [+] Working Tree   : {tree_msg}")
    print(f" [+] State Saved To : termux_equilibrium_state.json")
    print("=" * 74)

if __name__ == "__main__":
    equilibrium_pulse()
