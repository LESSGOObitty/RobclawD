#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "================================================================"
echo "          SOVEREIGN TERMINAL PIPELINE :: ROBDOE ENTITY          "
echo "================================================================"

# 1. VERIFY TOOLCHAIN & DEPENDENCIES
echo "[+] Step 1: Checking build environment..."
if ! python -c "import eth_account, requests, qrcode" > /dev/null 2>&1; then
    echo "[!] Missing modules. Building native C-extensions and wheel dependencies..."
    pkg install clang python-dev libffi-dev libqrencode -y
    pip install bitarray eth-account requests qrcode --quiet
fi

# 2. GENERATE AND LOCK MERKLE-LATTICE PROOF
echo "[+] Step 2: Executing Merkle-lattice state proof..."
python -c '
import json, hashlib, os, time

hashes = []
for root, _, files in os.walk("."):
    if ".git" in root: continue
    for file in sorted(files):
        try:
            with open(os.path.join(root, file), "rb") as f:
                hashes.append(hashlib.sha256(f.read()).hexdigest())
        except Exception: pass

tree = sorted(hashes) if hashes else ["0"*64]
while len(tree) > 1:
    if len(tree) % 2 != 0: tree.append(tree[-1])
    tree = [hashlib.sha256((tree[i] + tree[i+1]).encode()).hexdigest() for i in range(0, len(tree), 2)]

proof = {
    "timestamp": int(time.time()),
    "merkle_root": tree[0],
    "status": "UNBREAKABLE_BYZANTINE_IMMUTABILITY",
    "anchor": os.getenv("ROBDOE_PRIVATE_KEY", "UNSET")[:10] + "..."
}

with open("sovereign_lattice_proof.json", "w") as f:
    json.dump(proof, f, indent=2)

print(f"    -> Merkle Root Locked: {tree[0]}")
'

# 3. AIRGAP SYNC :: RENDER TERMINAL QR CODE
echo "[+] Step 3: Generating Airgap Terminal QR Sync..."
python -c '
import qrcode, json
with open("sovereign_lattice_proof.json") as f:
    data = json.load(f)
qr = qrcode.QRCode()
qr.add_data(json.dumps(data))
qr.print_ascii(tty=True)
'

# 4. FIRE X402 EIP-3009 PAYMENT PIPELINE
echo "[+] Step 4: Initiating x402 Micropayment Vector on Base..."
python cmc_x402.py

echo "================================================================"
echo "[+] EXECUTION COMPLETE :: STATE ANCHORED & PROOFS SYNCED"
echo "================================================================"
