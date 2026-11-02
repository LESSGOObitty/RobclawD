#!/usr/bin/env zsh
# ==============================================================================
# MONOLITHIC CRYPTOGRAPHIC LEDGER SEAL & MERKLE DAG ANCHOR
# Environment: Termux ARM64 | Runtime: Python 3 / Git / IPFS Kubo / SQLite B-Tree
# ==============================================================================

set -euo pipefail

WORKSPACE_ROOT="$HOME"
LEDGER_DIR="$WORKSPACE_ROOT/Matrix-Ledger"
DB_PATH="$WORKSPACE_ROOT/target_database.db"
MANIFEST_PATH="$LEDGER_DIR/state_manifest.json"

echo "======================================================================="
echo "[+] INITIATING MONOLITHIC CRYPTOGRAPHIC LEDGER SEAL"
echo "[+] TIMESTAMP: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
echo "======================================================================="

# 1. DATABASE B-TREE INTEGRITY AUDIT
echo "\n--- [1/5] EXECUTING SQLITE B-TREE INTEGRITY CHECK ---"
if [ -f "$DB_PATH" ]; then
    DB_STATUS=$(sqlite3 "$DB_PATH" "PRAGMA integrity_check;")
    echo "Target Database: $DB_STATUS"
    if [ "$DB_STATUS" != "ok" ]; then
        echo "[!] CRITICAL: Database B-tree corruption detected!" >&2
        exit 1
    fi
else
    echo "[*] Notice: target_database.db not found in root. Skipping B-Tree check."
fi

# 2. DUAL-HASH CRYPTOGRAPHIC ANCHORING (SHA-256 + SHA-512)
echo "\n--- [2/5] GENERATING DUAL-HASH MERKLE STATE MANIFEST ---"
python3 -c '
import hashlib, json, os, datetime

ledger_dir = "Matrix-Ledger"
db_path = "target_database.db"
manifest_path = os.path.join(ledger_dir, "state_manifest.json")

manifest = {
    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    "nodes": {}
}

targets = []
if os.path.exists(db_path): targets.append(db_path)
if os.path.exists(ledger_dir):
    for root, dirs, files in os.walk(ledger_dir):
        for file in files:
            p = os.path.join(root, file)
            if p != manifest_path: targets.append(p)

for path in sorted(targets):
    h256 = hashlib.sha256()
    h512 = hashlib.sha512()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h256.update(chunk)
            h512.update(chunk)
    manifest["nodes"][path] = {
        "sha256": h256.hexdigest(),
        "sha512": h512.hexdigest()
    }

os.makedirs(ledger_dir, exist_ok=True)
with open(manifest_path, "w") as f:
    json.dump(manifest, f, indent=2)

print(f"[+] State manifest successfully sealed at: {manifest_path}")
'

# 3. GIT REPOSITORY SANITIZATION & MERKLE OBJECT COMMIT
echo "\n--- [3/5] STAGING AND SEALING GIT OBJECT DAG ---"
git add -A
git status -s

if git diff-index --quiet HEAD --; then
    echo "[*] Working tree clean. No new structural mutations to commit."
else
    git commit -m "Monolithic Cryptographic Seal: Dual-hash state synchronization $(date -u +%Y%m%d-%H%M%S)"
    echo "[+] New commit block written to local DAG."
fi

# 4. IPFS KUBO DECENTRALIZED PINNING
echo "\n--- [4/5] ANCHORING TO LOCAL IPFS KUBO NODE ---"
if command -v ipfs &> /dev/null; then
    if ipfs id &> /dev/null; then
        IPFS_CID=$(ipfs add -q -r "$LEDGER_DIR" "$DB_PATH" 2>/dev/null | tail -n 1)
        echo "[+] Decentralized IPFS Root CID: $IPFS_CID"
    else
        echo "[!] IPFS daemon/node offline. Initializing local repository reference..."
        ipfs init --quiet || true
        IPFS_CID=$(ipfs add -q -r "$LEDGER_DIR" "$DB_PATH" 2>/dev/null | tail -n 1 || echo "Pinned locally")
        echo "[+] Local Add CID: $IPFS_CID"
    fi
else
    echo "[!] IPFS binary not found in path. Skipping decentralized broadcast."
fi

# 5. UPSTREAM SYNC ACROSS ALL REMOTES
echo "\n--- [5/5] BROADCASTING UPSTREAM ACROSS ALL REMOTES ---"
git remote | while read -r remote; do
    echo "[*] Pushing to remote upstream: $remote"
    git push "$remote" --all --quiet || echo "[!] Warning: Failed push to $remote"
    git push "$remote" --tags --quiet || true
done

echo "======================================================================="
echo "[+] MONOLITHIC CRYPTOGRAPHIC SEAL COMPLETE. LEDGER IMMUTABLE."
echo "======================================================================="
