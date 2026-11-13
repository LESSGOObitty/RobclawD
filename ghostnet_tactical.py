#!/data/data/com.termux/files/usr/bin/env python3
"""
Ghostnet // Tactical Street-Grade Asynchronous Proxy Daemon
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
Profile: Zero fluff, raw telemetry, aggressive local routing, elite armored sockets.
"""
import asyncio
import sys
import os
import time
import hashlib
import logging

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[36m[%(asctime)s]\x1b[0m \x1b[32m[TACTICAL]\x1b[0m %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)]
)
log = logging.getLogger("GhostnetTactical")

CONFIG = {
    "HOST": "127.0.0.1",
    "PORT": 9050,
    "BUFSZ": 131072, # 128KB tactical chunk sizing
    "CODENAME": "GHOSTNET-TACTICAL-EDITION-V1"
}

class TacticalLedger:
    def __init__(self):
        self.hits = 0
        self.bytes_moved = 0
        self.start_time = time.time()

    def record(self, size: int):
        self.hits += 1
        self.bytes_moved += size

    def stats(self):
        uptime = int(time.time() - self.start_time)
        return f"Uptime: {uptime}s | Packets: {self.hits} | Thru: {self.bytes_moved} bytes"

ledger = TacticalLedger()

async def tactical_proxy_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    peer = writer.get_extra_info('peername')
    peer_id = f"{peer[0]}:{peer[1]}" if peer else "local_mesh"
    log.info(f"\x1b[33m[+] LOCK ACQUIRED:\x1b[0m Inbound link from {peer_id}")
    
    try:
        while True:
            raw_packet = await reader.read(CONFIG["BUFSZ"])
            if not raw_packet:
                break
            
            sig = hashlib.blake2b(raw_packet, digest_size=8).hexdigest()
            ledger.record(len(raw_packet))
            
            log.info(f"\x1b[35m[INTERCEPT]\x1b[0m Chunk: {len(raw_packet)}B | Hash: {sig} | \x1b[34m[{ledger.stats()}]\x1b[0m")
            
            # Tactical loopback / forward relay
            writer.write(raw_packet)
            await writer.drain()
            
    except asyncio.CancelledError:
        log.warning(f"\x1b[31m[-] LINK DROPPED:\x1b[0m Session cancelled for {peer_id}")
    except Exception as err:
        log.error(f"\x1b[31m[!] FAULT:\x1b[0m {peer_id} -> {err}")
    finally:
        writer.close()
        await writer.wait_closed()
        log.info(f"\x1b[31m[-] SECURED:\x1b[0m Connection cleaned for {peer_id}")

async def main():
    server = await asyncio.start_server(
        tactical_proxy_handler, 
        CONFIG["HOST"], 
        CONFIG["PORT"],
        limit=CONFIG["BUFSZ"]
    )
    
    print("\n" + "="*68)
    print(f" \x1b[1;32m[GHOSTNET TACTICAL ONLINE]\x1b[0m // {CONFIG['CODENAME']}")
    print(f" \x1b[1;36m[NODE]\x1b[0m root@robdoe.com // BIND: {CONFIG['HOST']}:{CONFIG['PORT']}")
    print("="*68 + "\n")
    
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\x1b[31m[!] TACTICAL SHUTDOWN BY OPERATOR. CHANNELS CLEARED.\x1b[0m")
        sys.exit(0)
