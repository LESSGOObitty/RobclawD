#!/usr/bin/env python3
"""
ROBDOE ROOT AUTHORITY // Cryptographic Ledger Sealer
Computes sequential SHA-256 hash chains across all ledger checkpoints.
"""

import hashlib
import json
import os
import sys

LEDGER_PATH = ".telemetry_ledger.jsonl"
SIG_PATH = ".ledger_state.sig"

def seal_ledger():
    if not os.path.exists(LEDGER_PATH):
        print(f"[!] Error: Ledger not found at {LEDGER_PATH}")
        sys.exit(1)
        
    current_hash = hashlib.sha256(b"ROBDOE_GENESIS_ANCHOR").hexdigest()
    checkpoint_count = 0
    
    with open(LEDGER_PATH, "r") as f:
        for line in f:
            line_str = line.strip()
            if line_str:
                checkpoint_count += 1
                # Chain previous hash with current line content
                block_data = f"{current_hash}:{line_str}".encode("utf-8")
                current_hash = hashlib.sha256(block_data).hexdigest()
                
    signature_record = {
        "checkpoints_sealed": checkpoint_count,
        "root_hash": current_hash,
        "anchor": "espVmark:2c3f1b0af3a2367a"
    }
    
    with open(SIG_PATH, "w") as sig_file:
        json.dump(signature_record, sig_file, indent=2)
        
    print(f"=========================================================")
    print(f" [CRYPTOGRAPHIC SEAL SUCCESSFUL]")
    print(f"=========================================================")
    print(f" Checkpoints Processed : {checkpoint_count}")
    print(f" Merkle Root Hash      : {current_hash}")
    print(f" Signature Stored At   : {SIG_PATH}")
    print(f"=========================================================")

if __name__ == "__main__":
    seal_ledger()
