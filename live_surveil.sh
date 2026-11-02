#!/usr/bin/env bash
set -euo pipefail

echo "====================================================="
echo " LIVE TELEMETRY SURVEILLANCE LOOP [ ( . Y . ) ]"
echo "====================================================="

while true; do
    clear
    echo "[*] Querying live network state anchor..."
    RESPONSE=$(curl -s -X POST https://ethereum-rpc.publicnode.com \
      -H "Content-Type: application/json" \
      --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", false],"id":1}')
    
    if command -v jq &> /dev/null; then
        BLOCK_HEX=$(echo "$RESPONSE" | jq -r '.result.number')
        BLOCK_NUM=$((BLOCK_HEX))
        BLOCK_HASH=$(echo "$RESPONSE" | jq -r '.result.hash')
        STATE_ROOT=$(echo "$RESPONSE" | jq -r '.result.stateRoot')
        
        echo "-----------------------------------------------------"
        echo " [STATUS] LOCKED & ACTIVE"
        echo " Block Number : ${BLOCK_NUM}"
        echo " Block Hash   : ${BLOCK_HASH}"
        echo " State Root   : ${STATE_ROOT}"
        echo " System Time  : $(date -u +%T) UTC"
        echo "-----------------------------------------------------"
    else
        echo "$RESPONSE"
    fi
    
    echo "[*] Cycling feed in 5 seconds (Press Ctrl+C to drop loop)..."
    sleep 5
done
