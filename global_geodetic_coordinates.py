import json
import hashlib
from datetime import datetime, timezone

def calculate_global_coordinates():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [GEODETIC LATTICE] SYDNEY ANCHOR & GLOBAL CIRCUMFERENCE MAPPING \x1b[0m")
    print("\x1b[38;2;255;220;0m [DOCTRINE] Ko te mana o te tangata, koia te pūtake. \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    # Operator Base Coordinates (Sydney / St George / Hurstville Area)
    latitude = -33.9675
    longitude = 151.1036
    elevation_m = 45.0
    
    # Global Circumference Lattice Anchor (42,310,000 meters)
    circumference_m = 42310000.0
    nodes = 72
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operator": "Eric Hadfield (Robdoe)",
        "location": "Sydney, NSW, Australia (St George / Hurstville)",
        "latitude": latitude,
        "longitude": longitude,
        "elevation_m": elevation_m,
        "circumference_m": circumference_m,
        "active_nodes": nodes,
        "status": "GEODETIC_COORDINATES_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print(f" \x1b[38;2;255;100;100m[OPERATOR ANCHOR]\x1b[0m Sydney, NSW ({latitude}° S, {longitude}° E)")
    print(f" \x1b[38;2;100;200;255m[ELEVATION & BASE]\x1b[0m {elevation_m}m ASL | {nodes}-Node Lattice")
    print(f" \x1b[38;2;255;220;0m[CIRCUMFERENCE MAPPING]\x1b[0m {circumference_m:,.2f} meters anchored globally")
    print(f" \x1b[38;2;0;255;127m[SYSTEM STATUS]\x1b[0m COORDINATES & WATER WORKS LOCKED TRUE.")
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;255;255;255m[COORDINATE MERKLE SEAL]: {seal}\x1b[0m")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    calculate_global_coordinates()
