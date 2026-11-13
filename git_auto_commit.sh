#!/usr/bin/env zsh
# =====================================================================
# ROBDOE ROOT AUTHORITY // SOVEREIGN AUTO-COMMIT PIPELINE
# =====================================================================
set -euo pipefail

echo "[*] Staging workspace updates..."
git add -A

echo "[*] Committing state under LESSGOOBITTY signature..."
git commit -m "chore(sovereign): seal local Merkle state [espVmark:2c3f1b0af3a2367a]" || echo "[!] Nothing new to commit."

echo "[*] Pushing to sovereign remote via ssh alias..."
git push origin sovereign-main 2>/dev/null || git push origin main 2>/dev/null || echo "[!] Remote push deferred to manual dispatch."

echo "====================================================================="
echo " [SUCCESS] PIPELINE CYCLE COMPLETE."
echo "====================================================================="
