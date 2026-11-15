#!/data/data/com.termux/files/usr/bin/zsh
echo "🧹 Starting Termux Workspace & Log Prune..."

# 1. Truncate / Clear large SEMA/EVM execution logs
if [ -d "$HOME/workspace/RobDoeAI-Core" ]; then
  echo "[-] Truncating execution logs..."
  find "$HOME/workspace/RobDoeAI-Core" -name "*.log" -exec truncate -s 0 {} \;
  echo "[+] Logs cleared."
fi

# 2. Clean Package & Pip Caches
echo "[-] Cleaning package manager and pip caches..."
pkg clean -y
pip cache purge 2>/dev/null || true

# 3. Display current storage usage
echo "========================================="
echo "📊 Current Storage Status (~/workspace):"
df -h $HOME
echo "========================================="
echo "✅ Termux maintenance complete!"
