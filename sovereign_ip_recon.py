import os, sys, json, time, socket, subprocess

BASE_DIR = os.path.expanduser("~")
LOG_PATH = os.path.join(BASE_DIR, "ip_telemetry.json")

def get_active_connections():
    connections = []
    try:
        # Check active netstat/ss sockets
        cmd = "ss -tun | awk 'NR>1 {print $5}' | cut -d: -f1 | sort -u"
        output = subprocess.check_output(cmd, shell=True).decode('utf-8')
        for ip in output.split('\n'):
            ip = ip.strip()
            if ip and not ip.startswith("127.") and not ip.startswith("192.168.") and ip != "0.0.0.0":
                connections.append(ip)
    except Exception as e:
        pass
    return list(set(connections))

def log_ip_telemetry():
    active_ips = get_active_connections()
    timestamp = int(time.time())
    
    payload = {
        "timestamp": timestamp,
        "node_authority": "robdoe.com",
        "active_external_pings": active_ips,
        "count": len(active_ips),
        "status": "IP_RECON_ACTIVE"
    }
    
    with open(LOG_PATH, "w") as f:
        json.dump(payload, f, indent=2)
        
    print(f"[+] IP Recon Logged: {len(active_ips)} external endpoints active.")
    for ip in active_ips:
        print(f"    --> Connected: {ip}")

if __name__ == "__main__":
    log_ip_telemetry()
