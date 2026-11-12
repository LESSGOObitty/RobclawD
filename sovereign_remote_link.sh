#!/bin/bash
# ======================================================================
# CROSS-NETWORK SOVEREIGN TUNNEL LINK
# ======================================================================

echo "[+] Initializing cross-region secure tunnel bridge..."

# Check if Tailscale or SSH client tools are present
if ! command -v ssh &> /dev/null; then
    pkg install -y openssh
fi

echo "========================================================================"
echo " [READY] To link your QLD Termux node directly to your machine:"
echo " 1. Run 'sshd' in Termux to open port 8022."
echo " 2. Connect via your secure tunnel or mesh IP address:"
echo "    ssh -p 8022 $(whoami)@<your-node-mesh-ip>"
echo "========================================================================"
