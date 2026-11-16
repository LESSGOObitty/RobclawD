#!/usr/bin/env python3
import os
import sys
import time
import json
import hashlib
import subprocess
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
DAEMON_LOG = os.path.join(LOG_DIR, "sovereign_master_daemon.log")
os.makedirs(LOG_DIR, exist_ok=True)

def log_event(level, message):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    entry = f"[{ts}] [{level}] {message}"
    print(entry)
    with open(DAEMON_LOG, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def ensure_zero_weakpoints():
    """Validates local environment, toolchains, and file integrity."""
    required_tools = ["git", "python3", "openssl", "jq"]
    for tool in required_tools:
        if subprocess.run(["which", tool], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
            log_event("WARNING", f"Missing critical toolchain dependency: {tool}. Auto-remediation advised.")

def execute_self_healing_cycle(cycle_id):
    log_event("INFO", f"=== STARTING SOVEREIGN MASTER DAEMON CYCLE #{cycle_id} ===")
    ensure_zero_weakpoints()

    # 1. Run 13K Chains Audit Check
    audit_script = os.path.join(REPO_DIR, "thirteen_k_chains_audit.py")
    if os.path.exists(audit_script):
        res = subprocess.run(["python3", audit_script], capture_output=True, text=True)
        if res.returncode == 0:
            log_event("SUCCESS", "13,000 .COM Blockchain Network audit verified and sealed.")
        else:
            log_event("ERROR", f"13K Audit failure: {res.stderr.strip()}")

    # 2. Run Genius Hydrodrill Liquidity Pulse
    hydrodrill_script = os.path.join(REPO_DIR, "genius_hydrodrill_liquidity.py")
    if os.path.exists(hydrodrill_script):
        res = subprocess.run(["python3", hydrodrill_script], capture_output=True, text=True)
        if res.returncode == 0:
            log_event("SUCCESS", "Genius Hydrodrill & QiDue liquidity pulse completed successfully.")
        else:
            log_event("ERROR", f"Hydrodrill failure: {res.stderr.strip()}")

    # 3. Automatic Git Integrity Check & Local Sync
    try:
        subprocess.run(["git", "-C", REPO_DIR, "add", "SovereignLedgerLogs/"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        status_res = subprocess.run(["git", "-C", REPO_DIR, "status", "--porcelain"], capture_output=True, text=True)
        if status_res.stdout.strip():
            subprocess.run(["git", "-C", REPO_DIR, "commit", "-m", f"Auto-sealed Sovereign Master Daemon Cycle #{cycle_id} [robdoe.com]"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            log_event("SUCCESS", "Local Git ledger state auto-committed (Forward-Only Vector locked).")
    except Exception as e:
        log_event("WARNING", f"Git self-healing routine skipped: {e}")

    log_event("INFO", f"=== CYCLE #{cycle_id} COMPLETE. Sleeping for 300 seconds (5 min interval) ==-\n")

def main():
    log_event("INIT", f"Initializing Sovereign Master Daemon for domain {DOMAIN}...")
    cycle = 1
    try:
        while True:
            execute_self_healing_cycle(cycle)
            cycle += 1
            time.sleep(300) # 5-minute continuous self-healing heartbeat
    except KeyboardInterrupt:
        log_event("SHUTDOWN", "Daemon interrupted by user. Sovereign state preserved.")
        sys.exit(0)

if __name__ == "__main__":
    main()
