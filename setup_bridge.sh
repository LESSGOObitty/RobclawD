#!/usr/bin/env zsh
unsetopt bang_hist
unsetopt nomatch

mkdir -p ~/bridge
rm -f ~/bridge/event_channel
mkfifo ~/bridge/event_channel

cat << 'INNER_EOF' > ~/bridge/bridge_daemon.py
import os
import sys
import time

PIPE_PATH = os.path.expanduser("~/bridge/event_channel")

print(f"[+] Bridge Active on: {PIPE_PATH}")
print("[+] Listening for local/serial event streams...")

while True:
    try:
        with open(PIPE_PATH, "r") as pipe:
            for line in pipe:
                line = line.strip()
                if line:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"[{timestamp}] [BRIDGE OUT] -> {line}")
    except Exception as e:
        print(f"[!] Pipe error: {e}")
        time.sleep(1)
INNER_EOF

cat << 'INNER_EOF' > ~/.tmux.conf
set -g mouse on
set -g status-style bg=black,fg=cyan
set -g status-left '#[fg=green][#S] '
set -g status-right '#[fg=yellow]%Y-%m-%d %H:%M:%S'
set -g history-limit 50000
set -g base-index 1
setw -g pane-base-index 1
INNER_EOF

echo 'unsetopt bang_hist' >> ~/.zshrc
echo 'unsetopt nomatch' >> ~/.zshrc
echo 'alias bridge-listen="python3 ~/bridge/bridge_daemon.py"' >> ~/.zshrc
echo 'alias send-event="echo \$1 > ~/bridge/event_channel"' >> ~/.zshrc

echo "[+] Setup complete."
