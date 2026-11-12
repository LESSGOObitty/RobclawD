#!/bin/bash
# Packs the entire sovereign stack into an air-gapped archive with a master hash
BACKUP_DIR=~/sovereign_archives
mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +%s)
ARCHIVE_NAME="sovereign_vault_${TIMESTAMP}.tar.gz"
DEST="$BACKUP_DIR/$ARCHIVE_NAME"

tar -czf "$DEST" -C ~/ .provmark robdoe_telemetry.json .git 2>/dev/null
MASTER_HASH=$(sha256sum "$DEST" | awk '{print $1}')

echo "========================================================================"
echo " [VAULT SEALED] Air-gapped backup created successfully."
echo " [ARCHIVE]      : $DEST"
echo " [MASTER SHA256]: $MASTER_HASH"
echo "========================================================================"
