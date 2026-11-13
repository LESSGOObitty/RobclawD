import socket

HOST = '0.0.0.0'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print(f"[*] Wi-Fi Telemetry Server listening on port {PORT}...")

try:
    while True:
        conn, addr = server.accept()
        print(f"[+] ESP32 Connected from {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"[TELEMETRY] {data.decode('utf-8', errors='ignore').strip()}")
except KeyboardInterrupt:
    print("\n[*] Shutting down server.")
finally:
    server.close()
