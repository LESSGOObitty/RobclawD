#!/usr/bin/env python3
import sys
import time
import json
import hashlib
from datetime import datetime, timezone

def run_enhanced_pipeline(target_cycles: int = 1000000, batch_size: int = 25000):
    print(f"[*] Initializing high-velocity Termux pipeline for {target_cycles:,} cycles...")
    
    start_time = time.perf_counter()
    accumulated_hash = hashlib.sha256(b"genesis").hexdigest()
    
    for i in range(1, target_cycles + 1):
        tick_data = f"{i}:{accumulated_hash}".encode('utf-8')
        accumulated_hash = hashlib.sha256(tick_data).hexdigest()
        
        if i % batch_size == 0:
            elapsed = time.perf_counter() - start_time
            rate = i / elapsed if elapsed > 0 else 0
            
            checkpoint = {
                "cycles_processed": i,
                "current_hash": accumulated_hash[:16],
                "rate_ops_sec": round(rate, 2),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
            
            sys.stdout.write(f"[⚡] Checkpoint: {json.dumps(checkpoint)}\n")
            sys.stdout.flush()

    total_time = time.perf_counter() - start_time
    print(f"[✓] Pipeline complete. Processed {target_cycles:,} cycles in {total_time:.4f}s.")

if __name__ == "__main__":
    cycles = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
    run_enhanced_pipeline(target_cycles=cycles)
