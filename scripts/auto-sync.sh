#!/data/data/com.termux/files/usr/bin/zsh
cd ~/workspace/RobDoeAI-Core || exit 1

while true; do
  echo "[$(date)] Running automated sync..." >> ~/workspace/sync.log
  git fetch --all --prune >> ~/workspace/sync.log 2>&1
  git pull --rebase origin main >> ~/workspace/sync.log 2>&1
  sleep 3600 # Repeats every 1 hour
done
