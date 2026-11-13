#!/data/data/com.termux/files/usr/bin/env zsh
# ==============================================================================
# ROBDOEAI-CORE // WORKSPACE FOLDER INSPECTOR
# ==============================================================================

set -euo pipefail

WORKSPACE="$HOME/master-lattice/RobDoeAI-Core"
cd "$WORKSPACE"

echo "=========================================================================="
echo " [AUDIT] ACTIVE DIRECTORIES & SUB-LATTICES"
echo "=========================================================================="
find . -maxdepth 3 -not -path '*/.*' -not -path './__pycache__*' | sort

echo "=========================================================================="
echo " [DISK USAGE & SUMMARY]"
echo "=========================================================================="
du -sh * 2>/dev/null || true
echo "=========================================================================="
