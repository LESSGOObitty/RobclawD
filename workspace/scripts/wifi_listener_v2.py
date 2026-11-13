import socketserver
import datetime
import os

PORT = 9090
LOG_FILE = os.path.expanduser("~/workspace/telemetry.log")

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

class TelemetryHandler(socketserver.BaseRequestHandler):
    def handle(self):
        client_ip = self.client_address[0]
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[+] [{timestamp}] ESP32 Connected: {client_ip}")
        try:
            while True:
                data = self.request.recv(1024)
                if not data:
                    break
                payload = data.decode('utf-8', errors='ignore').strip()
                log_entry = f"[{datetime.datetime.now().isoformat()}] [{client_ip}] {payload}"
                print(f"[TELEMETRY] {log_entry}")
                with open(LOG_FILE, "a") as f:
                    f.write(log_entry + "\n")
        except Exception as e:
            print(f"[-] Connection error with {client_ip}: {e}")

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    print(f"[*] Starting Threaded Wi-Fi Telemetry Daemon on port {PORT}...")
    with ThreadedTCPServer(("0.0.0.0", PORT), TelemetryHandler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Shutting down telemetry daemon cleanly.")
