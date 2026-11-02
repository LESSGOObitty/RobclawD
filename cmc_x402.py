import os
import secrets
import time
import requests
from eth_account import Account
from eth_account.messages import encode_typed_data

BASE_RPC = os.getenv("BASE_RPC_URL", "https://mainnet.base.org")
PRIVATE_KEY = os.getenv("ROBDOE_PRIVATE_KEY")

if not PRIVATE_KEY:
    print("[ERR] ROBDOE_PRIVATE_KEY environment variable is not set.")
    exit(1)

account = Account.from_key(PRIVATE_KEY)

def sign_eip3009_authorization(pay_req):
    accept_data = pay_req["accepts"][0]
    
    pay_to = accept_data["payTo"]
    asset = accept_data["asset"]
    value = int(accept_data["amount"])
    
    valid_after = 0
    valid_before = int(time.time()) + accept_data.get("maxTimeoutSeconds", 30)
    nonce = "0x" + secrets.token_hex(32)

    domain = {
        "name": accept_data.get("extra", {}).get("name", "USD Coin"),
        "version": accept_data.get("extra", {}).get("version", "2"),
        "chainId": 8453,
        "verifyingContract": asset
    }

    types = {
        "TransferWithAuthorization": [
            {"name": "from", "type": "address"},
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"},
            {"name": "validAfter", "type": "uint256"},
            {"name": "validBefore", "type": "uint256"},
            {"name": "nonce", "type": "bytes32"}
        ]
    }

    message = {
        "from": account.address,
        "to": pay_to,
        "value": value,
        "validAfter": valid_after,
        "validBefore": valid_before,
        "nonce": bytes.fromhex(nonce[2:])
    }

    signable_msg = encode_typed_data(domain, types, message)
    signed = account.sign_message(signable_msg)

    return {
        "v": signed.v,
        "r": hex(signed.r),
        "s": hex(signed.s),
        "from": account.address,
        "to": pay_to,
        "value": str(value),
        "validAfter": str(valid_after),
        "validBefore": str(valid_before),
        "nonce": nonce
    }

def fetch_x402_data(endpoint_url):
    print(f"[SYS] Querying: {endpoint_url}")
    res = requests.get(endpoint_url)

    if res.status_code == 402:
        print("[SYS] HTTP 402 Payment Required received. Signing EIP-3009 USDC authorization...")
        pay_req = res.json()
        
        sig_data = sign_eip3009_authorization(pay_req)
        headers = {"PAYMENT-SIGNATURE": requests.compat.quote(str(sig_data))}
        
        print("[SYS] Retrying request with PAYMENT-SIGNATURE header...")
        final_res = requests.get(endpoint_url, headers=headers)
        return final_res.json()
    
    return res.json()

if __name__ == "__main__":
    url = "https://pro-api.coinmarketcap.com/x402/v3/cryptocurrency/listings/latest?start=1&limit=10"
    data = fetch_x402_data(url)
    print(data)
