#!/data/data/com.termux/files/usr/bin/zsh
BACKUP_DIR="$HOME/storage/shared/Download/TermuxBackups"
mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ARCHIVE_NAME="termux_backup_$TIMESTAMP.tar.gz"

echo "📦 Packaging Termux workspace & dotfiles..."
tar -czf "$BACKUP_DIR/$ARCHIVE_NAME" \
  -C "$HOME" \
  .zshrc .termux scripts workspace \
  --exclude=".venv" \
  --exclude="node_modules" 2>/dev/null

echo "✅ Backup saved to: Download/TermuxBackups/$ARCHIVE_NAME"
