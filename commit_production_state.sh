#!/data/data/com.termux/files/usr/bin/env zsh
# ==============================================================================
# ROBDOEAI-CORE // PRODUCTION COMMIT & HYGIENE UTILITY
# ==============================================================================
# Identity: root@robdoe.com // 1 of 1 Sovereign Monolith
# ==============================================================================

set -euo pipefail
setopt +o nomatch 2>/dev/null || true

echo "[*] Ensuring critical scripts and workspace manifests are tracked..."
git add workspace/scripts/ workspace/manifests/ verify_lattice_fsck.sh clean_and_lock_git.sh 2>/dev/null || true

echo "[*] Committing sovereign production state for robdoe.inc-charity..."
git commit -m "prod(core): commit verified workspace scripts, telemetry engines, and charity funding alignment [1 of 1]" || echo "[*] Changes already committed or clean."

echo "[+] Ready for push."
