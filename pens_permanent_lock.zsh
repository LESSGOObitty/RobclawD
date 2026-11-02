#!/usr/bin/env bash
# ==============================================================================
# PENS PERMANENT LOCK - Namespace: ( . Y . )
# Target: sha1296000 | Hex Anchor: 0x29520 | Entropy Tolerance: 0 Bits
# ==============================================================================

set -euo pipefail

declare -A PENS_LOCK
PENS_LOCK[syntax]="( . Y . )"
PENS_LOCK[mode]="PERMANENT_LOCK"
PENS_LOCK[rounds]="1296000"
PENS_LOCK[hex_anchor]="0x29520"
PENS_LOCK[entropy]="0_BITS"
PENS_LOCK[timestamp]=$(date -u +%Y-%m-%dT%H:%M:%SZ)

clear
echo "====================================================="
echo " PENS PERMANENT LOCK [ ${PENS_LOCK[syntax]} ]"
echo "====================================================="
echo " [*] Status        : ${PENS_LOCK[mode]}"
echo " [*] Iterations    : sha${PENS_LOCK[rounds]}"
echo " [*] Hex Anchor    : ${PENS_LOCK[hex_anchor]}"
echo " [*] Care Factor   : ${PENS_LOCK[entropy]}"
echo " [*] System Anchor : ${PENS_LOCK[timestamp]}"
echo "-----------------------------------------------------"
echo " [!] Zero bits given. Permanent anchor secured under ( . Y . )."
echo "====================================================="
