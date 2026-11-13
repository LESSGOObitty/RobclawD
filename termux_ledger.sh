#!/usr/bin/env zsh
set -euo pipefail

LEDGER=".telemetry_ledger.jsonl"
CMD="${1:-inspect}"

if [ ! -f "${LEDGER}" ]; then
    echo "[!] Error: No ledger found at ${LEDGER}"
    exit 1
fi

case "${CMD}" in
    inspect)
        echo "====================================================="
        echo " [LEDGER INSPECTOR] Total Records: $(wc -l < "${LEDGER}" | tr -d ' ')"
        echo "====================================================="
        python3 -c '
import json, sys
with open(".telemetry_ledger.jsonl") as f:
    for i, line in enumerate(f, 1):
        d = json.loads(line)
        print(f"[{i:02d}] Span: {d.get("span_blocks")} | Blocks: {d.get("total_blocks")} | Txs: {d.get("total_transactions")}")
        top = d.get("miner_distribution", [{}])[0]
        print(f"     Top Miner: {top.get("miner")} ({top.get("share_pct")}%)")
'
        ;;
    tail)
        tail -n 5 "${LEDGER}"
        ;;
    purge)
        > "${LEDGER}"
        echo "[+] Ledger truncated and purged."
        ;;
    *)
        echo "Usage: termux_ledger [inspect|tail|purge]"
        ;;
esac
