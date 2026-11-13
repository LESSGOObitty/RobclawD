#!/usr/bin/env python3
"""
ROBDOE ROOT AUTHORITY // West Coast Infrastructure Latency Probe
Benchmarks endpoint response times and socket availability for telemetry relay.
"""

import socket
import time
import sys

# Target endpoints (adjust or expand as needed for US-West or WA relays)
ENDPOINTS = {
    "US-West (Oregon / San Jose)": "1d.eth.merkle.io",
    "Western Australia (Perth Relay)": "rpc.ankr.com",
    "Cloudflare Edge Gateway": "1.1.1.1"
}

def probe_endpoints():
    print("=========================================================")
    print(" [WEST COAST TELEMETRY] Network Latency & Reachability Probe")
    print("=========================================================")
    
    for name, host in ENDPOINTS.items():
        start_time = time.time()
        try:
            # Resolve and attempt a quick socket connection on HTTPS port
            ip = socket.gethostbyname(host)
            s = socket.create_connection((ip, 443), timeout=3.0)
            s.close()
            latency = (time.time() - start_time) * 1000
            print(f" [+] {name:<32} : {latency:6.2f} ms ({ip})")
        except Exception as e:
            print(f" [!] {name:<32} : OFFLINE / TIMEOUT")
            
    print("=========================================================")

if __name__ == "__main__":
    probe_endpoints()
