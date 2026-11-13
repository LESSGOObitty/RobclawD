#!/usr/bin/env bash
# ==============================================================================
# Script Name: log_rotate.sh
# Description: Termux-optimized log rotation, timestamping, & SHA-256 verification
# ==============================================================================

# Configuration
LOG_DIR="${HOME}/workspace/telemetry"
LOG_NAME="system.log"
TARGET_LOG="${LOG_DIR}/${LOG_NAME}"
MANIFEST_FILE="${LOG_DIR}/sha256_manifest.txt"
MAX_BACKUPS=5

# Ensure telemetry directory exists
mkdir -p "$LOG_DIR"

# Initialize log file if missing
if [ ! -f "$TARGET_LOG" ]; then
    echo "[!] Target log file not found at $TARGET_LOG. Initializing fresh file."
    touch "$TARGET_LOG"
    exit 0
fi

# Exit early if the log file is empty
if [ ! -s "$TARGET_LOG" ]; then
    echo "[*] Log file is empty. Rotation bypassed."
    exit 0
fi

# Generate UTC/Local timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ROTATED_LOG="${LOG_DIR}/system_${TIMESTAMP}.log"

echo "[+] Rotating active log -> system_${TIMESTAMP}.log"
mv "$TARGET_LOG" "$ROTATED_LOG"
touch "$TARGET_LOG"

# Generate SHA-256 checksum and append to manifest
echo "[+] Calculating SHA-256 integrity checksum..."
cd "$LOG_DIR" || exit 1
sha256sum "$(basename "$ROTATED_LOG")" >> "$MANIFEST_FILE"
echo "[+] Checksum sealed into: $(basename "$MANIFEST_FILE")"

# Enforce backup rotation limit
echo "[+] Pruning archive logs (retaining latest $MAX_BACKUPS)..."
# Get sorted list of rotated logs (newest first)
mapfile -t BACKUP_FILES < <(ls -1t system_*.log 2>/dev/null)

if [ ${#BACKUP_FILES[@]} -gt $MAX_BACKUPS ]; then
    for ((i=$MAX_BACKUPS; i<${#BACKUP_FILES[@]}; i++)); do
        echo "[!] Pruning expired log: ${BACKUP_FILES[$i]}"
        rm -f "${BACKUP_FILES[$i]}"
    done
fi

echo "[✓] Log rotation and integrity check successfully completed."
