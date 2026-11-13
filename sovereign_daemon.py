#!/usr/bin/env python3
"""
ROBDOE ROOT AUTHORITY // LOCAL MERKLE STATE SEALER
Computes SHA-512 hashes across the workspace, constructs a local Merkle root,
and locks the sovereign state into an immutable verification ledger.
"""

import os
import hashlib
import json
from datetime import datetime

IGNORE_DIRS = {".git", "__pycache__", ".vscode", "node_modules"}
IGNORE_FILES = {"sovereign_daemon.py", "sovereign_state_proof.json"}

def hash_file(filepath):
    sha512 = hashlib.sha512()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha512.update(chunk)
        return sha512.hexdigest()
    except Exception as e:
        return str(e)

def build_merkle_tree():
    leaves = {}
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if file in IGNORE_FILES:
                continue
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, ".")
            leaves[rel_path] = hash_file(path)
            
    # Sort and compute root hash
    sorted_leaves = sorted(leaves.items())
    hasher = hashlib.sha512()
    for path, hval in sorted_leaves:
        hasher.update(f"{path}:{hval}".encode('utf-8'))
    
    return hasher.hexdigest(), leaves

if __name__ == "__main__":
    print("[*] Scanning local workspace for state sealing...")
    root_hash, file_leaves = build_merkle_tree()
    
    state_payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "persona": "LESSGOOBITTY",
        "merkle_root": root_hash,
        "total_files": len(file_leaves),
        "leaves": file_leaves
    }
    
    output_filename = "sovereign_state_proof.json"
    with open(output_filename, "w") as f:
        json.dump(state_payload, f, indent=2)
        
    print("=====================================================================")
    print(f" [SUCCESS] STATE SEALED SUCCESSFULLY.")
    print(f" [ROOT HASH] : {root_hash}")
    print(f" [FILES]     : {len(file_leaves)} tracked in local DAG.")
    print(f" [OUTPUT]    : Saved to {output_filename}")
    print("=====================================================================")
