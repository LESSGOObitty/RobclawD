#!/usr/bin/env zsh
KEY_PATH="$HOME/.ssh/id_ed25519_lessgoobitty"

echo "[*] Ensuring correct SSH config format for host aliasing..."
cat << EOT > "$HOME/.ssh/config"
Host github.com-lessgoobitty
    HostName github.com
    User git
    IdentityFile $KEY_PATH
    IdentitiesOnly yes
EOT
chmod 600 "$HOME/.ssh/config"

echo "[*] Testing key fingerprint against GitHub alias..."
ssh -Tv -i "$KEY_PATH" -o StrictHostKeyChecking=accept-new git@github.com-lessgoobitty || true

echo "[*] Cloning repository using explicit SSH alias URL..."
rm -rf likec4Robdoe
git clone git@github.com-lessgoobitty:backupsonbackupsrobby-cyber/likec4Robdoe.git

echo "====================================================================="
echo " [STATUS] Clone sequence dispatched, brother."
echo "====================================================================="
