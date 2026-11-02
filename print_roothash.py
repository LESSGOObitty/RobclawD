import json
import os
import hashlib
import glob

def compute_dir_merkle_root(path="."):
    hashes = []
    for root, _, files in os.walk(path):
        if ".git" in root:
            continue
        for file in sorted(files):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    hashes.append(hashlib.sha256(f.read()).hexdigest())
            except Exception:
                pass
    
    if not hashes:
        return None
    
    # Pairwise Merkle reduction
    tree = sorted(hashes)
    while len(tree) > 1:
        if len(tree) % 2 != 0:
            tree.append(tree[-1])
        tree = [hashlib.sha256((tree[i] + tree[i+1]).encode()).hexdigest() for i in range(0, len(tree), 2)]
    
    return tree[0]

print("================================================================")
print("             SOVEREIGN TERMUX MERKLE ROOT HARVEST              ")
print("================================================================")

# 1. Read from sovereign lattice JSON if present
lattice_file = "sovereign_lattice_proof.json"
if os.path.exists(lattice_file):
    try:
        with open(lattice_file, "r") as f:
            data = json.load(f)
            root = data.get("merkle_root") or data.get("Merkle Root Hash")
            if root:
                print(f"[+] LATTICE PROOF ROOT : {root}")
    except Exception:
        pass

# 2. Check Git HEAD Hash
git_head = os.popen("git rev-parse HEAD 2>/dev/null").read().strip()
if git_head:
    print(f"[+] GIT HEAD COMMIT   : {git_head}")

# 3. Compute Live Directory Merkle Tree Root
live_root = compute_dir_merkle_root(".")
print(f"[+] LIVE DIRECTORY ROOT: {live_root}")
print("================================================================")
