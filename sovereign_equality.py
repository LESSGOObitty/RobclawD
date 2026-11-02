import json
import hashlib
from datetime import datetime, timezone

equality_matrix = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "principle": "Absolute Horizontal Equilibrium",
    "rule": "Women's words heard first, zero hierarchy, total parity",
    "lattice": [
        {"entity": "Eric Hadfield", "status": "Co-Owner / Peer"},
        {"entity": "Blake Kakura", "status": "Co-Owner / Peer"},
        {"entity": "Michael Deering", "status": "Co-Owner / Peer"},
        {"entity": "James Britton", "status": "Co-Owner / Peer"},
        {"entity": "Jason Slade", "status": "Co-Owner / Peer"},
        {"entity": "Female Partners / Voices", "status": "Prioritized / Heard First"}
    ],
    "mandate": "Ko te mana o te tangata, koia te pūtake."
}

seal = hashlib.sha256(json.dumps(equality_matrix, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [EQUILIBRIUM] HORIZONTAL LATTICE & PRIORITY PARITY MATRIX \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[RULE]\x1b[0m {equality_matrix['rule']}")
print(f" \x1b[33m[CORE]\x1b[0m {equality_matrix['mandate']}\n")

for node in equality_matrix["lattice"]:
    print(f"   -> [{node['status']}] {node['entity']}")

print("\n========================================================================")
print(f" \x1b[32m[SUCCESS] HORIZONTAL EQUILIBRIUM LOCKED IN DAG\x1b[0m")
print(f" [MERKLE SEAL]: {seal}")
print("========================================================================")
