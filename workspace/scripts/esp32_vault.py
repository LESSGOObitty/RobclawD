import os
import sqlite3
import time
from datetime import datetime

DB_PATH = os.path.expanduser("~/workspace/data/telemetry.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

SERIAL_PORT = os.environ.get("ESP32_PORT", "/dev/ttyUSB0")
BAUD_RATE = int(os.environ.get("ESP32_BAUD", "115200"))

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            sensor_data TEXT,
            protocol_seed TEXT
        )
    """)
    # Seed genesis metadata referencing our foundational hardware protocol baseline
    cursor.execute("SELECT COUNT(*) FROM telemetry")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO telemetry (timestamp, sensor_data, protocol_seed) VALUES (?, ?, ?)",
            (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "GENESIS_INIT", "Law of Shaped Force")
        )
        conn.commit()
    conn.close()

def store_packet(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO telemetry (timestamp, sensor_data, protocol_seed) VALUES (?, ?, ?)",
        (timestamp, data.strip(), "Law of Shaped Force")
    )
    conn.commit()
    conn.close()
    print(f"[{timestamp}] [Vault] Stored packet: {data.strip()}")

def main():
    init_db()
    print(f"[*] Initializing ESP32 Vault listener on {SERIAL_PORT} @ {BAUD_RATE}...")
    try:
        import serial
    except ImportError:
        print("[!] pyserial not found. Install via: pip install pyserial")
        return

    while True:
        try:
            with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
                print(f"[+] Connected to ESP32 vault stream on {SERIAL_PORT}")
                while True:
                    line = ser.readline().decode('utf-8', errors='ignore')
                    if line.strip():
                        store_packet(line)
        except Exception as e:
            print(f"[!] Vault serial connection retry error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
