import os, sys, json, time, subprocess, urllib.request

BASE_DIR = os.path.expanduser("~")
TELEMETRY_PATH = os.path.join(BASE_DIR, "robdoe_telemetry.json")

def fetch_current_ip():
    try:
        # Fetch current external/mesh dynamic IP address
        with urllib.request.urlopen("https://api.ipify.org?format=json", timeout=3) as resp:
            data = json.loads(resp.read().decode())
            return data.get("ip")
    except Exception:
        # Fallback to local network interface detection
        try:
            cmd = "ip route get 1.1.1.1 | grep -oP 'src \\K\\S+'"
            return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        except Exception:
            return "127.0.0.1"

def update_node_routing():
    current_ip = fetch_current_ip()
    timestamp = int(time.time())
    
    print("========================================================================")
    print(" [ROBDOE.COM] DYNAMIC IP ROUTE RESOLVER")
    print("========================================================================")
    print(f" [+] Active Shuffled Endpoint IP : {current_ip}")
    print(f" [+] Timestamp                   : {timestamp}")
    
    # Read telemetry and inject current network state
    telemetry = {}
    if os.path.exists(TELEMETRY_PATH):
        with open(TELEMETRY_PATH, "r") as f:
            telemetry = json.load(f)
            
    telemetry["dynamic_routing"] = {
        "last_known_ip": current_ip,
        "shuffled_at": timestamp,
        "status": "ROUTE_ACTIVE"
    }
    
    with open(TELEMETRY_PATH, "w") as f:
        json.dump(telemetry, f, indent=2)
        
    print(f" [✓] Telemetry state updated with route {current_ip}")
    print("========================================================================")
    return current_ip

if __name__ == "__main__":
    ip = update_node_routing()
    
    # Quick launcher for interactive connection
    print("\n [!] To connect directly to your target host using this dynamic route:")
    print(f"     ssh -p 8022 robdoe@{ip}")
