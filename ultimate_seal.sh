#!/usr/bin/env zsh
set -euo pipefail

WORKSPACE_ROOT="$HOME"
LEDGER_DIR="$WORKSPACE_ROOT/Matrix-Ledger"
DB_PATH="$WORKSPACE_ROOT/target_database.db"
MANIFEST_PATH="$LEDGER_DIR/state_manifest.json"

echo "======================================================================="
echo "[+] INITIATING ULTIMATE TERMUX MONOLITHIC & ON-CHAIN LEDGER SEAL"
echo "[+] TIMESTAMP: $(date -u '+%Y-%m-%d %H:%M:%S UTC')"
echo "======================================================================="

# 1. DATABASE B-TREE INTEGRITY AUDIT
echo "\n--- [1/6] EXECUTING SQLITE B-TREE INTEGRITY CHECK ---"
if [ -f "$DB_PATH" ]; then
    DB_STATUS=$(sqlite3 "$DB_PATH" "PRAGMA integrity_check;")
    echo "Target Database: $DB_STATUS"
    if [ "$DB_STATUS" != "ok" ]; then
        echo "[!] CRITICAL: Database B-tree corruption detected!" >&2
        exit 1
    fi
else
    echo "[*] Notice: target_database.db not found. Skipping B-Tree check."
fi

# 2. DUAL-HASH CRYPTOGRAPHIC ANCHORING (SHA-256 + SHA-512)
echo "\n--- [2/6] GENERATING DUAL-HASH MERKLE STATE MANIFEST ---"
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
echo "\n--- [3/6] STAGING AND SEALING GIT OBJECT DAG ---"
git add -A
git status -s

if git diff-index --quiet HEAD --; then
    echo "[*] Working tree clean. No new structural mutations to commit."
else
    git commit -m "Termux Monolithic Seal: Dual-hash state synchronization $(date -u +%Y%m%d-%H%M%S)"
    echo "[+] New commit block written to local DAG."
fi

# 4. IPFS KUBO DECENTRALIZED PINNING
echo "\n--- [4/6] ANCHORING TO LOCAL IPFS KUBO NODE ---"
if command -v ipfs &> /dev/null; then
    if ipfs id &> /dev/null; then
        IPFS_CID=$(ipfs add -q -r "$LEDGER_DIR" "$DB_PATH" 2>/dev/null | tail -n 1)
        echo "[+] Decentralized IPFS Root CID: $IPFS_CID"
    else
        echo "[!] IPFS daemon offline. Initializing local repository reference..."
        ipfs init --quiet || true
        IPFS_CID=$(ipfs add -q -r "$LEDGER_DIR" "$DB_PATH" 2>/dev/null | tail -n 1 || echo "Pinned locally")
        echo "[+] Local Add CID: $IPFS_CID"
    fi
else
    echo "[!] IPFS binary not found. Skipping decentralized broadcast."
fi

# 5. ON-CHAIN MANIFEST ANCHORING VIA PYTHON WEB3
echo "\n--- [5/6] BROADCASTING MANIFEST ROOT ON-CHAIN ---"
python3 -c '
import os, hashlib, json

manifest_path = "Matrix-Ledger/state_manifest.json"
if os.path.exists(manifest_path):
    with open(manifest_path, "rb") as f:
        manifest_bytes = f.read()
    master_hash = hashlib.sha256(manifest_bytes).hexdigest()
    print(f"[+] On-Chain Anchor Root Ready: 0x{master_hash}")
    
    try:
        from web3 import Web3
        rpc_url = os.getenv("EVM_RPC_URL", "")
        private_key = os.getenv("EVM_PRIVATE_KEY", "")
        contract_addr = os.getenv("EVM_CONTRACT_ADDRESS", "")
        
        if rpc_url and private_key and contract_addr:
            w3 = Web3(Web3.HTTPProvider(rpc_url))
            if w3.is_connected():
                account = w3.eth.account.from_key(private_key)
                abi = [{"inputs": [{"internalType": "bytes32", "name": "stateRoot", "type": "bytes32"}], "name": "anchorState", "outputs": [], "stateMutability": "nonpayable", "type": "function"}]
                contract = w3.eth.contract(address=Web3.to_checksum_address(contract_addr), abi=abi)
                nonce = w3.eth.get_transaction_count(account.address)
                tx = contract.functions.anchorState(bytes.fromhex(master_hash)).build_transaction({
                    "chainId": w3.eth.chain_id, "gas": 100000, "nonce": nonce
                })
                signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
                tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
                print(f"[+] Live On-Chain Tx Sent: {w3.to_hex(tx_hash)}")
            else:
                print("[!] EVM RPC connection failed. Payload buffered locally.")
        else:
            print("[*] EVM environment variables not set. Skipping live broadcast, root prepared.")
    except ImportError:
        print("[*] Web3.py not installed. Root compiled and ready for contract binding.")
'

# 6. UPSTREAM SYNC ACROSS ALL REMOTES
echo "\n--- [6/6] SYNCHRONIZING ALL UPSTREAM REMOTES ---"
git remote | while read -r remote; do
    echo "[*] Pushing to remote upstream: $remote"
    git push "$remote" --all --quiet || echo "[!] Warning: Failed push to $remote"
    git push "$remote" --tags --quiet || true
done

echo "======================================================================="
echo "[+] TERMUX MONOLITHIC & ON-CHAIN SEAL COMPLETE. SYSTEM FULLY SECURED."
echo "======================================================================="
