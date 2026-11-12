#!/bin/zsh

echo "[*] Current system time (Default):"
date

echo "[+] Forcing session time-lock to CST (America/Chicago)..."
export TZ='America/Chicago'

echo "[*] Verified CST time-lock:"
date
echo "[*] UTC Reference:"
date -u +"%Y-%m-%dT%H:%M:%SZ"
