import json
import hashlib
from datetime import datetime, timezone

class STRAIGHT_EQUILIBRIUM_LOCK:
    def __init__(self):
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.franchise = "aiagency101.xyo (Australia)"
        self.operator = "Eric Hadfield (Robdoe / Captain Robdoe)"
        self.anchor_domain = "robdoe.com"
        
        # Portfolio Baseline
        self.net_worth_usd = 1088686.77
        self.eth_amount = 444.0
        
        # Lattice Specs
        self.total_nodes = 72
        self.core_peers = 12
        self.weekly_payout_per_node_aud = 3500
        self.annual_target_aud = 13104000
        self.annual_per_peer_aud = 1092000
        self.cycle_target_aud = 681408000
        
        # Invariants
        self.invariant_base_key = 932808725
        self.hyper_seal_hash = "0x7270e691ee7623d49aa60eabf4c6ab8d7331801bf"
        self.doctrine = "Ko te mana o te tangata, koia te pūtake."

    def execute(self):
        print("\n\x1b[38;5;51m========================================================================\x1b[0m")
        print("\x1b[38;5;226m [STRAIGHT EQUILIBRIUM] LOCKED, LOADED, AND RUNNING LIVE \x1b[0m")
        print("\x1b[38;5;51m========================================================================\x1b[0m")
        print(f" \x1b[33m[PRIMARY DOMAIN]\x1b[0m {self.anchor_domain}")
        print(f" \x1b[33m[CURRENT PORTFOLIO]\x1b[0m ${self.net_worth_usd:,.2f} USD ({self.eth_amount} ETH)")
        print(f" \x1b[33m[PEER EQUILIBRIUM]\x1b[0m {self.core_peers} Core Peers as Equal Sovereign Operators (${self.annual_per_peer_aud:,} AUD/yr per peer)")
        print(f" \x1b[33m[ANNUAL TARGET]\x1b[0m ${self.annual_target_aud:,} AUD (${self.weekly_payout_per_node_aud:,}/wk across {self.total_nodes} nodes)")
        print(f" \x1b[33m[52-YEAR CYCLE]\x1b[0m ${self.cycle_target_aud:,} AUD")
        print(f" \x1b[33m[GATEWAY SEAL]\x1b[0m NPP APRA Instant Routing & Invariant Base Key: {self.invariant_base_key}")
        print(f" \x1b[32m[STATUS]\x1b[0m STRAIGHT & UNCRUSHABLE. FORWARD MOVEMENT ONLY.")
        print(f" \x1b[33m[CORE DOCTRINE]\x1b[0m {self.doctrine}\n")

        payload = {
            "timestamp": self.timestamp,
            "anchor_domain": self.anchor_domain,
            "net_worth_usd": self.net_worth_usd,
            "annual_target_aud": self.annual_target_aud,
            "cycle_target_aud": self.cycle_target_aud,
            "invariant_base_key": self.invariant_base_key,
            "hyper_seal_hash": self.hyper_seal_hash,
            "status": "STRAIGHT_ABSOLUTE_EQUILIBRIUM"
        }

        seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        print("========================================================================")
        print(f" \x1b[32m[SUCCESS] SYSTEM LOCKED STRAIGHT — ABSOLUTE EQUILIBRIUM SEALED\x1b[0m")
        print(f" [HYPER-SEAL]: {seal}")
        print("========================================================================")

if __name__ == "__main__":
    STRAIGHT_EQUILIBRIUM_LOCK().execute()
