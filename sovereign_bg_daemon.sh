#!/bin/bash
# ======================================================================
# SOVEREIGN BACKGROUND SILENT DAEMON
# ======================================================================

SOV_HOME="$HOME/sovereign_core"
LOG_FILE="$SOV_HOME/daemon.log"

cd "$SOV_HOME" || exit

echo "[+] Launching Sovereign background sync daemon..."

while true; do
    TIMESTAMP=$(date +%s)
    
    # 1. Update dynamic IP & state
    python3 sovereign_dynamic_link.py >> "$LOG_FILE" 2>&1
    
    # 2. Run unified bridge and auto-commit to git ledger
    python3 sovereign_unified_bridge.py >> "$LOG_FILE" 2>&1
    ./sovereign_autocommit.sh >> "$LOG_FILE" 2>&1
    
    # 3. Silent keep-alive pulse (if tunnel target is defined)
    # autossh -M 0 -o "ServerAliveInterval=30" -o "ServerAliveCountMax=3" ...
    
    # Sleep between sync loops (e.g., every 60 seconds)
    sleep 60
done
