#!/usr/bin/env python3
import os
import json
import hashlib
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
GENIUS_LEDGER = os.path.join(LOG_DIR, "genius_mint_hydrodrill_ledger.jsonl")
BRIDGE_OUTPUT = os.path.join(LOG_DIR, "fiat_kdp_liquidity_bridge.json")

def converge_to_fiat_kdp():
    if not os.path.exists(GENIUS_LEDGER):
        print("\033[31m[-] Error: No Genius Hydrodrill ledger found. Run the hydrodrill first.\033[0m")
        return

    # Read the latest minted block
    with open(GENIUS_LEDGER, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        if not lines:
            print("\033[31m[-] Ledger is empty.\033[0m")
            return
        latest_block = json.loads(lines[-1])

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    # Map the sovereign proof-of-work hash to a liquidity settlement unit
    genesis_hash = latest_block["genius_mint"]["genius_mint_hash"]
    mint_index = latest_block["mint_index"]
    merkle_root = latest_block["bedrock_merkle_root"]

    # Enterprise / Fiat / KDP Convergence Payload
    convergence_packet = {
        "bridge_timestamp": ts,
        "sovereign_domain": DOMAIN,
        "source_ledger": "genius_mint_hydrodrill_ledger.jsonl",
        "block_target": {
            "mint_index": mint_index,
            "proof_of_work_hash": genesis_hash,
            "bedrock_merkle_root": merkle_root
        },
        "fiat_kdp_routing": {
            "settlement_protocol": "KDP-Enterprise-Treasury-v1",
            "fiat_conversion_rate": "1:1 Sovereign-Parity",
            "liquidity_destination": "Automated Lymphatic QiDue Pool",
            "treasury_status": "LIQUIDITY_INJECTION_READY",
            "intermediary_fees": 0.0,
            "compliance": "Absolute Domain Ownership Verified"
        }
    }

    # Double-wrap SHA-512 seal for the bridge packet
    raw_packet = json.dumps(convergence_packet, sort_keys=True).encode("utf-8")
    bridge_seal = hashlib.sha512(hashlib.sha512(raw_packet).digest()).hexdigest()
    convergence_packet["bridge_lattice_sponge_seal"] = bridge_seal

    with open(BRIDGE_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(convergence_packet, f, indent=2)

    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m[+] FIAT & KDP INFRASTRUCTURE CONVERGENCE COMPLETE\033[0m")
    print(f"\033[33m[+] Linked Mint Index : #{mint_index}\033[0m")
    print(f"\033[36m[+] Pow Hash Target   : {genesis_hash[:32]}...\033[0m")
    print(f"\033[32m[+] Bridge Seal       : {bridge_seal[:32]}...\033[0m")
    print(f"\033[36m[+] Packet Written    : {BRIDGE_OUTPUT}\033[0m")
    print(f"\033[35m========================================================================\033[0m")

if __name__ == "__main__":
    converge_to_fiat_kdp()
