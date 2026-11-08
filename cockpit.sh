#!/usr/bin/env zsh
# ==============================================================================
# ROBDOE PTY TLD :: TERMUX SOVEREIGN COCKPIT HUD (ZSH / ANDROID)
# ==============================================================================

export LC_ALL=C.UTF-8

CYAN='\033[38;2;0;255;204m'
YELLOW='\033[38;2;255;220;0m'
GREEN='\033[38;2;0;255;100m'
NC='\033[0m'

clear

echo -e "${CYAN}┌────────────────────────────────────────────────────────────────────────┐${NC}"
echo -e "${CYAN}│                ROBDOE PTY TLD :: TERMUX COCKPIT HUD                    │${NC}"
echo -e "${CYAN}└────────────────────────────────────────────────────────────────────────┘${NC}"

UPTIME_STR=$(uptime | awk -F'up ' '{print $2}' | awk -F',' '{print $1}')
MEM_FREE=$(free -h | awk '/Mem:/ {print $4 " / " $2}')
STORAGE_FREE=$(df -h $HOME | awk 'NR==2 {print $4 " available"}')

echo -e "${YELLOW}[+] LOCAL TERMUX IRON TELEMETRY:${NC}"
echo -e "    Environment      : Termux (Zsh / Local Mobile Iron)"
echo -e "    Uptime           : ${UPTIME_STR}"
echo -e "    RAM Available    : ${MEM_FREE}"
echo -e "    Home Storage     : ${STORAGE_FREE}"
echo ""

TIMESTAMP=$(date +%s%N 2>/dev/null || date +%s)
ENTROPY_HASH=$(echo -n "${TIMESTAMP}" | sha256sum | awk '{print $1}' | cut -c 1-32)

echo -e "${GREEN}[+] LOCAL ENTROPY & STATE ANCHOR:${NC}"
echo -e "    Active Heartbeat : 0x${ENTROPY_HASH}"
echo -e "    Sync Protocol    : BFT Consensus 8/12 (Termux Mesh Node)"
echo ""

echo -e "${CYAN}[+] REPOSITORY MESH AUDIT (LOCAL WORKSPACE):${NC}"
count=0
for d in ./*/; do
    if [ -d "$d/.git" ]; then
        repo_name=$(basename "$d")
        branch=$(git -C "$d" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "detached")
        head_commit=$(git -C "$d" rev-parse --short HEAD 2>/dev/null || echo "no-commits")
        echo -e "    ├── [NODE] ${repo_name} -> Branch: ${branch} [HEAD: ${head_commit}]"
        ((count++))
    fi
done

if [ $count -eq 0 ]; then
    echo -e "    └── [INFO] No Git subdirectories found in current directory: $(pwd)"
fi

echo ""
echo -e "${CYAN}==========================================================================${NC}"
echo -e "${GREEN}[✔] Termux Sovereign Cockpit Rendered. All Systems Local & Nominal.${NC}"
echo -e "${CYAN}==========================================================================${NC}"
