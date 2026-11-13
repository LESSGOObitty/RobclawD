#!/usr/bin/env zsh
# =====================================================================
# ROBDOE ROOT AUTHORITY // AUTONOMOUS TELEMETRY & OVERDRIVE ENGINE v8.0
# =====================================================================
set -euo pipefail

MODE="${1:-dashboard}"
ANCHOR="espVmark:2c3f1b0af3a2367a"
PERSONA="LESSGOObitty"
EMAIL="Robdoeaiagency101tenet@gmail.com"

# High-Contrast ANSI Palette
C_CYAN='\033[1;36m'
C_GREEN='\033[1;32m'
C_YELLOW='\033[1;33m'
C_RED='\033[1;31m'
C_DIM='\033[0;90m'
C_RESET='\033[0m'

# --- FUNCTION: EMERGENCY SURGICAL RECLAMATION ---
perform_cleanup() {
    BEFORE_KB=$(df / | awk 'NR==2 {print $4}')
    
    # 1. Nuke build caches & package debris
    npm cache clean --force 2>/dev/null || true
    pip cache purge 2>/dev/null || true
    rm -rf ~/.cache/* /tmp/* node_modules/.cache 2>/dev/null || true
    
    # 2. Git garbage collection & loose object compaction
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        rm -f .git/objects/pack/tmp_pack_* 2>/dev/null || true
        git reflog expire --expire=now --all 2>/dev/null || true
        git gc --prune=now --aggressive 2>/dev/null || true
    fi
    
    # 3. Package manager archives
    apt-get clean 2>/dev/null || true
    pkg clean 2>/dev/null || true
    
    AFTER_KB=$(df / | awk 'NR==2 {print $4}')
    awk "BEGIN {printf \"%.2f\", (${AFTER_KB} - ${BEFORE_KB}) / 1024}"
}

# Auto-purge if disk is critically jammed (>= 90%)
CURRENT_PCT=$(df / | awk 'NR==2 {gsub("%",""); print $5}')
if [ "${CURRENT_PCT}" -ge 90 ]; then
    echo -e "${C_RED}[!] CRITICAL DISK CAPACITY (${CURRENT_PCT}%). AUTO-PURGING...${C_RESET}"
    RECLAIMED=$(perform_cleanup)
    echo -e "${C_GREEN}[+] Reclaimed ${RECLAIMED} MB instantly.${C_RESET}"
fi

# --- MODE 1: SURGICAL CLEANUP (--clean) ---
if [[ "${MODE}" == "--clean" ]]; then
    echo -e "${C_YELLOW}[*] INITIATING EXPLICIT STORAGE RECLAMATION...${C_RESET}"
    RECLAIMED_MB=$(perform_cleanup)
    echo -e "${C_GREEN}[+] RECLAMATION COMPLETE. Headroom delta: +${RECLAIMED_MB} MB${C_RESET}"
    df -h / | awk 'NR==2 {print "    Current Disk: " $3 " / " $2 " (" $5 " used, " $4 " free)"}'
    exit 0
fi

# --- MODE 2: AUTONOMOUS WATCHDOG (--watch) ---
if [[ "${MODE}" == "--watch" ]]; then
    echo -e "${C_CYAN}[*] LAUNCHING AUTONOMOUS DISK GUARDRAIL (Interval: 30s)...${C_RESET}"
    echo -e "${C_DIM}    Press Ctrl+C to detach to background.${C_RESET}"
    while true; do
        PCT=$(df / | awk 'NR==2 {gsub("%",""); print $5}')
        if [ "${PCT}" -ge 85 ]; then
            RECLAIMED=$(perform_cleanup)
            echo -e "${C_GREEN}[+] Auto-purged ${RECLAIMED} MB at $(date -u +"%T") (Disk at ${PCT}%)${C_RESET}"
        fi
        sleep 30
    done
fi

# Gather Core Telemetry
TS_ISO=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
UNAME_STR="$(uname -srmo) | Node: $(uname -n)"
DISK_PCT=$(df / | awk 'NR==2 {gsub("%",""); print $5}')
DISK_INFO=$(df -h / | awk 'NR==2 {print $3 " / " $2 " (" $5 " used, " $4 " free)"}')
MEM_INFO=$(free -h 2>/dev/null | awk '/Mem:/ {print $3 " / " $2 " used"}' || echo "N/A")

# Git & Merkle State
IN_GIT=false
BRANCH="N/A"
HASH="0000000"
DIRTY="0"
AHEAD_BEHIND="N/A"
REMOTE_URL="N/A"
STATE_SEAL="UNSEALED"

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    IN_GIT=true
    BRANCH=$(git branch --show-current 2>/dev/null || echo "DETACHED")
    HASH=$(git rev-parse --short HEAD 2>/dev/null || echo "0000000")
    DIRTY=$(git status --porcelain | wc -l | tr -d ' ')
    REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "NO_REMOTE")
    AHEAD_BEHIND=$(git rev-list --left-right --count @{u}...HEAD 2>/dev/null | awk '{print "Behind:"$1" Ahead:"$2}' || echo "Local-only")
    STATE_SEAL=$( (git rev-parse HEAD 2>/dev/null; git status --porcelain; echo "${ANCHOR}") | sha256sum | cut -c1-16 )
fi

# Hardware Serial / ESP32 Bus Check
SERIAL_DEVS=$(ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null | tr '\n' ' ' || true)
[[ -z "${SERIAL_DEVS}" ]] && SERIAL_DEVS="None attached"

# Toolchain & Web3 Stack Check
PY_VER=$(python3 --version 2>/dev/null | awk '{print $2}' || echo "None")
WEB3_PY=$(python3 -c "import web3; print(web3.__version__)" 2>/dev/null || echo "Not installed")
NODE_VER=$(node -v 2>/dev/null || echo "None")
HARDHAT_VER=$(npx hardhat --version 2>/dev/null || echo "Not initialized")
ONLINE=false
curl -s --max-time 1 https://api.github.com >/dev/null && ONLINE=true

# --- MODE 3: JSON TELEMETRY EXPORT (--json) ---
if [[ "${MODE}" == "--json" ]]; then
    python3 -c '
import json, sys
payload = {
    "timestamp": sys.argv[1],
    "persona": sys.argv[2],
    "email": sys.argv[3],
    "anchor": sys.argv[4],
    "disk_pct": int(sys.argv[5]),
    "disk_info": sys.argv[6],
    "git": {
        "active": sys.argv[7] == "true",
        "branch": sys.argv[8],
        "head": sys.argv[9],
        "dirty_files": int(sys.argv[10]),
        "state_seal": f"sha256:{sys.argv[11]}"
    },
    "toolchain": {
        "python": sys.argv[12],
        "web3_py": sys.argv[13],
        "node": sys.argv[14],
        "hardhat": sys.argv[15]
    },
    "serial_bus": sys.argv[16].strip(),
    "online": sys.argv[17] == "true"
}
print(json.dumps(payload, indent=2))
' "${TS_ISO}" "${PERSONA}" "${EMAIL}" "${ANCHOR}" "${DISK_PCT}" "${DISK_INFO}" "${IN_GIT}" "${BRANCH}" "${HASH}" "${DIRTY}" "${STATE_SEAL}" "${PY_VER}" "${WEB3_PY}" "${NODE_VER}" "${HARDHAT_VER}" "${SERIAL_DEVS}" "${ONLINE}"
    exit 0
fi

# --- MODE 4: APPEND IMMUTABLE LEDGER CHECKPOINT (--seal) ---
if [[ "${MODE}" == "--seal" ]]; then
    LEDGER_FILE=".telemetry_ledger.jsonl"
    "$0" --json | tr -d '\n' | sed 's/  */ /g' >> "${LEDGER_FILE}"
    echo "" >> "${LEDGER_FILE}"
    echo -e "${C_GREEN}[+] CRYPTOGRAPHIC CHECKPOINT APPENDED TO ${LEDGER_FILE}${C_RESET}"
    echo -e "    Seal: ${C_CYAN}sha256:${STATE_SEAL}${C_RESET} @ ${TS_ISO}"
    exit 0
fi

# --- MODE 5: INSTALL GIT PRE-COMMIT HOOK (--install-hook) ---
if [[ "${MODE}" == "--install-hook" ]]; then
    if [[ "${IN_GIT}" != "true" ]]; then
        echo -e "${C_RED}[!] Error: Not inside a Git repository.${C_RESET}"
        exit 1
    fi
    HOOK_PATH=".git/hooks/pre-commit"
    cat << 'HOOKEOF' > "${HOOK_PATH}"
#!/usr/bin/env zsh
echo "[*] Git Pre-Commit Hook: Verifying Merkle State Seal..."
if ./termux_status.sh --seal >/dev/null 2>&1; then
    echo "[+] State Seal verified and logged to ledger."
else
    echo "[!] Warning: Telemetry ledger checkpoint failed to log."
fi
HOOKEOF
    chmod +x "${HOOK_PATH}"
    echo -e "${C_GREEN}[+] Git pre-commit hook installed successfully at ${HOOK_PATH}${C_RESET}"
    exit 0
fi

# --- MODE 6: EXPORT SNAPSHOT ARCHIVE (--export) ---
if [[ "${MODE}" == "--export" ]]; then
    ARCHIVE_NAME="robdoe_telemetry_snapshot_$(date +%Y%m%d_%H%M%S).tar.gz"
    tar -czf "${ARCHIVE_NAME}" .telemetry_ledger.jsonl *.sh 2>/dev/null || true
    echo -e "${C_GREEN}[+] SNAPSHOT EXPORTED: ${ARCHIVE_NAME}${C_RESET}"
    exit 0
fi

# --- DEFAULT MODE: TACTICAL DASHBOARD ---
echo -e "${C_CYAN}=====================================================================${C_RESET}"
echo -e "${C_CYAN} [ROBDOE.TERMUX] // AUTONOMOUS OVERDRIVE ENGINE v8.0${C_RESET}"
echo -e "${C_CYAN}=====================================================================${C_RESET}"

echo -e " ${C_GREEN}[PERSONA]${C_RESET}   : ${PERSONA} ${C_DIM}[${ANCHOR}]${C_RESET}"
echo -e " ${C_GREEN}[EMAIL]${C_RESET}     : ${EMAIL}"
echo -e " ${C_GREEN}[HANDLES]${C_RESET}   : gh:@LadbotOneLad | gh:@backupsonbackups-cyber"
echo -e " ${C_GREEN}[UNAME]${C_RESET}     : ${UNAME_STR}"

# Storage Alert Coloring + Auto-Blame
if [ "${DISK_PCT}" -ge 90 ]; then
    DISK_COLOR=$C_RED
elif [ "${DISK_PCT}" -ge 75 ]; then
    DISK_COLOR=$C_YELLOW
else
    DISK_COLOR=$C_GREEN
fi
echo -e " ${C_GREEN}[STORAGE]${C_RESET}   : ${DISK_COLOR}${DISK_INFO}${C_RESET}"
if [ "${DISK_PCT}" -ge 90 ]; then
    TOP_HOGS=$(du -sh * .git 2>/dev/null | sort -hr | head -n 3 | tr '\n' ' | ')
    echo -e " ${C_RED}[DISK ALERT]${C_RESET}: Heavyweights -> ${TOP_HOGS}(Run: status --clean)"
fi
echo -e " ${C_GREEN}[MEMORY]${C_RESET}    : ${MEM_INFO}"

# Chassis Battery & Thermal
if command -v termux-battery-status >/dev/null 2>&1; then
    BAT_DATA=$(termux-battery-status 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d.get('percentage')}% ({d.get('status')}) | {d.get('temperature')}°C\")" 2>/dev/null || echo "API Timeout")
    echo -e " ${C_GREEN}[CHASSIS]${C_RESET}   : Battery ${BAT_DATA}"
