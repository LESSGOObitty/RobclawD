import os
import sys
from web3 import Web3
from eth_account import Account

# Configuration
RPC_URL = os.environ.get("EVM_RPC_URL", "https://polygon-rpc.com")
PRIVATE_KEY = os.environ.get("UD_PRIVATE_KEY", "")

def init_wallet():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print(f"[-] Error: Unable to connect to EVM RPC node at {RPC_URL}")
        sys.exit(1)
        
    print(f"[+] Connected to EVM Node (Chain ID: {w3.eth.chain_id})")
    
    if not PRIVATE_KEY:
        print("[-] Warning: UD_PRIVATE_KEY/EVM_PRIVATE_KEY not set in environment.")
        print("    Generate or export a signer key with: export UD_PRIVATE_KEY='0x...'")
        return w3, None
        
    account = Account.from_key(PRIVATE_KEY)
    balance_wei = w3.eth.get_balance(account.address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    
    print(f"[+] Signer Address : {account.address}")
    print(f"[+] Wallet Balance : {balance_eth} ETH/MATIC")
    
    return w3, account

if __name__ == "__main__":
    print("[*] Initializing EVM Ecosystem Wallet...")
    w3, account = init_wallet()
    if account:
        print("[+] Wallet ready for BFT state anchoring and contract dispatch.")
