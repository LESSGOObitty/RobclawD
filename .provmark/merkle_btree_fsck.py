import json
import sqlite3
import hashlib
import os
import sys

def keccak256(data_bytes):
    return hashlib.sha3_256(data_bytes).hexdigest()

class ProvMarkFSCK:
    def __init__(self):
        self.db_path = os.path.expanduser("~/.provmark/state_vault.db")
        self.corrupted_nodes = 0
        self.verified_nodes = 0

    def run_diagnostic(self):
        print("\n\033[1;36m================================================================\033[0m")
        print("\033[1;33m[~] INITIALISING MERKLE DAG & B-TREE DIAGNOSTIC VERIFICATION (fsck)\033[0m")
        print(f"    Target Database Vault: {self.db_path}")
        print("\033[1;36m================================================================\033[0m")

        if not os.path.exists(self.db_path):
            print("\033[1;31m[-] FSCK CRITICAL ERROR: State Vault Database File Missing.\033[0m")
            sys.exit(1)

        # Connect to persistent storage index
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            # Query all stored block states chronologically
            cursor.execute("SELECT root_hash, leaf_data, cosmic_time, block_height FROM cosmic_blocks ORDER BY block_height ASC")
            blocks = cursor.fetchall()
        except sqlite3.OperationalError:
            print("\033[1;31m[-] FSCK CRITICAL ERROR: Table 'cosmic_blocks' is missing or corrupted.\033[0m")
            conn.close()
            sys.exit(1)

        if not blocks:
            print("\033[1;33m[!] FSCK NOTICE: Database is empty. No Merkle blocks found to audit.\033[0m")
            conn.close()
            sys.exit(0)

        print(f"[+] Found {len(blocks)} State Entries in B-Tree Index. Commencing deep hash validation...\n")

        for stored_root, leaf_json, cosmic_json, height in blocks:
            # 1. Parse and verify structural content
            leaves = json.loads(leaf_json)
            
            # Reconstruct the exact binary tree layer to verify the root
            leaf_hashes = []
            for leaf in leaves:
                # Re-serialize to verify immutable content
                serialized_leaf = json.dumps(leaf, sort_keys=True)
                leaf_hashes.append(keccak256(serialized_leaf.encode('utf-8')))

            # Standard binary Merkle reduction loop
            current_level = leaf_hashes
            while len(current_level) > 1:
                next_level = []
                if len(current_level) % 2 != 0:
                    current_level.append(current_level[-1])
                for i in range(0, len(current_level), 2):
                    combined = current_level[i] + current_level[i+1]
                    next_level.append(keccak256(combined.encode('utf-8')))
                current_level = next_level

            computed_root = current_level[0] if current_level else keccak256(b"EMPTY_TREE")

            # 2. Assert structural equality against the B-Tree primary key
            if computed_root == stored_root:
                print(f"    \033[1;32m[OK]\033[0m Block #{height} -> Root Match: 0x{stored_root[:16]}... verified.")
                self.verified_nodes += 1
            else:
                print(f"    \033[1;31m[CORRUPTED]\033[0m Block #{height} -> HASH MISMATCH!")
                print(f"        Expected: 0x{stored_root}")
                print(f"        Computed: 0x{computed_root}")
                self.corrupted_nodes += 1

        conn.close()

        # Final Summary Reports
        print("\n\033[1;36m================================================================\033[0m")
        if self.corrupted_nodes == 0:
            print(f"\033[1;32m[+] FSCK SUCCESS: System state is 100% stable.\033[0m")
            print(f"    Verified Blocks: {self.verified_nodes} | Compromised States: 0")
        else:
            print(f"\033[1;31m[!] FSCK ALERT: {self.corrupted_nodes} structural violations detected!\033[0m")
            print(f"    Verified Blocks: {self.verified_nodes} | Corrupted Blocks: {self.corrupted_nodes}")
        print("\033[1;36m================================================================\033[0m")

if __name__ == "__main__":
    auditor = ProvMarkFSCK()
    auditor.run_diagnostic()
