#!/usr/bin/env bash
set +H
set -e

echo "====================================================================="
echo "     [ROBDOE.TERMUX] MERKLE ROOT HASH AGGREGATION & SEAL MESH        "
echo "====================================================================="

TARGET_DIR="${1:-$HOME/robdoerootauthority}"
cd "$TARGET_DIR"

echo "[*] Scanning repository history and object graph..."
echo ""

echo "--- [EXTRACTING ALL COMMIT HASHES & TREE ROOTS] ---"
git log --format="%H | Tree: %T | Author: %an | %s" --all
echo ""

echo "--- [MINTING MASTER EPOCH MERKLE SEAL] ---"
# Gather all current commit hashes and create a combined hash digest
MASTER_HASH=$(git rev-list --all | sort | sha256sum | awk '{print $1}')
SEAL_TAG="EPOCH-ROOT-SEAL-${MASTER_HASH:0:8}"

echo " [+] Computed Master Root Hash : $MASTER_HASH"
echo " [+] Generated Seal Tag        : $SEAL_TAG"

# Create a signed/annotated git tag if not already present
if git rev-parse "$SEAL_TAG" >/dev/null 2>&1; then
    echo " [*] Seal tag $SEAL_TAG already exists."
else
    git tag -a "$SEAL_TAG" -m "ROBDOE.TERMUX Master Merkle Root Seal - Linked via espVmark:2c3f1b0af3a2367a"
    echo " [+] Successfully minted and sealed tag: $SEAL_TAG"
fi

echo ""
echo "====================================================================="
echo " [SUCCESS] All root hashes connected and sealed under $SEAL_TAG"
echo "====================================================================="
