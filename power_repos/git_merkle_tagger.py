#!/usr/bin/env python3
import hashlib
import subprocess
import sys

def run_git(args):
    res = subprocess.run(["git"] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"[-] Git error: {res.stderr.strip()}")
        sys.exit(1)
    return res.stdout.strip()

def keccak256(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

class GitMerkleBTree:
    def __init__(self, object_hashes: list[str]):
        self.leaves = [keccak256(bytes.fromhex(h)) for h in object_hashes]
        if not self.leaves:
            print("[-] No git objects found to hash.")
            sys.exit(1)
        if len(self.leaves) % 2 != 0:
            self.leaves.append(self.leaves[-1])
        self.root = self._build(self.leaves)

    def _build(self, current_layer):
        while len(current_layer) > 1:
            next_layer = []
            for i in range(0, len(current_layer), 2):
                l = current_layer[i]
                r = current_layer[i+1] if i+1 < len(current_layer) else current_layer[i]
                pair = keccak256(l + r) if l < r else keccak256(r + l)
                next_layer.append(pair)
            current_layer = next_layer
        return current_layer[0]

if __name__ == "__main__":
    # 1. Fetch current local git tree object hashes
    raw_objects = run_git(["rev-parse", "HEAD^{tree}"]).splitlines()
    # Alternatively gather recent commit SHAs as state leaves
    commit_history = run_git(["log", "-n", "8", "--format=%H"]).splitlines()

    # Combine tree state + recent commits into deterministic Merkle leaf pool
    leaf_pool = commit_history + raw_objects
    
    # 2. Compute Merkle B-Tree Root
    tree = GitMerkleBTree(leaf_pool)
    root_hex = tree.root.hex()
    
    print(f"[*] Workspace Merkle Root: 0x{root_hex}")

    # 3. Apply Tag: SHA1296000ARC
    tag_name = "SHA1296000ARC"
    tag_message = f"Merkle B-Tree State Root: 0x{root_hex}"
    
    # Check if tag exists and delete local/remote ref if needed to overwrite cleanly
    subprocess.run(["git", "tag", "-d", tag_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    run_git(["tag", "-a", tag_name, "-m", tag_message])
    print(f"[+] Successfully sealed and stamped local git tag: {tag_name}")
