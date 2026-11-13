#!/usr/bin/env python3
"""
ROBDOE ROOT AUTHORITY // Dynamic Route Optimizer
Binds telemetry traffic to the lowest-latency active gateway.
"""

import json
import os
import socket
import time

ROUTES = {
    "cloudflare_edge": {"host": "1.1.1.1", "port": 443, "priority": 1},
    "wa_perth": {"host": "rpc.ankr.com", "port": 443, "priority": 2},
    "us_west": {"host": "1d.eth.merkle.io", "port": 443, "priority": 3}
}

CONFIG_PATH = ".telemetry_route.json"

def select_best_route():
    print("[*] Benchmarking active gateway responsiveness...")
    best_node = None
    lowest_latency = float('inf')
    
    for name, data in ROUTES.items():
        start = time.time()
        try:
            ip = socket.gethostbyname(data["host"])
            s = socket.create_connection((ip, data["port"]), timeout=2.0)
            s.close()
            latency = (time.time() - start) * 1000
            print(f" [+] Gateway [{name}] -> {latency:.2f} ms")
            if latency < lowest_latency:
                lowest_latency = latency
                best_node = {"name": name, "host": data["host"], "ip": ip, "latency_ms": round(latency, 2)}
        except Exception:
            print(f" [!] Gateway [{name}] -> OFFLINE")
            
    if best_node:
        with open(CONFIG_PATH, "w") as f:
            json.dump(best_node, f, indent=2)
        print(f"\n[+] Active Route Locked: {best_node['name']} ({best_node['ip']}) @ {best_node['latency_ms']}ms")
    else:
        print("[!] Warning: All gateways unresponsive. Falling back to local loopback.")

if __name__ == "__main__":
    select_best_route()
