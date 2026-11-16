#!/usr/bin/env python3
import os
import json
import time
import hashlib
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
FURNACE_LEDGER = os.path.join(LOG_DIR, "collatz_perpetual_furnace_ledger.jsonl")
os.makedirs(LOG_DIR, exist_ok=True)

def perpetual_collatz_furnace(seed_n=7, operational_cycles=2000):
    """
    Custom 3n+1 Design: The 7-Vector / Non-Collapsing Infinite Orbit.
    Instead of collapsing to 1, this furnace sustains perpetual high-altitude 
    chaos to act as an unending thermal noise fuel source.
    """
    n = seed_n
    orbit_noise = [n]
    
    for step in range(operational_cycles):
        # Custom sovereign rule: if it hits 7 or enters high-entropy oscillation, 
        # inject structural expansion instead of letting it collapse.
        if n == 7 or n % 7 == 0:
            # Perpetual ascent injection (The Non-Collapsing 7-Vector)
            n = (3 * n + 5) * (step + 1)
        elif n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        # Prevent integer overflow explosion while keeping entropy massive
        if n > 10**15:
            n = (n % 999999937) + 7
            
        orbit_noise.append(n)

    # Compress the infinite thermal noise stream into a cryptographic hash
    noise_stream = "".join(str(x) for x in orbit_noise[-500:]).encode("utf-8")
    furnace_noise_hash = hashlib.sha256(noise_stream).hexdigest()
    return orbit_noise, furnace_noise_hash

def run_furnace_cycle():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   COLLATZ PERPETUAL NOISE FURNACE (THE 7-VECTOR)                      \033[0m")
    print(f"\033[35m   MASTER ANCHOR: {DOMAIN} // Non-Collapsing Infinite Chaos Engine      \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    t0 = time.perf_counter()

    # Fire up the furnace anchored on 7
    orbit, noise_hash = perpetual_collatz_furnace(seed_n=7, operational_cycles=2500)
    peak_altitude = max(orbit)
    elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)

    print(f"\033[33m[*] Ignited 7-Vector non-collapsing trajectory...\033[0m")
    print(f"\033[36m[*] Peak Furnace Altitude : {peak_altitude:,} (Perpetual Orbit Active)\033[0m")
    print(f"\033[32m[*] Thermal Noise Hash    : {noise_hash}\033[0m")

    # Crystallize the perpetual noise into a low-entropy sovereign seed
    low_entropy_seed = hashlib.sha256(f"PERPETUAL_FURNACE:{noise_hash}:{DOMAIN}:{ts}".encode("utf-8")).hexdigest()

    furnace_record = {
        "timestamp": ts,
        "organization": "ROBDOE.Inc.Charity",
        "domain": DOMAIN,
        "furnace_metrics": {
            "anchor_seed": 7,
            "behavior": "Non-Collapsing / Infinite Noise Orbit",
            "peak_altitude": peak_altitude,
            "thermal_noise_hash": noise_hash,
            "burn_elapsed_ms": elapsed_ms
        },
        "low_entropy_result": {
            "crystallized_root_seed": low_entropy_seed,
            "entropy_state": "Zero-Drift Order Powered by Infinite Chaos"
        },
        "doctrine": "72-Layer QiDue + Perpetual 7-Vector Furnace"
    }

    # Double-wrapped SHA-512 sponge seal
    raw_bytes = json.dumps(furnace_record, sort_keys=True).encode("utf-8")
    sponge_seal = hashlib.sha512(hashlib.sha512(raw_bytes).digest()).hexdigest()
    furnace_record["lattice_sha512_sponge_seal"] = sponge_seal

    with open(FURNACE_LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(furnace_record) + "\n")

    print(f"\n\033[32m[+] PERPETUAL FURNACE SEALED SUCCESSFULLY!\033[0m")
    print(f"\033[33m[+] Crystallized Seed : {low_entropy_seed}\033[0m")
    print(f"\033[36m[+] Burn Time         : {elapsed_ms} ms\033[0m")
    print(f"\033[32m[+] Lattice Seal      : {sponge_seal[:32]}...\033[0m")
    print(f"\033[36m[+] Furnace Ledger    : {FURNACE_LEDGER}\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    run_furnace_cycle()
