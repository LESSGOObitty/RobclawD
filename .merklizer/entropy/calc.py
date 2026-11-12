import os
import hashlib
import time

entropy_dir = os.path.expanduser("~/.merklizer/entropy")
state_file = os.path.join(entropy_dir, "state.hex")

def measure_entropy():
    # Gather system state seeds from local pseudo-random & environmental noise
    seed_data = os.urandom(64) + str(time.time_ns()).encode() + str(os.getpid()).encode()
    digest = hashlib.sha3_512(seed_data).hexdigest()
    return digest

current_digest = measure_entropy()
print(f"[+] Directional Entropy Vector: {current_digest[:32]}...")

with open(state_file, "a") as f:
    f.write(f"{time.time()}::{current_digest}\n")
