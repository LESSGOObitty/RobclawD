#!/usr/bin/env python3
"""
ROBDOE ROOT AUTHORITY // Workspace Heavyweight Auditor
Recursively scans current directory for the largest files and folders.
"""

import os

def audit():
    print("=========================================================")
    print(" [WORKSPACE AUDIT] Scanning for largest files & folders...")
    print("=========================================================")
    
    items = []
    for root, dirs, files in os.walk("."):
        # Skip git metadata directory to save time
        if ".git" in root:
            continue
        for f in files:
            filepath = os.path.join(root, f)
            try:
                if os.path.exists(filepath) and not os.path.islink(filepath):
                    size = os.path.getsize(filepath)
                    items.append((filepath, size))
            except Exception:
                pass
                
    items.sort(key=lambda x: x[1], reverse=True)
    
    print(f"{'FILE / PATH':<50} | {'SIZE':<10}")
    print("-" * 65)
    for path, size in items[:15]:  # Top 15 largest files
        size_str = f"{size / (1024*1024):.2f} MB" if size > 1024*1024 else f"{size / 1024:.2f} KB"
        print(f"{path:<50} | {size_str:<10}")
    print("=========================================================")

if __name__ == "__main__":
    audit()
