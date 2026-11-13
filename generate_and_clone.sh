#!/usr/bin/env zsh
KEY_PATH="$HOME/.ssh/id_ed25519_lessgoobitty"
EMAIL="Robdoeaiagency101tenet@gmail.com"

echo "[*] Creating .ssh directory if needed..."
mkdir -p "$HOME/.ssh"
chmod 700 "$HOME/.ssh"

echo "[*] Generating Ed25519 SSH key for LESSGOOBITTY..."
ssh-keygen -t ed25519 -C "$EMAIL" -f "$KEY_PATH" -N ""

echo "[*] Configuring SSH host alias..."
cat << EOT > "$HOME/.ssh/config"
Host github.com-lessgoobitty
    HostName github.com
    User git
    IdentityFile $KEY_PATH
    IdentitiesOnly yes
EOT
chmod 600 "$HOME/.ssh/config"

echo "[*] Starting SSH agent and adding key..."
eval "$(ssh-agent -s)" || true
ssh-add "$KEY_PATH" || true

echo "[*] Attempting repository clone..."
git clone git@github.com-lessgoobitty:backupsonbackupsrobby-cyber/likec4Robdoe.git || true

echo "====================================================================="
echo " [PUBLIC KEY] Copy this public key to your GitHub account (LESSGOOBITTY):"
echo "---------------------------------------------------------------------"
cat "${KEY_PATH}.pub"
echo "====================================================================="
