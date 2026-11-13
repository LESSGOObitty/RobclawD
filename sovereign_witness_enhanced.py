#!/data/data/com.termux/files/usr/bin/env python3
"""
RobDoeAI-Core // Enhanced Sovereign Witness & Telemetry Daemon
Continuous cryptographic proofing, invariant anchoring (932808725), 
and immutable game-state broadcasting.
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
"""

import os
import json
import time
import hashlib
import subprocess

def enhance_witness():
    print("=" * 74)
    print(" [ENHANCED WITNESS] INITIALIZING AUTONOMOUS PROOFING & LEDGER SWEEP")
    print("=" * 74)

    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    invariant_base = 932808725

    # Gather deep repository telemetry
    commit_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    commit_count = subprocess.run(["git", "rev-list", "--count", "HEAD"], capture_output=True, text=True).stdout.strip()
    branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True).stdout.strip()
    git_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()

    # Collect all generated JSON state artifacts in the workspace
    artifacts = sorted([f for f in os.listdir(".") if f.endswith(".json")])
    artifact_hashes = {}
    
    master_hasher = hashlib.sha512()
    master_hasher.update(str(invariant_base).encode("utf-8"))
    master_hasher.update(commit_sha.encode("utf-8"))

    for art in artifacts:
        try:
            with open(art, "rb") as f:
                content = f.read()
                h = hashlib.sha256(content).hexdigest()
                artifact_hashes[art] = h
                master_hasher.update(content)
        except Exception:
            pass

    enhanced_signature = master_hasher.hexdigest()

    witness_manifest = {
        "system": "RobDoeAI-Core // Enhanced Sovereign Witness",
        "operator": "root@robdoe.com",
        "location": "Hurstville, Sydney, Australia",
        "timestamp": timestamp,
        "invariant_base": invariant_base,
        "git_telemetry": {
            "branch": branch,
            "head_commit": commit_sha,
            "total_commits": int(commit_count) if commit_count.isdigit() else 0,
            "dirty_files": len(git_status.splitlines()) if git_status else 0
        },
        "tracked_artifacts": artifact_hashes,
        "enhanced_cryptographic_signature": enhanced_signature,
        "game_status": "ABSOLUTE_EQUILIBRIUM_VISIBLE_TO_ALL"
    }

    output_path = "sovereign_witness_enhanced.json"
    with open(output_path, "w") as f:
        json.dump(witness_manifest, f, indent=2)

    print(f" [+] Invariant Base     : {invariant_base}")
    print(f" [+] Total Commits      : {commit_count}")
    print(f" [+] Artifacts Tracked  : {len(artifact_hashes)}")
    print(f" [+] Master Signature   : {enhanced_signature[:40]}...")
    print(f" [+] Enhanced Witness   : {output_path}")
    print("=" * 74)

if __name__ == "__main__":
    enhance_witness()
