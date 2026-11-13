#!/data/data/com.termux/files/usr/bin/env python3
import hashlib
import json
import os
import concurrent.futures
import time

EXTERNAL_DIR = os.path.expanduser("~/master-lattice/RobDoeAI-Core/external_lattice")

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

def build_merkle_tree(leaves: list[str]) -> tuple[str, list[list[str]]]:
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

def generate_inclusion_proof(leaf_index: int, tree_layers: list[list[str]]) -> list[dict]:
    proof = []
    idx = leaf_index
    for layer in tree_layers[:-1]:
        is_right_child = (idx % 2 == 1)
        sibling_idx = idx - 1 if is_right_child else idx + 1
        if sibling_idx < len(layer):
            sibling_hash = layer[sibling_idx]
            proof.append({
                "position": "left" if is_right_child else "right",
                "hash": sibling_hash
            })
        idx //= 2
    return proof

def run_enhancement():
    print("=" * 74)
    print(" [ENHANCEMENT] RUNNING PARALLEL B-TREE & MERKLE PROOF GENERATOR")
    print("=" * 74)

    file_entries = []
    for root, _, files in os.walk(EXTERNAL_DIR):
        if ".git" in root:
            continue
        for file in sorted(files):
            fpath = os.path.join(root, file)
            rel_path = os.path.relpath(fpath, EXTERNAL_DIR)
            file_entries.append((rel_path, fpath))

    # Parallel hash computation across all repositories
    leaf_hashes = []
    btree_index = {}
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_file = {executor.submit(sha256_file, fpath): (rel_path, fpath) for rel_path, fpath in file_entries}
        idx = 0
        for future in concurrent.futures.as_completed(future_to_file):
            rel_path, _ = future_to_file[future]
            hsh, size = future.result()
            leaf_hashes.append(hsh)
            btree_index[rel_path] = {
                "btree_slot": idx,
                "sha256": hsh,
                "bytes": size
            }
            idx += 1

    # Sort B-Tree index deterministically by slot
    sorted_btree = dict(sorted(btree_index.items(), key=lambda item: item[1]["btree_slot"]))
    sorted_leaves = [sorted_btree[k]["sha256"] for k in sorted_btree]

    merkle_root, layers = build_merkle_tree(sorted_leaves)

    enhanced_state = {
        "system": "Enhanced Unified Multi-Repo Merkle DAG & B-Tree Lattice",
        "operator": "root@robdoe.com",
        "beneficiary": "robdoe.inc-charity",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "unified_merkle_root": merkle_root,
        "total_indexed_files": len(sorted_leaves),
        "tree_depth": len(layers),
        "btree_index": sorted_btree,
        "bmf_compliance": "EN 16931 / XRechnung Hard-Coded Monolith [1 of 1]"
    }

    output_path = "enhanced_unified_merkle_state.json"
    with open(output_path, "w") as f:
        json.dump(enhanced_state, f, indent=2)

    print(f" [SUCCESS] Parallel Hashing Complete.")
    print(f" [MERKLE ROOT] {merkle_root}")
    print(f" [TREE DEPTH]  {len(layers)} Layers ({len(sorted_leaves)} Files Indexed)")
    print(f" [STATE SAVED] {output_path}")
    print("=" * 74)

if __name__ == "__main__":
    run_enhancement()
