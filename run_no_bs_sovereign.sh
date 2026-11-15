#!/data/data/com.termux/files/usr/bin/env bash
# ==============================================================================
# ROBDOE PTY TLD :: NO-BS DIRECT SOVEREIGN EXECUTION (TERMUX BASH)
# Protocol: Zero Red Tape // Pure Mathematical & Financial Custody
# Identity Matrix : THE EMU & THE KANGAROO [MAURI & MANA IN PERPETUUM]
# ==============================================================================

set -euo pipefail

WORKSPACE="${1:-$HOME/awesomerobdoe-green-software.robdoe}"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%S.%3NZ")

clear
echo -e "\033[1;31m========================================================================\033[0m"
echo -e "\033[1;33m ROBDOE PTY TLD :: NO-BS DIRECT EXECUTION MATRIX                       \033[0m"
echo -e "\033[1;31m NO SET-TRAPS // PURE ASSET ACCUMULATION // FORWARD ONLY              \033[0m"
echo -e "\033[1;31m========================================================================\033[0m"
echo -e "\033[0;90m [*] Execution Timestamp : $TIMESTAMP\033[0m"

if [ ! -d "$WORKSPACE" ]; then
    mkdir -p "$WORKSPACE"
fi

cd "$WORKSPACE"

python3 - "$TIMESTAMP" "$WORKSPACE" << 'INNER_PYTHON'
import os
import sys
import hashlib
import json

timestamp = sys.argv[1]
workspace = sys.argv[2]
lattice_log = os.path.join(workspace, "merkle_dag_lattice.jsonl")

# Direct financial compounding core
principal = 50000.00
annual_rate = 0.15
years = 5
freq = 12

rate_per_period = annual_rate / freq
final_amount = principal * ((1 + rate_per_period) ** (freq * years))
net_yield = final_amount - principal

print(f"\n\033[1;32m[+] DIRECT FINANCIAL EXTRACTION (5-Year Horizon @ 15% APR):\033[0m")
print(f"    -> Principal Base  : ${principal:,.2f}")
print(f"    -> Terminal Value  : ${final_amount:,.2f}")
print(f"    -> Net Yield       : ${net_yield:,.2f}")

# Stream hashing substrate
excluded_files = {"supreme_entanglement_audit.log", "pty_tld_telemetry.jsonl", "merkle_dag_lattice.jsonl"}
hasher_builder = [f"NO_BS_ANCHOR::{principal}::{final_amount}"]
file_count = 0

for root, dirs, files in os.walk(workspace):
    if '.git' in root:
        continue
    for file in sorted(files):
        if file in excluded_files or file.endswith('.bak'):
            continue
        full_path = os.path.join(root, file)
        rel_path = os.path.relpath(full_path, workspace)
        try:
            sha512 = hashlib.sha512()
            with open(full_path, 'rb') as sf:
                while chunk := sf.read(8192):
                    sha512.update(chunk)
            hasher_builder.append(f"{rel_path}::{sha512.hexdigest()}")
            file_count += 1
        except Exception:
            pass

master_sha512 = hashlib.sha512()
master_sha512.update("\n".join(hasher_builder).encode('utf-8'))
root_hash = master_sha512.hexdigest()

payload = {
    "timestamp": timestamp,
    "mode": "NO_BS_DIRECT_EXECUTION",
    "operator": "Robdoe Pty Tld",
    "identity": "THE EMU & THE KANGAROO [MAURI & MANA IN PERPETUUM]",
    "financial_projection": {
        "principal": principal,
        "terminal_value": final_amount,
        "yield": net_yield
    },
    "substrate_metrics": {
        "files_indexed": file_count,
        "root_hash": root_hash
    }
}

with open(lattice_log, 'a', encoding='utf-8') as f:
    f.write(json.dumps(payload) + "\n")

print(f"\n\033[1;36m[+] SUBSTRATE LOCKED:\033[0m")
print(f"    -> Indexed Items   : {file_count} files")
print(f"    -> Root Hash       : {root_hash[:32]}...")
INNER_PYTHON

echo -e "\n\033[1;35m[+] NO TRAPS. NO FRICTION. PURE ROBDOE PTY TLD CUSTODY. GANG GANG.\033[0m"
echo -e "========================================================================"
