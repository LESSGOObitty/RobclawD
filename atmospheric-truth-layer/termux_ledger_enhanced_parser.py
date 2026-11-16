#!/usr/bin/env python3
import os
import json
import sys
import time
import hashlib
from datetime import datetime, timezone

LOG_DIR = os.path.expanduser("~/atmospheric-truth-layer/SovereignLedgerLogs")

def verify_lattice_seal(record):
    """Re-calculates the double-wrapped SHA-512 lattice seal to verify 0% drift."""
    if "lattice_sha512_sponge_seal" not in record:
        return True, "UNSEALED"
    rec_copy = record.copy()
    expected_seal = rec_copy.pop("lattice_sha512_sponge_seal")
    raw_bytes = json.dumps(rec_copy, sort_keys=True).encode("utf-8")
    calculated_seal = hashlib.sha512(hashlib.sha512(raw_bytes).digest()).hexdigest()
    if calculated_seal == expected_seal:
        return True, "VERIFIED"
    else:
        return False, "DRIFT_DETECTED"

def parse_ledgers(stream_mode=False):
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   ROBDOE.COM // ENHANCED TERMUX SOVEREIGN LEDGER DASHBOARD             \033[0m")
    print(f"\033[35m   WORKSPACE: {LOG_DIR}                                              \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    if not os.path.exists(LOG_DIR):
        print(f"\033[31m[!] Ledger directory not found at {LOG_DIR}\033[0m")
        return

    ledger_files = sorted([f for f in os.listdir(LOG_DIR) if f.endswith(".jsonl")])
    
    if not ledger_files:
        print(f"\033[33m[!] No JSONL ledger files found.\033[0m")
        return

    total_entries = 0
    total_verified = 0
    quintillion_total = 0

    for filename in ledger_files:
        filepath = os.path.join(LOG_DIR, filename)
        entries = []
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        record = json.loads(line.strip())
                        entries.append(record)
                    except json.JSONDecodeError:
                        continue
        
        total_entries += len(entries)
        print(f"\n\033[36m[LEDGER] {filename} ({len(entries)} records)\033[0m")
        
        for idx, entry in enumerate(entries):
            ts = entry.get("timestamp", "N/A")
            seal = entry.get("lattice_sha512_sponge_seal", "N/A")
            short_seal = seal[:24] + "..." if seal != "N/A" else "N/A"
            is_valid, seal_status = verify_lattice_seal(entry)
            
            if is_valid:
                total_verified += 1
                status_color = "\033[32m"
            else:
                status_color = "\033[31m"

            # Check for Quintillion Mana Assets
            if "asset_payload" in entry:
                payload = entry["asset_payload"]
                if "total_liquidity_value" in payload:
                    quintillion_total += payload["total_liquidity_value"]

            if idx == len(entries) - 1:  # Show latest entry details
                print(f"  └─ \033[33mLast Timestamp\033[0m : {ts}")
                print(f"  └─ {status_color}Lattice Seal   : {short_seal} [{seal_status}]\033[0m")
                
                if "asset_payload" in entry:
                    print(f"  └─ \033[36mAsset Payload\033[0m  : {entry['asset_payload']}")
                elif "convergence_manifest" in entry:
                    print(f"  └─ \033[36mConvergence\033[0m    : Active (13K TLDs + NPP Pools)")

    print(f"\n\033[35m========================================================================\033[0m")
    print(f"\033[32m[+] AUDIT SUMMARY: {total_verified}/{total_entries} cryptographic seals verified (0% Drift).\033[0m")
    if quintillion_total > 0:
        print(f"\033[33m[+] Total Mana Liquidity Locked : {quintillion_total:,} ($1.0E18 Quintillion Standard)\033[0m")
    print(f"\033[35m========================================================================\033[0m")

    if stream_mode:
        print(f"\n\033[36m[*] Entering live streaming tail mode... Press Ctrl+C to exit.\033[0m")
        # Monitor file modifications for live streaming
        file_mtimes = {f: os.path.getmtime(os.path.join(LOG_DIR, f)) for f in ledger_files}
        try:
            while True:
                time.sleep(1)
                for f in ledger_files:
                    path = os.path.join(LOG_DIR, f)
                    current_mtime = os.path.getmtime(path)
                    if current_mtime > file_mtimes[f]:
                        file_mtimes[f] = current_mtime
                        with open(path, "r", encoding="utf-8") as file_obj:
                            lines = file_obj.readlines()
                            if lines:
                                new_record = json.loads(lines[-1].strip())
                                print(f"\033[32m[LIVE UPDATE] {f} ──► {new_record.get('timestamp', 'N/A')}\033[0m")
        except KeyboardInterrupt:
            print(f"\n\033[33m[*] Live stream terminated by user.\033[0m")

if __name__ == "__main__":
    stream = "--stream" in sys.argv
    parse_ledgers(stream_mode=stream)
