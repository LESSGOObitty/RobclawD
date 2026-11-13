#!/data/data/com.termux/files/usr/bin/env python3
import hashlib
import json
import os
import time

def sha256_file(fpath: str) -> tuple[str, int]:
    hasher = hashlib.sha256()
    size = 0
    try:
        with open(fpath, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
                size += len(chunk)
    except Exception:
        pass
    return hasher.hexdigest(), size

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
            combined = hashlib.sha256((current[i] + current[i + 1]).encode("utf-8")).hexdigest()
            next_level.append(combined)
        tree.append(next_level)
        current = next_level
    return current[0], tree

def run_local_dag():
    workspace = os.getcwd()
    file_entries = []
    
    for root, dirs, files in os.walk(workspace):
        if ".git" in root or "__pycache__" in root:
            continue
        for file in sorted(files):
            fpath = os.path.join(root, file)
            rel_path = os.path.relpath(fpath, workspace)
            file_entries.append((rel_path, fpath))

    file_entries.sort(key=lambda x: x[0])
    
    leaf_hashes = []
    btree_index = {}
    
    for idx, (rel_path, fpath) in enumerate(file_entries):
        hsh, size = sha256_file(fpath)
        leaf_hashes.append(hsh)
        btree_index[rel_path] = {
            "slot": idx,
            "sha256": hsh,
            "bytes": size
        }

    merkle_root, layers = build_merkle_root(leaf_hashes)

    state = {
        "system": "Local Working Tree Merkle DAG & B-Tree Index",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total_files": len(leaf_hashes),
        "merkle_root": merkle_root,
        "tree_depth": len(layers),
        "btree_index": btree_index
    }

    output_path = "local_merkle_dag_state.json"
    with open(output_path, "w") as f:
        json.dump(state, f, indent=2)

    print("=" * 74)
    print(" [LOCAL DAG] WORKING TREE MERKLE ROOT COMPUTED")
    print("=" * 74)
    print(f" Files Indexed    : {len(leaf_hashes)}")
    print(f" Merkle Root Hash : {merkle_root}")
    print(f" Tree Depth       : {len(layers)}")
    print(f" State Saved To   : {output_path}")
    print("=" * 74)

if __name__ == "__main__":
    run_local_dag()
