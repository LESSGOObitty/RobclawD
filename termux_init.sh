#!/bin/bash
# Total Termux Infrastructure Bootstrap

echo "[+] Updating repositories and upgrading packages..."
pkg update -y && pkg upgrade -y

echo "[+] Installing core development & cryptographic tools..."
pkg install -y git python jq openssl termux-api coreutils nano curl wget net-tools

echo "[+] Requesting storage access (grant permission on screen)..."
termux-setup-storage

echo "[+] Binding custom shell aliases in ~/.bashrc..."
cat << 'ALIAS_EOF' >> ~/.bashrc

# Sovereign Short Aliases
alias sov="cd ~/sovereign_core && ./sovereign.sh"
alias sovb="cd ~/sovereign_core && ./sovereign.sh bridge"
alias sovh="cd ~/sovereign_core && ./sovereign.sh hud"
alias sova="cd ~/sovereign_core && ./sovereign.sh backup"
alias prov="cd ~/.provmark && ls -la"
alias inv="jq -r '.invariant' ~/robdoe_telemetry.json 2>/dev/null"
ALIAS_EOF

source ~/.bashrc

echo "========================================================================"
echo " [✓] BOOTSTRAP COMPLETE"
echo " [!] Run: source ~/.bashrc"
echo " [!] Run: sovb (to bridge), sovh (for HUD), sova (to archive)"
echo "========================================================================"
