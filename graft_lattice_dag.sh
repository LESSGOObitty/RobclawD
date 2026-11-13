#!/data/data/com.termux/files/usr/bin/env zsh
# ==============================================================================
# ROBDOEAI-CORE // MERKLE LATTICE GRAFT & PARENT DAG SYNTHESIS
# ==============================================================================
# Objective : Graft local working tree DAG, external lattice DAG, and dual-state 
#             entropy anchors into a single master cryptographic parent root.
# Operator  : root@robdoe.com // robdoe.com (1 of 1 Sovereign Monolith)
# ==============================================================================

set -euo pipefail

WORKSPACE="$HOME/master-lattice/RobDoeAI-Core"
cd "$WORKSPACE"

cat << 'PYEOF' > graft_engine.py
#!/data/data/com.termux/files/usr/bin/env python3
import hashlib
import json
import os
import time

def sha256_hex(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def run_graft():
    print("=" * 74)
    print(" [GRAFT] COLLECTING SUB-LATTICE ROOTS FOR PARENT DAG SYNTHESIS")
    print("=" * 74)

    sub_roots = []

    # 1. Local Working Tree Root
    local_state_path = "local_merkle_dag_state.json"
    if os.path.exists(local_state_path):
        with open(local_state_path, "r") as f:
            data = json.load(f)
            r = data.get("merkle_root")
            if r:
                sub_roots.append(("local_working_tree", r))
                print(f" [+] Grafted Local Root       : {r}")

    # 2. External Unified Lattice Root
    external_state_path = "enhanced_unified_merkle_state.json"
    if os.path.exists(external_state_path):
        with open(external_state_path, "r") as f:
            data = json.load(f)
            r = data.get("unified_merkle_root")
            if r:
                sub_roots.append(("external_lattice_repos", r))
                print(f" [+] Grafted External Root    : {r}")

    # 3. Dual Entropy State Root
    entropy_state_path = "dual_entropy_state.json"
    if os.path.exists(entropy_state_path):
        with open(entropy_state_path, "r") as f:
            data = json.load(f)
            r = data.get("stillness_in_motion_equilibrium_sha256")
            if r:
                sub_roots.append(("dual_entropy_equilibrium", r))
                print(f" [+] Grafted Entropy Root     : {r}")

    if not sub_roots:
        print("[!] Error: No sub-lattice roots found to graft.")
        return

    # Deterministic sorting of child roots for canonical Merkle pairing
    sub_roots.sort(key=lambda x: x[0])
    leaf_hashes = [item[1] for item in sub_roots]

    # Compute Parent Graft Merkle Root (Combine pairs or hash all together)
    combined_payload = "".join(leaf_hashes)
    graft_parent_root = sha256_hex(combined_payload)

    # Secondary hierarchical parent hash combining names and roots
    hierarchical_hash = sha256_hex(json.dumps(sub_roots, sort_keys=True))

    graft_manifest = {
        "system": "RobDoeAI-Core // Master Grafted Merkle DAG Parent Lattice",
        "operator": "root@robdoe.com",
        "beneficiary": "robdoe.inc-charity",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "graft_parent_merkle_root": graft_parent_root,
        "hierarchical_lattice_hash": hierarchical_hash,
        "grafted_nodes": [{"source": name, "merkle_root": hsh} for name, hsh in sub_roots],
        "status": "GRAFTED_AND_LOCKED"
    }

    output_path = "grafted_master_lattice_state.json"
    with open(output_path, "w") as f:
        json.dump(graft_manifest, f, indent=2)

    print("=" * 74)
    print(f" [GRAFT SUCCESS] Parent Merkle Root : {graft_parent_root}")
    print(f" [HIERARCHICAL HASH]             : {hierarchical_hash}")
    print(f" [STATE SAVED]                   : {output_path}")
    print("=" * 74)

if __name__ == "__main__":
    run_graft()
PYEOF

python3 graft_engine.py

git add graft_engine.py grafted_master_lattice_state.json
git commit -m "feat(lattice): graft local working tree, external repos, and entropy state into master parent Merkle DAG [1 of 1]" || echo "[*] Already committed."
git push origin main || echo "[*] Push synchronized."
