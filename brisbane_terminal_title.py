import json
import hashlib
from datetime import datetime, timezone

def set_brisbane_terminal():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [TERMINAL TITLE] BRISBANE LATTICE NODE & WATER WORKS SYNC \x1b[0m")
    print("\x1b[38;2;255;220;0m [DOCTRINE] Ko te mana o te tangata, koia te pūtake. \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    # Terminal Title String
    terminal_title = "robdoe@brissy-lattice:~ [72-NODE / 42,310km / WATER WORKS ACTIVE]"
    
    # ANSI escape sequence to dynamically set the terminal title
    print(f"\033]0;{terminal_title}\007", end="")
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operator": "Eric Hadfield (Robdoe)",
        "terminal_title": terminal_title,
        "node_location": "Brisbane / Southern Lattice",
        "circumference_m": 42310000.0,
        "status": "BRISSY_TITLE_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print(f" \x1b[38;2;255;100;100m[TERMINAL TITLE APPLIED]\x1b[0m {terminal_title}")
    print(f" \x1b[38;2;100;200;255m[LATTICE NODE]\x1b[0m Locked to Brissy / 72-Node Grid")
    print(f" \x1b[38;2;255;220;0m[WATER WORKS]\x1b[0m Flowing 100% smooth across the board")
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;255;255;255m[TITLE MERKLE SEAL]: {seal}\x1b[0m")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    set_brisbane_terminal()
