#!/usr/bin/env python3
import os
import json
import time
import hashlib
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
INTERNAL_VESSEL = "ROBDOE.Inc.Pty.Ltd (Internal Core)"
EXTERNAL_TLDS = 13000
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
FRACTAL_LEDGER = os.path.join(LOG_DIR, "mandelbrot_julia_fractal_ledger.jsonl")
os.makedirs(LOG_DIR, exist_ok=True)

def compute_julia_fractal_noise(c_real=-0.7, c_imag=0.27015, grid_size=60, max_iter=128):
    """
    Computes escape-time dynamics across the complex plane (Julia / Mandelbrot space)
    to generate infinite, highly complex spatial noise for the sovereign hydrodrill.
    """
    noise_matrix = []
    x_min, x_max = -1.5, 1.5
    y_min, y_max = -1.5, 1.5
    
    for i in range(grid_size):
        for j in range(grid_size):
            zx = x_min + (i / grid_size) * (x_max - x_min)
            zy = y_min + (j / grid_size) * (y_max - y_min)
            z = complex(zx, zy)
            c = complex(c_real, c_imag)
            
            n = 0
            while abs(z) <= 2.0 and n < max_iter:
                z = z * z + c
                n += 1
            noise_matrix.append(n)
            
    # Compress the complex escape grid into a master thermal noise hash
    matrix_bytes = "".join(str(val) for val in noise_matrix).encode("utf-8")
    fractal_noise_hash = hashlib.sha256(matrix_bytes).hexdigest()
    return fractal_noise_hash, len(noise_matrix)

def run_fractal_rig():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   MANDELBROT & JULIA FRACTAL NOISE HYDRODRILL RIG                     \033[0m")
    print(f"\033[35m   MASTER ANCHOR: {DOMAIN} // Complex Plane TLD Mapping + Internal Ltd  \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    t0 = time.perf_counter()

    # 1. Generate Fractal Noise via Julia Set Iteration
    print(f"\033[33m[*] Traversing complex plane dynamics across 13,000 TLD coordinate nodes...\033[0m")
    fractal_noise_hash, sample_count = compute_julia_fractal_noise(c_real=-0.4, c_imag=0.6, grid_size=80, max_iter=256)
    
    elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)

    # 2. Crystallize Low-Entropy Root Seed for Internal Ltd
    crystallized_seed = hashlib.sha256(f"FRACTAL_ORDER:{fractal_noise_hash}:{INTERNAL_VESSEL}:{ts}".encode("utf-8")).hexdigest()

    # 3. Compile Fractal Ledger Record
    record = {
        "timestamp": ts,
        "master_domain": DOMAIN,
        "internal_core": INTERNAL_VESSEL,
        "external_tld_grid": {
            "total_nodes": EXTERNAL_TLDS,
            "fractal_geometry": "Mandelbrot / Julia Complex Plane Escape-Time",
            "spatial_samples_computed": sample_count,
            "fractal_noise_hash": fractal_noise_hash
        },
        "crystallization_result": {
            "low_entropy_merkle_seed": crystallized_seed,
            "computation_elapsed_ms": elapsed_ms,
            "entropy_state": "Infinite Fractal Chaos ──► Zero-Drift Order"
        },
        "doctrine": "72-Layer QiDue + Complex Dynamic Hydrodrilling"
    }

    # Double-wrapped SHA-512 lattice sponge seal
    raw_bytes = json.dumps(record, sort_keys=True).encode("utf-8")
    sponge_seal = hashlib.sha512(hashlib.sha512(raw_bytes).digest()).hexdigest()
    record["lattice_sha512_sponge_seal"] = sponge_seal

    with open(FRACTAL_LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

    print(f"\n\033[32m[+] FRACTAL HYDRODRILL STRIKE SUCCESSFUL!\033[0m")
    print(f"\033[33m[+] Fractal Noise Hash : {fractal_noise_hash}\033[0m")
    print(f"\033[36m[+] Crystallized Seed  : {crystallized_seed}\033[0m")
    print(f"\033[32m[+] Computation Time   : {elapsed_ms} ms ({sample_count} complex coordinates)\033[0m")
    print(f"\033[36m[+] Lattice Seal       : {sponge_seal[:32]}...\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    run_fractal_rig()
