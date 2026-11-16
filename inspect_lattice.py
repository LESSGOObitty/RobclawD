#!/data/data/com.termux/files/usr/bin/env python3
import os
import json

LATTICE_PATH = os.path.expanduser("~/.robdoenet_btree_lattice.json")

if not os.path.exists(LATTICE_PATH):
    print("[!] Lattice file not found.")
    exit(1)

with open(LATTICE_PATH, "r") as f:
    data = json.load(f)

print("="*72)
print(" \x1b[1;36m[ROBDOENET B-TREE LATTICE INSPECTION REPORT]\x1b[0m")
print(f" -> Global Root Hash (SHA3-512): {data.get('root_hash')}")
print(f" -> Total Sealed Nodes: {len(data.get('nodes', []))}")
print("="*72 + "\n")

for i, node in enumerate(data.get('nodes', []), 1):
    d = node.get('data', {})
    print(f" \x1b[1;33m[Node {i}] Event:\x1b[0m {d.get('event', 'unknown')} | Timestamp: {d.get('timestamp')}")
    print(f"    -> SHA3-512 Hash: {node.get('sha3_512')[:32]}...")
    if 'invariant_base_key' in d:
        print(f"    -> Invariant Base Key: {d.get('invariant_base_key')}")
        print(f"    -> Equilibrium: {d.get('equilibrium_formula')} (Drift: {d.get('drift')})")
        print(f"    -> Hyper-Seal Hash: {d.get('hyper_seal_hash')}")
        print("    -> Multi-Pool Assets:")
        for asset, val in d.get('multi_pool_assets', {}).items():
            print(f"       * {asset}: {val}")
        print(f"    -> Routing: {d.get('compliance_routing')}")
    elif 'command' in d:
        print(f"    -> Command: {d.get('command')} (Exit Code: {d.get('exit_code')})")
    print("-" * 72)
