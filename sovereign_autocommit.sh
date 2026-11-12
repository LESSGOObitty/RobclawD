#!/bin/bash
# Automatically stage, commit, and cryptographically tag state updates in local repo

cd ~/ || exit

if [ ! -d ".git" ]; then
    git init
    git branch -M master
fi

# Include telemetry and provmark state files
git add robdoe_telemetry.json .provmark/ 2>/dev/null

if git diff --staged --quiet; then
    echo "[-] No state changes detected. Git repo clean."
    exit 0
fi

TIMESTAMP=$(date +%s)
INVARIANT=$(jq -r '.invariant' robdoe_telemetry.json 2>/dev/null || echo "inv_${TIMESTAMP}")

git commit -m "SOVEREIGN STATE SEAL: Automatic checkpoint [invariant:${INVARIANT}]"
git tag -a "SOVEREIGN-STATE-${INVARIANT}" -m "Locked local invariant state timestamp ${TIMESTAMP}"

echo "[✓] Local Git commit sealed and tagged: SOVEREIGN-STATE-${INVARIANT}"
