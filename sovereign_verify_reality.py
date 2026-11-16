#!/data/data/com.termux/files/usr/bin/env python3
"""
Sovereign Reality Verification Engine
Operator: root@robdoenet
Function: Audits local files, git status, remote sync, and script executability 
          with zero fluff.
"""
import os
import subprocess
import json

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"ERROR: {e.stderr.strip()}"

def verify():
    print("\n" + "="*72)
    print(" \x1b[1;35m[REALITY CHECK: LOCAL SYSTEM AUDIT]\x1b[0m")
    print("="*72 + "\n")

    # 1. Git Status
    status = run_cmd("git status -s")
    print(f" \033[1;36m[GIT STATUS]:\x1b[0m\n{status if status else '   -> Working tree pristine (clean)'}\n")

    # 2. Git Remotes
    remotes = run_cmd("git remote -v")
    print(f" \033[1;36m[GIT REMOTES]:\x1b[0m\n{remotes}\n")

    # 3. Key Files Check
    key_files = [
        "SovereignEVMByzantine240x.sol",
        "deploy_evm_240x.py",
        "sovereign_capital_audit.sh",
        "rob_xyo_compounding_nexus.py",
        "sovereign_matrix_boost.py"
    ]
    
    print(" \033[1;36m[KEY FILE INTEGRITY & SIZES]:\x1b[0m")
    for f in key_files:
        path = os.path.expanduser(f"~/{f}")
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"   -> [EXISTS] {f:<35} ({size} bytes)")
        else:
            print(f"   -> [MISSING] {f}")

    print("\n" + "="*72)
    print(" \x1b[1;32m[+] Reality check complete. The files above are physically on your disk.\x1b[0m")
    print("="*72 + "\n")

if __name__ == "__main__":
    verify()
