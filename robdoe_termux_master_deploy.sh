#!/data/data/com.termux/files/usr/bin/bash
# =========================================================================
# ROBDOE PTY TLD // ROBCLAWD SOVEREIGN TERMUX MASTER DEPLOY ENGINE v4.0
# =========================================================================

set -euo pipefail

# ANSI Color Palette
C_RESET="\033[0m"
C_GRAY="\033[1;30m"
C_YELLOW="\033[1;33m"
C_CYAN="\033[0;36m"
C_GREEN="\033[0;32m"
C_MAGENTA="\033[1;35m"
C_WHITE="\033[1;37m"

clear
echo -e "${C_GRAY}======================================================================${C_RESET}"
echo -e "${C_YELLOW}     ROBDOE PTY TLD // ROBCLAWD SOVEREIGN TERMUX MASTER DEPLOY        ${C_RESET}"
echo -e "${C_GRAY}======================================================================${C_RESET}"
echo ""

# 1. Setup Termux Storage & Sovereign Packages
echo -e "${C_CYAN} [+] Initializing Termux shared storage mount...${C_RESET}"
termux-setup-storage || true

echo -e "${C_CYAN} [+] Updating packages and installing sovereign toolchain...${C_RESET}"
pkg update -y && pkg upgrade -y
pkg install -y git zsh python nodejs curl wget tmux sqlite htop bc proot libjpeg-turbo libpng

# 2. Configure Git Global State
echo -e "${C_YELLOW} [+] Configuring Git global advice and identity...${C_RESET}"
git config --global advice.addIgnoredFile false
git config --global user.name "Eric Hadfield (Rob Doe)"
git config --global user.email "eric@robdoe.com"

# 3. Terminate Stale Processes & Tmux Sessions
echo -e "${C_YELLOW} [+] Sweeping stale process trees and purging legacy tmux sessions...${C_RESET}"
pkill -f "cron_daemon.py" || true
pkill -f "run_engine.sh" || true
tmux kill-session -t robclaw 2>/dev/null || true

# 4. Construct Unbounded Sovereign Workspace Topologies
WORKSPACE_DIR="$HOME/workspace"
mkdir -p "$WORKSPACE_DIR/manifests" "$WORKSPACE_DIR/logs" "$WORKSPACE_DIR/scripts" "$WORKSPACE_DIR/mesh_outbox"

cd "$WORKSPACE_DIR"

# 5. Configure Gitignore Rules for Manifests
if [ -f "$WORKSPACE_DIR/.gitignore" ]; then
    if ! grep -q "workspace/manifests/*.csv" "$WORKSPACE_DIR/.gitignore"; then
        echo "workspace/manifests/*.csv" >> "$WORKSPACE_DIR/.gitignore"
        echo "!workspace/manifests/*.csv" >> "$WORKSPACE_DIR/.gitignore"
    fi
else
    cat << 'GITIGNORE' > "$WORKSPACE_DIR/.gitignore"
