#!/bin/bash
# Setup Termux SSH Daemon

echo "[+] Installing OpenSSH..."
pkg install -y openssh

echo "[+] Setting local password for user: $(whoami)..."
passwd

echo "[+] Starting SSH Server on Port 8022..."
sshd

IP_ADDR=$(ifconfig wlan0 2>/dev/null | grep 'inet ' | awk '{print $2}')
echo "========================================================================"
echo " [✓] SSH DAEMON ACTIVE"
echo " [CONNECT FROM POWERSHELL]: ssh $(whoami)@${IP_ADDR:-<your-termux-ip>} -p 8022"
echo "========================================================================"
