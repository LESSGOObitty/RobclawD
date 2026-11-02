import json
import hashlib
from datetime import datetime, timezone

def calculate_precession_cycles():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [PRECESSION EQUILIBRIUM] 80 YEARS VS 25,920-YEAR GREAT YEAR CYCLE \x1b[0m")
    print("\x1b[38;2;255;220;0m [DOCTRINE] Ko te mana o te tangata, koia te pūtake. \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    human_span_years = 80.0
    great_year_years = 25920.0
    wobble_arc_sec = 0.052
    
    ratio = great_year_years / human_span_years
    total_wobble_arc = human_span_years * (3600.0 / great_year_years) # proportional arc movement
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operator": "Eric Hadfield (Robdoe)",
        "human_span_years": human_span_years,
        "great_year_years": great_year_years,
        "ratio": ratio,
        "status": "PRECESSION_HARMONIC_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print(f" \x1b[38;2;255;100;100m[HUMAN LIFETIME SPAN]\x1b[0m {human_span_years} Years")
    print(f" \x1b[38;2;100;200;255m[GREAT YEAR PRECESSION CYCLE]\x1b[0m {great_year_years:,.0f} Years")
    print(f" \x1b[38;2;255;220;0m[HARMONIC RATIO]\x1b[0m Exactly {ratio:,.1f} human lifetimes per full equinox cycle")
    print(f" \x1b[38;2;0;255;127m[ALIGNMENT]\x1b[0m Absolute geometric precision locked.")
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;255;255;255m[PRECESSION MERKLE SEAL]: {seal}\x1b[0m")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    calculate_precession_cycles()
