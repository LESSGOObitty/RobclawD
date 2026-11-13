#!/usr/bin/env zsh
# Safe execution script - prevents shell exit on error

echo "[*] Checking SSH key status..."
KEY_PATH="$HOME/.ssh/id_ed25519_lessgoobitty"

if [ ! -f "$KEY_PATH" ]; then
    echo "[!] Error: SSH key not found at $KEY_PATH"
    echo "[*] Please generate or place your key there first."
    exit 1
fi

echo "[*] Ensuring SSH agent is running..."
eval "$(ssh-agent -s)" || true
ssh-add "$KEY_PATH" || true

echo "[*] Attempting clone of likec4Robdoe..."
git clone git@github.com-lessgoobitty:backupsonbackupsrobby-cyber/likec4Robdoe.exit 2>/dev/null || \
git clone git@github.com-lessgoobitty:backupsonbackupsrobby-cyber/likec4Robdoe.git

if [ $? -eq 0 ]; then
    echo "[+] Clone successful!"
else
    echo "[!] Clone failed with exit code $?. Check your repository access rights or URL."
fi

echo "====================================================================="
echo " [READY] Session kept alive. Press Enter or run commands freely."
echo "====================================================================="
