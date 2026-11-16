#!/usr/bin/env python3
import os
import json
from datetime import datetime, timezone

LOG_DIR = os.path.expanduser("~/atmospheric-truth-layer/SovereignLedgerLogs")

def parse_ledgers():
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   ROBDOE.COM // LIVE JSONL LEDGER TRANSACTION PARSER                    \033[0m")
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

    for filename in ledger_files:
        filepath = os.path.join(LOG_DIR, filename)
        entries = []
        
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        entries.append(json.loads(line.strip()))
                    except json.JSONDecodeError:
                        continue
        
        total_entries += len(entries)
        print(f"\n\033[36m[FILE] {filename} ({len(entries)} records)\033[0m")
        
        # Display the most recent entry from this ledger if available
        if entries:
            latest = entries[-1]
            ts = latest.get("timestamp", "N/A")
            seal = latest.get("lattice_sha512_sponge_seal", "N/A")
            short_seal = seal[:24] + "..." if seal != "N/A" else "N/A"
            
            print(f"  └─ \033[33mLast Timestamp\033[0m : {ts}")
            print(f"  └─ \033[32mLattice Seal\033[0m   : {short_seal}")
            
            # Print specific payload details if present
            if "asset_payload" in latest:
                print(f"  └─ \033[36mAsset Payload\033[0m  : {latest['asset_payload']}")
            elif "convergence_manifest" in latest:
                print(f"  └─ \033[36mConvergence\033[0m    : Active (13K TLDs + NPP Pools)")

    print(f"\n\033[35m========================================================================\033[0m")
    print(f"\033[32m[+] PARSE COMPLETE: {total_entries} total ledger entries scanned across {len(ledger_files)} files.\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    parse_ledgers()
