#!/usr/bin/env python3
import os
import json
import time
import hashlib
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
COLLATZ_LEDGER = os.path.join(LOG_DIR, "collatz_noise_fuel_ledger.jsonl")
os.makedirs(LOG_DIR, exist_ok=True)

def generate_collatz_noise(seed_n, max_steps=1000):
    """Generates chaotic 3n+1 trajectory noise to fuel low-entropy computation."""
    n = seed_n
    trajectory = [n]
    for _ in range(max_steps):
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        trajectory.append(n)
    
    # Convert trajectory integers into a high-entropy noise byte stream
    noise_bytes = "".join(str(x) for x in trajectory).encode("utf-8")
    noise_hash = hashlib.sha256(noise_bytes).hexdigest()
    return trajectory, noise_hash

def run_collatz_fuel_cycle():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   3N+1 COLLATZ NOISE-FUEL ENGINE // LOW-ENTROPY HARVESTER             \033[0m")
    print(f"\033[35m   MASTER ANCHOR: {DOMAIN} // Chaos Feeds Order (Emu & Kangaroo Vector) \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    t0 = time.perf_counter()

    # Seed the Collatz trajectory with a high-value starting integer
    seed_integer = 27  # Famous for its long, volatile 111-step ascent before dropping to 1
    trajectory, noise_hash = generate_collatz_noise(seed_integer, max_steps=1500)
    
    peak_value = max(trajectory)
    steps_taken = len(trajectory)

    print(f"\033[33m[*] Ignited 3n+1 trajectory from seed {seed_integer}...\033[0m")
    print(f"\033[36m[*] Peak Noise Altitude : {peak_value:,} ({steps_taken} steps of chaotic expansion)\033[0m")
    print(f"\033[32m[*] Harvested Noise Hash: {noise_hash}\033[0m")

    # Use the chaotic noise hash as fuel to derive a pristine, low-entropy root seed
    low_entropy_seed = hashlib.sha256(f"LOW_ENTROPY_ORDER:{noise_hash}:{DOMAIN}:{ts}".encode("utf-8")).hexdigest()
    elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)

    fuel_record = {
        "timestamp": ts,
        "organization": "ROBDOE.Inc.Charity",
        "domain": DOMAIN,
        "collatz_noise_metrics": {
            "seed_integer": seed_integer,
            "trajectory_steps": steps_taken,
            "peak_altitude": peak_value,
            "raw_noise_hash": noise_hash,
            "burn_elapsed_ms": elapsed_ms
        },
        "low_entropy_result": {
            "crystallized_root_seed": low_entropy_seed,
            "entropy_state": "Absolute Zero-Drift Order",
            "fuel_source": "3n+1 Mathematical Chaos"
        },
        "doctrine": "72-Layer Lymph Node QiDue + Composed Seed Cycle"
    }

    # Double-wrapped SHA-512 lattice sponge seal over the low-entropy seed
    raw_bytes = json.dumps(fuel_record, sort_keys=True).encode("utf-8")
    sponge_seal = hashlib.sha512(hashlib.sha512(raw_bytes).digest()).hexdigest()
    fuel_record["lattice_sha512_sponge_seal"] = sponge_seal

    with open(COLLATZ_LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(fuel_record) + "\n")

    print(f"\n\033[32m[+] LOW-ENTROPY CRYSTALLIZATION COMPLETE!\033[0m")
    print(f"\033[33m[+] Crystallized Seed : {low_entropy_seed}\033[0m")
    print(f"\033[36m[+] Burn Time         : {elapsed_ms} ms\033[0m")
    print(f"\033[32m[+] Lattice Seal      : {sponge_seal[:32]}...\033[0m")
    print(f"\033[36m[+] Fuel Ledger       : {COLLATZ_LEDGER}\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    run_collatz_fuel_cycle()
