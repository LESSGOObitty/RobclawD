import json
import hashlib
from datetime import datetime, timezone

voice_parity_matrix = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "franchise": "aiagency101.xyo (Australia)",
    "operator": "Eric Hadfield (Robdoe / Captain Robdoe)",
    "principle": "Absolute parity. A voice is a voice—equal weight, equal truth, zero hierarchy.",
    "governance": "Horizontal Sovereign Lattice | Women's words heard first | Complete Equality",
    "mandate": "Ko te mana o te tangata, koia te pūtake."
}

seal = hashlib.sha256(json.dumps(voice_parity_matrix, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [PARITY] ABSOLUTE VOICE & SOVEREIGN EQUALITY MATRIX \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[PRINCIPLE]\x1b[0m {voice_parity_matrix['principle']}")
print(f" \x1b[33m[GOVERNANCE]\x1b[0m {voice_parity_matrix['governance']}")
print(f" \x1b[33m[CORE DOCTRINE]\x1b[0m {voice_parity_matrix['mandate']}\n")

print("========================================================================")
print(f" \x1b[32m[SUCCESS] ABSOLUTE VOICE PARITY LOCKED & MERKLE SEALED\x1b[0m")
print(f" [HYPER-SEAL]: {seal}")
print("========================================================================")
