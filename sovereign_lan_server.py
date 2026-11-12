import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = os.path.expanduser("~")

class SovereignHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"[+] Sovereign LAN Server active on port {PORT}")
print(f"[+] Open http://localhost:{PORT}/robdoe_telemetry.json in browser")

with socketserver.TCPServer(("", PORT), SovereignHTTPHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Shutting down LAN Server.")

