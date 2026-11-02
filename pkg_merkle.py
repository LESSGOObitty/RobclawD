#!/usr/bin/env python3
import os, sys, secrets, hashlib, tarfile
from datetime import datetime

def generate_local_entropy(num_bytes=32):
    urandom_bytes = secrets.token_bytes(num_bytes)
    ns_jitter = str(os.times()).encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(urandom_bytes)
    hasher.update(ns_jitter)
    return hasher.digest()

def calculate_git_merkle_root(git_dir):
    objects_dir = os.path.join(git_dir, "objects")
    if not os.path.exists(objects_dir):
        raise FileNotFoundError(f"Git objects directory not found: {objects_dir}")
    object_hashes = []
    for root, _, files in os.walk(objects_dir):
        for file in files:
            file_path = os.path.join(root, file)
            hasher = hashlib.sha256()
            try:
                with open(file_path, "rb") as f:
                    while chunk := f.read(65536):
                        hasher.update(chunk)
                object_hashes.append(hasher.hexdigest())
            except Exception:
                continue
    object_hashes.sort()
    root_hasher = hashlib.sha256()
    for obj_hash in object_hashes:
        root_hasher.update(obj_hash.encode('utf-8'))
    return root_hasher.hexdigest(), len(object_hashes)

def package_bundle(repo_dir=".", output_archive="merkle_state.pkg.tar.gz"):
    git_dir = os.path.join(repo_dir, ".git")
    if not os.path.exists(git_dir):
        print("[-] Error: No local .git repository found.")
        sys.exit(1)

    print("[+] Calculating Merkle root hash across local .git objects...")
    merkle_root, obj_count = calculate_git_merkle_root(git_dir)
    print(f"    -> Scanned Objects : {obj_count}")
    print(f"    -> Merkle Root     : {merkle_root}")

    print("[+] Generating 32-byte local entropy anchor...")
    entropy_bytes = generate_local_entropy(32)
    entropy_hex = entropy_bytes.hex()
    print(f"    -> Entropy Anchor : {entropy_hex}")

    manifest_path = "MANIFEST.seal"
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    seal_hasher = hashlib.sha256()
    seal_hasher.update(merkle_root.encode('utf-8'))
    seal_hasher.update(entropy_bytes)
    state_seal = seal_hasher.hexdigest()

    manifest_content = (
        f"TIMESTAMP={timestamp}\n"
        f"OBJECT_COUNT={obj_count}\n"
        f"MERKLE_ROOT={merkle_root}\n"
        f"ENTROPY_ANCHOR={entropy_hex}\n"
        f"STATE_SEAL={state_seal}\n"
    )

    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(manifest_content)

    print("[+] Creating compressed local package tarball...")
    with tarfile.open(output_archive, "w:gz") as tar:
        tar.add(git_dir, arcname=".git")
        tar.add(manifest_path, arcname="MANIFEST.seal")

    if os.path.exists(manifest_path):
        os.remove(manifest_path)

    print(f"[✔] Package created successfully: {output_archive}")
    print(f"[✔] Final State Seal Hash    : {state_seal}")

if __name__ == "__main__":
    package_bundle()
