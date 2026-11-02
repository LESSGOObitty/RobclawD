import json
import hashlib
from datetime import datetime, timezone

def execute_horse_mane_matrix():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [MANE & WATER MATRIX] STRADDLING IDENTITY, NOISE & HYDRATION \x1b[0m")
    print("\x1b[38;2;255;220;0m [DOCTRINE] Ko te mana o te tangata, koia te pūtake. \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "protocol": "Calculated Identity & Mane Control",
        "noise_ratio": "Straddled and Harnessed",
        "hydration_status": "Horse drinking deep from the water works",
        "status": "MANE_AND_WATER_EQUILIBRIUM_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print(f" \x1b[38;2;255;100;100m[IDENTITY GRIP]\x1b[0m Straddling the static and the signal with absolute precision")
    print(f" \x1b[38;2;100;200;255m[MANE GUIDANCE]\x1b[0m Holding the reins, leading the beast right to the stream")
    print(f" \x1b[38;2;255;220;0m[WATER WORKS]\x1b[0m Drinking deep, fully saturated, 100% flow locked")
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;255;255;255m[MANE MERKLE SEAL]: {seal}\x1b[0m")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    execute_horse_mane_matrix()
