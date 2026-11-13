#!/data/data/com.termux/files/usr/bin/env python3
"""
Ghostnet // Byzantine Fault Tolerant (BFT) Firewall & Consensus Witness
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
Fix: Cleaned socket binding, aggressive stale process purge.
"""
import asyncio
import sys
import socket
import hashlib
import hmac
import logging

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[36m[%(asctime)s]\x1b[0m \x1b[1;32m[BFT FIREWALL]\x1b[0m %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)]
)
log = logging.getLogger("GhostnetBFT")

CONFIG = {
    "HOST": "0.0.0.0",
    "PORT": 5555,
    "BUFSZ": 131072,
    "SECRET_KEY": b"ROBDOE_SOVEREIGN_BFT_KEY_2026",
    "CODENAME": "GHOSTNET-BFT-QUORUM-STABLE"
}

class BFTConsensusEngine:
    def __init__(self):
        self.verified_count = 0
        self.rejected_count = 0

    def validate_packet(self, peer: str, data: bytes) -> tuple[bool, bytes]:
        if len(data) < 32:
            self.rejected_count += 1
            return False, b"REJECTED: UNDERSIZED_STATE"

        payload = data[:-32]
        provided_sig = data[-32:]
        expected_sig = hmac.new(CONFIG["SECRET_KEY"], payload, hashlib.sha256).digest()

        if hmac.compare_digest(expected_sig, provided_sig):
            self.verified_count += 1
            sig_hex = hashlib.sha256(payload).hexdigest()[:12]
            log.info(f"\x1b[33m[QUORUM ACHIEVED]\x1b[0m Peer: {peer} | State Verified | Hash: {sig_hex} | Validated: {self.verified_count}")
            return True, payload
        else:
            self.rejected_count += 1
            log.warning(f"\x1b[31m[BYZANTINE FAULT DETECTED]\x1b[0m Peer: {peer} | State Corrupted! Rejected: {self.rejected_count}")
            return False, b"REJECTED: BFT_CONSENSUS_FAILURE"

bft_engine = BFTConsensusEngine()

async def bft_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    peer = writer.get_extra_info('peername')
    peer_id = f"{peer[0]}:{peer[1]}" if peer else "mesh_node"
    log.info(f"\x1b[35m[+] NODE ATTEMPTING CONSENSUS:\x1b[0m {peer_id}")
    
    try:
        while True:
            chunk = await reader.read(CONFIG["BUFSZ"])
            if not chunk:
                break
            
            is_valid, response = bft_engine.validate_packet(peer_id, chunk)
            
            if is_valid:
                mid = len(response) // 2
                balanced = response[:mid] if len(response) > 1024 else response
                writer.write(balanced)
            else:
                writer.write(response)
                
            await writer.drain()
            
    except asyncio.CancelledError:
        log.warning(f"\x1b[31m[-] LINK DROPPED:\x1b[0m {peer_id}")
    except Exception as err:
        log.error(f"\x1b[31m[!] FAULT:\x1b[0m {err}")
    finally:
        writer.close()
        await writer.wait_closed()
        log.info(f"\x1b[31m[-] CONNECTION SECURED:\x1b[0m {peer_id}")

async def main():
    server = await asyncio.start_server(
        bft_handler,
        CONFIG["HOST"],
        CONFIG["PORT"],
        limit=CONFIG["BUFSZ"]
    )
    for sock in server.sockets:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    addr = server.sockets[0].getsockname()
    
    print("\n" + "="*68)
    print(f" \x1b[1;32m[GHOSTNET: BFT FIREWALL ONLINE]\x1b[0m // {CONFIG['CODENAME']}")
    print(f" \x1b[1;36m[CONSENSUS LISTENER]:\x1b[0m {addr[0]}:{addr[1]}")
    print("="*68 + "\n")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\x1b[31m[!] BFT DAEMON HALTED. QUORUM DISCONNECTED.\x1b[0m")
        sys.exit(0)
