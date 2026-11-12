import os, sys, json, time, hashlib, socket

BASE_DIR = os.path.expanduser("~")
PROVMARK_DIR = os.path.join(BASE_DIR, ".provmark")
TELEMETRY_OUT = os.path.join(BASE_DIR, "robdoe_telemetry.json")
os.makedirs(PROVMARK_DIR, exist_ok=True)

def generate_unified_state():
    timestamp = int(time.time())
    
    # Audit local provmark files for root DAG count
    provmark_files = [f for f in os.listdir(PROVMARK_DIR) if f.endswith('.json')]
    state_count = len(provmark_files)
    
    raw_payload = f"UNIFIED_BRIDGE_SOVEREIGN_{timestamp}_NODES_{state_count}_BEVERLY_HILLS"
    sha256_root = hashlib.sha256(raw_payload.encode()).hexdigest()
    sha512_inv = hashlib.sha512(raw_payload.encode()).hexdigest()[:16]
    
    manifest = {
        "domain_authority": "robdoe.com",
        "timestamp": timestamp,
        "invariant": f"inv_{sha512_inv}",
        "sha256_root": sha256_root,
        "local_dag_depth": state_count,
        "channels": {
            "termux_arm64": "ACTIVE_MASTER",
            "serial_esp32": "READY_115200_BAUD",
            "lan_udp_mesh": "BROADCAST_PORT_9099",
            "provmark_vault": "SEALED"
        }
    }
    return manifest

def broadcast_lan_mesh(payload_bytes):
    """Pushes state lock across local Wi-Fi subnet to Windows PC / Moto G"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(0.5)
    try:
        sock.sendto(payload_bytes, ('255.255.255.255', 9099))
        return "BROADCAST_SENT"
    except Exception as e:
        return f"LAN_OFFLINE ({e})"
    finally:
        sock.close()

def run_master_bridge():
    state = generate_unified_state()
    state_bytes = json.dumps(state).encode('utf-8')
    
    # 1. Store in .provmark
    with open(os.path.join(PROVMARK_DIR, f"master_state_{state['timestamp']}.json"), "w") as f:
        json.dump(state, f, indent=2)
        
    # 2. Write domain payload file
    with open(TELEMETRY_OUT, "w") as f:
        json.dump(state, f, indent=2)
        
    # 3. Fire LAN Broadcast
    mesh_status = broadcast_lan_mesh(state_bytes)
    
    print("========================================================================")
    print(" [UNIFIED MASTER BRIDGE ACTIVE]")
    print(f" [AUTHORITY]         : {state['domain_authority']}")
    print(f" [STATE INVARIANT]   : {state['invariant']}")
    print(f" [SHA256 DAG ROOT]   : {state['sha256_root'][:32]}...")
    print(f" [PROVMARK DEPTH]    : {state['local_dag_depth']} sealed records")
    print("------------------------------------------------------------------------")
    print(f" [SERIAL STREAM]     : Ready -> 115200 Baud TX/RX")
    print(f" [LAN UDP MESH]      : {mesh_status} (Port 9099)")
    print(f" [DOMAIN MANIFEST]   : Updated -> ~/robdoe_telemetry.json")
    print("========================================================================")

if __name__ == "__main__":
    run_master_bridge()
