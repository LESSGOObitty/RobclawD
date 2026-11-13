#!/data/data/com.termux/files/usr/bin/env python3
"""
RobDoeAI-Core // Native Termux Asynchronous TCP Proxy Daemon
Operator: root@robdoe.com (1 of 1 Sovereign Monolith)
"""
import asyncio
import sys

async def handle_client(reader, writer):
    peer = writer.get_extra_info('peername')
    print(f"[+] Connection established from {peer}")
    try:
        while True:
            data = await reader.read(4096)
            if not data:
                break
            # Echo / Forward stream logic for local socket testing
            writer.write(data)
            await writer.drain()
    except Exception as e:
        print(f"[-] Error handling client {peer}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"[-] Connection closed for {peer}")

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8080)
    addr = server.sockets[0].getsockname()
    print("=" * 74)
    print(f" [DAEMON] LOCAL PROXY LISTENING ON {addr[0]}:{addr[1]}")
    print("=" * 74)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Proxy daemon stopped by operator.")
        sys.exit(0)
