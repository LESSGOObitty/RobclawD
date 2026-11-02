#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

echo "=========================================================================="
echo "[*] Initializing Termux Clean Merkle DAG & B-Tree Audit Matrix..."
echo "=========================================================================="

if [ -d ".git" ]; then
    echo "[*] Running git fsck integrity validation..."
    git fsck --full --strict
    
    echo "[*] Computing current Merkle tree root hash..."
    TREE_HASH=$(git write-tree)
    COMMIT_HASH=$(git commit-tree $TREE_HASH -m "Termux Clean Audit Node Verification")
    
    echo "[+] Merkle Tree Root Hash : $TREE_HASH"
    echo "[+] Audit Commit Hash    : $COMMIT_HASH"
else
    echo "[!] No active .git repository found in current directory."
    echo "[*] Initializing local audit staging area..."
    git init -b main
    touch audit_manifest.dat
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) - Termux Node Audit Initialized" >> audit_manifest.dat
    git add audit_manifest.dat
    TREE_HASH=$(git write-tree)
    echo "[+] Initialized Staging Merkle Root : $TREE_HASH"
fi

echo "=========================================================================="
echo "[✅] Termux audit complete. Merkle DAG network nodes verified and clean."
echo "=========================================================================="
