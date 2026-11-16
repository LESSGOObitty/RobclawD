#!/usr/bin/env python3
import os
import json
import hashlib
from datetime import datetime, timezone

DOMAIN = "robdoe.com"
REPO_DIR = os.path.expanduser("~/atmospheric-truth-layer")
LOG_DIR = os.path.join(REPO_DIR, "SovereignLedgerLogs")
EVM_LEDGER = os.path.join(LOG_DIR, "evm_token_ecosystem_ledger.jsonl")
EVM_WITNESS_LOG = os.path.join(REPO_DIR, "external_witness_evm.log")
os.makedirs(LOG_DIR, exist_ok=True)

def register_token_action(standard, token_name, action_type, metadata):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    # Read previous ledger state for chaining
    prev_hash = "0" * 64
    seq_index = 0
    if os.path.exists(EVM_LEDGER):
        with open(EVM_LEDGER, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            if lines:
                last_entry = json.loads(lines[-1])
                prev_hash = last_entry["lattice_sha512_sponge_seal"]
                seq_index = last_entry["seq_index"] + 1

    packet = {
        "seq_index": seq_index,
        "timestamp": ts,
        "organization": "ROBDOE.Inc.Charity",
        "domain": DOMAIN,
        "token_standard": standard.upper(), # ERC-20, ERC-721, ERC-1155
        "token_name": token_name,
        "action": action_type, # MINT, TRANSFER, BATCH_DEPLOY, LIQUIDITY_LOCK
        "metadata": metadata,
        "previous_seal": prev_hash,
        "lymphatic_circulation": "QiDue 72-Layer Aligned"
    }

    raw_bytes = json.dumps(packet, sort_keys=True).encode("utf-8")
    sponge_seal = hashlib.sha512(hashlib.sha512(raw_bytes).digest()).hexdigest()
    packet["lattice_sha512_sponge_seal"] = sponge_seal

    with open(EVM_LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(packet) + "\n")

    witness_line = (
        f"[{ts}] [{standard.upper()} //{token_name}] [{action_type}] "
        f"[SEQ: {seq_index}] [SEAL: {sponge_seal[:24]}...]\n"
    )
    with open(EVM_WITNESS_LOG, "a", encoding="utf-8") as f:
        f.write(witness_line)

    print(f"\033[32m[+] EVM TOKEN REGISTERED: {standard.upper()} ({token_name}) -> {action_type}\033[0m")
    print(f"\033[36m[+] Seal: {sponge_seal[:32]}...\033[0m")

if __name__ == "__main__":
    print(f"\033[35m========================================================================\033[0m")
    print(f"\033[32m   ROBDOE.INC.CHARITY :: EVM TOKEN ECOSYSTEM BRIDGE (ERC-20/721/1155)    \033[0m")
    print(f"\033[35m========================================================================\033[0m")

    # Example 1: ERC-20 Sovereign Liquidity Token Mint
    register_token_action(
        "ERC-20", 
        "QiDue Lymphatic Fluid Token (QDT)", 
        "MINT", 
        {"supply": "72,000,000", "routing": "Zero-Slippage Treasury Pool"}
    )

    # Example 2: ERC-721 Sovereign KDP Publishing & Asset Deed
    register_token_action(
        "ERC-721", 
        "Cozy Hygge KDP Publishing Deed #01", 
        "MINT_DEED", 
        {"author": "robdoe.com", "royalty_split": "100% Direct Treasury"}
    )

    # Example 3: ERC-1155 Multi-Token Asset Bundle
    register_token_action(
        "ERC-1155", 
        "Sovereign Infrastructure & Publishing Batch Pack", 
        "BATCH_DEPLOY", 
        {"token_ids": [101, 102, 103], "quantities": [1, 1000, 50]}
    )
    print(f"\033[35m========================================================================\033[0m")
