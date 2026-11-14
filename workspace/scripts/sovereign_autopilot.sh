#!/data/data/com.termux/files/usr/bin/bash

WORKSPACE="$HOME/workspace"
LOG_FILE="$WORKSPACE/logs/autopilot.log"
AUDIT_SCRIPT="$WORKSPACE/scripts/audit_manifest.py"
GUARDIAN_SCRIPT="$WORKSPACE/scripts/git_guardian.py"
CRON_SCRIPT="$WORKSPACE/scripts/cron_daemon.py"
ENGINE_SCRIPT="$WORKSPACE/scripts/run_engine.sh"

# Acquire wake lock to prevent Android Doze from killing background processes
command -v termux-wake-lock >/dev/null 2>&1 && termux-wake-lock

echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] [BOOT] Sovereign Autopilot Watchdog Online" >> "$LOG_FILE"

while true; do
    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

    # 1. Self-Healing Process Supervision
    if [ -f "$CRON_SCRIPT" ] && ! pgrep -f "cron_daemon.py" > /dev/null; then
        echo "[$TIMESTAMP] [HEAL] cron_daemon.py down. Respawning..." >> "$LOG_FILE"
        python3 "$CRON_SCRIPT" >> "$WORKSPACE/logs/cron_daemon.log" 2>&1 &
    fi

    if [ -f "$ENGINE_SCRIPT" ] && ! pgrep -f "run_engine.sh" > /dev/null; then
        echo "[$TIMESTAMP] [HEAL] run_engine.sh down. Respawning..." >> "$LOG_FILE"
        bash "$ENGINE_SCRIPT" >> "$WORKSPACE/logs/run_engine.log" 2>&1 &
    fi

    # 2. Cryptographic Merkle DAG State Audit
    if [ -f "$AUDIT_SCRIPT" ]; then
        python3 "$AUDIT_SCRIPT" >> "$LOG_FILE" 2>&1
    fi

    # 3. Autonomous Git Sync & State Checkpoint
    if [ -f "$GUARDIAN_SCRIPT" ]; then
        python3 "$GUARDIAN_SCRIPT" >> "$LOG_FILE" 2>&1
    elif [ -d "$WORKSPACE/.git" ]; then
        cd "$WORKSPACE" || exit
        if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit -m "chore(autopilot): state seal $TIMESTAMP" >> "$LOG_FILE" 2>&1
            git push origin main >> "$LOG_FILE" 2>&1
        fi
    fi

    # 4. Log Rotation (Cap logs at 5000 lines to preserve flash storage)
    for log in "$WORKSPACE/logs/"*.log; do
        [ -f "$log" ] && tail -n 5000 "$log" > "$log.tmp" && mv "$log.tmp" "$log"
    done

    # Cycle interval: 15 minutes (900s)
    sleep 900
done
