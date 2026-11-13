#!/usr/bin/env zsh
set -euo pipefail

echo "[*] Scanning top space consumers in $(pwd)..."
du -h -max-depth=1 2>/dev/null | sort -hr

echo "[*] Purging git reflog history and pruning loose objects..."
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo "[*] Cleaning npm/pip/cargo/cache debris..."
rm -rf ~/.npm/_cacache 2>/dev/null || true
rm -rf ~/.cargo/registry/cache 2>/dev/null || true
rm -rf ~/.local/share/Trash/* 2>/dev/null || true

echo "====================================================================="
echo " [CHECK] Updated Disk Status:"
df -h / | awk 'NR==1 || NR==2 {print "  " $0}'
echo "====================================================================="
