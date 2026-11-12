#!/bin/bash
# Local Termux Audio Telemetry Beacon
# Requirements: termux-api installed (pkg install termux-api)

INVARIANT=$(jq -r '.invariant' ~/robdoe_telemetry.json 2>/dev/null || echo "UNKNOWN")
DEPTH=$(jq -r '.local_dag_depth' ~/robdoe_telemetry.json 2>/dev/null || echo "0")

echo "[+] Triggering local hardware audio state alert..."
termux-tts-speak "Sovereign node verified. Invariant ${INVARIANT:0:8}. Vault depth ${DEPTH}."
termux-vibrate -d 100
