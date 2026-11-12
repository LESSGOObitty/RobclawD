#!/bin/bash
# Push Termux state files directly to Windows PC

WIN_IP="192.168.1.150"
WIN_USER="RobDoe"
DEST_PATH="C:/sovereign_vault/"

echo "[+] Uploading telemetry to Windows machine..."
scp ~/robdoe_telemetry.json "${WIN_USER}@${WIN_IP}:${DEST_PATH}"

echo "[+] Uploading latest backup archive..."
LATEST_BACKUP=$(ls -t ~/sovereign_core/archives/*.tar.gz 2>/dev/null | head -n 1)
if [ -n "$LATEST_BACKUP" ]; then
    scp "$LATEST_BACKUP" "${WIN_USER}@${WIN_IP}:${DEST_PATH}"
    echo "[✓] Backup transferred: $LATEST_BACKUP"
else
    echo "[!] No backup archives found to send."
fi
