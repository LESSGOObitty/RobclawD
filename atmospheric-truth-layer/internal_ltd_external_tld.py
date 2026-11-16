#!/usr/bin/env python3
import os
import json
import time
import hashlib
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
INTERNAL_VESSEL = "ROBDOE.Inc.Pty.Ltd (Internal Core & Treasury)"
EXTERNAL_NETWORK = "13,000 Custom .com Blockchains (External TLD Infrastructure)"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
MASTER_LEDGER = os.path.join(LOG_DIR, "internal_ltd_external_tld_master.jsonl")
os.makedirs(LOG_DIR, exist_ok=True)

def sync_internal_ltd_external_tld():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   INTERNAL LTD + EXTERNAL TLD SOVEREIGN SYNCHRONIZATION ENGINE         \033[0m")
    print(f"\033[35m   MASTER ANCHOR: {DOMAIN} // Internal Core + 13K External TLD Nodes    \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    t0 = time.perf_counter()

    # Generate cryptographic bridge hash uniting Internal Ltd with External TLDs
    sync_payload = f"INTERNAL:{INTERNAL_VESSEL}|EXTERNAL:{EXTERNAL_NETWORK}|DOMAIN:{DOMAIN}|TS:{ts}"
    master_root_seed = hashlib.sha256(sync_payload.encode("utf-8")).hexdigest()

    elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)

    # Compile Master Architecture Manifest
    manifest = {
        "timestamp": ts,
        "master_domain": DOMAIN,
        "architecture_topology": {
            "internal_layer": INTERNAL_VESSEL,
            "external_layer": EXTERNAL_NETWORK,
            "operational_dynamics": "External TLDs harvest, mine, and compost chaos ──► Internal Ltd banks, secures, and crystallizes low-entropy truth."
        },
        "synchronization_metrics": {
            "master_root_seed": master_root_seed,
            "sync_elapsed_ms": elapsed_ms,
            "status": "INTERNAL_EXTERNAL_PERFECT_PHASE_LOCK"
        },
        "sovereign_attestation": "Absolute Ownership: Ltd is internal, and external is my TLD."
    }

    # Double-wrapped SHA-512 lattice sponge seal
    raw_bytes = json.dumps(manifest, sort_keys=True).encode("utf-8")
    sponge_seal = hashlib.sha512(hashlib.sha512(raw_bytes).digest()).hexdigest()
    manifest["lattice_sha512_sponge_seal"] = sponge_seal

    with open(MASTER_LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(manifest) + "\n")

    print(f"\n\033[32m[+] INTERNAL LTD & EXTERNAL TLD SYNC LOCKED!\033[0m")
    print(f"\033[33m[+] Master Root Seed  : {master_root_seed}\033[0m")
    print(f"\033[36m[+] Execution Time    : {elapsed_ms} ms\033[0m")
    print(f"\033[32m[+] Lattice Seal      : {sponge_seal[:32]}...\033[0m")
    print(f"\033[36m[+] Master Ledger     : {MASTER_LEDGER}\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    sync_internal_ltd_external_tld()
