#!/data/data/com.termux/files/usr/bin/env python3
"""
Sovereign Merkle DAG Compiler & State Freezer
Operator: root@robdoenet (Permanent Anchor: 34.68.218.70 | robdoe.com)
Function: Walks the local repository, computes cryptographic content-addressable 
          Merkle DAG nodes for all tracked files, and seals the root hash.
"""
import os
import hashlib
import json
import datetime

EXCLUDES = {".git", "__pycache__", ".robdoenet_daemon.log"}

def hash_file(filepath):
    hasher = hashlib.sha3_256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def build_merkle_dag():
    print("\n" + "="*72)
    print(" \x1b[1;35m[BUILDING SOVEREIGN MERKLE DAG LATTICE]\x1b[0m")
    print("="*72 + "\n")

    dag_nodes = {}
    root_hasher = hashlib.sha3_256()

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDES]
        for file in files:
            if file.startswith(".robdoenet_daemon"):
                continue
            rel_path = os.path.relpath(os.path.join(root, file), ".")
            if any(exc in rel_path for exc in EXCLUDES):
                continue
            
            try:
                f_hash = hash_file(rel_path)
                dag_nodes[rel_path] = f_hash
                root_hasher.update(f"{rel_path}:{f_hash}".encode("utf-8"))
                print(f" \033[1;36m[DAG NODE]:\x1b[0m {rel_path:<45} -> \033[1;32m{f_hash[:16]}...\x1b[0m")
            except Exception as e:
                pass

    merkle_root = root_hasher.hexdigest()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+11:00"

    dag_manifest = {
        "operator": "root@robdoenet",
        "domain": "robdoe.com",
        "timestamp": timestamp,
        "merkle_root": merkle_root,
        "nodes": dag_nodes
    }

    manifest_path = ".robdoenet_merkle_dag_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(dag_manifest, f, indent=2)

    print("\n" + "="*72)
    print(f" \x1b[1;32m[+] MERKLE ROOT HASH LOCKED:\x1b[0m {merkle_root}")
    print(f" \x1b[1;36m[+] Manifest sealed at:\x1b[0m {manifest_path}")
    print("="*72 + "\n")

if __name__ == "__main__":
    build_merkle_dag()
