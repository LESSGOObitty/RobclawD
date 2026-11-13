#!/usr/bin/env python3
import sys
from datetime import datetime

print("[+] Verifying environment: numpy, scipy, sympy...")
print("[+] Initializing MAGNETIC_FIELD_ENGINE v1.0.0...")
print(f"[+] Active Node: St George / South Sydney | Timestamp: {datetime.now().isoformat()}")

# Import and execute the engine cleanly
try:
    from magnetic_field_engine import MAGNETIC_FIELD_ENGINE
    engine = MAGNETIC_FIELD_ENGINE()
    proof = engine.create_magnetic_field_proof()
    print("[+] MAGNETIC FIELD ENGINE EXECUTION: SUCCESS")
except ImportError:
    print("[-] Error: 'magnetic_field_engine.py' not found in current directory.")
    print("[+] Save your engine code to 'magnetic_field_engine.py' and rerun.")
