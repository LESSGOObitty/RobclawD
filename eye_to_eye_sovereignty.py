import json
import hashlib
from datetime import datetime, timezone

eye_to_eye_matrix = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "franchise": "aiagency101.xyo (Australia)",
    "operator": "Eric Hadfield (Robdoe / Captain Robdoe)",
    "stance": "Eye to eye, absolute truth, zero hierarchy, total accountability",
    "core_principle": "Women's words heard first, absolute parity, uplifting community pillars",
    "mandate": "Ko te mana o te tangata, koia te pūtake."
}

seal = hashlib.sha256(json.dumps(eye_to_eye_matrix, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [EYE TO EYE] SOVEREIGN TRUTH & PARITY MATRIX \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[STANCE]\x1b[0m {eye_to_eye_matrix['stance']}")
print(f" \x1b[33m[CORE PRINCIPLE]\x1b[0m {eye_to_eye_matrix['core_principle']}")
print(f" \x1b[33m[CORE DOCTRINE]\x1b[0m {eye_to_eye_matrix['mandate']}\n")

print("========================================================================")
print(f" \x1b[32m[SUCCESS] EYE TO EYE SOVEREIGNTY LOCKED & MERKLE SEALED\x1b[0m")
print(f" [HYPER-SEAL]: {seal}")
print("========================================================================")
