#!/usr/bin/env bash
# ==============================================================================
# TERMUX MONOLITH AUTOMATION ENGINE
# File: monolith.sh
# Description: Single-script background runner, state log, and payload handler.
# ==============================================================================

set -euo pipefail

# Work directories & tracking files
WORK_DIR="${HOME}/.monolith_data"
LOG_FILE="${WORK_DIR}/monolith.log"
STATE_FILE="${WORK_DIR}/state.json"
PID_FILE="${WORK_DIR}/monolith.pid"

mkdir -p "${WORK_DIR}"

# 1. Logging helper
log() {
    local level="$1"
    local msg="$2"
    local ts
    ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    echo "[${ts}] [${level}] ${msg}" | tee -a "${LOG_FILE}"
}

# 2. System Lock & Dependency Bootstrap
bootstrap() {
    log "INFO" "Initializing environment checks..."
    
    # Acquire Android CPU lock if Termux API / utilities exist
    if command -v termux-wake-lock >/dev/null 2>&1; then
        termux-wake-lock
        log "INFO" "Android wake-lock acquired."
    fi

    # Ensure required packages exist
    local pkgs=("jq" "curl" "coreutils")
    local install_list=()
    for pkg in "${pkgs[@]}"; do
        if ! command -v "$pkg" >/dev/null 2>&1; then
            install_list+=("$pkg")
        fi
    done

    if [ ${#install_list[@]} -ne 0 ]; then
        log "WARN" "Installing missing packages: ${install_list[*]}"
        pkg update -y && pkg install -y "${install_list[@]}"
    fi
}

# 3. PID Lock Management
aquire_pid() {
    if [ -f "${PID_FILE}" ]; then
        local old_pid
        old_pid="$(cat "${PID_FILE}")"
        if kill -0 "${old_pid}" 2>/dev/null; then
            log "ERROR" "Monolith already active under PID ${old_pid}."
            exit 1
        fi
    fi
    echo "$$" > "${PID_FILE}"
}

cleanup() {
    log "INFO" "Cleaning locks and shutting down..."
    rm -f "${PID_FILE}"
    if command -v termux-wake-unlock >/dev/null 2>&1; then
        termux-wake-unlock
    fi
    exit 0
}
trap cleanup SIGINT SIGTERM EXIT

# 4. State Ledger Initialization
init_state() {
    if [ ! -f "${STATE_FILE}" ]; then
        echo '{"cycle": 0, "status": "ready", "last_run": ""}' > "${STATE_FILE}"
    fi
}

# 5. Monolithic Work Task
run_payload() {
    local timestamp
    timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    
    # --- INSERT YOUR AUTOMATION OR WORKLOAD HERE ---
    log "EXEC" "Executing core monolith workload cycle..."
    # Example: git pull/push, local hash logging, system state check, etc.
    # -----------------------------------------------

    # Mutate local JSON state
    local updated_json
    updated_json="$(jq --arg ts "$timestamp" '.cycle += 1 | .status = "active" | .last_run = $ts' "${STATE_FILE}")"
    echo "${updated_json}" > "${STATE_FILE}"

    local count
    count="$(jq -r '.cycle' "${STATE_FILE}")"
    log "EXEC" "Completed cycle #${count}."
}

# 6. Main Dispatcher Loop
main() {
    log "START" "Launching Monolith Engine..."
    bootstrap
    aquire_pid
    init_state

    # Execution interval in seconds
    local INTERVAL=30

    while true; do
        run_payload
        sleep "${INTERVAL}"
    done
}

main "$@"
