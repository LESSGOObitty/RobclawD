#!/data/data/com.termux/files/usr/bin/env zsh
# ==============================================================================
# ROBDOEAI-CORE // GIT IGNORE & REPOSITORY HYGIENE UTILITY
# ==============================================================================
# Target:   Termux // Exclude IPFS daemon files and cache noise from git status
# Identity: root@robdoe.com // 1 of 1 Sovereign Monolith
# ==============================================================================

set -euo pipefail
setopt +o nomatch 2>/dev/null || true

echo "[*] Configuring .gitignore to isolate sovereign core assets..."

cat << 'GITIGNORE' > .gitignore
# IPFS Daemon & Local State Noise
.ipfs/
.git-credentials
.termux_authinfo
.lattice_entropy_state

# Runtime Logs & Temp Scripts
live_broadcast_engine.py
run_sovereign_lattice.py
thermal_check.py
witness_and_hubs_seal.py

# Submodules & Workspace Caches
Matrix/
Matrix-Ledger/
master-lattice/
robdoerootauthority/
LESSGOObitty-Root
GITIGNORE

git add .gitignore
git commit -m "chore(git): update .gitignore to seal core repository noise [1 of 1]" || echo "[*] .gitignore already staged."

echo "[+] Repository telemetry sanitized and ready."
