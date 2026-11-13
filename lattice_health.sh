#!/data/data/com.termux/files/usr/bin/env zsh
set -euo pipefail

PRIMARY_HASH=$(git rev-parse --short=12 HEAD)
BRANCH_COUNT=$(git branch --list 'lattice-node-vector-*' | wc -l | tr -d ' ')
TAG_COUNT=$(git tag -l 'lattice-root-*' | wc -l | tr -d ' ')
ENTROPY_STATE=$(head -n 1 .lattice_entropy_state 2>/dev/null || echo "CALIBRATED")

printf "\n"
printf "==================================================================\n"
printf " ROBDOEAI-CORE // EXECUTIVE INFRASTRUCTURE TELEMETRY\n"
printf "==================================================================\n"
printf " %-24s : %s\n" "Entity" "RobDoe Foundation"
printf " %-24s : %s\n" "Primary Merkle Root" "$PRIMARY_HASH"
printf " %-24s : %s / 72 Active\n" "Distributed Vectors" "$BRANCH_COUNT"
printf " %-24s : %s Verified\n" "Sovereign Root Tags" "$TAG_COUNT"
printf " %-24s : %s\n" "Entropy Telemetry" "$ENTROPY_STATE"
printf " %-24s : %s\n" "Working Tree" "$(git status -s | wc -l | tr -d ' ') uncommitted changes"
printf "==================================================================\n\n"
