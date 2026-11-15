#!/data/data/com.termux/files/usr/bin/zsh
export PATH="/data/data/com.termux/files/usr/bin:$PATH"
termux-wake-lock

SEMA_DIR="$HOME/workspace/RobDoeAI-Core/sema_mesh"

while true; do
  python3 "$SEMA_DIR/engine/sema_engine.py"
  sleep 3600
done
