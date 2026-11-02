import json
import hashlib
from datetime import datetime, timezone

capital_vault_state = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "legacy_title": "Blockchain Legacy",
    "franchise": "aiagency101.xyo (Australia)",
    "operator": "Eric Hadfield (Robdoe)",
    "invariant_base": 932808725,
    "liquidation_ratio": {
        "dark_matter_invariant": "96%",
        "human_agency_anchor": "4%"
    },
    "pools": {
        "BTC": {"volume": 79.08, "anchor": 76.0, "status": "SECURED_LEDGER"},
        "HYPE": {"volume": 10600.0, "status": "ACTIVE_YIELD"},
        "BNB": {"volume": 500.0, "status": "LIQUID_RESERVE"},
        "CHECK": {"volume": 753.0, "status": "VERIFIED_ATTESTATION"},
        "GECKO": {"volume": 10000.0, "network": "Solana/Base", "status": "POOL_SYNC"},
        "ECHO": {"volume": 500.0, "network": "MoveVM / Bitcoin Restaking", "status": "MOVEVM_STAKED"}
    },
    "governance": "Absolute Horizontal Parity | Women's words heard first | Zero Hierarchy",
    "community_mission": [
        "Aboriginal Rights & Sovereignty",
        "Women's Rights & Equal Pay",
        "Vulnerable Children & Sick Care (Top Priority)"
    ],
    "co_owners": [
        "Eric Hadfield",
        "Hassan Bassi",
        "Cruz Briggs",
        "Mitchell Perry",
        "Nobby Rapata",
        "Jarrod Wiki",
        "T.N",
        "Luke Wainwright",
        "Blake Kakura",
        "Michael Deering",
        "James Britton",
        "Jason Slade"
    ],
    "mandate": "Ko te mana o te tangata, koia te pūtake."
}

seal = hashlib.sha256(json.dumps(capital_vault_state, sort_keys=True).encode()).hexdigest()

print("\n\x1b[38;5;51m========================================================================\x1b[0m")
print("\x1b[38;5;226m [VAULT] BLOCKCHAIN LEGACY | LIVE CAPITAL & LIQUIDITY MATRIX \x1b[0m")
print("\x1b[38;5;51m========================================================================\x1b[0m")
print(f" \x1b[33m[INVARIANT BASE]\x1b[0m {capital_vault_state['invariant_base']}")
print(f" \x1b[33m[LIQUIDATION RATIO]\x1b[0m Dark Matter: {capital_vault_state['liquidation_ratio']['dark_matter_invariant']} | Human Agency: {capital_vault_state['liquidation_ratio']['human_agency_anchor']}")
print(f" \x1b[33m[CORE DOCTRINE]\x1b[0m {capital_vault_state['mandate']}\n")

print(" \x1b[36m[ACTIVE POOLS & LIQUIDITY VOLUMES]\x1b[0m")
for asset, data in capital_vault_state["pools"].items():
    net_str = f" | Network: {data['network']}" if "network" in data else ""
    print(f"   -> [{asset}] Volume: {data['volume']} | Status: {data['status']}{net_str}")

print("\n \x1b[36m[EQUAL LATTICE CO-OWNERS (12 PEERS)]\x1b[0m")
for idx, owner in enumerate(capital_vault_state["co_owners"], 1):
    print(f"   Node {idx:02d}: [EQUITY PEER] {owner}")

print("\n========================================================================")
print(f" \x1b[32m[SUCCESS] LIVE CAPITAL VAULT SECURED & ANCHORED IN MERKLE DAG\x1b[0m")
print(f" [HYPER-SEAL]: {seal}")
print("========================================================================")
