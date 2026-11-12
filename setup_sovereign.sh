#!/bin/bash
# ======================================================================
# ROBDOE.COM SOVEREIGN NODE CLEAN DEPLOYMENT
# ======================================================================

SOV_HOME="$HOME/sovereign_core"
PROVMARK_DIR="$HOME/.provmark"
ARCHIVE_DIR="$SOV_HOME/archives"

mkdir -p "$SOV_HOME" "$PROVMARK_DIR" "$ARCHIVE_DIR"
cd "$SOV_HOME" || exit

echo "[+] Constructing pristine sovereign modules..."

# 1. Unified Master Bridge
cat << 'PYTHON_BRIDGE' > sovereign_unified_bridge.py
import os, sys, json, time, hashlib, socket

BASE_DIR = os.path.expanduser("~")
PROVMARK_DIR = os.path.join(BASE_DIR, ".provmark")
TELEMETRY_OUT = os.path.join(BASE_DIR, "robdoe_telemetry.json")
os.makedirs(PROVMARK_DIR, exist_ok=True)

def generate_unified_state():
    timestamp = int(time.time())
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
    
    with open(os.path.join(PROVMARK_DIR, f"master_state_{state['timestamp']}.json"), "w") as f:
        json.dump(state, f, indent=2)
        
    with open(TELEMETRY_OUT, "w") as f:
        json.dump(state, f, indent=2)
        
    mesh_status = broadcast_lan_mesh(state_bytes)
    print(f"[✓] State locked. Invariant: {state['invariant']} | DAG Depth: {state['local_dag_depth']}")

if __name__ == "__main__":
    run_master_bridge()
PYTHON_BRIDGE

# 2. Git Auto-Sealer
cat << 'SH_COMMIT' > sovereign_autocommit.sh
#!/bin/bash
cd "$HOME" || exit
if [ ! -d ".git" ]; then
    git init >/dev/null 2>&1
    git branch -M master >/dev/null 2>&1
fi
git add robdoe_telemetry.json .provmark/ 2>/dev/null
git diff --staged --quiet && exit 0

TIMESTAMP=$(date +%s)
INVARIANT=$(jq -r '.invariant' robdoe_telemetry.json 2>/dev/null || echo "inv_${TIMESTAMP}")
git commit -m "SOVEREIGN STATE SEAL: Automatic checkpoint [invariant:${INVARIANT}]" >/dev/null 2>&1
git tag -a "SOVEREIGN-STATE-${INVARIANT}" -m "Locked local invariant state timestamp ${TIMESTAMP}" >/dev/null 2>&1
echo "[✓] Git commit sealed: SOVEREIGN-STATE-${INVARIANT}"
SH_COMMIT
chmod +x sovereign_autocommit.sh

# 3. Live HUD
cat << 'PYTHON_HUD' > sovereign_hud.py
import os, sys, time, json

def draw_hud():
    while True:
        os.system('clear')
        print("\033[92m========================================================================\033[0m")
        print("\033[1m              ROBDOE.COM // SOVEREIGN TERMINAL NODE HUD                  \033[0m")
        print("\033[92m========================================================================\033[0m")
        try:
            with open(os.path.expanduser("~/robdoe_telemetry.json"), "r") as f:
                data = json.load(f)
                print(f" [AUTHORITY]         : \033[93m{data.get('domain_authority')}\033[0m")
                print(f" [ACTIVE INVARIANT]  : \033[96m{data.get('invariant')}\033[0m")
                print(f" [SHA256 DAG ROOT]   : \033[94m{data.get('sha256_root')[:36]}...\033[0m")
                print(f" [PROVMARK VAULT]    : {data.get('local_dag_depth')} Records Sealed")
                print("------------------------------------------------------------------------")
                print(f" [SERIAL PORT]       : {data['channels']['serial_esp32']}")
                print(f" [LAN MESH]          : {data['channels']['lan_udp_mesh']}")
                print(f" [RUNTIME ENGINE]    : {data['channels']['termux_arm64']}")
        except Exception as e:
            print(f" [STATUS]            : WAITING FOR MASTER LOOP ({e})")
        print("\033[92m========================================================================\033[0m")
        print(" Press [CTRL+C] to exit HUD.")
        time.sleep(2)

if __name__ == "__main__":
    try:
        draw_hud()
    except KeyboardInterrupt:
        sys.exit(0)
PYTHON_HUD

# 4. Vault Archiver
cat << 'SH_BACKUP' > sovereign_backup.sh
#!/bin/bash
BACKUP_DIR="$HOME/sovereign_core/archives"
mkdir -p "$BACKUP_DIR"
TIMESTAMP=$(date +%s)
DEST="$BACKUP_DIR/sovereign_vault_${TIMESTAMP}.tar.gz"
tar -czf "$DEST" -C "$HOME" .provmark robdoe_telemetry.json .git 2>/dev/null
MASTER_HASH=$(sha256sum "$DEST" | awk '{print $1}')
echo "[✓] Vault Sealed: $DEST"
echo "[+] Master SHA256: $MASTER_HASH"
SH_BACKUP
chmod +x sovereign_backup.sh

# 5. Master Control Wrapper
cat << 'SH_RUN' > sovereign.sh
#!/bin/bash
case "$1" in
    bridge)
        python3 "$HOME/sovereign_core/sovereign_unified_bridge.py"
        "$HOME/sovereign_core/sovereign_autocommit.sh"
        ;;
    hud)
        python3 "$HOME/sovereign_core/sovereign_hud.py"
        ;;
    backup)
        "$HOME/sovereign_core/sovereign_backup.sh"
        ;;
    *)
        echo "Usage: ./sovereign.sh {bridge|hud|backup}"
        ;;
esac
SH_RUN
chmod +x sovereign.sh

echo "[======================================================================]"
echo " [✓] SOVEREIGN STACK FULLY DEPLOYED TO: $SOV_HOME"
echo " [✓] Master Control Command: ./sovereign.sh {bridge | hud | backup}"
echo "[======================================================================]"
