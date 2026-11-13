import subprocess
import os
import datetime

LOG_FILE = os.path.expanduser("~/workspace/telemetry.log")
KUBO_IP = "34.68.218.70"
KUBO_API_PORT = "5001"
KUBO_GATEWAY_PORT = "8080"
MFS_TARGET = "/robdoe_telemetry.log"

def sync_to_ipfs():
    if not os.path.exists(LOG_FILE):
        print(f"[-] Telemetry log not found at {LOG_FILE}")
        return
        
    print(f"[*] Staging {LOG_FILE} to Kubo node at {KUBO_IP}...")
    api_multiaddr = f"/ip4/{KUBO_IP}/tcp/{KUBO_API_PORT}"
    
    try:
        # Add file to Kubo node via explicit remote API multiaddr
        add_res = subprocess.run(
            ["ipfs", "--api", api_multiaddr, "add", "-q", LOG_FILE],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        cid = add_res.stdout.strip()
        timestamp = datetime.datetime.now().isoformat()
        
        print(f"[+] Telemetry successfully pinned to Kubo node {KUBO_IP}!")
        print(f"    CID     : {cid}")
        print(f"    Timestamp: {timestamp}")
        
        # Mirror to MFS on the target node
        subprocess.run(["ipfs", "--api", api_multiaddr, "files", "rm", MFS_TARGET], stderr=subprocess.DEVNULL)
        subprocess.run(["ipfs", "--api", api_multiaddr, "files", "cp", f"/ipfs/{cid}", MFS_TARGET], check=True)
        
        print(f"[+] MFS Synced: mfs://{MFS_TARGET} -> {cid}")
        print(f"    Gateway URL : http://{KUBO_IP}:{KUBO_GATEWAY_PORT}/ipfs/{cid}")
        
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to communicate with Kubo node at {KUBO_IP}: {e.stderr.strip()}")
    except Exception as e:
        print(f"[-] Unexpected error: {e}")

if __name__ == "__main__":
    sync_to_ipfs()
