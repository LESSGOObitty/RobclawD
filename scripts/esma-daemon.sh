#!/data/data/com.termux/files/usr/bin/zsh
export PATH="/data/data/com.termux/files/usr/bin:$PATH"
BASE_DIR="$HOME/workspace/RobDoeAI-Core"

termux-wake-lock
cd "$BASE_DIR" || exit 1

while true; do
  git fetch --all --prune >> "$BASE_DIR/logs/git_sync.log" 2>&1 || true
  python3 "$BASE_DIR/engine/esma_engine.py"
  sleep 3600
done
