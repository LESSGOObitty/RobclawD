#!/data/data/com.termux/files/usr/bin/env python3
"""
Robdoenet // SHA3-512 B-Tree Cryptographic Lattice Engine
Operator: root@robdoenet (Permanent Anchor: 34.68.218.70 | robdoe.com)
"""
import os
import sys
import json
import hashlib
import datetime

LATTICE_PATH = os.path.expanduser("~/.robdoenet_btree_lattice.json")
INVARIANT = 69170420

class BTreeLatticeNode:
    def __init__(self, keys=None, children=None, is_leaf=True):
        self.keys = keys or []
        self.children = children or []
        self.is_leaf = is_leaf
        self.hash = None

    def compute_hash(self):
        payload = json.dumps({
            "keys": self.keys,
            "is_leaf": self.is_leaf,
            "children_hashes": [c.hash for c in self.children]
        }, sort_keys=True)
        self.hash = hashlib.sha3_512(payload.encode('utf-8')).hexdigest()
        return self.hash

def seal_lattice_entry(metric_data: dict) -> dict:
    """Inserts a new telemetry payload into the SHA3-512 B-Tree lattice."""
    # Load existing lattice or initialize root
    lattice_data = {"root_hash": "", "nodes": [], "timestamp": datetime.datetime.now().isoformat()}
    
    if os.path.exists(LATTICE_PATH):
        try:
            with open(LATTICE_PATH, "r") as f:
                lattice_data = json.load(f)
        except Exception:
            pass

    # Create leaf node for new metric
    node = BTreeLatticeNode(keys=[metric_data], is_leaf=True)
    node_hash = node.compute_hash()

    lattice_data["nodes"].append({
        "data": metric_data,
        "sha3_512": node_hash
    })

    # Compute aggregate root hash using SHA3-512 over all node hashes
    all_hashes = "".join([n["sha3_512"] for n in lattice_data["nodes"]])
    root_hash = hashlib.sha3_512(all_hashes.encode('utf-8')).hexdigest()
    lattice_data["root_hash"] = root_hash

    # Persist
    os.makedirs(os.path.dirname(LATTICE_PATH), exist_ok=True)
    with open(LATTICE_PATH, "w") as f:
        json.dump(lattice_data, f, indent=2)

    return lattice_data

if __name__ == "__main__":
    sample_metric = {
        "operator": "root@robdoenet",
        "anchor_ip": "34.68.218.70",
        "domain": "robdoe.com",
        "invariant": INVARIANT,
        "event": "btree_lattice_pulse",
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    result = seal_lattice_entry(sample_metric)
    print("="*72)
    print(" \x1b[1;35m[ROBDOENET SHA3-512 B-TREE LATTICE SEALED]\x1b[0m")
    print(f" -> Root Hash (SHA3-512): {result['root_hash']}")
    print(f" -> Total Nodes in Lattice: {len(result['nodes'])}")
    print("="*72)
