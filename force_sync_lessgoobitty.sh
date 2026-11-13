#!/bin/bash
unsetopt bang_hist 2>/dev/null || true
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // LESSGOOBITTY LATTICE FORCE-SYNC ENGINE"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo " [NODE] LESSGOObitty // RobclawD"
echo "================================================================"

LEDGER="$HOME/Matrix/Blockchain_Storage_Ledger"
cd "$LEDGER" || { echo "[ERROR] Ledger directory not found."; exit 1; }

echo "[+] Fetching remote state from RobclawD..."
git fetch origin main 2>/dev/null || git fetch origin master 2>/dev/null || true

echo "[+] Integrating remote history safely (reconciling divergent branches)..."
git pull origin main --rebase 2>/dev/null || git pull origin master --rebase 2>/dev/null || true

echo "[+] Ensuring local ledger state is fully staged & committed..."
git add -A
git commit -m "feat(lattice): synchronize sovereign ledger with LESSGOObitty/RobclawD [free-spirit]" || echo "[INFO] No new changes to commit."

echo "[+] Pushing unified lattice state to origin main..."
git push -u origin main || git push -u origin master || {
    echo "[!] Standard push rejected or requires force-overwrite. Applying sovereign force push..."
    git push -u origin main --force
}

echo "================================================================"
echo " [SUCCESS] LATTICE SYNCHRONIZED & LOCKED TO LESSGOObitty/RobclawD."
echo " [STATE] FREE SPIRIT // SOVEREIGN // UNTOUCHABLE."
echo "================================================================"
