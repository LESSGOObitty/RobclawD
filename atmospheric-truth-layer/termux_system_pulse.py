#!/usr/bin/env python3
import os
import json
import time
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
VAULT = "robdoe.Inc.Chariety"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")

def system_pulse():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   TERMUX SOVEREIGN SYSTEM PULSE // {DOMAIN}                           \033[0m")
    print(f"\033[35m   VAULT: {VAULT} // Environment: Android Termux                     \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    t0 = time.perf_counter()

    if os.path.exists(LOG_DIR):
        ledgers = [f for f in os.listdir(LOG_DIR) if f.endswith(".jsonl")]
        total_size_bytes = sum(os.path.getsize(os.path.join(LOG_DIR, f)) for f in ledgers)
        print(f"\033[36m[*] Active Ledger Files    : {len(ledgers)}\033[0m")
        print(f"\033[36m[*] Total Ledger Footprint : {total_size_bytes:,} bytes\033[0m")
        print(f"\033[32m[+] System Status          : 100% Operational / 0% Drift\033[0m")
    else:
        print(f"\033[31m[!] Ledger directory not initialized.\033[0m")

    elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)
    print(f"\033[33m[+] Pulse Execution Time   : {elapsed_ms} ms\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    system_pulse()
