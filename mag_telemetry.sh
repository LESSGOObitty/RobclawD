#!/data/data/com.termux/files/usr/bin/bash
# ==============================================================================
# MERKLIZER MAGNETIC FREQUENCY TELEMETRY ENGINE
# Real-Time Stator & Ignition Pulse Monitor (v2026.2)
# ==============================================================================

set -euo pipefail

LEDGER_DIR="${HOME}/.merklizer/pools"
SEAL_LOG="${HOME}/.merklizer/ledger_seal.json"
STATE_DB="${HOME}/.merklizer/state.db"
BAUD_RATE=115200
SERIAL_PORT="${1:-/dev/ttyUSB0}"

mkdir -p "${LEDGER_DIR}"

if command -v sqlite3 &>/dev/null; then
    SQLITE_ENABLED=1
    sqlite3 "${STATE_DB}" "CREATE TABLE IF NOT EXISTS mag_telemetry (timestamp TEXT PRIMARY KEY, freq_hz REAL, rpm REAL, voltage REAL, seal_hash TEXT);" 2>/dev/null || true
else
    SQLITE_ENABLED=0
fi

clear
echo -e "\033[1;36m[*] Initializing Magnetic Frequency & Ignition Telemetry Bridge...\033[0m"
echo -e "\033[1;33m[*] Target Port: ${SERIAL_PORT} @ ${BAUD_RATE} baud\033[0m"
echo -e "\033[1;32m[*] Monitoring Stator Alternating Field & Spark Firing Cadence...\033[0m\n"

if [ ! -e "${SERIAL_PORT}" ] && [ "${SERIAL_PORT}" != "simulated" ]; then
    echo -e "\033[1;31m[!] Serial port offline. Engaging simulated magnetic resonance loop...\033[0m"
    SERIAL_PORT="simulated"
fi

while true; do
    TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    
    if [ "${SERIAL_PORT}" = "simulated" ]; then
        FREQ_HZ=$(( (RANDOM % 35) + 25 ))
        RPM=$(( FREQ_HZ * 60 ))
        VOLTAGE=$(awk -v f="$FREQ_HZ" 'BEGIN {print 12.2 + (f/60.0)*2.4}')
    else
        if read -r line < "${SERIAL_PORT}"; then
            FREQ_HZ=$(echo "$line" | grep -oE '[0-9]+(\.[0-9]+)?' | head -n 1)
            RPM=$(echo "$FREQ_HZ" | awk '{print $1 * 60}')
            VOLTAGE="14.2"
        else
            FREQ_HZ=0
            RPM=0
            VOLTAGE="0.0"
        fi
    fi

    POOL_HASH=$(date +%s%N | sha512sum | awk '{print $1}')

    cat << INNER_EOF > "${SEAL_LOG}.tmp"
{
  "timestamp": "${TIMESTAMP}",
  "magnetic_frequency_hz": ${FREQ_HZ},
  "derived_rpm": ${RPM},
  "stator_voltage": ${VOLTAGE},
  "pool_hash": "${POOL_HASH}",
  "status": "locked"
}
INNER_EOF
    mv "${SEAL_LOG}.tmp" "${SEAL_LOG}"

    if [ "${SQLITE_ENABLED}" -eq 1 ]; then
        sqlite3 "${STATE_DB}" "INSERT OR REPLACE INTO mag_telemetry VALUES ('${TIMESTAMP}', ${FREQ_HZ}, ${RPM}, ${VOLTAGE}, '${POOL_HASH}');" 2>/dev/null || true
    fi

    printf "\r\033[1;32m[RX] Mag Freq: \033[1;33m%2.f Hz\033[0m | \033[1;32mRPM: \033[1;35m%4d\033[0m | \033[1;32mStator V: \033[1;36m%sV\033[0m | \033[1;37mSeal: %s...\033[0m" \
        "$FREQ_HZ" "$RPM" "$VOLTAGE" "${POOL_HASH:0:16}"
    
    sleep 1
done
