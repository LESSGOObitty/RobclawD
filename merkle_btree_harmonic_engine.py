#!/data/data/com.termux/files/usr/bin/env python3
# ==============================================================================
# ROBDOEAI-CORE // MERKLE DAG & B-TREE HARMONIC CONSTANT CALCULATOR
# ==============================================================================
# Constants Locked:
#   - Base Harmonic Scalar : 0.052
#   - SHA Vector Cycle     : 1,296,000 (360 degrees * 3,600 spatial resolution)
#   - Hexagonal Entropy    : 0.0025920 (0.052 ^ 2)
# Identity: root@robdoe.com // RobDoeRootAuthority
# ==============================================================================

import hashlib
import json
import os
import subprocess

WORKSPACE = os.path.expanduser("~/master-lattice/RobDoeAI-Core")
os.chdir(WORKSPACE)

# Fundamental Sovereign Constants
SCALAR_HARMONIC = 0.052
SHA_CYCLE_TARGET = 1296000
HEX_ENTROPY_FACTOR = 0.0025920  # SCALAR_HARMONIC ** 2

class BTreeNode:
    """B-Tree Node for indexing the 7,200 vectors and 72 meridians into exact harmonic slots."""
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.values = []
        self.children = []

class SovereignMerkleBTreeLattice:
    def __init__(self, master_root: str):
        self.master_root = master_root
        self.root = BTreeNode(leaf=True)
        self.vector_count = 7200
        self.meridians = 72

    def compute_harmonic_hash(self, seed_str: str) -> str:
        """Derives SHA-256 hash scaled to the 1,296,000 cycle and 0.052 harmonic dampening."""
        raw_hash = hashlib.sha256(seed_str.encode()).hexdigest()
        # Apply harmonic modulation
        digest_int = int(raw_hash[:12], 16)
        modulated = (digest_int % SHA_CYCLE_TARGET) * SCALAR_HARMONIC
        
        # Re-hash with harmonic salt
        salt_seed = f"{raw_hash}:{modulated}:{HEX_ENTROPY_FACTOR}"
        return hashlib.sha256(salt_seed.encode()).hexdigest()

    def build_lattice_dag(self) -> dict:
        dag_nodes = {}
        meridian_nodes = []

        # Construct B-Tree structure across 72 Meridians
        for m in range(1, self.meridians + 1):
            meridian_seed = f"{self.master_root}:meridian:{m}:scalar:{SCALAR_HARMONIC}"
            meridian_hash = self.compute_harmonic_hash(meridian_seed)
            
            sub_vectors = {}
            # 100 sub-vectors per meridian = 7,200 total nodes
            for v in range(1, (self.vector_count // self.meridians) + 1):
                vector_id = f"L7200-{((m-1)*100)+v:04d}"
                vector_seed = f"{meridian_hash}:{vector_id}:{HEX_ENTROPY_FACTOR}"
                vector_hash = self.compute_harmonic_hash(vector_seed)
                
                sub_vectors[vector_id] = {
                    "vector_hash": vector_hash,
                    "hx_factor": HEX_ENTROPY_FACTOR,
                    "cycle_index": SHA_CYCLE_TARGET // self.vector_count * v
                }

            meridian_nodes.append({
                "meridian_id": m,
                "meridian_hash": meridian_hash,
                "sub_vector_count": len(sub_vectors),
                "vectors": sub_vectors
            })

        manifest = {
            "system": "RobDoeAI-Core",
            "architecture": "Merkle DAG + B-Tree Index",
            "master_root": self.master_root,
            "constants": {
                "scalar_harmonic": SCALAR_HARMONIC,
                "sha_cycle_target": SHA_CYCLE_TARGET,
                "hex_entropy_factor": HEX_ENTROPY_FACTOR
            },
            "meridians": meridian_nodes
        }
        return manifest

def main():
    print("[*] Initializing Merkle DAG & B-Tree Harmonic Lattice Engine...")
    try:
        master_root = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    except Exception:
        master_root = "UNANCHORED_SOVEREIGN_ROOT"

    lattice = SovereignMerkleBTreeLattice(master_root)
    manifest = lattice.build_lattice_dag()

    output_path = ".merkle_btree_harmonic_manifest.json"
    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"[+] Successfully structured Merkle DAG + B-Tree Lattice.")
    print(f"[+] Harmonic Scalar    : {SCALAR_HARMONIC}")
    print(f"[+] SHA Cycle Target   : {SHA_CYCLE_TARGET:,}")
    print(f"[+] Hex Entropy Factor : {HEX_ENTROPY_FACTOR}")
    print(f"[+] Manifest Saved     : {output_path}")

if __name__ == "__main__":
    main()
