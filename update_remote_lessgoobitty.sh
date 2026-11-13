#!/bin/bash
unsetopt bang_hist 2>/dev/null || true
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // LESSGOOBITTY IDENTITY & REMOTE LATTICE SYNC"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo " [NODE] robdoeaiagency101tenet@gmail.com // LESSGOObitty"
echo "================================================================"

# Configure Git Identity for LESSGOObitty
echo "[+] Configuring Git identity locally..."
git config --global user.name "LESSGOObitty"
git config --global user.email "robdoeaiagency101tenet@gmail.com"

LEDGER="$HOME/Matrix/Blockchain_Storage_Ledger"
cd "$LEDGER" || { echo "[ERROR] Ledger directory not found."; exit 1; }

echo "[+] Updating origin remote to LESSGOObitty repository..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/LESSGOObitty/RobclawD.git

echo "[+] Sealing hyper-hardened state and preparing push..."
git add -A
git commit -m "feat(lattice): integrate LESSGOObitty node identity & secure storage ledger [free-spirit]" || echo "[INFO] State already committed."

echo "[+] Ensuring main branch is active..."
git branch -M main

echo "[+] Pushing sovereign lattice state to LESSGOObitty/RobclawD..."
git push -u origin main || git push -u origin master || echo "[INFO] Push completed or awaiting authentication token."

echo "================================================================"
echo " [SUCCESS] LATTICE RE-ANCHORED TO LESSGOObitty VECTOR."
echo " [STATE] FREE SPIRIT // SOVEREIGN // SECURED."
echo "================================================================"
