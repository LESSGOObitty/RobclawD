import os
import time
import subprocess
from datetime import datetime

LOG_PATH = os.path.expanduser("~/workspace/logs/thermal_pulse.log")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def get_battery_temp():
    try:
        res = subprocess.run(["termux-battery-status"], capture_output=True, text=True, timeout=3)
        import json
        data = json.loads(res.stdout)
        return data.get("temperature", 0.0), data.get("percentage", 0)
    except Exception:
        return 0.0, 0

while True:
    temp, pct = get_battery_temp()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_line = f"[{timestamp}] Battery: {pct}% | Temp: {temp}°C\n"
    with open(LOG_PATH, "a") as f:
        f.write(log_line)
        
    # Safety throttling if battery temp exceeds 42°C
    if temp > 42.0:
        print(f"[{timestamp}] [!] WARNING: High thermal state ({temp}°C). Throttling engine cycle...")
        time.sleep(60) # Cool-down pause
        
    time.sleep(300) # Check every 5 minutes
