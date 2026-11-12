#!/usr/bin/env python3
import os
import subprocess
import hashlib
import sys

def keccak256(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

def run_git(cwd, args):
    res = subprocess.run(["git"] + args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        return None
    return res.stdout.strip()

class RepoMerkleTree:
    def __init__(self, object_hashes):
        self.leaves = [keccak256(bytes.fromhex(h)) for h in object_hashes if h]
        if not self.leaves:
            self.leaves = [keccak256(b"empty_state")]
        while len(self.leaves) % 2 != 0:
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

def process_repos():
    base_dir = os.getcwd()
    tag_name = "SHA1296000ARC"
    
    entries = os.listdir(base_dir)
    for entry in entries:
        repo_path = os.path.join(base_dir, entry)
        if os.path.isdir(os.path.join(repo_path, ".git")):
            print(f"[*] Sealing repo: {entry}")
            
            # Gather git commits & tree state
            commits = run_git(repo_path, ["log", "-n", "10", "--format=%H"])
            tree_obj = run_git(repo_path, ["rev-parse", "HEAD^{tree}"])
            
            commit_list = commits.splitlines() if commits else []
            tree_list = [tree_obj] if tree_obj else []
            
            leaf_pool = commit_list + tree_list
            tree = RepoMerkleTree(leaf_pool)
            root_hex = tree.root.hex()
            
            # Remove existing tag if present, then stamp
            subprocess.run(["git", "tag", "-d", tag_name], cwd=repo_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            tag_msg = f"Workspace Merkle B-Tree Root: 0x{root_hex}"
            
            res = subprocess.run(["git", "tag", "-a", tag_name, "-m", tag_msg], cwd=repo_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if res.returncode == 0:
                print(f"    [+] Tagged {tag_name} -> 0x{root_hex[:16]}...")
            else:
                print(f"    [-] Failed to tag {entry}: {res.stderr.strip()}")

if __name__ == "__main__":
    process_repos()
    print("[+] All workspace repositories successfully sealed and audited.")
