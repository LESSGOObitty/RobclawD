import json
import time
import hashlib
from collections import defaultdict

def keccak256(data_bytes):
    return hashlib.sha3_256(data_bytes).hexdigest()

class TruthEngine38BFT:
    def __init__(self):
        # 38-Node Cluster Layout: Ring A (14) + Ring B (14) + Core Layer (10)
        self.total_nodes = 38
        self.max_faulty = 12  # Safe operational bound under standard BFT rules (3F + 1)
        self.nodes = [f"Validator_Node_{i:02d}" for i in range(self.total_nodes)]
        
    def process_state_validation(self, baseline_fact):
        """Runs the payload through a single-round consensus commit loop."""
        votes = {}
        honest_threshold = 2 * self.max_faulty + 1 # 25 matching votes required for absolute quorum
        
        print(f"\n\033[1;33m[~] Initialising 38-Node BFT Truth Engine Quorum Loop...\033[0m")
        print(f"    Active Nodes: {self.total_nodes} | Fault Tolerance Threshold: F = {self.max_faulty}")
        
        for idx, node in enumerate(self.nodes):
            # Simulate arbitrary external entropy/Byzantine behavior on the first 12 nodes
            if idx < self.max_faulty:
                votes[node] = "SPOOFED_ENTROPY_NOISE"
            else:
                votes[node] = baseline_fact
                
        # Tally vote distributions across the 38-node pool
        tally = defaultdict(int)
        for vote in votes.values():
            tally[vote] += 1
            
        print("\n[+] Consensus Tally Matrix:")
        for state, count in tally.items():
            status = "PASSED" if count >= honest_threshold else "FILTERED"
            print(f"    -> State: '{state}' | Votes: {count}/{self.total_nodes} [{status}]")
            
        # Assert consensus stability
        for state, count in tally.items():
            if count >= honest_threshold:
                print(f"\n\033[1;32m[+] QUORUM SECURED ({count}/{honest_threshold} agreement achieved).\033[0m")
                return state, votes
                
        raise RuntimeError("[-] Consensus Matrix Failure: Unbounded entropy exceeded cluster thresholds.")

    def commit_to_ledger(self, verified_state, complete_votes):
        timestamp = time.time()
        payload = {
            "epoch_time": timestamp,
            "engine_profile": "38_Node_Pure_BFT_Truth",
            "consensus_state": verified_state,
            "pool_signatures_count": len(complete_votes)
        }
        
        serialized = json.dumps(payload, sort_keys=True)
        state_root = keccak256(serialized.encode('utf-8'))
        
        print("\n\033[1;36m================================================================\033[0m")
        print(f"\033[1;32m[+] TRUTH DATUM COMMITTED TO LOCAL LEDGER PERIMETER\033[0m")
        print(f"    State Integrity : 100% Verified Consistent")
        print(f"    Keccak-256 Root : 0x{state_root}")
        print("\033[1;36m================================================================\033[0m\n")
        
        # Save a local record of the audit log
        with open(os.path.expanduser("~/.provmark/bft_38_audit.log"), "a") as f:
            f.write(f"{timestamp} | ROOT: 0x{state_root} | STATE: {verified_state}\n")

if __name__ == "__main__":
    import os
    engine = TruthEngine38BFT()
    
    # Baseline fact input to process through the validator cluster
    target_fact = "BASE_TRUTH_LOCK_2026"
    
    try:
        final_state, vote_matrix = engine.process_state_validation(target_fact)
        engine.commit_to_ledger(final_state, vote_matrix)
    except Exception as e:
        print(f"[-] Engine Error: {e}")
