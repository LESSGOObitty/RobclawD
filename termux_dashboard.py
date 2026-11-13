#!/usr/bin/env python3
"""
ROBDOE ROOT AUTHORITY // Terminal Command Center & Dashboard
Aggregates live filesystem health, route optimization, and cryptographic seals.
"""

import os
import json
import shutil

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    pct = (used / total) * 100
    return f"{free // (2**30)} GB free ({pct:.1f}% used)"

def load_json_file(filepath):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except Exception:
            return {"error": "Malformed or unreadable file"}
    return None

def render():
    disk = get_disk_usage()
    route = load_json_file(".telemetry_route.json")
    sig = load_json_file(".ledger_state.sig")
    
    # Read last ledger checkpoint
    ledger_summary = "No checkpoint logged"
    if os.path.exists(".telemetry_ledger.jsonl"):
        with open(".telemetry_ledger.jsonl", "r") as f:
            lines = [line.strip() for line in f if line.strip()]
            if lines:
                try:
                    last_cp = json.loads(lines[-1])
                    ledger_summary = f"{last_cp.get('total_blocks', 0)} blocks | {last_cp.get('total_transactions', 0)} txs"
                except Exception:
                    ledger_summary = "Parse error"

    print("=========================================================")
    print(" █▀▀ █▀█ █▀▄ █▀▄ █▀█ █▀▀   █▀█ █ █ █▀█ ▀█▀ █ █ █▀█ █▀█")
    print(" █▄▄ █▄█ █▄▀ █▄▀ █▄█ ██▄   █▀▄ █▄█ █▀▄  █  █▄█ █ █ █▀▀")
    print("=========================================================")
    print(f" [FS STORAGE] Headroom : {disk}")
    if route:
        print(f" [ROUTE LOCK] Gateway  : {route.get('name')} ({route.get('ip')}) @ {route.get('latency_ms')}ms")
    else:
        print(f" [ROUTE LOCK] Gateway  : Not initialized")
        
    print(f" [LEDGER CORE] Status  : {ledger_summary}")
    
    if sig:
        print(f" [STATE SEAL] Root Hash: {sig.get('root_hash', 'N/A')[:24]}... (Sealed)")
        print(f"               Anchor  : {sig.get('anchor')}")
    else:
        print(f" [STATE SEAL] Status   : Unsealed")
    print("=========================================================")

if __name__ == "__main__":
    render()