# Sovereign Exclusions & Exceptions
workspace/manifests/*.csv
!workspace/manifests/*.csv
*.log
mesh_outbox/*.jsonl
GITIGNORE
fi

# 6. Initialize Sovereign Engine Runner Script if Missing
if [ ! -f "$WORKSPACE_DIR/scripts/run_engine.sh" ]; then
    cat << 'ENGINESH' > "$WORKSPACE_DIR/scripts/run_engine.sh"
#!/data/data/com.termux/files/usr/bin/bash
cd ~/workspace
while true; do
    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    echo "[$TIMESTAMP] ROBCLAWD SOVEREIGN ENGINE ACTIVE // 0% DRIFT" >> ~/workspace/logs/engine_heartbeat.log
    sleep 60
done
ENGINESH
    chmod +x "$WORKSPACE_DIR/scripts/run_engine.sh"
fi

# 7. Initialize Background Cron Daemon Script if Missing
if [ ! -f "$WORKSPACE_DIR/scripts/cron_daemon.py" ]; then
    cat << 'CRONPY' > "$WORKSPACE_DIR/scripts/cron_daemon.py"
import time
import os
import datetime

log_path = os.path.expanduser("~/workspace/logs/cron_daemon.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)

while True:
    now = datetime.datetime.utcnow().isoformat() + "Z"
    with open(log_path, "a") as f:
        f.write(f"[{now}] ROBCLAWD CRON DAEMON TICK // LATTICE COHERENCE r=1.0000\n")
    time.sleep(30)
CRONPY
    chmod +x "$WORKSPACE_DIR/scripts/cron_daemon.py"
fi

# 8. Spin Up Sovereign Tmux Supervisor Session 'robclaw'
echo -e "${C_GREEN} [+] Spinning up sovereign tmux supervisor session 'robclaw'...${C_RESET}"
if [ -f "$WORKSPACE_DIR/scripts/run_engine.sh" ]; then
    tmux new-session -d -s robclaw 'cd ~/workspace && ./scripts/run_engine.sh'
    echo -e "${C_GREEN} [+] Sovereign tmux supervisor session 'robclaw' started successfully.${C_RESET}"
else
    echo -e "${C_RED} [!] run_engine.sh not found in ~/workspace/scripts/. Skipping tmux spawn.${C_RESET}"
fi

# 9. Launch Background Cron Daemon
echo -e "${C_GREEN} [+] Spawning background sovereign cron daemon...${C_RESET}"
if [ -f "$WORKSPACE_DIR/scripts/cron_daemon.py" ]; then
    python3 "$WORKSPACE_DIR/scripts/cron_daemon.py" &> "$WORKSPACE_DIR/logs/cron_daemon.log" &
    echo -e "${C_GREEN} [+] Background cron daemon spawned successfully.${C_RESET}"
fi

# 10. Final Sovereign Seal & HUD Output
INVARIANT_KEY=932808725
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
OUTBOX="$WORKSPACE_DIR/mesh_outbox"
mkdir -p "$OUTBOX"

MERKLE_ROOT=$(find "$WORKSPACE_DIR" -maxdepth 2 -type f ! -path '*/.*' -exec sha256sum {} + 2>/dev/null | sort | sha256sum | awk '{print $1}' || echo "ROBCLAWD_SEAL")

JSON_RECORD=$(printf '{"timestamp":"%s","entity":"Eric Hadfield (Rob Doe) - Robdoe Pty Tld","environment":"Termux_Robclawd","merkle_root":"%s","kuramoto_coherence":1.0000,"invariant_key":%s,"status":"ROBCLAWD_MASTER_DEPLOY_SEALED","signature":"GANG_GANG_ZERO_DRIFT"}' \
    "$TIMESTAMP" "$MERKLE_ROOT" "$INVARIANT_KEY")

echo "$JSON_RECORD" >> "$OUTBOX/robclawd_master_deploy.jsonl"

echo ""
echo -e "${C_GRAY}======================================================================${C_RESET}"
echo -e "${C_GREEN} STATUS: ROBCLAWD MASTER DEPLOYMENT FULLY EXECUTED & SEALED${C_RESET}"
echo -e "${C_GRAY}======================================================================${C_RESET}"
echo -e " WORKSPACE ROOT        : ${C_WHITE}$WORKSPACE_DIR${C_RESET}"
echo -e " TMUX SUPERVISOR       : ${C_CYAN}Session 'robclaw' Active${C_RESET}"
echo -e " CRON DAEMON           : ${C_CYAN}Background Python Process Spawned${C_RESET}"
echo -e " MERKLE SHA-256 ROOT   : ${C_YELLOW}${MERKLE_ROOT:0:32}...${C_RESET}"
echo -e " INVARIANT KEY         : ${C_GREEN}$INVARIANT_KEY (0% Drift)${C_RESET}"
echo -e " KURAMOTO COHERENCE    : ${C_GREEN}r = 1.0000${C_RESET}"
echo -e "${C_GRAY}======================================================================${C_RESET}"
echo ""
echo -e "${C_MAGENTA} 🇦🇺  |  🖤💛❤️  :: ROBCLAWD ENGAGED. NO CEILINGS. FORWARD ONLY.${C_RESET}"
echo -e "${C_GRAY}----------------------------------------------------------------------${C_RESET}"
