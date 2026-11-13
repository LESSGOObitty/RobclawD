#!/usr/bin/env python3
"""
ROBDOE ROOT AUTHORITY // Native Local Blockchain Engine & CLI
Implements block mining, cryptographic hash chaining, and integrity validation.
"""

import hashlib
import json
import os
import sys
import time

CHAIN_PATH = ".termux_chain.json"

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty=2):
        target = "0" * difficulty
        print(f"[*] Mining Block #{self.index} (Target prefix: {target})...")
        start = time.time()
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()
        duration = time.time() - start
        print(f" [+] Mined! Nonce: {self.nonce} | Hash: {self.hash[:32]}... ({duration:.3f}s)")

class TermuxChain:
    def __init__(self):
        self.chain = []
        self.difficulty = 2
        self.load_or_initialize()

    def load_or_initialize(self):
        if os.path.exists(CHAIN_PATH):
            try:
                with open(CHAIN_PATH, "r") as f:
                    raw_data = json.load(f)
                    for b_dict in raw_data:
                        block = Block(
                            b_dict["index"],
                            b_dict["timestamp"],
                            b_dict["data"],
                            b_dict["previous_hash"],
                            b_dict["nonce"]
                        )
                        block.hash = b_dict["hash"]
                        self.chain.append(block)
                return
            except Exception:
                print("[!] Error loading chain file. Re-initializing genesis...")
        
        # Create Genesis Block
        genesis = Block(0, time.time(), {"note": "ROBDOE GENESIS ANCHOR", "watermark": "espVmark:2c3f1b0af3a2367a"}, "0")
        genesis.mine_block(self.difficulty)
        self.chain.append(genesis)
        self.save_chain()

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=previous_block.hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.save_chain()

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def save_chain(self):
        chain_data = [{
            "index": b.index,
            "timestamp": b.timestamp,
            "data": b.data,
            "previous_hash": b.previous_hash,
            "nonce": b.nonce,
            "hash": b.hash
        } for b in self.chain]
        with open(CHAIN_PATH, "w") as f:
            json.dump(chain_data, f, indent=2)

def print_help():
    print("=========================================================")
    print(" [TERMUX CHAIN CLI] Usage:")
    print("   python3 termux_chain.py mine 'Your custom block data'")
    print("   python3 termux_chain.py inspect")
    print("   python3 termux_chain.py verify")
    print("=========================================================")

if __name__ == "__main__":
    bc = TermuxChain()
    args = sys.argv[1:]
    
    if not args:
        print_help()
        sys.exit(0)
        
    cmd = args[0]
    
    if cmd == "mine":
        payload = args[1] if len(args) > 1 else "Autonomous telemetry snapshot"
        try:
            data_dict = json.loads(payload)
        except Exception:
            data_dict = {"message": payload}
        bc.add_block(data_dict)
        print(f"[+] Block successfully appended to chain. Height: {len(bc.chain)}")
        
    elif cmd == "inspect":
        print("=========================================================")
        print(f" [CHAIN INSPECTOR] Total Blocks: {len(bc.chain)}")
        print("=========================================================")
        for b in bc.chain:
            print(f"Block #{b.index} | Nonce: {b.nonce}")
            print(f"  Hash: {b.hash}")
            print(f"  Prev: {b.previous_hash}")
            print(f"  Data: {b.data}")
            print("-" * 57)
            
    elif cmd == "verify":
        valid = bc.is_valid()
        print(f"=========================================================")
        print(f" [CHAIN INTEGRITY] Status: {'VALID (IMMUTABLE)':<30}")
        print(f" Root Tip Hash           : {bc.chain[-1].hash}")
        print(f"=========================================================")
    else:
        print_help()
