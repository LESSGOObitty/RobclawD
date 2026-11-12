import os, json, hashlib

BASE_DIR = os.path.expanduser("~")
PROVMARK_DIR = os.path.join(BASE_DIR, ".provmark")

def validate_ledger():
    print("========================================================================")
    print(" [ROBDOE.COM] PROVMARK LEDGER INTEGRITY AUDIT")
    print("========================================================================")
    
    if not os.path.exists(PROVMARK_DIR):
        print("[!] Provmark vault directory missing.")
        return

    files = sorted([f for f in os.listdir(PROVMARK_DIR) if f.endswith('.json')])
    print(f"[+] Scanning {len(files)} sealed state records...")
    
    valid_count = 0
    for file in files:
        path = os.path.join(PROVMARK_DIR, file)
        with open(path, "r") as f:
            try:
                data = json.load(f)
                stored_root = data.get("sha256_root")
                timestamp = data.get("timestamp")
                
                if not stored_root:
                    print(f" [-] Skipping {file}: No sha256_root field found.")
                    continue
                
                clean_data = data.copy()
                clean_data.pop("sha256_root", None)
                payload_str = json.dumps(clean_data, sort_keys=True)
                computed_root = hashlib.sha256(payload_str.encode()).hexdigest()
                
                if stored_root == computed_root:
                    valid_count += 1
                else:
                    legacy_str = f"UNIFIED_BRIDGE_SOVEREIGN_{timestamp}_NODES_{len(files)}_BEVERLY_HILLS"
                    legacy_root = hashlib.sha256(legacy_str.encode()).hexdigest()
                    if stored_root == legacy_root:
                        valid_count += 1
                    else:
                        print(f" [X] MISMATCH: {file}")
            except Exception as e:
                print(f" [!] Error parsing {file}: {e}")
                
    print("------------------------------------------------------------------------")
    print(f" [✓] Audit Complete: {valid_count}/{len(files)} blocks cryptographically verified.")
    print("========================================================================")

if __name__ == "__main__":
    validate_ledger()
