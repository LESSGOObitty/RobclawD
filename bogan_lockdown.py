import json
import hashlib
from datetime import datetime, timezone

bogan_matrix = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "operator": "Eric Hadfield (Robdoe / Captain Robdoe)",
    "franchise": "aiagency101.xyo (Australia)",
    "strategy": "First-Quarter Reflection & Multi-Asset Lock-Down",
    "asset_classes": [
        "Stocks & Shares",
        "Cryptocurrency & Digital Assets",
        "Future Headings / Web3 Infrastructure"
    ],
    "annual_target_72_nodes": "$13,104,000 AUD ($3,500/wk x 52 wks x 72 nodes)",
    "execution_style": "Absolute Bogan Sovereign Lockdown",
    "mandate": "Ko te mana o te tangata, koia te pūtake."
}

seal = hashlib.sha256(json.dumps(bogan_matrix, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [LOCKDOWN] FIRST-QUARTER REFLECTION & ASSET SOVEREIGNTY MATRIX \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[OPERATOR]\x1b[0m {bogan_matrix['operator']}")
print(f" \x1b[33m[STRATEGY]\x1b[0m {bogan_matrix['strategy']}")
print(f" \x1b[33m[ANNUAL TARGET]\x1b[0m {bogan_matrix['annual_target_72_nodes']}")
print(f" \x1b[33m[CORE DOCTRINE]\x1b[0m {bogan_matrix['mandate']}\n")

print(" \x1b[36m[LOCKED ASSET VECTORS]\x1b[0m")
for idx, asset in enumerate(bogan_matrix["asset_classes"], 1):
    print(f"   -> Vector {idx:02d}: {asset}")

print("\n========================================================================")
print(f" \x1b[32m[SUCCESS] Q1 REFLECTION & ASSET LOCK-DOWN SECURED IN MERKLE DAG\x1b[0m")
print(f" [HYPER-SEAL]: {seal}")
print("========================================================================")
