#!/usr/bin/env python3
import os
import time
import hashlib

def generate_local_entropy():
    # 1. Pull raw system hardware entropy
    raw_bytes = os.urandom(64)
    
    # 2. Capture nanosecond clock jitter
    nano_time = str(time.time_ns()).encode('utf-8')
    
    # 3. Mix payload with local system logic
    payload = raw_bytes + nano_time + b":eM2:SOVEREIGN_ROOT"
    
    # 4. Hash to deterministic root
    state_root = hashlib.sha256(payload).hexdigest()
    
    # 5. Package raw binary dump
    pkg_filename = "pkg_entropy.bin"
    with open(pkg_filename, "wb") as f:
        f.write(bytes.fromhex(state_root))
        
    print("=====================================================")
    print(" RAW LOCAL ENTROPY PACKAGE [ ( . Y . ) ]")
    print("=====================================================")
    print(f" [*] Local Jitter Time : {nano_time.decode('utf-8')}")
    print(f" [*] State Root Hash   : 0x{state_root}")
    print(f" [*] Package Created   : {pkg_filename} ({len(bytes.fromhex(state_root))} bytes)")
    print(" [STATUS] Zero external dependencies. Fully self-contained.")
    print("=====================================================")

if __name__ == "__main__":
    generate_local_entropy()
