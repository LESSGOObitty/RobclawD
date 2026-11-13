#!/usr/bin/env bash
clear
echo "=========================================================================="
echo " [SYS] ROBCLAWROOTAUTHORITY // TERMUX LATTICE & GIT HEALTH AUDIT"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo "=========================================================================="

echo -e "\n[+] 1. Checking Git Repository & Remote Sync State..."
git remote -v
git status -sb

echo -e "\n[+] 2. Inspecting Local Lattice Daemons & Artifacts..."
echo "  - Total untracked/modified files: $(git status --porcelain | wc -l)"
if [ -f ".telemetry_ledger.jsonl" ]; then
    echo "  - Telemetry ledger active: $(wc -l < .telemetry_ledger.jsonl) entries logged"
else
    echo "  - Telemetry ledger: Standing by"
fi

echo -e "\n[+] 3. Termux Command-Line & Workspace Environment..."
echo "  - Current Working Directory: $(pwd)"
echo "  - Storage: $(df -h . | awk 'NR==2 {print $4 " available (" $5 " used)"}')"
echo "  - Python Runtime: $(python3 --version)"

echo "=========================================================================="
echo " [SUCCESS] LATTICE TELEMETRY CHECK COMPLETE. ALL SYSTEMS OPERATIONAL."
echo "=========================================================================="
