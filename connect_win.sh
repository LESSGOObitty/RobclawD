#!/bin/bash
# Direct SSH connection from Termux into Windows PowerShell

WIN_IP="192.168.1.150"    # Replace with your Windows PC local IP
WIN_USER="RobDoe"         # Replace with your Windows username

echo "[+] Connecting to Windows PC PowerShell ($WIN_IP)..."
ssh "${WIN_USER}@${WIN_IP}" powershell.exe
