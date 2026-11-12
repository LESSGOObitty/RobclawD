#!/bin/bash
# Reconnecting tunnel helper for dynamic IP environments

target_host="$1"
target_user="${2:-RobDoe}"

if [ -z "$target_host" ]; then
    echo "Usage: ./tunnel_to_pc.sh <TARGET_IP_OR_HOSTNAME> [USER]"
    exit 1
fi

echo "[+] Establishing persistent connection loop to $target_host..."

while true; do
    echo "[•] Connecting to Windows PowerShell host ($target_host)..."
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 "${target_user}@${target_host}" "powershell.exe"
    
    echo "[!] Connection dropped or shifted IP. Reconnecting in 5 seconds..."
    sleep 5
done
