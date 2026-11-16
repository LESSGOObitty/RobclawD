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
EVM_WITNESS_LOG = os.path.join(REPO_DIR, "external_witness_evm.log")
SOLANA_LEDGER = os.path.join(REPO_DIR, "solana_atmospheric_ledger")
os.makedirs(LOG_DIR, exist_ok=True)

def qi_breathe_pulse(phase_name, seconds=0.3):
    """Simulates Qigong rhythmic breath timing before hydraulic engagement."""
    print(f"\033[36m[*] [QIGONG BREATH] {phase_name} ... circulating Qi through 72 lymph nodes\033[0m")
    time.sleep(seconds)

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

def hydrodrill_fa_jin_jet(worker_id, total_workers, seed_prefix, target_zeros, stop_event, result_queue):
    """Tai Chi / Wushu Fa Jin harmonic fluid jet worker."""
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
                "fa_jin_core": worker_id,
                "nonce": nonce,
                "genius_mint_hash": digest,
                "jet_hashes": hashes_checked
            })
            return
        nonce += step

def run_wushu_hydrodrill(difficulty_zeros=4):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    # 1. Internal Energetic Alignment (Qigong, Reiki, Tai Chi)
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   GENIUS HYDRODRILL :: WUSHU QIGONG & REIKI HARMONIC RIG v1.0          \033[0m")
    print(f"\033[35m   ANCHOR: {DOMAIN} // 72-Layer QiDue Doctrine + Fa Jin Strike          \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    qi_breathe_pulse("Inhale Deep (Gathering Universal Reiki Frequency)", 0.2)
    qi_breathe_pulse("Hold & Align (Tai Chi Yin-Yang Structural Balance)", 0.2)
    qi_breathe_pulse("Exhale & Ground (Rooting Stance into ARM64 Bedrock)", 0.2)

    merkle_root, file_count = compute_bedrock_merkle()

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
    
    # Infuse Reiki universal healing frequency & Wushu posture into the seed prefix
    seed_prefix = f"REIKI_QIGONG_FA_JIN|{DOMAIN}|IDX:{mint_index}|PREV:{prev_mint}|MERKLE:{merkle_root}|TS:{ts}|N:"

    print(f"\n\033[33m[~] Pressurizing {cores} Wushu Fa Jin fluid jets... striking bedrock...\033[0m")

    t0 = time.perf_counter()
    stop_event = mp.Event()
    result_queue = mp.Queue()
    workers = []

    for w in range(cores):
        p = mp.Process(
            target=hydrodrill_fa_jin_jet,
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

    # Compile Mint Record with Energetic Attunement Metadata
    mint_record = {
        "mint_index": mint_index,
        "timestamp": ts,
        "organization": "ROBDOE.Inc.Charity",
        "domain": DOMAIN,
        "energetic_discipline": {
            "qigong_breath": "Harmonized",
            "taichi_balance": "Yin-Yang Equilibrium",
            "reiki_frequency": "Universal Life-Force Attuned",
            "wushu_strike": "Fa Jin (發勁) Instantaneous Release"
        },
        "drilling_rig": {
            "method": "Wushu Qigong Hydrodrill High-Pressure Fa Jin Bore",
            "active_jets": cores,
            "difficulty_target": target,
            "elapsed_ms": elapsed_ms,
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

    with open(GENIUS_LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(mint_record) + "\n")

    witness_line = (
        f"[{ts}] [FA_JIN_GENIUS_MINT #{mint_index}] [HASH: {hit['genius_mint_hash']}] "
        f"[MERKLE: {merkle_root[:16]}...] [SPONGE: {sponge_seal[:24]}...]\n"
    )
    with open(EVM_WITNESS_LOG, "a", encoding="utf-8") as f:
        f.write(witness_line)

    if os.path.isfile(SOLANA_LEDGER):
        with open(SOLANA_LEDGER, "a", encoding="utf-8") as f:
            f.write(witness_line)

    print(f"\n\033[32m[+] FA JIN STRIKE ACHIEVED! (Core #{hit['fa_jin_core']} @ Nonce {hit['nonce']})\033[0m")
    print(f"\033[33m[+] Genius Hash    : {hit['genius_mint_hash']}\033[0m")
    print(f"\033[36m[+] Energy Flow    : {elapsed_ms} ms (~{hashrate_khs} kH/s across {cores} Qi channels)\033[0m")
    print(f"\033[32m[+] Lattice Seal   : {sponge_seal[:32]}...\033[0m")
    print(f"\033[36m[+] Ledger & Sync  : genius_mint_hydrodrill_ledger.jsonl (Witnessed)\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    run_wushu_hydrodrill(difficulty_zeros=4)
