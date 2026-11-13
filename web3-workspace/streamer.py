import time
import sys
import requests

RPC_URL = sys.argv[1] if len(sys.argv) > 1 else "https://ethereum-rpc.publicnode.com"

def rpc_call(method, params=[]):
    payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
    try:
        response = requests.post(RPC_URL, json=payload, timeout=10)
        return response.json().get("result")
    except Exception as e:
        print(f"[!] RPC Error: {e}")
        return None

print(f"[*] Connecting to RPC: {RPC_URL}")
block_hex = rpc_call("eth_blockNumber")
if not block_hex:
    print("[✘] Failed to connect or retrieve block number.")
    sys.exit(1)

last_block = int(block_hex, 16)
print(f"[✔] Connected successfully! Current Block: #{last_block}")
print("==================================================")
print("       LIVE BLOCK TELEMETRY STREAM ACTIVE         ")
print("==================================================\n")

while True:
    try:
        current_hex = rpc_call("eth_blockNumber")
        if current_hex:
            current_block = int(current_hex, 16)
            if current_block > last_block:
                for b in range(last_block + 1, current_block + 1):
                    block_data = rpc_call("eth_getBlockByNumber", [hex(b), False])
                    if block_data:
                        num = int(block_data["number"], 16)
                        miner = block_data.get("miner", "0x0")
                        tx_count = len(block_data.get("transactions", []))
                        print(f"📦 [BLOCK #{num}]")
                        print(f"   ├─ Hash: {block_data['hash']}")
                        print(f"   ├─ Miner: {miner}")
                        print(f"   └─ Transactions: {tx_count}")
                        print("-" * 50)
                last_block = current_block
        time.sleep(3)
    except KeyboardInterrupt:
        print("\n[+] Stream gracefully terminated by user.")
        break
    except Exception as e:
        print(f"[!] Loop error: {e}")
        time.sleep(5)
