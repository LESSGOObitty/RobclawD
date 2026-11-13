#!/data/data/com.termux/files/usr/bin/env python3
import os
import json
import time
import hashlib

def consolidate_clones():
    print("=" * 74)
    print(" [ALIGNMENT] CONSOLIDATING ALL CLONED VECTORS TO MASTER LATTICE ROOT")
    print("=" * 74)

    # Gather all generated state files across previous enhancement phases
    state_files = [
        "bounty_defense_state.json",
        "stillness_in_motion_state.json",
        "velocity_state.json",
        "hyper_enhanced_state.json",
        "recursive_enhanced_state.json",
        "omni_enhanced_state.json",
        "facelift_state.json",
        "mega_rejuvenated_state.json",
        "surgeon_precision_state.json",
        "marathon_endurance_state.json",
        "temporal_math_state.json",
        "work_equivalence_state.json",
        "sync_lock_state.json",
        "head_advance_state.json"
    ]

    consolidated_dag = []
    hasher = hashlib.sha256()

    for sf in state_files:
        if os.path.exists(sf):
            with open(sf, "r") as f:
                data = json.load(f)
                consolidated_dag.append(data)
                hasher.update(json.dumps(data, sort_keys=True).encode("utf-8"))

    root_merkle_hash = hasher.hexdigest()

    master_alignment = {
        "system": "RobDoeAI-Core // Master Lattice Alignment & Consolidation",
        "operator": "root@robdoe.com",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "aligned_clones_count": len(consolidated_dag),
        "unified_master_root_hash": root_merkle_hash,
        "status": "FULLY_ALIGNED_AND_ROOTED"
    }

    output_path = "master_aligned_root.json"
    with open(output_path, "w") as f:
        json.dump(master_alignment, f, indent=2)

    print(f" [+] Consolidated States : {len(consolidated_dag)} vectors aligned.")
    print(f" [+] Unified Master Root : {root_merkle_hash}")
    print(f" [+] State Exported To   : {output_path}")
    print("=" * 74)

if __name__ == "__main__":
    consolidate_clones()
