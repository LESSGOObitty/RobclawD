#!/data/data/com.termux/files/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-.}"
TEMP_DIR=$(mktemp -d "${TMPDIR:-/data/data/com.termux/files/usr/tmp}/merkle.XXXXXX")
trap 'rm -rf "$TEMP_DIR"' EXIT

HASH_LIST="$TEMP_DIR/hashes.tmp"

echo "[+] Scanning workspace: $TARGET_DIR"

find "$TARGET_DIR" -type f -not -path '*/.*' | sort | while read -r file; do
    file_hash=$(sha256sum "$file" | awk '{print $1}')
    leaf_hash=$(printf "%s  %s\n" "$file_hash" "$file" | sha256sum | awk '{print $1}')
    echo "$leaf_hash" >> "$HASH_LIST"
done

if [ ! -s "$HASH_LIST" ]; then
    echo "[-] No files found to index."
    exit 1
fi

TOTAL_LEAVES=$(wc -l < "$HASH_LIST")
echo "[+] Indexed $TOTAL_LEAVES leaf nodes."

LEVEL=0
CURRENT_LAYER="$HASH_LIST"

while [ $(wc -l < "$CURRENT_LAYER") -gt 1 ]; do
    NEXT_LAYER="$TEMP_DIR/layer_${LEVEL}.tmp"
    > "$NEXT_LAYER"

    awk 'NR%2{printf "%s ",$0; next} {print $0}' "$CURRENT_LAYER" | while read -r hash1 hash2; do
        if [ -z "$hash2" ]; then
            hash2="$hash1"
        fi
        parent_hash=$(printf "%s%s" "$hash1" "$hash2" | sha256sum | awk '{print $1}')
        echo "$parent_hash" >> "$NEXT_LAYER"
    done

    CURRENT_LAYER="$NEXT_LAYER"
    LEVEL=$((LEVEL + 1))
done

MERKLE_ROOT=$(cat "$CURRENT_LAYER")

echo "=============================================================================="
echo " MERKLE DAG ROOT: $MERKLE_ROOT"
echo " TOTAL DEPTH:     $LEVEL layers"
echo "=============================================================================="
