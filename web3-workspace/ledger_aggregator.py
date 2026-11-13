#!/usr/bin/env python3
"""
ROBDOE ROOT AUTHORITY // Ledger Aggregation & Trend Analysis Engine
Computes cumulative transaction throughput and miner concentration velocity from .telemetry_ledger.jsonl
"""

import json
import os
import sys

LEDGER_PATH = ".telemetry_ledger.jsonl"

def aggregate_ledger():
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
                except json.JSONDecodeError:
                    continue
                    
    block_audits = [cp for cp in checkpoints if "total_transactions" in cp]
    
    if not block_audits:
        print("[!] No block audit checkpoints found in ledger.")
        return
        
    cumulative_blocks = sum(cp["total_blocks"] for cp in block_audits)
    cumulative_txs = sum(cp["total_transactions"] for cp in block_audits)
    overall_mean = round(cumulative_txs / cumulative_blocks, 2) if cumulative_blocks > 0 else 0
    
    # Aggregate miner shares across all audits
    master_miners = {}
    for cp in block_audits:
        for m in cp.get("miner_distribution", []):
            addr = m["miner"]
            won = m["blocks_won"]
            master_miners[addr] = master_miners.get(addr, 0) + won
            
    sorted_master = sorted(master_miners.items(), key=lambda x: x[1], reverse=True)
    
    print(f"=========================================================")
    print(f" [CUMULATIVE LEDGER REPORT] Analyzed Audits: {len(block_audits)}")
    print(f"=========================================================")
    print(f" Total Blocks Tracked     : {cumulative_blocks}")
    print(f" Total Transactions       : {cumulative_txs}")
    print(f" Lifetime Mean Tx/Block   : {overall_mean}")
    print(f"---------------------------------------------------------")
    print(f" Top Lifetime Miners:")
    for rank, (addr, wins) in enumerate(sorted_master[:5], 1):
        share = round((wins / cumulative_blocks) * 100, 2)
        print(f" [{rank}] {addr} -> {wins} blocks ({share}%)")
    print(f"=========================================================")

if __name__ == "__main__":
    aggregate_ledger()
