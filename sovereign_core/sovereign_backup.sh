#!/bin/bash
BACKUP_DIR="$HOME/sovereign_core/archives"
mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +%s)
DEST="$BACKUP_DIR/sovereign_vault_${TIMESTAMP}.tar.gz"
tar -czf "$DEST" -C "$HOME" .provmark robdoe_telemetry.json .git 2>/dev/null
MASTER_HASH=$(sha256sum "$DEST" | awk '{print $1}')
echo "[✓] Vault Sealed: $DEST"
echo "[+] Master SHA256: $MASTER_HASH"
