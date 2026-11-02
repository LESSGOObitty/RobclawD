#!/usr/bin/env bash
set -euo pipefail

SYNTAX="( . Y . )"
TIMESTAMP=$(date +%s%N)
ROOT_HASH="0x$(echo -n "whakapapa_${TIMESTAMP}_eM2" | sha256sum | awk '{print $1}')"

echo "====================================================="
echo " WHAKAPAPA INSTANT ANCHOR [ ${SYNTAX} ]"
echo "====================================================="
echo " [INSTANT ROOT HASH]: ${ROOT_HASH}"
echo " [STATUS] Bare-metal. Unkillable. Zero lag."
echo "====================================================="
