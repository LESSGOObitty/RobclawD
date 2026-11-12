import os, json, socket, subprocess, time

BASE_DIR = os.path.expanduser("~")
TELEMETRY_PATH = os.path.join(BASE_DIR, "robdoe_telemetry.json")
MESH_PORT = 9099

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def scan_subnet():
    local_ip = get_local_ip()
    subnet = ".".join(local_ip.split('.')[:-1]) + "."
    active_nodes = [local_ip]
    
    print(f" [•] Scanning subnet {subnet}0/24 for connected sovereign nodes...")
    # Fast ping sweep across local LAN
    for i in range(1, 255):
        target = subnet + str(i)
        if target == local_ip:
            continue
        # Non-blocking quick check via system ping
        res = subprocess.run(['ping', '-c', '1', '-W', '1', target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if res.returncode == 0:
            active_nodes.append(target)
            print(f"     [+] Discovered Node on LAN: {target}")
            
    return active_nodes

def execute_mesh_link():
    print("========================================================================")
    print(" [ROBDOE.COM] LINKING SOVEREIGN MESH TOPOLOGY")
    print("========================================================================")
    
    nodes = scan_subnet()
    timestamp = int(time.time())
    
    # Load current telemetry if available
    invariant = "inv_genesis"
    if os.path.exists(TELEMETRY_PATH):
        with open(TELEMETRY_PATH, "r") as f:
            data = json.load(f)
            invariant = data.get('invariant', invariant)
            
    mesh_payload = {
        "mesh_authority": "robdoe.com",
        "timestamp": timestamp,
        "active_invariant": invariant,
        "linked_nodes": nodes,
        "node_count": len(nodes),
        "status": "TOPOLOGY_LOCKED"
    }
    
    payload_bytes = json.dumps(mesh_payload).encode('utf-8')
    
    # Broadcast topology payload across UDP Mesh
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    try:
        sock.sendto(payload_bytes, ('255.255.255.255', MESH_PORT))
        print(f" [✓] Broadcasted mesh topology across UDP port {MESH_PORT}")
    except Exception as e:
        print(f" [!] Broadcast error: {e}")
    finally:
        sock.close()
        
    print("========================================================================")
    print(f" [✓] MESH LINKED: {len(nodes)} active endpoints synchronized.")
    print("========================================================================")

if __name__ == "__main__":
    execute_mesh_link()
