import os
import hashlib
import json

def generate_merkle_dag():
    nodes = []
    print("[+] Scanning workspace for Merkle DAG nodes...")
    
    for root, dirs, files in os.walk("."):
        if ".git" in root or "storage" in root:
            continue
        for file in sorted(files):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                    nodes.append({
                        "path": file_path,
                        "sha256": file_hash
                    })
            except Exception:
                pass

    if not nodes:
        print("[!] No files found to index.")
        return

    # Extract hashes for tree reduction
    hashes = [n["sha256"] for n in nodes]
    
    # Pairwise Merkle reduction
    tree = sorted(hashes)
    while len(tree) > 1:
        if len(tree) % 2 != 0:
            tree.append(tree[-1])
        tree = [hashlib.sha256((tree[i] + tree[i+1]).encode()).hexdigest() for i in range(0, len(tree), 2)]

    dag_root = tree[0]
    
    manifest = {
        "node_count": len(nodes),
        "merkle_dag_root": dag_root,
        "nodes": nodes
    }

    with open("sovereign_lattice_proof.json", "w") as f:
        json.dump(manifest, f, indent=2)

    print("================================================================")
    print(f" [+] TOTAL NODES INDEXED : {len(nodes)}")
    print(f" [+] MERKLE DAG ROOT HASH: {dag_root}")
    print(" [+] Manifest written to : sovereign_lattice_proof.json")
    print("================================================================")

if __name__ == "__main__":
    generate_merkle_dag()
