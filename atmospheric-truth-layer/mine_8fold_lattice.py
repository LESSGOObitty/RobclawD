#!/usr/bin/env python3
import os
import json
import time
import socket
import hashlib
import subprocess
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
os.makedirs(LOG_DIR, exist_ok=True)

ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
slug = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

# 1. Fast Single-Pass SHA-256 Merkle DAG over atmospheric-truth-layer
leaf_hashes = []
indexed_files = []

for root, dirs, files in os.walk(REPO_DIR):
    # Skip .git and SovereignLedgerLogs to keep it instant and deterministic
    dirs[:] = [d for d in dirs if d not in (".git", "SovereignLedgerLogs", "__pycache__")]
    for fname in sorted(files):
        fpath = os.path.join(root, fname)
        try:
            h = hashlib.sha256()
            with open(fpath, "rb") as f:
                while chunk := f.read(65536):
                    h.update(chunk)
            digest = h.hexdigest()
            rel_path = os.path.relpath(fpath, REPO_DIR)
            leaf_hashes.append(digest)
            indexed_files.append({"file": rel_path, "sha256": digest})
        except OSError:
            continue

if leaf_hashes:
    layer = list(leaf_hashes)
    while len(layer) > 1:
        next_layer = []
        for i in range(0, len(layer), 2):
            left = layer[i]
            right = layer[i + 1] if (i + 1) < len(layer) else left
            next_layer.append(hashlib.sha256((left + right).encode("utf-8")).hexdigest())
        layer = next_layer
    merkle_root = layer[0]
else:
    merkle_root = "0" * 64

# 2. Instant 8-Fold Proof-of-Work Mining (In-Memory SHA-256)
t0 = time.perf_counter()
folds = []
for fold_idx in range(1, 9):
    nonce = 0
    prefix = f"{merkle_root}:{fold_idx}:{ts}:".encode("utf-8")
    while True:
        digest = hashlib.sha256(prefix + str(nonce).encode("utf-8")).hexdigest()
        if digest.startswith("000"):  # 3-hex-zero difficulty mined in <2ms in Python
            folds.append({"fold": fold_idx, "nonce": nonce, "hash": digest})
            break
        nonce += 1
mine_ms = round((time.perf_counter() - t0) * 1000, 2)

# 3. Git Head & Local Telemetry Check
try:
    git_head = subprocess.check_output(
        ["git", "-C", REPO_DIR, "rev-parse", "--short", "HEAD"],
        stderr=subprocess.DEVNULL
    ).decode().strip()
except Exception:
    git_head = "UNCOMMITTED_WORKING_TREE"

# 4. Assemble Manifest & Double-Wrapped SHA-512 Sponge Seal
manifest = {
    "timestamp": ts,
    "organization": "ROBDOE.Inc.Charity",
    "domain": DOMAIN,
    "geographic_anchor": "Beverly Hills, New South Wales, Australia",
    "workspace": REPO_DIR,
    "git_head": git_head,
    "merkle_dag": {
        "file_count": len(indexed_files),
        "merkle_root_sha256": merkle_root,
        "leaves": indexed_files
    },
    "mining_8fold": {
        "elapsed_ms": mine_ms,
        "difficulty": "000",
        "folds": folds
    },
    "doctrine": {
        "framework": "72 Systematic Economy Lymph Node QiDue Doctrine",
        "compliance": "AU & PND Honored // Uncompromised Tikanga",
        "movement": "Emu & Kangaroo Forward-Only Vector"
    }
}

raw_json = json.dumps(manifest, sort_keys=True).encode("utf-8")
pass1 = hashlib.sha512(raw_json).digest()
sponge_seal = hashlib.sha512(pass1).hexdigest()
manifest["lattice_sha512_sponge_seal"] = sponge_seal

manifest_path = os.path.join(LOG_DIR, f"Termux_8Fold_Manifest_{slug}.json")
audit_path = os.path.join(LOG_DIR, "Termux_8Fold_Audit.log")

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

with open(audit_path, "a", encoding="utf-8") as f:
    f.write(f"[{ts}] [DOMAIN: {DOMAIN}] [GIT: {git_head}] [MERKLE: {merkle_root}] [8FOLD_MS: {mine_ms}ms] [SEAL: {sponge_seal}]\n")

print(f"\033[35m========================================================================\033[0m")
print(f"\033[32m[+] 8-FOLD MINING & MERKLE DAG COMPLETE IN {mine_ms} ms\033[0m")
print(f"\033[36m[+] Files Indexed : {len(indexed_files)} (git:{git_head})\033[0m")
print(f"\033[33m[+] Merkle Root   : {merkle_root}\033[0m")
print(f"\033[32m[+] Lattice Seal  : {sponge_seal[:32]}...\033[0m")
print(f"\033[36m[+] Manifest      : {manifest_path}\033[0m")
print(f"\033[35m========================================================================\033[0m")
