#!/bin/bash
# Continuous Sovereign Background Loop
INTERVAL=30 # seconds

echo "[+] Initializing Sovereign Daemon (Heartbeat: ${INTERVAL}s)..."
while true; do
    # 1. Run master unified bridge
    python3 ~/sovereign_unified_bridge.py >/dev/null 2>&1
    
    # 2. Auto-seal git commit and tag
    ~/sovereign_autocommit.sh >/dev/null 2>&1
    
    sleep $INTERVAL
done
