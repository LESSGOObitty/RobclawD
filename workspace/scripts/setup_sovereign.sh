#!/data/data/com.termux/files/usr/bin/sh

echo "[*] Initializing sovereign environment enhancements..."

# 1. Ensure required terminal packages are present
pkg install -y fzf git-delta jq htop tmux sqlite python-pip >/dev/null 2>&1

# 2. Configure robust Zsh profile extensions (~/.zshrc additions)
ZSHRC="$HOME/.zshrc"

# Check if enhancements already exist
if ! grep -q "ROBCLAWD SOVEREIGN CONFIG" "$ZSHRC"; then
cat << 'EOT' >> "$ZSHRC"

# ==========================================
# ROBCLAWD SOVEREIGN CONFIG & ALIASES
# ==========================================
export WORKSPACE="$HOME/workspace"
export PATH="$WORKSPACE/scripts:$PATH"

# Prompt & History Tuning
HISTSIZE=10000
SAVEHIST=10000
setopt appendhistory
setopt sharehistory

# Quick Navigation Aliases
alias ws='cd ~/workspace'
alias scripts='cd ~/workspace/scripts'
alias logs='cd ~/workspace/logs'

# Sovereign Engine & Telemetry Aliases
alias engine-health='ps aux | grep -E "cron_daemon|esp32_vault|run_engine" | grep -v grep'
alias git-guardian='python3 ~/workspace/scripts/git_guardian.py'
alias node-pulse='python3 ~/workspace/scripts/node_pulse.py'
alias esp32-vault='sqlite3 ~/workspace/data/telemetry.db "SELECT * FROM telemetry ORDER BY id DESC LIMIT 15;"'
alias robcron='python3 ~/workspace/scripts/cron_daemon.py &> ~/workspace/logs/cron_daemon.log & echo "[+] Cron daemon spawned in background."'

# Enable colored output for core utils
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
EOT
    echo "[+] Appended sovereign configuration to ~/.zshrc"
else
    echo "[*] Sovereign config already present in ~/.zshrc"
fi

echo "[+] Sovereign environment setup complete. Run 'source ~/.zshrc' to apply."
