#!/usr/bin/env python3
import os
import json
import time
import hashlib
import multiprocessing as mp
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
GENIUS_LEDGER = os.path.join(LOG_DIR, "genius_mint_hydrodrill_ledger.jsonl")
SOLANA_LEDGER = os.path.join(REPO_DIR, "solana_atmospheric_ledger")
EVM_WITNESS_LOG = os.path.join(REPO_DIR, "external_witness_evm.log")
os.makedirs(LOG_DIR, exist_ok=True)

# 1. Extract Current Bedrock State (Workspace Merkle Root)
def compute_bedrock_merkle():
    leaves = []
    for root, dirs, files in os.walk(REPO_DIR):
        dirs[:] = [d for d in dirs if d not in (".git", "SovereignLedgerLogs", "__pycache__")]
        for fname in sorted(files):
            fpath = os.path.join(root, fname)
            try:
                h = hashlib.sha256()
                with open(fpath, "rb") as f:
                    while chunk := f.read(65536):
                        h.update(chunk)
                leaves.append(h.hexdigest())
            except OSError:
                continue
    if not leaves:
        return "0" * 64, 0
    count = len(leaves)
    while len(leaves) > 1:
        nxt = []
        for i in range(0, len(leaves), 2):
            l = leaves[i]
            r = leaves[i + 1] if (i + 1) < len(leaves) else l
            nxt.append(hashlib.sha256((l + r).encode("utf-8")).hexdigest())
        leaves = nxt
    return leaves[0], count

# 2. High-Pressure Hydraulic Jet Worker (Parallel Core Bore)
def hydrodrill_jet(worker_id, total_workers, seed_prefix, target_zeros, stop_event, result_queue):
    nonce = worker_id
    step = total_workers
    prefix_bytes = seed_prefix.encode("utf-8")
    hashes_checked = 0

    while not stop_event.is_set():
        digest = hashlib.sha256(prefix_bytes + str(nonce).encode("utf-8")).hexdigest()
        hashes_checked += 1
        if digest.startswith(target_zeros):
            stop_event.set()
            result_queue.put({
                "jet_core": worker_id,
                "nonce": nonce,
                "genius_mint_hash": digest,
                "jet_hashes": hashes_checked
            })
            return
        nonce += step

def run_genius_hydrodrill(difficulty_zeros=4):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    merkle_root, file_count = compute_bedrock_merkle()

    # Chain from previous Genius Mint strike if one exists
    prev_mint = "0" * 64
    mint_index = 0
    if os.path.exists(GENIUS_LEDGER):
        with open(GENIUS_LEDGER, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            if lines:
                last_block = json.loads(lines[-1])
                prev_mint = last_block["genius_mint"]["genius_mint_hash"]
                mint_index = last_block["mint_index"] + 1

    cores = min(mp.cpu_count(), 8)
    target = "0" * difficulty_zeros
    seed_prefix = f"GENIUS_MINT|{DOMAIN}|IDX:{mint_index}|PREV:{prev_mint}|MERKLE:{merkle_root}|TS:{ts}|N:"

    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[36m   GENIUS MINT HYDRODRILL ENGINE // HIGH-PRESSURE FLUID BORE            \033[0m")
    print(f"\033[35m   ANCHOR: {DOMAIN} | MINT #{mint_index} | JETS: {cores} CORES | TARGET: {target}*\033[0m")
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[90m[*] Bedrock Merkle : {merkle_root} ({file_count} files)\033[0m")
    print(f"\033[90m[*] Prev Mint Hash : {prev_mint[:32]}...\033[0m")
    print(f"\033[33m[~] Pressurizing {cores} hydraulic jets... boring into bedrock...\033[0m")

    t0 = time.perf_counter()
    stop_event = mp.Event()
    result_queue = mp.Queue()
    workers = []

    for w in range(cores):
        p = mp.Process(
            target=hydrodrill_jet,
            args=(w, cores, seed_prefix, target, stop_event, result_queue)
        )
        p.start()
        workers.append(p)

    hit = result_queue.get()
    for p in workers:
        p.join()

    elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)
    est_total_hashes = hit["jet_hashes"] * cores
    hashrate_khs = round((est_total_hashes / max(elapsed_ms / 1000.0, 0.0001)) / 1000.0, 2)

    # Double-Wrapped SHA-512 Lattice Sponge Seal
    mint_record = {
        "mint_index": mint_index,
        "timestamp": ts,
        "organization": "ROBDOE.Inc.Charity",
        "domain": DOMAIN,
        "geographic_anchor": "Beverly Hills, New South Wales, Australia",
        "drilling_rig": {
            "method": "Hydrodrilling High-Pressure Multi-Jet Bore",
            "active_jets": cores,
            "difficulty_target": target,
            "elapsed_ms": elapsed_ms,
            "est_total_hashes": est_total_hashes,
            "pressure_rate_khs": hashrate_khs
        },
        "bedrock_merkle_root": merkle_root,
        "previous_mint_hash": prev_mint,
        "genius_mint": hit,
        "doctrine_invariant": "Ko te mana o te tangata, koia te pūtake."
    }

    raw_bytes = json.dumps(mint_record, sort_keys=True).encode("utf-8")
    sponge_seal = hashlib.sha512(hashlib.sha512(raw_bytes).digest()).hexdigest()
    mint_record["lattice_sha512_sponge_seal"] = sponge_seal

    # 1. Append to Genius Mint Hydrodrill Ledger
    with open(GENIUS_LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(mint_record) + "\n")

    # 2. Bridge Witness Entry into Solana & EVM Logs
    witness_line = (
        f"[{ts}] [GENIUS_MINT #{mint_index}] [HASH: {hit['genius_mint_hash']}] "
        f"[MERKLE: {merkle_root[:16]}...] [SPONGE: {sponge_seal[:24]}...]\n"
    )
    with open(EVM_WITNESS_LOG, "a", encoding="utf-8") as f:
        f.write(witness_line)

    if os.path.isfile(SOLANA_LEDGER):
        with open(SOLANA_LEDGER, "a", encoding="utf-8") as f:
            f.write(witness_line)

    print(f"\n\033[32m[+] GENIUS MINT STRIKE! (Jet Core #{hit['jet_core']} @ Nonce {hit['nonce']})\033[0m")
    print(f"\033[33m[+] Genius Hash    : {hit['genius_mint_hash']}\033[0m")
    print(f"\033[36m[+] Bore Speed     : {elapsed_ms} ms (~{hashrate_khs} kH/s across {cores} jets)\033[0m")
    print(f"\033[32m[+] Lattice Seal   : {sponge_seal[:32]}...\033[0m")
    print(f"\033[36m[+] Genius Ledger  : {GENIUS_LEDGER}\033[0m")
    print(f"\033[36m[+] Witness Sync   : external_witness_evm.log & solana_atmospheric_ledger\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    # Remove old genesis_hydrodrill_mint.py if present so the workspace stays clean
    old_script = os.path.join(REPO_DIR, "genesis_hydrodrill_mint.py")
    if os.path.exists(old_script):
        os.remove(old_script)
    run_genius_hydrodrill(difficulty_zeros=4)
