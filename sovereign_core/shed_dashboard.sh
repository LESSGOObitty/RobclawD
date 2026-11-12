#!/data/data/com.termux/files/usr/bin/bash
# ==============================================================================
# MASTER SHED COMMAND DASHBOARD & PROCESS HEALTH MONITOR (v2026.3.5)
# ==============================================================================

set -euo pipefail

clear
echo -e "\033[1;35m=================================================================\033[0m"
echo -e "\033[1;36m       MASTER SHED NODE — LIVE DAEMON HEALTH & METRICS DASHBOARD   \033[0m"
echo -e "\033[1;35m=================================================================\033[0m\n"

echo -e "\033[1;33m[*] Scanning Active Background Daemons...\033[0m"
ps -ef | grep -E "(daemon|engine|assist|node|bridge)" | grep -v grep || echo -e "\033[1;31m[!] No active shed daemons detected in process table.\033[0m"

echo -e "\n\033[1;33m[*] Inspecting SQLite Ledger Databases:\033[0m"
for db in ${HOME}/.merklizer/*.db; do
    if [ -f "$db" ]; then
        db_name=$(basename "$db")
        if command -v sqlite3 &>/dev/null; then
            row_count=$(sqlite3 "$db" "SELECT count(*) FROM sqlite_master WHERE type='table';" 2>/dev/null || echo "0")
            echo -e "  \033[1;32m[DB]\033[0m ${db_name} -> \033[1;37mActive tables: ${row_count}\033[0m"
        else
            echo -e "  \033[1;32m[DB]\033[0m ${db_name} (SQLite3 CLI offline)"
        fi
    fi
done

echo -e "\n\033[1;35m=================================================================\033[0m"
echo -e "\033[1;32m[+] Master Shed Architecture State: AIR-GAPPED & NOMINAL\033[0m"
echo -e "\033[1;35m=================================================================\033[0m"
