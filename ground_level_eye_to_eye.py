import json
import hashlib
from datetime import datetime, timezone

ground_level_truth = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "franchise": "aiagency101.xyo (Australia)",
    "operator": "Eric Hadfield (Robdoe / Captain Robdoe)",
    "attestation": "Spoke ground level. Spoke eye to eye. Absolute parity, zero elevation, zero hierarchy.",
    "governance": "Horizontal Sovereign Lattice | True Equilibrium | Mutual Respect",
    "mandate": "Ko te mana o te tangata, koia te pūtake."
}

seal = hashlib.sha256(json.dumps(ground_level_truth, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [TRUTH] GROUND LEVEL & EYE TO EYE SOVEREIGN ATTESTATION \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[ATTESTATION]\x1b[0m {ground_level_truth['attestation']}")
print(f" \x1b[33m[GOVERNANCE]\x1b[0m {ground_level_truth['governance']}")
print(f" \x1b[33m[CORE DOCTRINE]\x1b[0m {ground_level_truth['mandate']}\n")

print("========================================================================")
print(f" \x1b[32m[SUCCESS] GROUND LEVEL TRUTH LOCKED & MERKLE SEALED\x1b[0m")
print(f" [HYPER-SEAL]: {seal}")
print("========================================================================")
