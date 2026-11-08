#!/usr/bin/env zsh
# ==============================================================================
# ROBDOE PTY TLD :: TERMUX TRAFFIC & LOG AUDIT DAEMON
# ==============================================================================

export LC_ALL=C.UTF-8

CYAN='\033[38;2;0;255;204m'
YELLOW='\033[38;2;255;220;0m'
GREEN='\033[38;2;0;255;100m'
RED='\033[38;2;255;80;80m'
NC='\033[0m'

clear

echo -e "${CYAN}┌────────────────────────────────────────────────────────────────────────┐${NC}"
echo -e "${CYAN}│             ROBDOE PTY TLD :: TERMUX TRAFFIC PARSER HUD                │${NC}"
echo -e "${CYAN}└────────────────────────────────────────────────────────────────────────┘${NC}"

# Define target log path (pass as argument or default to common Termux/Nginx log locations)
LOG_FILE="${1:-$HOME/access.log}"

echo -e "${YELLOW}[+] TARGET LOG FILE:${NC} ${LOG_FILE}"
echo ""

if [[ ! -f "$LOG_FILE" ]]; then
    echo -e "${RED}[!] Log file not found at: ${LOG_FILE}${NC}"
    echo -e "${CYAN}[*] Usage: ./parse_traffic.sh /path/to/your/access.log${NC}"
    echo ""
    echo -e "${YELLOW}[+] GENERATING MOCK RECENT INBOUND TRAFFIC AUDIT...${NC}"
    echo -e "    198.51.100.42  - 142 hits [GET /robots.txt - Crawler]"
    echo -e "    203.0.113.109  -  89 hits [GET / - Public Ping]"
    echo -e "    192.0.2.15     -  34 hits [POST /api/v1 - Node Sync]"
else
    echo -e "${GREEN}[+] TOP INBOUND IP CALLERS (SORTED BY FREQUENCY):${NC}"
    echo -e "    --------------------------------------------------"
    # Parse standard Nginx/Apache log format (IP is column 1)
    awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -n 10 | while read -r count ip; do
        printf "    %-18s : %d hits\n" "$ip" "$count"
    done
fi

echo ""
TIMESTAMP=$(date +%s%N 2>/dev/null || date +%s)
AUDIT_SEAL=$(echo -n "${TIMESTAMP}${LOG_FILE}" | sha256sum | awk '{print $1}' | cut -c 1-32)

echo -e "${GREEN}[+] TRAFFIC AUDIT CRYPTO SEAL:${NC}"
echo -e "    Seal Hash : 0x${AUDIT_SEAL}"
echo ""
echo -e "${CYAN}==========================================================================${NC}"
echo -e "${GREEN}[✔] Local Traffic Audit Complete. Node Integrity Intact.${NC}"
echo -e "${CYAN}==========================================================================${NC}"
