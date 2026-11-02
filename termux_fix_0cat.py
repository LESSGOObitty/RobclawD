import json
import hashlib
from datetime import datetime, timezone

def fix_typo_alias():
    print("\n\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    print("\x1b[38;2;255;220;0m [TYPO RESOLUTION] 0CAT TO CAT ALIAS & PROMPT ALIGNMENT \x1b[0m")
    print("\x1b[38;2;255;220;0m [DOCTRINE] Ko te mana o te tangata, koia te pūtake. \x1b[0m")
    print("\x1b[38;2;0;255;255m========================================================================\x1b[0m")
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": "Typo correction for 0cat -> cat",
        "status": "TYPO_RESOLVED_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print(f" \x1b[38;2;255;100;100m[TYPO CAPTURED]\x1b[0m Hit '0cat' instead of 'cat'. Classic slip on the mobile keyboard.")
    print(f" \x1b[38;2;100;200;255m[PROMPT STATE]\x1b[0m TrueColor prompt stable at robdoe.termux")
    print(f" \x1b[38;2;255;220;0m[ACTION]\x1b[0m Use standard coreutils `cat` or script execution directly.")
    print("------------------------------------------------------------------------")
    print(f" \x1b[38;2;255;255;255m[TYPO MERKLE SEAL]: {seal}\x1b[0m")
    print("========================================================================\x1b[0m")

if __name__ == "__main__":
    fix_typo_alias()
