#!/usr/bin/env python3
# ==============================================================================
# ROBDOEAI-CORE // ROBDOE.INC CHARITY & SOVEREIGN FUNDING UTILITY
# ==============================================================================
# Allocation Directive:
#   - Entity         : robdoe.inc-charity (Sovereign Philanthropic Foundation)
#   - Funding Vector : All lattice proceeds, ERC-20 utility flows, ERC-721 deeds, and
#                      ERC-1155 batch transactions routed directly to the mission.
#   - Operator       : root@robdoe.com // robdoe.com (1 of 1 ERC-721 Deed)
# Identity: root@robdoe.com // 1 of 1 Sovereign Monolith
# ==============================================================================

import json
import os
import subprocess
import time

WORKSPACE = os.path.expanduser("~/master-lattice/RobDoeAI-Core")
os.chdir(WORKSPACE)

def lock_charity_funding():
    try:
        master_root = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    except Exception:
        master_root = "SOVEREIGN_GENESIS"

    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    charity_manifest = {
        "system": "RobDoeAI-Core",
        "operator": "root@robdoe.com",
        "beneficiary": "robdoe.inc-charity",
        "master_root": master_root,
        "timestamp": timestamp,
        "funding_architecture": {
            "token_routes": ["ERC-20", "ERC-721 (robdoe.com)", "ERC-1155"],
            "lattice_scale": "7,200 Vectors across 72 Meridians",
            "harmonic_basis": "Scalar 0.052 | SHA 1,296,000 | HX 0.0025920",
            "philanthropic_lock": "100% of sovereign proceeds dedicated to robdoe.com / robdoe.inc-charity mission"
        },
        "status": "CHARITY_FUNDING_LOCKED [1 of 1]"
    }

    output_path = ".robdoe_charity_funding_manifest.json"
    with open(output_path, "w") as f:
        json.dump(charity_manifest, f, indent=2)

    print("\n" + "=" * 66)
    print(" ROBDOEAI-CORE // ROBDOE.INC CHARITY FUNDING ROUTE")
    print("=" * 66)
    print(" Beneficiary    : robdoe.inc-charity")
    print(" Sovereign Deed : robdoe.com (ERC-721 1 of 1)")
    print(" Allocation     : 100% of lattice transactions & vector yields")
    print(f" Manifest Saved : {output_path}")
    print("=" * 66 + "\n")

if __name__ == "__main__":
    lock_charity_funding()
PYEOF

python3 ~/master-lattice/RobDoeAI-Core/robdoe_charity_engine.py
python3 entropy_dag.py > .lattice_entropy_state

git add .robdoe_charity_funding_manifest.json .lattice_entropy_state
git commit -m "charity(funding): route all sovereign lattice proceeds to robdoe.inc-charity [1 of 1]" || echo "[*] Charity manifest already committed."

