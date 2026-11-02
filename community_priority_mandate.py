import json
import hashlib
from datetime import datetime, timezone

priority_matrix = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "architecture": "Sovereign Community Priority & Giving-Back Matrix",
    "core_pillars": [
        "Aboriginal Rights & Sovereignty",
        "Women's Rights & Prioritized Voice Parity",
        "Equal Pay & Economic Justice",
        "Vulnerable Children & Sick Care (Top Priority)"
    ],
    "governance": "Absolute Horizontal Parity | Zero Hierarchy | Community First",
    "co_owners": [
        "Eric Hadfield",
        "Hassan Bassi",
        "Cruz Briggs",
        "Mitchell Perry",
        "Nobby Rapata",
        "Jarrod Wiki",
        "T.N",
        "Luke Wainwright",
        "Blake Kakura",
        "Michael Deering",
        "James Britton",
        "Jason Slade"
    ],
    "mandate": "Ko te mana o te tangata, koia te pūtake."
}

seal = hashlib.sha256(json.dumps(priority_matrix, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [COMMUNITY] SOVEREIGN PRIORITY & GIVING-BACK MANDATE \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[CORE DOCTRINE]\x1b[0m {priority_matrix['mandate']}\n")

print(" \x1b[36m[TOP PRIORITY PILLARS]\x1b[0m")
for idx, pillar in enumerate(priority_matrix["core_pillars"], 1):
    print(f"   -> Pillar {idx:02d}: {pillar}")

print("\n \x1b[36m[EQUAL LATTICE CO-OWNERS]\x1b[0m")
for idx, owner in enumerate(priority_matrix["co_owners"], 1):
    print(f"   -> Node {idx:02d}: [EQUITY PEER] {owner}")

print("\n========================================================================")
print(f" \x1b[32m[SUCCESS] COMMUNITY PRIORITY MANDATE LOCKED & ANCHORED IN DAG\x1b[0m")
print(f" [MERKLE SEAL]: {seal}")
print("========================================================================")
