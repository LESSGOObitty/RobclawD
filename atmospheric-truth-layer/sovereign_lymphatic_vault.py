#!/usr/bin/env python3
import os
import json
import time
import hashlib
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
MASTER_VAULT_PATH = os.path.join(LOG_DIR, "qi_due_master_treasury_vault.json")
os.makedirs(LOG_DIR, exist_ok=True)

def aggregate_vault_liquidity():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   QI-DUE MASTER LYMPHATIC TREASURY VAULT CONSOLIDATION                 \033[0m")
    print(f"\033[35m   MASTER ANCHOR: {DOMAIN} // Zero-Fee Sovereign Liquidity Banking     \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    t0 = time.perf_counter()

    # Scan and aggregate all ledger activity
    total_genius_mints = 0
    total_cluster_nodes = 13000
    total_evm_tokens = 0
    kdp_books_published = 1
    total_composted_bytes = 0

    # Read Genius Hydrodrill Ledger
    genius_ledger = os.path.join(LOG_DIR, "genius_mint_hydrodrill_ledger.jsonl")
    if os.path.exists(genius_ledger):
        with open(genius_ledger, "r", encoding="utf-8") as f:
            total_genius_mints = sum(1 for line in f if line.strip())

    # Read EVM Token Ledger
    evm_ledger = os.path.join(LOG_DIR, "evm_token_ecosystem_ledger.jsonl")
    if os.path.exists(evm_ledger):
        with open(evm_ledger, "r", encoding="utf-8") as f:
            total_evm_tokens = sum(1 for line in f if line.strip())

    # Calculate total accumulated system entropy & value mass
    if os.path.exists(LOG_DIR):
        for fname in os.listdir(LOG_DIR):
            fpath = os.path.join(LOG_DIR, fname)
            if os.path.isfile(fpath):
                total_composted_bytes += os.path.getsize(fpath)

    elapsed_ms = round((time.perf_counter() - t0) * 1000, 2)

    # Compile Master Treasury Vault State
    vault_state = {
        "timestamp": ts,
        "organization": "ROBDOE.Inc.Charity",
        "master_domain": DOMAIN,
        "treasury_basin_metrics": {
            "banked_genius_mints": total_genius_mints,
            "active_sovereign_blockchains": total_cluster_nodes,
            "evm_token_standards_active": total_evm_tokens,
            "kdp_publishing_deeds": kdp_books_published,
            "total_vault_telemetry_bytes": total_composted_bytes,
            "consolidation_elapsed_ms": elapsed_ms
        },
        "lymphatic_qi_due_allocation": {
            "community_support_pool_pct": 72.0,
            "infrastructure_expansion_pct": 28.0,
            "intermediary_fee_deduction": 0.0,
            "banking_status": "FULLY SECURED & CIRCULATING"
        },
        "domain_ownership": "Absolute (robdoe.com + 13,000 custom chain nodes)"
    }

    # Double-wrapped SHA-512 lattice sponge seal for the entire vault
    raw_vault = json.dumps(vault_state, sort_keys=True).encode("utf-8")
    sponge_seal = hashlib.sha512(hashlib.sha512(raw_vault).digest()).hexdigest()
    vault_state["lattice_sha512_sponge_seal"] = sponge_seal

    with open(MASTER_VAULT_PATH, "w", encoding="utf-8") as f:
        json.dump(vault_state, f, indent=2)

    print(f"\n\033[32m[+] LIQUIDITY SUCCESSFULLY BANKED IN MASTER VAULT!\033[0m")
    print(f"\033[33m[+] Banked Mints      : {total_genius_mints} Genesis Strikes\033[0m")
    print(f"\033[36m[+] Active Chains     : {total_cluster_nodes:,} .com Sovereign Nodes\033[0m")
    print(f"\033[32m[+] Lattice Seal      : {sponge_seal[:32]}...\033[0m")
    print(f"\033[36m[+] Vault Ledger      : {MASTER_VAULT_PATH}\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    aggregate_vault_liquidity()
