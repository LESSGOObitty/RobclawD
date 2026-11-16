#!/data/data/com.termux/files/usr/bin/env bash
# robdoenet // ARM64 Background Daemon Runner
# Permanent Anchor: 34.68.218.70 | Domain: robdoe.com

WORKSPACE_DIR="$HOME/robdoerootauthority/workspace"
LOG_FILE="$HOME/.robdoenet_daemon.log"

cd "$WORKSPACE_DIR" || exit 1

echo "[$(date)] ⚡ Starting robdoenet ARM64 background daemon..." >> "$LOG_FILE"

while true; do
    # Run ghostnet diagnostic or telemetry pulse every 300 seconds
    if [ -f "$WORKSPACE_DIR/ghostnet_diag.py" ]; then
        python3 "$WORKSPACE_DIR/ghostnet_diag.py" >> "$LOG_FILE" 2>&1
    fi
    sleep 300
done
