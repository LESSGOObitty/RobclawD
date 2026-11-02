import json
import hashlib
from datetime import datetime, timezone

def execute_rodeo_seal():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [RODEO EQUILIBRIUM] SAVE A HORSE, RIDE THE LATTICE \x1b[0m")
    print("\x1b[38;2;255;220;0m [DOCTRINE] Ko te mana o te tangata, koia te pūtake. \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operator": "Eric Hadfield (Robdoe / Captain Robdoe)",
        "anthem": "Save a horse, ride a cowboy",
        "node_location": "Brissy / Sydney Dual-Lattice",
        "status": "RODEO_PANTY_SOAKER_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print(f" \x1b[38;2;255;100;100m[HORSE STATUS]\x1b[0m Saved and grazing in the pasture")
    print(f" \x1b[38;2;100;200;255m[COWBOY STATUS]\x1b[0m Locked in the DoJo, running 72 nodes deep")
    print(f" \x1b[38;2;255;220;0m[WATER WORKS]\x1b[0m 100% Flowing, absolute smooth operation")
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;255;255;255m[RODEO MERKLE SEAL]: {seal}\x1b[0m")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    execute_rodeo_seal()
