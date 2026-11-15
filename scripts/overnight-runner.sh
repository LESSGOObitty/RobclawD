#!/data/data/com.termux/files/usr/bin/zsh
exec > ~/workspace/mesh-execution.log 2>&1
echo "=== Overnight Node Run Started: $(date) ==="
termux-wake-lock

cd ~/workspace/RobDoeAI-Core || exit 1
while true; do
  git fetch --all --prune
  python3 ~/scripts/mesh-router.py
  sleep 3600 # 1-hour cycle
done
