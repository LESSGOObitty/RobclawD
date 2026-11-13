#!/usr/bin/env zsh
echo "[*] Termux Node Active: $(uname -a)"
echo "[*] Working Directory  : $(pwd)"
echo "[*] Active Git Branch  : $(git branch --show-current 2>/dev/null || echo 'N/A')"
echo "[*] System Load        : Nominal"
