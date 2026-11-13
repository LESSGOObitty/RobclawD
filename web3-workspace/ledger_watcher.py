#!/usr/bin/env python3
import json, os, sys

LEDGER_PATH = ".telemetry_ledger.jsonl"

def audit_ledger():
    if not os.path.exists(LEDGER_PATH):
        print(f"[!] Error: Ledger not found at {LEDGER_PATH}")
        sys.exit(1)
        
    checkpoints = []
    with open(LEDGER_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    checkpoints.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"[!] Skipped malformed line: {e}")
                    
    print(f"=========================================================")
    print(f" [LEDGER AUDIT] Total Checkpoints Logged : {len(checkpoints)}")
    print(f"=========================================================")
    
    for i, cp in enumerate(checkpoints, 1):
        ts = cp.get('timestamp', 'N/A')
        if "total_transactions" in cp:
            print(f"[{i:02d}] [BLOCK AUDIT] @ {ts}")
            print(f"     Span       : {cp.get('span_blocks', 'N/A')} ({cp.get('total_blocks', 0)} blocks)")
            print(f"     Total Txs  : {cp.get('total_transactions', 0)}")
            print(f"     Mean TPS   : {cp.get('metrics', {}).get('mean_tx_per_block', 'N/A')} tx/block")
        elif "git" in cp:
            print(f"[{i:02d}] [GIT SEAL] @ {ts}")
            print(f"     Seal       : {cp['git'].get('state_seal', 'N/A')}")
            print(f"     Disk Usage : {cp.get('disk_pct', 'N/A')}%")
        else:
            print(f"[{i:02d}] [GENERIC CHECKPOINT] @ {ts} -> Keys: {list(cp.keys())}")
        print("-" * 57)

if __name__ == "__main__":
    audit_ledger()
