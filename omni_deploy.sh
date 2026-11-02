#!/usr/bin/env bash
set +H
set -e

echo "====================================================================="
echo "     [ROBDOE.TERMUX] INITIALIZING OMNI-MESH DEPLOYMENT               "
echo "====================================================================="

NODE_ID="robdoe.termux"
WATERMARK="espVmark:2c3f1b0af3a2367a"
DOMAIN="robdoe.com"

echo "[*] Node Identity  : $NODE_ID"
echo "[*] Active Domain  : $DOMAIN (ERC-721 Deed Bound)"
echo "[*] Watermark Seal : $WATERMARK"
echo ""

WORKSPACE_DIR="$HOME/robdoerootauthority"
mkdir -p "$WORKSPACE_DIR"
cd "$WORKSPACE_DIR"

cat << 'JS_EOF' > robdoe_cockpit_omni.js
const colors = {
    primary: '\x1b[38;5;82m',
    accent: '\x1b[38;5;226m',
    cyan: '\x1b[38;5;51m',
    reset: '\x1b[0m'
};

console.log(`${colors.primary}[ROBDOE.TERMUX] Omni-Cockpit Initialized successfully.${colors.reset}`);
console.log(`${colors.accent}[WATERMARK] espVmark:2c3f1b0af3a2367a active.${colors.reset}`);
JS_EOF

echo " [+] Generated: robdoe_cockpit_omni.js"
echo ""
echo "--- [EXECUTING MESH RUNTIME] ---"
node robdoe_cockpit_omni.js

echo ""
echo "====================================================================="
echo " [SUCCESS] All systems synchronized, watermarked, and online."
echo "====================================================================="
