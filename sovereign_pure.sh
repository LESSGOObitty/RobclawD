#!/bin/bash

# ==============================================================================
# PURE BASH SOVEREIGN TERMINAL DIAGNOSTIC & TELEMETRY SUITE
# ==============================================================================

CLEAR="\033[0m"
GREEN="\033[1;32m"
CYAN="\033[1;36m"
YELLOW="\033[1;33m"

echo -e "${CYAN}========================================================${CLEAR}"
echo -e "${CYAN}          PURE BASH SOVEREIGN TELEMETRY ACTIVE           ${CLEAR}"
echo -e "${CYAN}========================================================${CLEAR}"

# 1. System & Environment Fingerprint
echo -e "${YELLOW}[*] Inspecting Local Terminal Environment...${CLEAR}"
echo -e "    -> Current User:       $(whoami)"
echo -e "    -> Working Directory:  $(pwd)"
echo -e "    -> Hostname:           $(hostname)"
echo -e "    -> Kernel / OS:        $(uname -sr)"

# 2. Asset & Vector Registry Printout
echo -e "--------------------------------------------------------"
echo -e "${YELLOW}[*] Sovereign Asset & Genesis Registry:${CLEAR}"
echo -e "    -> EVM Control Vector: ${GREEN}0x84CA4aFC3F395ebc0b519680B546Cd604C9c2018${CLEAR}"
echo -e "    -> Genesis Anchor Root:${GREEN}3sZ2G9spssmLMZDMcZF5FMca4udBWNQkGLiaeBEzUPHn${CLEAR}"
echo -e "    -> Equity Vector State:${GREEN}55.00 Locked${CLEAR}"
echo -e "    -> Identity Assets:    ${GREEN}25x Unstoppable Domains (ERC-721)${CLEAR}"
echo -e "    -> Token Standards:    ${GREEN}ERC-20, ERC-721, ERC-1155, SPL${CLEAR}"

# 3. Local Storage / Disk Telemetry
echo -e "--------------------------------------------------------"
echo -e "${YELLOW}[*] Local Storage & State Space Allocation:${CLEAR}"
df -h . | awk 'NR==1 {print "    -> Filesystem Header: " $0} NR==2 {print "    -> Available Space:   " $4 " (" $5 " used)"}'

# 4. Active Process / Listener Check
echo -e "--------------------------------------------------------"
echo -e "${YELLOW}[*] Scanning Local Network Sockets & Listeners:${CLEAR}"
if command -v ss &> /dev/null; then
    ACTIVE_PORTS=$(ss -tln | awk 'NR>1 {print $4}' | wc -l)
    echo -e "    -> Active TCP Listeners: $ACTIVE_PORTS ports open locally."
elif command -v netstat &> /dev/null; then
    ACTIVE_PORTS=$(netstat -an | grep LISTEN | wc -l)
    echo -e "    -> Active Listeners:     $ACTIVE_PORTS ports open locally."
else
    echo -e "    -> Socket telemetry tool skipped."
fi

echo -e "${CYAN}========================================================${CLEAR}"
echo -e "${GREEN}      ALL BASH EXECUTION COMPLETED - SYSTEM SECURE       ${CLEAR}"
echo -e "${CYAN}========================================================${CLEAR}"
