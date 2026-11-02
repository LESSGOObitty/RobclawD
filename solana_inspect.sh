#!/bin/bash

SOL_ADDR="3sZ2G9spssmLMZDMcZF5FMca4udBWNQkGLiaeBEzUPHn"
SOL_RPC="https://api.mainnet-beta.solana.com"

echo "========================================================"
echo "          INSPECTING SOLANA ANCHOR ACCOUNT DATA        "
echo "========================================================"
echo "[*] Target Address: $SOL_ADDR"

curl -s -X POST -H "Content-Type: application/json" \
  --data "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"getAccountInfo\",\"params\":[\"$SOL_ADDR\", {\"encoding\":\"jsonParsed\"}]}" \
  "$SOL_RPC" | jq '.'

echo "========================================================"
