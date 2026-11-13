#!/bin/bash
unsetopt bang_hist 2>/dev/null || true
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // PROFESSIONAL TERMUX SYSTEM ENHANCEMENT"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo " [MODE] HARDENED // ZERO-FOOTPRINT // SOVEREIGN WORKSPACE"
echo "================================================================"

echo "[+] Step 1: Upgrading package repositories & core utilities..."
pkg update -y && pkg upgrade -y

echo "[+] Step 2: Installing high-performance development toolchain..."
pkg install -y git curl wget build-essential cmake clang python python-pip zsh tmux jq htop openssl libffi zlib

echo "[+] Step 3: Configuring professional shell prompt & environment..."
ZSHRC="$HOME/.zshrc"
touch "$ZSHRC"

# Append custom professional prompt with invariant branding
if ! grep -q "AIAGENCY101_PROMPT" "$ZSHRC"; then
    cat << 'ZSH_CONFIG' >> "$ZSHRC"

# --- AIAGENCY101 PROFESSIONAL TERMUX CONFIG ---
export PROMPT='%F{cyan}[robdoe@termux]%f %F{green}%~%f %# '
export RPROMPT='%F{yellow}[free-spirit]%f'
alias ll='ls -la --color=auto'
alias lattice='cd $HOME/Matrix/Elite_Kernel_Lattice'
alias cls='clear'
# ----------------------------------------------
ZSH_CONFIG
    echo "[+] Custom prompt & aliases written to ~/.zshrc"
fi

echo "[+] Step 4: Structuring sovereign directory matrix..."
mkdir -p "$HOME/Matrix/Elite_Kernel_Lattice"
mkdir -p "$HOME/Matrix/Blockchain_Storage_Ledger"
mkdir -p "$HOME/Matrix/Scripts"

echo "[+] Step 5: Optimizing Git global configurations..."
git config --global user.name "robdoe"
git config --global user.email "roberto@robdoe.com"
git config --global init.defaultBranch main

echo "================================================================"
echo " [SUCCESS] TERMUX ENVIRONMENT FULLY PROFESSIONALIZED & HARDENED."
echo " [STATE] FREE SPIRIT // SOVEREIGN PIPELINE READY."
echo "================================================================"