fi

# Hardware Serial Bus
echo -e " ${C_GREEN}[SERIAL BUS]${C_RESET}: ${SERIAL_DEVS}"

# Git & Merkle State
if [[ "${IN_GIT}" == "true" ]]; then
    echo -e " ${C_GREEN}[GIT HEAD]${C_RESET}  : ${BRANCH} @ ${HASH} (${DIRTY} uncommitted | ${AHEAD_BEHIND})"
    echo -e " ${C_GREEN}[STATE SEAL]${C_RESET}: sha256:${C_CYAN}${STATE_SEAL}${C_RESET}"
    echo -e " ${C_GREEN}[ORIGIN]${C_RESET}    : ${REMOTE_URL}"
else
    echo -e " ${C_GREEN}[GIT HEAD]${C_RESET}  : Not inside a git repository"
fi

# GitHub CLI & Auth
if command -v gh >/dev/null 2>&1; then
    GH_USER=$(gh api user -q '.login' 2>/dev/null || echo "UNAUTHENTICATED")
    echo -e " ${C_GREEN}[GH CLI]${C_RESET}    : Active Session -> @${GH_USER}"
else
    GH_GIT_USER=$(git config user.name 2>/dev/null || echo "Unset")
    GH_GIT_EMAIL=$(git config user.email 2>/dev/null || echo "Unset")
    echo -e " ${C_GREEN}[GH CONFIG]${C_RESET} : ${GH_GIT_USER} <${GH_GIT_EMAIL}>"
fi

# Toolchain & Uplink
NET_STR=$([[ "${ONLINE}" == "true" ]] && echo "${C_GREEN}GITHUB API ONLINE${C_RESET}" || echo "${C_RED}OFFLINE / AIRGAPPED${C_RESET}")
echo -e " ${C_GREEN}[RUNTIME]${C_RESET}   : Py ${PY_VER} (Web3 ${WEB3_PY}) | Node ${NODE_VER} (Hardhat ${HARDHAT_VER})"
echo -e " ${C_GREEN}[UPLINK]${C_RESET}    : ${NET_STR}"
echo -e "${C_DIM} [MODES]     : status | status --clean | status --seal | status --watch | status --install-hook | status --export${C_RESET}"
echo -e "${C_CYAN}=====================================================================${C_RESET}"
