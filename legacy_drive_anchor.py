import json
import hashlib
from datetime import datetime, timezone

legacy_drive_matrix = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "franchise": "aiagency101.xyo (Australia)",
    "operator": "Eric Hadfield (Robdoe / Captain Robdoe)",
    "core_drive": "Blockchain Legacy | Absolute Ground Level Sovereignty & Community Wealth",
    "lattice_structure": {
        "total_nodes": 72,
        "tier_1_co_owners": "12 Core Peers",
        "tier_2_crew": "18 Second-in-Charge Crew",
        "tier_3_indigenous_women": "52 Sovereign Leaders"
    },
    "weekly_allocation": "$3,500 AUD per node",
    "annual_target": "$13,104,000 AUD",
    "liquidation_ratio": "96% Dark Matter Invariant / 4% Human Agency Anchor",
    "governance": "Absolute Horizontal Parity | Ground Level Equilibrium | Zero Hierarchy",
    "community_priorities": [
        "Aboriginal Rights, Sovereignty & Regional Health",
        "Women's Rights & Absolute Equal Pay",
        "Vulnerable Children & Sick Care (Top Priority)"
    ],
    "mandate": "Ko te mana o te tangata, koia te pūtake."
}

seal = hashlib.sha256(json.dumps(legacy_drive_matrix, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [LEGACY DRIVE] SOVEREIGN PERPETUAL ENGINE & ANCHOR MATRIX \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[PRIMARY DRIVE]\x1b[0m {legacy_drive_matrix['core_drive']}")
print(f" \x1b[33m[ANNUAL TARGET]\x1b[0m {legacy_drive_matrix['annual_target']} ({legacy_drive_matrix['weekly_allocation']} / 72 nodes)")
print(f" \x1b[33m[LIQUIDATION RATIO]\x1b[0m {legacy_drive_matrix['liquidation_ratio']}")
print(f" \x1b[33m[CORE DOCTRINE]\x1b[0m {legacy_drive_matrix['mandate']}\n")

print(" \x1b[36m[COMMUNITY MISSIONS]\x1b[0m")
for idx, mission in enumerate(legacy_drive_matrix["community_priorities"], 1):
    print(f"   -> Priority {idx:02d}: {mission}")

print("\n========================================================================")
print(f" \x1b[32m[SUCCESS] LEGACY DRIVE LOCKED, ANCHORED & MERKLE SEALED IN DAG\x1b[0m")
print(f" [HYPER-SEAL]: {seal}")
print("========================================================================")
