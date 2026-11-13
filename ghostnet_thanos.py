#!/data/data/com.termux/files/usr/bin/env python3
"""
Ghostnet // Thanos Edition: The Absolute Equilibrium & Pruning Engine
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
Fix: Corrected asyncio.start_server wrapper usage to support custom buffers cleanly.
"""
import asyncio
import sys
import time
import hashlib
import logging

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[35m[%(asctime)s]\x1b[0m \x1b[1;31m[THANOS SNAP]\x1b[0m %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)]
)
log = logging.getLogger("GhostnetThanos")

CONFIG = {
    "HOST": "127.0.0.1",
    "PORT": 9050,
    "BUFSZ": 131072,
    "CODENAME": "GHOSTNET-INFINITY-BALANCE-STABLE"
}

class EquilibriumLedger:
    def __init__(self):
        self.snaps = 0
        self.bytes_balanced = 0

    def balance_packet(self, data: bytes) -> bytes:
        self.snaps += 1
        self.bytes_balanced += len(data)
        
        mid = len(data) // 2
        pruned_data = data[:mid] if len(data) > 1024 else data
        
        sig = hashlib.sha256(data).hexdigest()[:12]
        log.info(f"\x1b[32m[BALANCED]\x1b[0m Snap #{self.snaps} | Raw: {len(data)}B -> Retained: {len(pruned_data)}B | Hash: {sig}")
        return pruned_data

ledger = EquilibriumLedger()

async def thanos_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    peer = writer.get_extra_info('peername')
    peer_id = f"{peer[0]}:{peer[1]}" if peer else "inevitable_node"
    log.info(f"\x1b[36m[+] REALITY ANCHORED:\x1b[0m Stream linked from {peer_id}")
    
    try:
        while True:
            chunk = await reader.read(CONFIG["BUFSZ"])
            if not chunk:
                break
            
            balanced_payload = ledger.balance_packet(chunk)
            writer.write(balanced_payload)
            await writer.drain()
            
    except asyncio.CancelledError:
        log.warning(f"\x1b[31m[-] REALITY SHIFT:\x1b[0m Stream closed for {peer_id}")
    except Exception as err:
        log.error(f"\x1b[31m[!] ANOMALY DETECTED:\x1b[0m {err}")
    finally:
        writer.close()
        await writer.wait_closed()
        log.info(f"\x1b[31m[-] EQUILIBRIUM REACHED:\x1b[0m Session cleared.")

async def main():
    # Using asyncio.start_server with standard parameters, bypassing raw loop.create_server arg mismatch
    server = await asyncio.start_server(
        thanos_handler,
        CONFIG["HOST"],
        CONFIG["PORT"],
        limit=CONFIG["BUFSZ"]
    )
    
    # Force socket reuse at the socket socket-level
    for sock in server.sockets:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    addr = server.sockets[0].getsockname()
    
    print("\n" + "="*68)
    print(f" \x1b[1;31m[GHOSTNET: THANOS EDITION ONLINE]\x1b[0m // {CONFIG['CODENAME']}")
    print(f" \x1b[1;33m[INEVITABLE]\x1b[0m root@robdoe.com // TARGET: {addr[0]}:{addr[1]}")
    print("="*68 + "\n")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        import socket
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\x1b[31m[!] SNAP EXECUTED. UNIVERSE BALANCED. SHUTTING DOWN.\x1b[0m")
        sys.exit(0)
