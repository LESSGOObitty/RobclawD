#!/usr/bin/env bash
set +H

echo "====================================================================="
echo "     [ROBDOE.TERMUX] MERKLE DAG METRICS SWEEP                        "
echo "====================================================================="

TARGET_DIR="${1:-$HOME/robdoerootauthority}"
if [ -d "$TARGET_DIR/.git" ]; then
    cd "$TARGET_DIR"
    echo "[*] Target Git Repository : $(pwd)"
    echo ""
    
    echo "--- [GIT OBJECT STORE SIZE] ---"
    du -sh .git/objects
    echo ""
    
    echo "--- [TOTAL COMMITS & MERKLE SEALS] ---"
    git rev-list --all --count 2>/dev/null || echo "Count unavailable"
    echo ""
    
    echo "--- [LATEST SIGNED TAGS / ROOT SEALS] ---"
    git tag -l | tail -n 10
    echo ""
    
    echo "--- [LOOSE OBJECT COUNT & PACK FILES] ---"
    echo "Loose objects : $(find .git/objects -type f | wc -l)"
    echo "Pack files    : $(ls .git/objects/pack/*.pack 2>/dev/null | wc -l)"
else
    echo "[-] No Git/Merkle repository found at $TARGET_DIR"
    echo "[*] Checking overall home directory storage..."
    du -sh ~
fi

echo "====================================================================="
echo " [STATUS] DAG inspection complete."
echo "====================================================================="
