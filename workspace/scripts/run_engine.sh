#!/data/data/com.termux/files/usr/bin/sh
export HOME=/data/data/com.termux/files/home
export PATH=/data/data/com.termux/files/usr/bin:$PATH

LOG_DIR="$HOME/workspace/logs"
SUPERVISOR_LOG="$LOG_DIR/engine.log"
BROADCAST_LOG="$LOG_DIR/broadcast.log"
WITNESS_LOG="$LOG_DIR/witness.log"
HEALTH_JSON="$LOG_DIR/health.json"
MAX_LOG_SIZE=$((5 * 1024 * 1024)) # 5 MB threshold

rotate_logs() {
    for log in "$SUPERVISOR_LOG" "$BROADCAST_LOG" "$WITNESS_LOG"; do
        if [ -f "$log" ] && [ $(stat -c%s "$log" 2>/dev/null || echo 0) -gt $MAX_LOG_SIZE ]; then
            TIMESTAMP=$(date +'%Y%m%d_%H%M%S')
            mv "$log" "${log%.log}_$TIMESTAMP.log"
            echo "[$(date)] Log rotated due to size limit." > "$log"
        fi
    done
}

update_health() {
    cat << JSON > "$HEALTH_JSON"
{
  "node": "RobclawD-Termux",
  "status": "$1",
  "timestamp": "$(date -u +'%Y-%m-%dT%H:%M:%SZ')",
  "pid_broadcast": "${2:-null}",
  "pid_witness": "${3:-null}"
}
JSON
}

echo "[$(date)] === SOVEREIGN ENGINE SUPERVISOR (SPLIT LOGS) ===" | tee -a "$SUPERVISOR_LOG"

while true; do
    rotate_logs
    update_health "BOOTING"
    
    echo "[$(date)] [*] Spawning live_broadcast_engine.py -> broadcast.log" | tee -a "$SUPERVISOR_LOG"
    python3 -u "$HOME/live_broadcast_engine.py" >> "$BROADCAST_LOG" 2>&1 &
    BROADCAST_PID=$!

    echo "[$(date)] [*] Spawning witness_and_hubs_seal.py -> witness.log" | tee -a "$SUPERVISOR_LOG"
    python3 -u "$HOME/witness_and_hubs_seal.py" >> "$WITNESS_LOG" 2>&1 &
    WITNESS_PID=$!

    update_health "RUNNING" "$BROADCAST_PID" "$WITNESS_PID"

    while kill -0 $BROADCAST_PID 2>/dev/null && kill -0 $WITNESS_PID 2>/dev/null; do
        sleep 30
    done

    update_health "CRASHED_RESTARTING"
    echo "[$(date)] [!] Engine process exited. Cleaning up PIDs..." | tee -a "$SUPERVISOR_LOG"
    
    kill $BROADCAST_PID $WITNESS_PID 2>/dev/null
    wait $BROADCAST_PID $WITNESS_PID 2>/dev/null
    sleep 10
done
