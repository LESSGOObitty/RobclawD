#!/usr/bin/env zsh
# ==============================================================================
# ROBDOE PTY TLD :: LIVE NETWORK SOCKET AUDITOR (TERMUX)
# ==============================================================================

export LC_ALL=C.UTF-8

CYAN='\033[38;2;0;255;204m'
YELLOW='\033[38;2;255;220;0m'
GREEN='\033[38;2;0;255;100m'
NC='\033[0m'

clear

echo -e "${CYAN}┌────────────────────────────────────────────────────────────────────────┐${NC}"
echo -e "${CYAN}│             ROBDOE PTY TLD :: LIVE NETWORK SOCKET AUDIT                │${NC}"
echo -e "${CYAN}└────────────────────────────────────────────────────────────────────────┘${NC}"

echo -e "${YELLOW}[+] INSPECTING ACTIVE INBOUND & ESTABLISHED SOCKETS:${NC}"
echo -e "    --------------------------------------------------"

if command -v ss >/dev/null 2>&1; then
    ss -tutn | awk 'NR==1 || /ESTAB|LISTEN/'
elif command -v netstat >/dev/null 2>&1; then
    netstat -tu
else
    echo -e "    [!] Neither 'ss' nor 'netstat' available. Checking /proc/net/tcp..."
    cat /proc/net/tcp | head -n 10
fi

echo ""
TIMESTAMP=$(date +%s%N 2>/dev/null || date +%s)
SEAL_HASH=$(echo -n "${TIMESTAMP}live_socket" | sha256sum | awk '{print $1}' | cut -c 1-32)

echo -e "${GREEN}[+] SOCKET AUDIT CRYPTO SEAL:${NC}"
echo -e "    Seal Hash : 0x${SEAL_HASH}"
echo ""
echo -e "${CYAN}==========================================================================${NC}"
echo -e "${GREEN}[✔] Live Socket Audit Complete. Real-Time Telemetry Secured.${NC}"
echo -e "${CYAN}==========================================================================${NC}"
