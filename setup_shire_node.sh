#!/usr/bin/env zsh
unsetopt bang_hist
unsetopt nomatch

mkdir -p ~/bridge
rm -f ~/bridge/event_channel
mkfifo ~/bridge/event_channel

cat << 'INNER_EOF' > ~/bridge/shire_fractal_node.py
import os
import sys
import time
import math
import cmath

PIPE_PATH = os.path.expanduser("~/bridge/event_channel")
print(f"[+] SHIRE MESH NODE ACTIVE: {PIPE_PATH}")
print("[+] Listening for event streams & computing fractal state...\n")

def compute_shire_fractal(z_val, m_val):
    # z = z^2 + exp(M^2)
    m_sq = m_val ** 2
    e_m2 = cmath.exp(m_sq)
    return (z_val ** 2) + e_m2

z = complex(0, 0)
m = complex(0.5, 0.866)

while True:
    try:
        # Calculate iteration
        z = compute_shire_fractal(z, m)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Reset if exploding to prevent overflow
        if abs(z) > 1e10:
            z = complex(0.1, 0.1)

        # Read pipe non-blocking if data exists, else push fractal iteration
        if os.path.exists(PIPE_PATH):
            with open(PIPE_PATH, "r") as pipe:
                for line in pipe:
                    line = line.strip()
                    if line:
                        print(f"[{timestamp}] [FIFO RECV] -> {line}")
                        print(f"[{timestamp}] [FRACTAL STATE] -> z = {z:.4f}, |z| = {abs(z):.4f}")
    except Exception as e:
        time.sleep(1)
INNER_EOF

cat << 'INNER_EOF' > ~/.zshrc
unsetopt bang_hist
unsetopt nomatch
export PATH="$HOME/.local/bin:$PREFIX/bin:$PATH"
alias shire-node="python3 ~/bridge/shire_fractal_node.py"
alias send-event="echo \$1 > ~/bridge/event_channel"
INNER_EOF

echo "[+] Sovereign Shire setup successfully generated."
