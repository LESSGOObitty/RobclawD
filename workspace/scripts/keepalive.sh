#!/data/data/com.termux/files/usr/bin/sh
echo "[*] Requesting Android Wake-Lock to protect background daemons..."
termux-wake-lock

echo "[*] Current Wake-Lock Status:"
termux-wake-lock -v 2>/dev/null || echo "Wake-lock active (termux-api active)."

echo "[*] Checking battery optimization settings..."
echo "    Tip: Ensure Termux is set to 'Unrestricted' battery mode in Android Settings."
