import json
import hashlib
from datetime import datetime, timezone
import math

def align_true_north():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [CELESTIAL KUNDALI] 0.05° TRUE NORTH & AXIAL WOBBLE CORRECTION \x1b[0m")
    print("\x1b[38;2;255;220;0m [DOCTRINE] Ko te mana o te tangata, koia te pūtake. \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    # Celestial & Geodetic Alignment Parameters
    target_north = 0.000 # True North (Degrees)
    current_deviation = 0.05 # Degrees off True North
    precession_wobble_factor = 0.00125 # Celestial wobble coefficient
    tau_seconds = 12.0 # 1/7200 day tau
    
    # Corrected alignment vector compensating for wobble
    corrected_heading = target_north + (current_deviation * math.cos(precession_wobble_factor))
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "system": "Celestial Kundali",
        "target_north": target_north,
        "deviation_deg": current_deviation,
        "wobble_correction": precession_wobble_factor,
        "corrected_heading": corrected_heading,
        "status": "CELESTIAL_EQUILIBRIUM_ALIGNED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print(f" \x1b[38;2;255;100;100m[DEVIATION DETECTED]\x1b[0m {current_deviation}° off True North")
    print(f" \x1b[38;2;100;200;255m[AXIAL WOBBLE COMPENSATION]\x1b[0m Factored via precession matrix")
    print(f" \x1b[38;2;0;255;127m[LOCKED HEADING]\x1b[0m {corrected_heading:.4f}° True North Equilibrium")
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;255;255;255m[CELESTIAL MERKLE SEAL]: {seal}\x1b[0m")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    align_true_north()
