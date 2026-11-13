import math
import os
from collections import Counter

LOG_FILE = os.path.expanduser("~/workspace/telemetry.log")

def calculate_shannon_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    frequencies = Counter(data)
    total_length = len(data)
    entropy = 0.0
    for count in frequencies.values():
        probability = count / total_length
        entropy -= probability * math.log2(probability)
    return entropy

def analyze_telemetry():
    if not os.path.exists(LOG_FILE):
        print(f"[-] Telemetry log not found at {LOG_FILE}")
        return
    with open(LOG_FILE, "rb") as f:
        content = f.read()
    entropy = calculate_shannon_entropy(content)
    max_entropy = 8.0
    redundancy = (1 - (entropy / max_entropy)) * 100
    print(f"[*] --- TELEMETRY ENTROPY ANALYSIS ---")
    print(f"[*] Total Log Size     : {len(content)} bytes")
    print(f"[*] Shannon Entropy    : {entropy:.4f} bits/byte")
    print(f"[*] Data Redundancy    : {redundancy:.2f}%")
    print(f"[*] Information State  : {'High Noise / Random' if entropy > 4.5 else 'Structured / Repetitive'}")

if __name__ == "__main__":
    analyze_telemetry()
