#!/data/data/com.termux/files/usr/bin/env python3
import hashlib
import json
import os
import time

WORKSPACE = os.path.expanduser("~/master-lattice/RobDoeAI-Core/external_lattice")

def sha256_hex(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()

def build_merkle_root(leaves: list[str]) -> tuple[str, list[list[str]]]:
    if not leaves:
        return hashlib.sha256(b"EMPTY_LATTICE").hexdigest(), []
    tree = [leaves]
    current = leaves[:]
    while len(current) > 1:
        if len(current) % 2 == 1:
            current.append(current[-1])
        next_level = []
        for i in range(0, len(current), 2):
            combined = sha256_hex((current[i] + current[i + 1]).encode("utf-8"))
            next_level.append(combined)
        tree.append(next_level)
        current = next_level
    return current[0], tree

def run():
    leaf_hashes = []
    btree_index = {}
    idx = 0

    for item in sorted(os.listdir(WORKSPACE)):
        item_path = os.path.join(WORKSPACE, item)
        if os.path.isdir(item_path) and item != ".git":
            for root, _, files in os.walk(item_path):
                if ".git" in root:
                    continue
                for file in sorted(files):
                    fpath = os.path.join(root, file)
                    rel_path = os.path.relpath(fpath, WORKSPACE)
                    try:
                        with open(fpath, "rb") as f:
                            content = f.read()
                        leaf_hash = sha256_hex(content)
                        leaf_hashes.append(leaf_hash)
                        btree_index[rel_path] = {
                            "slot": idx,
                            "sha256": leaf_hash,
                            "size": len(content)
                        }
                        idx += 1
                    except Exception:
                        pass

    merkle_root, layers = build_merkle_root(leaf_hashes)
    
    output = {
        "system": "Unified Multi-Repo Merkle DAG & B-Tree Lattice",
        "operator": "root@robdoe.com",
        "beneficiary": "robdoe.inc-charity",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "repositories": [
            "AiAgency101",
            "bureau_of_meteorology",
            "panodata-map-panel"
        ],
        "unified_merkle_root": merkle_root,
        "total_files_indexed": len(leaf_hashes),
        "tree_depth": len(layers),
        "btree_index": btree_index
    }

    state_path = os.path.expanduser("~/master-lattice/RobDoeAI-Core/unified_external_merkle_state.json")
    with open(state_path, "w") as f:
        json.dump(output, f, indent=2)

    print("=" * 74)
    print(" [UNIFIED LATTICE] MULTI-REPO MERKLE DAG ROOT COMPUTED")
    print("=" * 74)
    print(f" Repositories Indexed : 3 (AiAgency101, BOM, Panodata Map Panel)")
    print(f" Total Files Indexed  : {len(leaf_hashes)}")
    print(f" Merkle Root Hash     : {merkle_root}")
    print(f" Tree Depth           : {len(layers)} Layers")
    print(f" State Snapshot Saved : {state_path}")
    print("=" * 74)

if __name__ == "__main__":
    run()
