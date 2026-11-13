#!/data/data/com.termux/files/usr/bin/env python3
import hashlib
import json
import math
import os
import secrets
import time
from collections import Counter

MERKLE_STATE_FILE = "enhanced_unified_merkle_state.json"
QUINTILLION_FILE = ".quintillion_equity_ledger_state.json"

def shannon_entropy(data: bytes) -> float:
    """Compute exact Shannon entropy in bits per byte (0.0 = pure order, 8.0 = max chaos)."""
    if not data:
        return 0.0
    length = len(data)
    counts = Counter(data)
    entropy = 0.0
    for count in counts.values():
        p = count / length
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def generate_high_entropy_seed(merkle_root: str) -> dict:
    """High-Entropy State: Hardware CSPRNG + nanosecond timing jitter + Merkle root fusion."""
    raw_csprng = secrets.token_bytes(64)
    jitter_ns = str(time.perf_counter_ns()).encode("utf-8")
    root_bytes = merkle_root.encode("utf-8")

    fused_chaos = hashlib.sha512(raw_csprng + jitter_ns + root_bytes).digest()
    entropy_score = shannon_entropy(raw_csprng)

    return {
        "mode": "HIGH_ENTROPY_CHAOS_SEED",
        "shannon_bits_per_byte": entropy_score,
        "theoretical_max": 8.0,
        "csprng_hex": raw_csprng.hex(),
        "fused_sha512_key": fused_chaos.hex(),
        "purpose": "Cryptographic nonces, ERC-721/1155 salt generation, ZKP blinding factors"
    }

def synthesize_low_entropy_lock(merkle_root: str) -> dict:
    """Low-Entropy State: Canonical sorted JSON + zero-whitespace deterministic compression."""
    canonical_core = {
        "beneficiary": "robdoe.inc-charity",
        "bmf_mandate": "EN_16931_XRECHNUNG_2027",
        "equity_units": 1000000000000000000,
        "lattice_vectors": 7200,
        "meridians": 72,
        "merkle_root": merkle_root,
        "operator": "root@robdoe.com",
        "sovereign_deed": "robdoe.com"
    }
    # Deterministic zero-entropy-overhead serialization
    packed_bytes = json.dumps(canonical_core, sort_keys=True, separators=(",", ":")).encode("utf-8")
    low_entropy_hash = hashlib.sha256(packed_bytes).hexdigest()

    # Pure stillness reference vector (zero Shannon entropy)
    stillness_vector = b"\x00" * 64
    stillness_entropy = shannon_entropy(stillness_vector)
    canonical_entropy = shannon_entropy(packed_bytes)

    return {
        "mode": "LOW_ENTROPY_DETERMINISTIC_LOCK",
        "stillness_vector_entropy": stillness_entropy,
        "canonical_payload_entropy": canonical_entropy,
        "canonical_sha256": low_entropy_hash,
        "packed_bytes": len(packed_bytes),
        "purpose": "Immutable B-Tree root anchoring, zero-drift ledger verification, BMF compliance"
    }

def run_dual_entropy():
    merkle_root = "c1fe439476a2f613d766a869d9d34b93c384d0deab0dbd0e9350d82a308a2d30"
    if os.path.exists(MERKLE_STATE_FILE):
        with open(MERKLE_STATE_FILE, "r") as f:
            data = json.load(f)
            merkle_root = data.get("unified_merkle_root", merkle_root)

    high_state = generate_high_entropy_seed(merkle_root)
    low_state = synthesize_low_entropy_lock(merkle_root)

    # Dual-state equilibrium signature (Stillness in Motion)
    equilibrium_sig = hashlib.sha256(
        (high_state["fused_sha512_key"] + low_state["canonical_sha256"]).encode("utf-8")
    ).hexdigest()

    dual_manifest = {
        "system": "RobDoeAI-Core // Dual-State Entropy Engine (Stillness in Motion)",
        "operator": "root@robdoe.com",
        "beneficiary": "robdoe.inc-charity",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "anchored_merkle_root": merkle_root,
        "high_entropy_domain": high_state,
        "low_entropy_domain": low_state,
        "stillness_in_motion_equilibrium_sha256": equilibrium_sig
    }

    with open("dual_entropy_state.json", "w") as f:
        json.dump(dual_manifest, f, indent=2)

    print("=" * 74)
    print(" [DUAL ENTROPY] HIGH CHAOS SEED & LOW ORDER LOCK SYNTHESIZED")
    print("=" * 74)
    print(f" [HIGH ENTROPY] Shannon Rate   : {high_state['shannon_bits_per_byte']} / 8.0 bits/byte")
    print(f" [HIGH ENTROPY] Fused SHA-512  : {high_state['fused_sha512_key'][:32]}...")
    print("-" * 74)
    print(f" [LOW ENTROPY]  Stillness Vec  : {low_state['stillness_vector_entropy']} bits/byte (Absolute Zero Drift)")
    print(f" [LOW ENTROPY]  Canonical Hash : {low_state['canonical_sha256']}")
    print("-" * 74)
    print(f" [EQUILIBRIUM]  Stillness in Motion : {equilibrium_sig}")
    print("=" * 74)

if __name__ == "__main__":
    run_dual_entropy()
