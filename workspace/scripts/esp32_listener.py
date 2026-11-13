import glob
import sys
import time

try:
    import serial
except ImportError:
    print("[-] pyserial missing. Run: pip install pyserial")
    sys.exit(1)

def find_serial_port():
    ports = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')
    return ports

def main():
    print("[*] Initializing ESP32 Serial Telemetry Daemon...")
    while True:
        ports = find_serial_port()
        if not ports:
            print("[-] No serial devices found (/dev/ttyUSB* or /dev/ttyACM*). Retrying...")
            time.sleep(3)
            continue
            
        port = ports[0]
        print(f"[+] Found active interface on {port}. Opening at 115200 baud...")
        try:
            with serial.Serial(port, 115200, timeout=1) as ser:
                while True:
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line:
                        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                        print(f"[{timestamp}] [TELEMETRY] {line}")
        except Exception as e:
            print(f"[-] Serial stream error on {port}: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()
