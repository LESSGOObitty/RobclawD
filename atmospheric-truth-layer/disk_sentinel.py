#!/usr/bin/env python3
"""
ROBDOE ROOT AUTHORITY // Advanced Disk Sentinel & Purge Engine
Scans and reclaims storage across Termux home environment.
"""

import os
import shutil
import subprocess

TARGETS_TO_PURGE = [
    os.path.expanduser("~/.cache"),
    os.path.expanduser("~/.npm"),
    os.path.expanduser("~/.pip"),
    os.path.expanduser("~/.local/share/Trash"),
    os.path.expanduser("$PREFIX/tmp")
]

def get_disk_stats():
    total, used, free = shutil.disk_usage("/")
    pct = (used / total) * 100
    return total, used, free, pct

def scan_heavyweights():
    print("[*] Scanning home directory for space hogs (>10MB)...")
    heavyweights = []
    home = os.path.expanduser("~")
    
    for root, dirs, files in os.walk(home):
        # Skip certain system dirs to avoid permission errors
        if ".termux" in root or "usr" in root:
            continue
        for d in dirs:
            dir_path = os.path.join(root, d)
            try:
                if os.path.islink(dir_path):
                    continue
                size = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, filenames in os.walk(dir_path) for f in filenames if os.path.exists(os.path.join(dp, f)))
                if size > 10 * 1024 * 1024: # > 10MB
                    heavyweights.append((dir_path, size))
            except Exception:
                pass
        break # Top level scan only for speed
        
    heavyweights.sort(key=lambda x: x[1], reverse=True)
    return heavyweights

def execute_purge():
    total_before, used_before, free_before, pct_before = get_disk_stats()
    print(f"[*] Initial Storage State : {free_before // (2**20)} MB free ({pct_before:.1f}% used)")
    
    freed_bytes = 0
    for target in TARGETS_TO_PURGE:
        expanded = os.path.expandvars(target)
        if os.path.exists(expanded):
            try:
                size = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, filenames in os.walk(expanded) for f in filenames if os.path.exists(os.path.join(dp, f)))
                shutil.rmtree(expanded, ignore_errors=True)
                os.makedirs(expanded, exist_ok=True)
                freed_bytes += size
                print(f" [+] Purged: {expanded} (~{size // (2**20)} MB reclaimed)")
            except Exception as e:
                print(f" [!] Could not purge {expanded}: {e}")

    # Git garbage collection
    if os.path.exists(".git"):
        try:
            subprocess.run(["git", "gc", "--prune=now", "--aggressive"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(" [+] Optimized local Git object database.")
        except Exception:
            pass

    total_after, used_after, free_after, pct_after = get_disk_stats()
    print("=========================================================")
    print(f" [RECLAMATION COMPLETE]")
    print(f" Free Storage Before : {free_before // (2**20)} MB")
    print(f" Free Storage After  : {free_after // (2**20)} MB")
    print(f" Net Space Reclaimed : ~{freed_bytes // (2**20)} MB")
    print(f" Current Usage       : {pct_after:.1f}%")
    print("=========================================================")

if __name__ == "__main__":
    execute_purge()
