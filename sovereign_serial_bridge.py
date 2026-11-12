import os, sys, time, json

SERIAL_PORT = "/dev/ttyUSB0"  # Adjust for Termux /dev/ttyACM0 if needed
BAUD_RATE = 115200
TELEMETRY_PATH = os.path.expanduser("~/robdoe_telemetry.json")

def push_to_serial():
    if not os.path.exists(TELEMETRY_PATH):
        print("[-] Telemetry file not found. Run unified bridge first.")
        return
        
    with open(TELEMETRY_PATH, "r") as f:
        data = f.read()
        
    print(f"[+] Targeting Serial Port {SERIAL_PORT} at {BAUD_RATE} baud...")
    print(f"[+] Payload Size: {len(data)} bytes")
    
    # In Termux, direct hardware serial access requires termux-api or pySerial with USB permissions
    try:
        import serial
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
            ser.write(data.encode('utf-8') + b'\n')
            print("[✓] State payload successfully broadcasted over physical serial line.")
    except ImportError:
        print("[!] PySerial not installed. Run: pip install pyserial")
    except Exception as e:
        print(f"[!] Serial hardware offline or locked ({e}). State maintained locally in vault.")

if __name__ == "__main__":
    push_to_serial()
