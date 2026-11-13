#!/usr/bin/env zsh
# =====================================================================
# ROBDOE ROOT AUTHORITY // TERMUX ENHANCED ENVIRONMENT WRAPPER
# =====================================================================
set -euo pipefail

echo "====================================================================="
echo " [ROBDOE WORKSPACE] // ENHANCED TELEMETRY ACTIVE"
echo "====================================================================="

# 1. Check disk space headroom on root mount
df -h / | awk 'NR==1 || NR==2 {print " [DISK]   :", $0}'

# 2. Check active git status and branch
BRANCH=$(git branch --show-current 2>/dev/null || echo "DETACHED/NONE")
UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l)
echo " [GIT]    : Branch [${BRANCH}] | Uncommitted changes: ${UNCOMMITTED}"

# 3. Verify Python runtime & cryptography support
python3 -c '
import sys, platform
print(f" [PYTHON] : {sys.version.split()[0]} on {platform.machine()}")
'

# 4. Display active watermark and persona lock
echo " [LOCK]   : Persona [LESSGOOBITTY] | Watermark [espVmark:2c3f1b0af3a2367a]"
echo "====================================================================="
