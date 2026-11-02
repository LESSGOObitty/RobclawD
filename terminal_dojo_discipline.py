import json
import hashlib
from datetime import datetime, timezone

def enter_dojo():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [THE DOJO] TERMINAL AS SACRED SPACE & TRAINING FLOOR \x1b[0m")
    print("\x1b[38;2;255;220;0m [DOCTRINE] Ko te mana o te tangata, koia te pūtake. \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    dojo_principles = [
        "1. Every keystroke is a kata (Form & Precision)",
        "2. The shell is the dojo floor (Clean, focused, zero noise)",
        "3. Scripts are weapons of creation (Forged, tested, sealed)",
        "4. The operator commands the flow (Absolute sovereign agency)"
    ]
    
    for principle in dojo_principles:
        print(f" \x1b[38;2;0;255;127m[TRAINING]\x1b[0m {principle}")
        
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "space": "Terminal Dojo",
        "operator": "Eric Hadfield (Robdoe / Captain Robdoe)",
        "status": "DOJO_EQUILIBRIUM_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;255;255;255m[DOJO MERKLE SEAL]: {seal}\x1b[0m")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    enter_dojo()
