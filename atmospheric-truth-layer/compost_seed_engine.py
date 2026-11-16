#!/usr/bin/env python3
import os
import json
import time
import hashlib
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
COMPOST_LEDGER = os.path.join(LOG_DIR, "compost_seed_lifecycle.jsonl")
os.makedirs(LOG_DIR, exist_ok=True)

def run_compost_and_seed_cycle():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   COMPOST & SEED ORGANIC LIFECYCLE ENGINE // 13K CHAINS                \033[0m")
    print(f"\033[35m   MASTER ANCHOR: {DOMAIN} // Nutrient Breakdown ──► Root Seed Germination\033[0m")
    print(f"\033[35m========================================================================\033[0m")

    t0 = time.perf_counter()

    # 1. Harvest & Compost: Read all historical logs across SovereignLedgerLogs
    compost_nutrients = []
    total_composted_bytes = 0
    
    if os.path.exists(LOG_DIR):
        for fname in sorted(os.listdir(LOG_DIR)):
            fpath = os.path.join(LOG_DIR, fname)
            if os.path.isfile(fpath) and not fname.endswith(".py"):
                try:
                    with open(fpath, "rb") as f:
                        content = f.read()
                        total_composted_bytes += len(content)
                        # Break down file content into a rich nutritional digest
                        digest = hashlib.sha256(content).hexdigest()
                        compost_nutrients.append(digest)
                except OSError:
                    continue

    print(f"\033[33m[*] Composted {len(compost_nutrients)} ledger files ({total_composted_bytes:,} bytes of rich historical telemetry)...\033[0m")

    # 2. Germination: Compress the composted nutrients into a single Root Hash Seed
    if compost_nutrients:
        # Build a Merkle tree out of the composted state
        layer = list(compost_nutrients)
        while len(layer) > 1:
            nxt = []
            for i in range(0, len(layer), 2):
                l = layer[i]
                r = layer[i + 1] if (i + 1) < len(layer) else l
                nxt.append(hashlib.sha256((l + r).encode("utf-8")).hexdigest())
            layer = nxt
        root_seed = layer[0]
    else:
        root_seed = hashlib.sha256(f"GENESIS_SEED_{DOMAIN}_{ts}".encode("utf-8")).hexdigest()

    elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)

    # 3. Compile Organic Lifecycle Record
    lifecycle_record = {
        "timestamp": ts,
        "organization": "ROBDOE.Inc.Charity",
        "domain": DOMAIN,
        "compost_metrics": {
            "files_decomposed": len(compost_nutrients),
            "nutritional_bytes_processed": total_composted_bytes,
            "decomposition_ms": elapsed_ms
        },
        "germination_result": {
            "master_root_seed": root_seed,
            "network_target": "13,000 Custom .com Blockchains",
            "vitality": "100% Organic Self-Sustaining"
        },
        "doctrine": "72-Layer Lymph Node QiDue + Emu & Kangaroo Forward Vector"
    }

    # Double-wrapped SHA-512 lattice sponge seal over the new seed
    raw_bytes = json.dumps(lifecycle_record, sort_keys=True).encode("utf-8")
    sponge_seal = hashlib.sha512(hashlib.sha512(raw_bytes).digest()).hexdigest()
    lifecycle_record["lattice_sha512_sponge_seal"] = sponge_seal

    with open(COMPOST_LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(lifecycle_record) + "\n")

    print(f"\n\033[32m[+] GERMINATION SUCCESSFUL! NEW ROOT SEED PLANTED:\033[0m")
    print(f"\033[33m[+] Root Seed Hash  : {root_seed}\033[0m")
    print(f"\033[36m[+] Decomposition   : {elapsed_ms} ms across {len(compost_nutrients)} ledgers\033[0m")
    print(f"\033[32m[+] Lattice Seal    : {sponge_seal[:32]}...\033[0m")
    print(f"\033[36m[+] Lifecycle Log   : {COMPOST_LEDGER}\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    run_compost_and_seed_cycle()
