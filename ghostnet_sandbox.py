#!/data/data/com.termux/files/usr/bin/env python3
"""
Ghostnet // Tactical Sandbox & Packet Mutation Engine
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
Function: Intercepts, isolates, and analyzes local TCP test streams in real-time.
"""
import asyncio
import sys
import time
import hashlib
import logging

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[36m[%(asctime)s]\x1b[0m \x1b[31m[SANDBOX]\x1b[0m %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)]
)
log = logging.getLogger("GhostnetSandbox")

CONFIG = {
    "HOST": "127.0.0.1",
    "PORT": 9050,
    "BUFSZ": 131072,
    "CODENAME": "GHOSTNET-SANDBOX-EDITION"
}

class SandboxLedger:
    def __init__(self):
        self.intercepted_count = 0
        self.total_bytes = 0

    def log_payload(self, size: int, sig: str):
        self.intercepted_count += 1
        self.total_bytes += size
        log.info(f"\x1b[33m[MUTATION LAB]\x1b[0m Packet #{self.intercepted_count} | Size: {size}B | BLAKE2b: {sig}")

ledger = SandboxLedger()

async def sandbox_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    peer = writer.get_extra_info('peername')
    peer_id = f"{peer[0]}:{peer[1]}" if peer else "local_probe"
    log.info(f"\x1b[32m[+] TEST PROBE ATTACHED:\x1b[0m {peer_id}")
    
    try:
        while True:
            payload = await reader.read(CONFIG["BUFSZ"])
            if not payload:
                break
            
            sig = hashlib.blake2b(payload, digest_size=8).hexdigest()
            ledger.log_payload(len(payload), sig)
            
            # Sandbox mutation / inspection hook:
            # Here we can inspect raw bytes, test payloads, or mirror back safely.
            # E.g., appending sovereign telemetry marker or mirroring intact.
            
            writer.write(payload)
            await writer.drain()
            
    except asyncio.CancelledError:
        log.warning(f"\x1b[31m[-] SANDBOX RESET:\x1b[0m Probe {peer_id} disconnected.")
    except Exception as err:
        log.error(f"\x1b[31m[!] EXCEPTION:\x1b[0m {err}")
    finally:
        writer.close()
        await writer.wait_closed()
        log.info(f"\x1b[31m[-] SECURED:\x1b[0m Sandbox session flushed for {peer_id}")

async def main():
    server = await asyncio.start_server(sandbox_handler, CONFIG["HOST"], CONFIG["PORT"], limit=CONFIG["BUFSZ"])
    addr = server.sockets[0].getsockname()
    
    print("\n" + "="*68)
    print(f" \x1b[1;31m[GHOSTNET SANDBOX ACTIVE]\x1b[0m // {CONFIG['CODENAME']}")
    print(f" \x1b[1;36m[ISOLATION ZONE]\x1b[0m root@robdoe.com // TARGET: {addr[0]}:{addr[1]}")
    print("="*68 + "\n")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\x1b[31m[!] SANDBOX TERMINATED. ALL BUFFERS PURGED.\x1b[0m")
        sys.exit(0)
