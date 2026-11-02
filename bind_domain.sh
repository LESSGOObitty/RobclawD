#!/usr/bin/env bash
set -euo pipefail

PRIMARY_DOMAIN="robertdoe.pw"
NAMESPACE="( . Y . )"
LOG_FILE="robertdoe_anchor.log"

clear
echo "====================================================="
echo " DOMAIN ANCHOR BINDING ENGINE [ ${NAMESPACE} ]"
echo " Target Domain : ${PRIMARY_DOMAIN}"
echo " Log Destination: ${LOG_FILE}"
echo "====================================================="

while true; do
    # Pull latest block number directly from the raw wire
    RPC_RESPONSE=$(curl -s -X POST https://ethereum-rpc.publicnode.com \
      -H "Content-Type: application/json" \
      --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}')
    
    BLOCK_HEX=$(echo "$RPC_RESPONSE" | jq -r '.result // "0x0"')
    TIMESTAMP=$(date -u +%s)
    
    # Cryptographic binding: Z = z² + eM2 incorporating domain + block state
    RAW_PAYLOAD="${PRIMARY_DOMAIN}:${BLOCK_HEX}:${TIMESTAMP}:eM2"
    ANCHOR_HASH="0x$(echo -n "$RAW_PAYLOAD" | sha256sum | awk '{print $1}')"
    
    # Output to screen and append to sovereign local log
    ENTRY="[${TIMESTAMP}] DOMAIN=${PRIMARY_DOMAIN} | BLOCK=${BLOCK_HEX} | ROOT=${ANCHOR_HASH}"
    echo "$ENTRY" | tee -a "$LOG_FILE"
    
    echo "-----------------------------------------------------"
    sleep 5
done
