#!/bin/bash
cd "$HOME" || exit
if [ ! -d ".git" ]; then
    git init >/dev/null 2>&1
    git branch -M master >/dev/null 2>&1
fi
git add robdoe_telemetry.json .provmark/ 2>/dev/null
git diff --staged --quiet && exit 0

TIMESTAMP=$(date +%s)
INVARIANT=$(jq -r '.invariant' robdoe_telemetry.json 2>/dev/null || echo "inv_${TIMESTAMP}")
git commit -m "SOVEREIGN STATE SEAL: Automatic checkpoint [invariant:${INVARIANT}]" >/dev/null 2>&1
git tag -a "SOVEREIGN-STATE-${INVARIANT}" -m "Locked local invariant state timestamp ${TIMESTAMP}" >/dev/null 2>&1
echo "[✓] Git commit sealed: SOVEREIGN-STATE-${INVARIANT}"
