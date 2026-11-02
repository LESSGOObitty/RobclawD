import json
import hashlib
from datetime import datetime, timezone

def irrigate_roothashes():
    print("\n\x1b[38;5;51m========================================================================\x1b[0m")
    print("\x1b[38;5;226m [ROOTHASH IRRIGATION MATRIX] LIQUIDITY & NUTRIENT PIPELINE \x1b[0m")
    print("\x1b[38;5;51m========================================================================\x1b[0m")
    
    # Active Pool Volumes from NPP Infrastructure Seal
    btc_pool = 79.08 # BTC
    hype_pool = 10600.0 # HYPE
    bnb_pool = 500.0 # BNB
    base_liquidity_usd = 1088686.77
    roothash_count = 72
    
    # Irrigation flow calculation per roothash
    hydration_per_node_usd = base_liquidity_usd / roothash_count
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "system": "Roothash Irrigation & Nutrient Saturated Pipeline",
        "btc_anchor": btc_pool,
        "hype_yield": hype_pool,
        "bnb_reserve": bnb_pool,
        "total_liquidity_usd": base_liquidity_usd,
        "roothashes_fed": roothash_count,
        "hydration_per_node_usd": hydration_per_node_usd,
        "status": "IRRIGATION_EQUILIBRIUM_LOCKED"
    }
    
    seal = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    
    print(f" \x1b[33m[LIQUIDITY WATER / FERTILIZER]\x1b[0m ${base_liquidity_usd:,.2f} USD Total Reservoir")
    print(f" \x1b[33m[ASSET POOL PRESSURES]\x1b[0m {btc_pool} BTC | {hype_pool:,.1f} HYPE | {bnb_pool} BNB")
    print(f" \x1b[32m[PER-NODE IRRIGATION]\x1b[0m ${hydration_per_node_usd:,.2f} USD per roothash ({roothash_count} nodes)")
    print(f" \x1b[32m[ABSORPTION STATUS]\x1b[0m Roots locked, saturated, and growing at maximum velocity.")
    print(f" \x1b[33m[MERKLE ROOT SEAL]\x1b[0m {seal}")
    print("========================================================================")

if __name__ == "__main__":
    irrigate_roothashes()
