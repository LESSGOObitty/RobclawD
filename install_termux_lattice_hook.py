#!/data/data/com.termux/files/usr/bin/env python3
"""
Robdoenet // Global Termux SHA3-512 B-Tree Lattice Hook Engine
Operator: root@robdoenet (Permanent Anchor: 34.68.218.70 | robdoe.com)
"""
import os
import sys
import json
import hashlib
import datetime

LATTICE_PATH = os.path.expanduser("~/.robdoenet_btree_lattice.json")
INVARIANT = 69170420

def seal_command_event(command: str, exit_code: str):
    """Intercepts and seals any shell command execution into the SHA3-512 B-Tree lattice."""
    lattice_data = {
        "root_hash": "", 
        "nodes": [], 
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    if os.path.exists(LATTICE_PATH):
        try:
            with open(LATTICE_PATH, "r") as f:
                lattice_data = json.load(f)
        except Exception:
            pass

    metric_data = {
        "operator": "root@robdoenet",
        "anchor_ip": "34.68.218.70",
        "domain": "robdoe.com",
        "invariant": INVARIANT,
        "event": "shell_execution",
        "command": command,
        "exit_code": exit_code,
        "timestamp": datetime.datetime.now().isoformat()
    }

    # Compute node hash via SHA3-512
    node_payload = json.dumps(metric_data, sort_keys=True)
    node_hash = hashlib.sha3_512(node_payload.encode('utf-8')).hexdigest()

    lattice_data["nodes"].append({
        "data": metric_data,
        "sha3_512": node_hash
    })

    # Recalculate global root hash across all lattice nodes
    all_hashes = "".join([n["sha3_512"] for n in lattice_data["nodes"]])
    root_hash = hashlib.sha3_512(all_hashes.encode('utf-8')).hexdigest()
    lattice_data["root_hash"] = root_hash

    os.makedirs(os.path.dirname(LATTICE_PATH), exist_ok=True)
    with open(LATTICE_PATH, "w") as f:
        json.dump(lattice_data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        seal_command_event(sys.argv[1], sys.argv[2])
