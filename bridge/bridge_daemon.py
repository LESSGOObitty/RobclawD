import os
import sys
import time

PIPE_PATH = os.path.expanduser("~/bridge/event_channel")

print(f"[+] Bridge Active on: {PIPE_PATH}")
print("[+] Listening for local/serial event streams...")

while True:
    try:
        with open(PIPE_PATH, "r") as pipe:
            for line in pipe:
                line = line.strip()
                if line:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"[{timestamp}] [BRIDGE OUT] -> {line}")
    except Exception as e:
        print(f"[!] Pipe error: {e}")
        time.sleep(1)
