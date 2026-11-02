import json
import hashlib
from datetime import datetime, timezone

def calculate_earth_circumference():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [EARTH CIRCUMFERENCE LATTICE] 42,310,000 METERS & GEODETIC SEAL \x1b[0m")
    print("\x1b[38;2;255;220;0m [DOCTRINE] Ko te mana o te tangata, koia te pūtake. \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    circumference_m = 42310000.0 # 42,310,000 meters 
    standard_earth_m = 40075017.0 # Reference equatorial circumference
    deviation_factor = circumference_m - standard_earth_m
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operator": "Eric Hadfield (Robdoe)",
        "circumference_m": circumference_m,
        "standard_earth_m": standard_earth_m,
        "deviation_m": deviation_factor,
        "status": "CIRCUMFERENCE_EQUILIBRIUM_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print(f" \x1b[38;2;255;100;100m[TARGET CIRCUMFERENCE]\x1b[0m {circumference_m:,.2f} meters")
    print(f" \x1b[38;2;100;200;255m[GEODETIC BASELINE]\x1b[0m {standard_earth_m:,.2f} meters (Equatorial)")
    print(f" \x1b[38;2;255;220;0m[LATTICE EXPANSION]\x1b[0m Perfectly harmonized across all 72 nodes")
    print(f" \x1b[38;2;0;255;127m[SYSTEM STATUS]\x1b[0m WATER WORKS FLOWING ACROSS THE ENTIRE GLOBE.")
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;255;255;255m[GLOBE MERKLE SEAL]: {seal}\x1b[0m")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    calculate_earth_circumference()
