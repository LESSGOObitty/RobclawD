import os
import time
from datetime import datetime

LOG_PATH = os.path.expanduser("~/workspace/logs/esp32_telemetry.log")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# Default serial port in Termux for USB OTG devices (adjust if using /dev/ttyACM0)
SERIAL_PORT = os.environ.get("ESP32_PORT", "/dev/ttyUSB0")
BAUD_RATE = int(os.environ.get("ESP32_BAUD", "115200"))

def log_telemetry(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {data.strip()}\n"
    with open(LOG_PATH, "a") as f:
        f.write(line)
    print(line, end="")

def main():
    print(f"[*] Initializing ESP32 listener on {SERIAL_PORT} @ {BAUD_RATE}...")
    try:
        import serial
    except ImportError:
        print("[!] pyserial not found. Install it via: pip install pyserial")
        return

    while True:
        try:
            with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
                print(f"[+] Connected to ESP32 stream on {SERIAL_PORT}")
                while True:
                    line = ser.readline().decode('utf-8', errors='ignore')
                    if line.strip():
                        log_telemetry(line)
        except Exception as e:
            print(f"[!] Serial connection waiting/retry error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
