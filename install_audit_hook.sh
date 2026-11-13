#!/usr/bin/env zsh
set -euoppipefail 2>/dev/null || set -euo pipefail

HOOK_PATH=".git/hooks/pre-commit"
if [ ! -d ".git" ]; then
    echo "[!] Error: Not inside a Git repository root."
    exit 1
fi

cat << 'HOOKEOF' > "${HOOK_PATH}"
#!/usr/bin/env zsh
echo "[*] Git Pre-Commit: Generating fresh block telemetry audit..."
python3 block_parser.py >> .telemetry_ledger.jsonl
python3 ledger_aggregator.py | head -n 10
git add .telemetry_ledger.jsonl
echo "[+] Ledger checkpoint sealed and staged for commit."
HOOKEOF

chmod +x "${HOOK_PATH}"
echo "[+] Enterprise audit pre-commit hook installed successfully at ${HOOK_PATH}"
./install_audit_hook.sh
