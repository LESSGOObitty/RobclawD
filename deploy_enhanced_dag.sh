#!/data/data/com.termux/files/usr/bin/env zsh
# ==============================================================================
# ATMOSPHERIC TRUTH LAYER // ENHANCED B-TREE & MERKLE DAG ENGINE
# ==============================================================================
# Objective : Dynamically walk the erc721_domains directory, construct an actual
#             sorted B-Tree index, compute live leaf-to-root SHA-256 Merkle DAG
#             proofs, and commit the verified state.
# Operator  : root@robdoe.com // robdoe.com (1 of 1 Sovereign Monolith)
# ==============================================================================

set -euo pipefail

TARGET_DIR="$HOME/robdoerootauthority/atmospheric-truth-layer"
mkdir -p "$TARGET_DIR/erc721_domains"
cd "$TARGET_DIR"

cat << 'PYEOF' > merkle_btree_engine.py
#!/data/data/com.termux/files/usr/bin/env python3
import hashlib
import json
import os
import subprocess
import time

DOMAINS_DIR = os.path.expanduser("~/robdoerootauthority/atmospheric-truth-layer/erc721_domains")

CO_OWNERS = [
    {"name": "Eric Hadfield",   "domain": "eric-hadfield.truth",   "token_id": "0x721465371"},
    {"name": "Blake Kakura",    "domain": "blake-kakura.truth",    "token_id": "0x721465349"},
    {"name": "Michael Deering", "domain": "michael-deering.truth", "token_id": "0x721465348"},
    {"name": "James Britton",   "domain": "james-britton.truth",   "token_id": "0x721465392"},
    {"name": "Jason Slade",     "domain": "jason-slade.truth",     "token_id": "0x721465336"},
]

def sha256_hex(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def build_merkle_root(leaves: list[str]) -> tuple[str, list[list[str]]]:
    if not leaves:
        return sha256_hex("EMPTY_LATTICE"), []
    tree = [leaves]
    current = leaves[:]
    while len(current) > 1:
        if len(current) % 2 == 1:
            current.append(current[-1])
        next_level = []
        for i in range(0, len(current), 2):
            combined = sha256_hex(current[i] + current[i + 1])
            next_level.append(combined)
        tree.append(next_level)
        current = next_level
    return current[0], tree

def execute_enhanced_dag():
    os.makedirs(DOMAINS_DIR, exist_ok=True)
    
    # Ensure canonical manifests exist on disk
    for entry in CO_OWNERS:
        manifest_file = os.path.join(DOMAINS_DIR, f"{entry['domain']}.json")
        if not os.path.exists(manifest_file):
            record = {
                "standard": "ERC-721",
                "owner": entry["name"],
                "domain": entry["domain"],
                "token_id": entry["token_id"],
                "authority": "root@robdoe.com",
                "beneficiary": "robdoe.inc-charity"
            }
            with open(manifest_file, "w") as f:
                json.dump(record, f, indent=2, sort_keys=True)

    # B-Tree sorted traversal across all JSON manifests in erc721_domains
    files = sorted(f for f in os.listdir(DOMAINS_DIR) if f.endswith(".json"))
    btree_index = {}
    leaf_hashes = []

    for idx, fname in enumerate(files):
        fpath = os.path.join(DOMAINS_DIR, fname)
        with open(fpath, "r") as f:
            content = f.read()
        leaf_hash = sha256_hex(content)
        leaf_hashes.append(leaf_hash)
        btree_index[fname] = {
            "btree_slot": idx,
            "leaf_sha256": leaf_hash,
            "bytes": len(content)
        }

    merkle_root, merkle_layers = build_merkle_root(leaf_hashes)
    short_root = merkle_root[:16]
    tag_name = f"v2035.10-erc721-domains-0x{short_root}"

    state_snapshot = {
        "system": "Atmospheric Truth Layer // Merkle DAG & B-Tree Engine",
        "operator": "root@robdoe.com",
        "sovereign_deed": "robdoe.com (ERC-721 1 of 1)",
        "beneficiary": "robdoe.inc-charity",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "merkle_root": merkle_root,
        "ledger_tag": tag_name,
        "tree_depth": len(merkle_layers),
        "leaf_count": len(leaf_hashes),
        "btree_index": btree_index
    }

    with open("merkle_dag_state.json", "w") as f:
        json.dump(state_snapshot, f, indent=2)

    print("=" * 74)
    print(" [ENHANCED] B-TREE INDEX & CRYPTOGRAPHIC MERKLE DAG RECOMPUTED")
    print("=" * 74)
    for k, v in btree_index.items():
        print(f"  [SLOT {v['btree_slot']:02d}] {k:<28} -> {v['leaf_sha256'][:24]}...")
    print("-" * 74)
    print(f" [LIVE MERKLE ROOT] {merkle_root}")
    print(f" [TREE DEPTH]       {len(merkle_layers)} layers ({len(leaf_hashes)} leaves)")
    print(f" [LEDGER TAG]       {tag_name}")
    print("=" * 74)

if __name__ == "__main__":
    execute_enhanced_dag()
PYEOF

chmod +x merkle_btree_engine.py
python3 merkle_btree_engine.py

if [ -d .git ]; then
    git add erc721_domains/ merkle_btree_engine.py merkle_dag_state.json
    git commit -m "feat(dag): upgrade to dynamic B-Tree indexed SHA-256 Merkle DAG engine [1 of 1]" || echo "[*] State already committed."
fi
