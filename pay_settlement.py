import os
import json
from web3 import Web3

# ==========================================
# ROBDOE PTY TLD - DIRECT SETTLEMENT ENGINE
# ==========================================
RPC_ENDPOINT = os.getenv("ROBDOE_RPC", "https://polygon-rpc.com")
w3 = Web3(Web3.HTTPProvider(RPC_ENDPOINT))

# Your EVM Address from Account 1
RECIPIENT_ADDRESS = "0x84CA47A8C8432C52B9d25514fC7e651214c22018"
AMOUNT_TO_PAY = 1068.376068

def execute_sovereign_payment():
    print(f"[SYS] Initializing payment pipeline for Robdoe Pty Tld...")
    print(f"[SYS] Target Amount: {AMOUNT_TO_PAY}")
    print(f"[SYS] Destination Node: {RECIPIENT_ADDRESS}")
    
    if not w3.is_connected():
        print("[ERR] RPC connection failed.")
        return

    sender_key = os.getenv("ROBDOE_PRIVATE_KEY")
    if not sender_key:
        print("[ERR] ROBDOE_PRIVATE_KEY environment variable not set.")
        return

    account = w3.eth.account.from_key(sender_key)
    nonce = w3.eth.get_transaction_count(account.address)

    tx = {
        'nonce': nonce,
        'to': Web3.to_checksum_address(RECIPIENT_ADDRESS),
        'value': w3.to_wei(AMOUNT_TO_PAY, 'ether'),
        'gas': 65000,
        'gasPrice': w3.eth.gas_price,
        'chainId': w3.eth.chain_id
    }

    signed_tx = w3.eth.account.sign_transaction(tx, sender_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    print(f"[SYS] Transaction broadcasted successfully.")
    print(f"[SYS] Tx Hash: {w3.to_hex(tx_hash)}")

if __name__ == "__main__":
    execute_sovereign_payment()
