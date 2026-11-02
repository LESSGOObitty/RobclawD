import json
import hashlib
from datetime import datetime, timezone

def trace_whakapapa():
    print("\n\x1b[38;5;51m========================================================================\x1b[0m")
    print("\x1b[38;5;226m [WHAKAPAPA GENEALOGY] ROOT ANCESTRY & LATTICE LINEAGE \x1b[0m")
    print("\x1b[38;5;51m========================================================================\x1b[0m")
    
    lineage = [
        "Ko te pūtake (The Source / Genesis Key)",
        "Ko te wai (The Liquidity / Nutrient Flow)",
        "Ko ngā roothash (The Cryptographic Lineage)",
        "Ko te mana tangata (Sovereign Agency & Operation)"
    ]
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "framework": "Whakapapa Roothash Lineage",
        "doctrine": "Ko te mana o te tangata, koia te pūtake.",
        "generations": lineage,
        "status": "WHAKAPAPA_EQUILIBRIUM_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    for i, gen in enumerate(lineage, 1):
        print(f" \x1b[33m[GEN 0{i}]\x1b[0m {gen}")
        
    print("------------------------------------------------------------------------")
    print(f" \x1b[32m[LINEAGE STATUS]\x1b[0m Unbroken connection from soil to chain.")
    print(f" \x1b[33m[MERKLE SEAL]\x1b[0m {seal}")
    print("========================================================================")

if __name__ == "__main__":
    trace_whakapapa()
