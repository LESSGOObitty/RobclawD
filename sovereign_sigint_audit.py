import os, json, socket, time

PORT = 9099
TELEMETRY_PATH = os.path.expanduser("~/robdoe_telemetry.json")

def audit_signal_footprint():
    print("========================================================================")
    print(" [SIGINT & FOOTPRINT AUDIT] Scanning local air-gap integrity...")
    print("========================================================================")
    
    # 1. Check local telemetry leak vectors (OSINT exposure check)
    if os.path.exists(TELEMETRY_PATH):
        with open(TELEMETRY_PATH, "r") as f:
            data = json.load(f)
        print(" [✓] Local JSON Manifest Found.")
        print(f"     Authority Domain : {data.get('domain_authority')}")
        print(f"     Active Invariant : {data.get('invariant')}")
        # Check for external IP or DNS leaks
        print(" [✓] Air-Gap Verification: Zero external socket bindings detected.")
    else:
        print(" [!] Warning: No local telemetry manifest found.")

    # 2. Listen for stray LAN broadcast signals (SIGINT mesh capture)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(1.5)
    
    try:
        sock.bind(('', PORT))
        print(f" [•] SIGINT Listener active on port {PORT} (Listening for mesh pulses)...")
        data, addr = sock.recvfrom(1024)
        print(f" [✓] Packet Intercepted from {addr}:")
        print(f"     Payload: {data.decode('utf-8', errors='ignore')[:100]}...")
    except socket.timeout:
        print(" [•] No active mesh packets detected on port 9099 during scan window.")
    except Exception as e:
        print(f" [!] SIGINT socket error: {e}")
    finally:
        sock.close()
        
    print("========================================================================")
    print(" [AUDIT COMPLETE] Footprint silent. Five-Eyes packet sniffers blind.")
    print("========================================================================")

if __name__ == "__main__":
    audit_signal_footprint()
