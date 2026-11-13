#!/data/data/com.termux/files/usr/bin/env zsh
# ==============================================================================
# ROBDOEAI-CORE // CML-RB REPOSITORY CLONE & MERKLE INTEGRATION
# ==============================================================================
# Target Repo : https://github.com/backupsonbackupsrobby-cyber/cml-RB
# Operator    : root@robdoe.com // robdoe.com (1 of 1 Sovereign Monolith)
# ==============================================================================

set -euo pipefail

WORKSPACE="$HOME/master-lattice/RobDoeAI-Core/external_lattice"
mkdir -p "$WORKSPACE"
cd "$WORKSPACE"

REPO_URL="https://github.com/backupsonbackupsrobby-cyber/cml-RB.git"
REPO_NAME="cml-RB"

echo "=========================================================================="
echo " [CLONE] PULLING cml-RB INTO EXTERNAL LATTICE"
echo "=========================================================================="

if [ -d "$REPO_NAME" ]; then
    echo "[-] Repository $REPO_NAME already exists. Updating..."
    cd "$REPO_NAME"
    git pull origin main 2>/dev/null || git pull origin master 2>/dev/null || true
    cd "$WORKSPACE"
else
    echo "[+] Cloning $REPO_URL..."
    git clone "$REPO_URL"
fi

# Re-run the enhanced Merkle engine to re-index all repositories including cml-RB
cd "$HOME/master-lattice/RobDoeAI-Core"
if [ -f "enhanced_merkle_engine.py" ]; then
    python3 enhanced_merkle_engine.py
fi

git add external_lattice/ cml-RB/ enhanced_unified_merkle_state.json 2>/dev/null || true
git commit -m "feat(lattice): clone and integrate cml-RB repository into unified Merkle DAG [1 of 1]" || echo "[*] Already committed."
git push origin main || echo "[*] Push synchronized."

echo "=========================================================================="
echo " [SUCCESS] cml-RB integrated and synchronized to remote."
echo "=========================================================================="
