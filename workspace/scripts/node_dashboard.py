import http.server
import socketserver
import json
import os

PORT = 8080
HEALTH_PATH = os.path.expanduser("~/workspace/logs/health.json")
MANIFEST_DIR = os.path.expanduser("~/workspace/manifests")

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        # Read health beacon
        health_data = "{}"
        if os.path.exists(HEALTH_PATH):
            with open(HEALTH_PATH, "r") as f:
                health_data = f.read()
                
        # Find latest manifest
        latest_manifest = "None"
        if os.path.exists(MANIFEST_DIR):
            manifests = sorted(os.listdir(MANIFEST_DIR))
            if manifests:
                latest_manifest = manifests[-1]

        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>RobclawD Node Dashboard</title>
    <meta http-equiv="refresh" content="10">
    <style>
        body {{ background: #0f172a; color: #38bdf8; font-family: monospace; padding: 20px; }}
        h1 {{ color: #f43f5e; border-bottom: 1px solid #334155; padding-bottom: 10px; }}
        pre {{ background: #1e293b; padding: 15px; border-radius: 8px; border: 1px solid #334155; color: #f8fafc; }}
        .badge {{ background: #10b981; color: #000; padding: 2px 8px; border-radius: 4px; font-weight: bold; }}
    </style>
</head>
<body>
    <h1>🛡️ RobclawD Sovereign Node Dashboard</h1>
    <p>Status: <span class="badge">ONLINE</span> &bull; Auto-refreshing every 10s</p>
    
    <h2>Health Beacon</h2>
    <pre>{json.dumps(json.loads(health_data), indent=2) if health_data != "{}" else "Waiting for health beacon..."}</pre>
    
    <h2>Latest Manifest</h2>
    <pre>{latest_manifest}</pre>
</body>
</html>
"""
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        print(f"[+] Node dashboard running at http://127.0.0.1:{PORT}")
        httpd.serve_forever()
