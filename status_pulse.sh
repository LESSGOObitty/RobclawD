#!/usr/bin/env zsh
echo "[*] System Pulse Check..."
echo "[+] User        : $(git config --global user.name)"
echo "[+] Email       : $(git config --global user.email)"
echo "[+] SSH Key     : $(ls -la ~/.ssh/id_ed25519_lessgoobitty 2>/dev/null || echo 'Missing')"
echo "[+] Active Repos: $(find . -maxdepth 2 -name '.git' | wc -l)"
echo "[+] Terminal    : Termux // Zsh (Nominal)"
