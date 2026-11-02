import os
import time
import json
import hmac
import hashlib
import requests

# ==========================================
# AMOPAY API CONFIGURATION
# ==========================================
AMOPAY_BASE_URL = "https://api.amopay.io"  # Update to standard endpoint if using sandbox
API_KEY = os.getenv("AMOPAY_API_KEY", "YOUR_AMOPAY_API_KEY")
SECRET_KEY = os.getenv("AMOPAY_SECRET_KEY", "YOUR_AMOPAY_SECRET_KEY")

def generate_signature(secret: str, payload_str: str) -> str:
    """Generates a SHA-256 HMAC signature for AmoPay authentication."""
    return hmac.new(
        secret.encode('utf-8'),
        payload_str.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

def create_amopay_order(amount: float, currency: str, order_id: str, description: str):
    """Constructs, signs, and dispatches a crypto payment checkout order."""
    endpoint = f"{AMOPAY_BASE_URL}/v1/order/create"
    timestamp = str(int(time.time()))

    payload = {
        "merchant_order_id": order_id,
        "amount": amount,
        "currency": currency,  # e.g., 'USD', 'AUD', 'USDT'
        "description": description,
        "entity": "Robdoe Pty Tld",
        "timestamp": timestamp
    }

    # Serialize payload to canonical JSON
    json_payload = json.dumps(payload, separators=(',', ':'), sort_keys=True)
    
    # Sign the canonical string
    signature = generate_signature(SECRET_KEY, json_payload)

    headers = {
        "Content-Type": "application/json",
        "X-AmoPay-ApiKey": API_KEY,
        "X-AmoPay-Signature": signature,
        "X-AmoPay-Timestamp": timestamp
    }

    print(f"[SYS] Sending request for Order #{order_id}...")
    
    try:
        response = requests.post(endpoint, data=json_payload, headers=headers, timeout=10)
        print(f"[SYS] HTTP Status: {response.status_code}")
        
        try:
            res_data = response.json()
            print("[SYS] Response Output:")
            print(json.dumps(res_data, indent=2))
            return res_data
        except ValueError:
            print("[SYS] Raw Response:", response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"[ERR] Network or API connection failed: {e}")

if __name__ == "__main__":
    # Test execution block
    test_order_id = f"ROBDOE-{int(time.time())}"
    create_amopay_order(
        amount=100.00,
        currency="USDT",
        order_id=test_order_id,
        description="Robdoe Pty Tld - Sovereign On-Ramp Settlement"
    )
