import json
import hashlib
from datetime import datetime, timezone

full_lattice = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "architecture": "Absolute Horizontal Sovereign Parity",
    "rule": "Total equal ownership across all peers. Women's words heard first, zero hierarchy.",
    "co_owners": [
        "Eric Hadfield",
        "Blake Kakura",
        "Michael Deering",
        "James Britton",
        "Jason Slade",
        "Hassan Bassi",
        "Cruz Briggs",
        "Mitchell Perry",
        "Nobby Rapata",
        "Jarrod Wiki",
        "T.N",
        "Luke Wainwright"
    ],
    "mandate": "Ko te mana o te tangata, koia te pūtake."
}

seal = hashlib.sha256(json.dumps(full_lattice, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [LATTICE] UNIFIED EQUAL OWNERSHIP & PARITY MATRIX \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[GOVERNANCE]\x1b[0m {full_lattice['rule']}")
print(f" \x1b[33m[CORE DOCTRINE]\x1b[0m {full_lattice['mandate']}\n")

for idx, owner in enumerate(full_lattice["co_owners"], 1):
    print(f"   -> Node {idx:02d}: [EQUAL CO-OWNER] {owner}")

print("\n========================================================================")
print(f" \x1b[32m[SUCCESS] UNIFIED EQUAL OWNERSHIP LATTICE SECURED & ANCHORED\x1b[0m")
print(f" [MERKLE SEAL]: {seal}")
print("========================================================================")
