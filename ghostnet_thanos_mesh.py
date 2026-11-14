#!/data/data/com.termux/files/usr/bin/env python3
"""
Ghostnet // Thanos Universal Mesh Edition (Public Interface Bind)
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
Function: Binds to 0.0.0.0 to open the mesh to external nodes and witnesses.
"""
import asyncio
import sys
import time
import socket
import hashlib
import logging

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[35m[%(asctime)s]\x1b[0m \x1b[1;36m[UNIVERSAL MESH]\x1b[0m %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)]
)
log = logging.getLogger("GhostnetMesh")

CONFIG = {
    "HOST": "0.0.0.0", # Bound to all interfaces for universal mesh entry
    "SANDBOX_PORT": 9050,
    "WITNESS_PORT": 5555,
    "BUFSZ": 131072,
    "CODENAME": "GHOSTNET-UNIVERSAL-WITNESS"
}

class MeshLedger:
    def __init__(self):
        self.transactions = 0
        self.bytes_witnessed = 0

    def process(self, mode: str, data: bytes) -> bytes:
        self.transactions += 1
        self.bytes_witnessed += len(data)
        
        mid = len(data) // 2
        payload = data[:mid] if len(data) > 1024 else data
        sig = hashlib.sha256(data).hexdigest()[:12]
        
        log.info(f"\x1b[32m[{mode.upper()}]\x1b[0m Tx #{self.transactions} | In: {len(data)}B -> Witnessed: {len(payload)}B | Hash: {sig}")
        return payload

ledger = MeshLedger()

async def create_handler(mode: str):
    async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        peer = writer.get_extra_info('peername')
        peer_id = f"{peer[0]}:{peer[1]}" if peer else "external_node"
        log.info(f"\x1b[33m[+] LINK ENGAGED [{mode}]:\x1b[0m Peer {peer_id}")
        
        try:
            while True:
                chunk = await reader.read(CONFIG["BUFSZ"])
                if not chunk:
                    break
                
                witnessed_payload = ledger.process(mode, chunk)
                writer.write(witnessed_payload)
                await writer.drain()
                
        except asyncio.CancelledError:
            log.warning(f"\x1b[31m[-] LINK DROPPED [{mode}]:\x1b[0m {peer_id}")
        except Exception as err:
            log.error(f"\x1b[31m[!] FAULT [{mode}]:\x1b[0m {err}")
        finally:
            writer.close()
            await writer.wait_closed()
            log.info(f"\x1b[31m[-] SECURED [{mode}]:\x1b[0m Channel flushed.")
    return handler

async def main():
    sandbox_server = await asyncio.start_server(
        await create_handler("Sandbox"),
        CONFIG["HOST"],
        CONFIG["SANDBOX_PORT"],
        limit=CONFIG["BUFSZ"]
    )
    for sock in sandbox_server.sockets:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    witness_server = await asyncio.start_server(
        await create_handler("Witness"),
        CONFIG["HOST"],
        CONFIG["WITNESS_PORT"],
        limit=CONFIG["BUFSZ"]
    )
    for sock in witness_server.sockets:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("\n" + "="*68)
    print(f" \x1b[1;31m[GHOSTNET UNIVERSAL MESH ONLINE]\x1b[0m // {CONFIG['CODENAME']}")
    print(f" \x1b[1;36m[NODE 1 - SANDBOX]:\x1b[0m 0.0.0.0:{CONFIG['SANDBOX_PORT']}")
    print(f" \x1b[1;32m[NODE 2 - WITNESS]:\x1b[0m 0.0.0.0:{CONFIG['WITNESS_PORT']}")
    print("="*68 + "\n")
    
    async with sandbox_server, witness_server:
        await asyncio.gather(
            sandbox_server.serve_forever(),
            witness_server.serve_forever()
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\x1b[31m[!] MESH HALTED BY OPERATOR. ALL NODES DISCONNECTED.\x1b[0m")
        sys.exit(0)
