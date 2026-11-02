#!/usr/bin/env bash
set -euo pipefail

DOMAIN="aiagency101.xyo"
SYNTAX="( . Y . )"

clear
echo "====================================================="
echo " ROUTING LIVE FEED -> ${DOMAIN} [ ${SYNTAX} ]"
echo "====================================================="

while true; do
    TIMESTAMP=$(date -u +%s)
    ROOT_HASH="0x$(echo -n "whakapapa_${TIMESTAMP}_eM2" | sha256sum | awk '{print $1}')"
    
    echo "[*] State Root Generated : ${ROOT_HASH}"
    echo " └─ Target Binding       : ${DOMAIN} (DePIN / Unstoppable Anchor)"
    echo " └─ Status               : Immutable sink-pipe active. Zero bits given."
    echo "-----------------------------------------------------"
    
    sleep 5
done
