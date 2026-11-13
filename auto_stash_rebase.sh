#!/data/data/com.termux/files/usr/bin/env zsh
# ==============================================================================
# ROBDOEAI-CORE // UNSTAGED CHANGES STASH, REBASE & SYNC
# ==============================================================================
# Operator : root@robdoe.com // robdoe.com (1 of 1 Sovereign Monolith)
# ==============================================================================

set -euo pipefail

WORKSPACE="$HOME/master-lattice/RobDoeAI-Core"
cd "$WORKSPACE"

echo "=============================================================================="
echo " [STASH RECOVERY] STASHING LOCAL ARTIFACTS, REBASING & POPPING"
echo "=============================================================================="

git stash || echo "[*] Nothing to stash."
git pull --rebase origin main
git stash pop || echo "[*] No stash to pop."

git add .
git commit -m "feat(core): auto-stash, rebase, and reconcile remote divergence [1 of 1]" || echo "[*] Already committed."
git push origin main

cat << 'PYEOF' > stash_recovery_state.py
import json
import time

state = {
    "system": "RobDoeAI-Core // Stash Rebase Reconciliation",
    "operator": "root@robdoe.com",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "status": "STASH_REBASE_PUSH_COMPLETE"
}

with open("stash_recovery_state.json", "w") as f:
    json.dump(state, f, indent=2)

print(" [+] Stash recovery state recorded.")
PYEOF

python3 stash_recovery_state.py
git add stash_recovery_state.json
git commit -m "feat(core): log stash recovery state verification [1 of 1]" || echo "[*] Already committed."
git push origin main
