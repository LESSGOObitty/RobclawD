#!/usr/bin/env python3
import os
import sys
import secrets
import hashlib
import tarfile
from datetime import datetime

def generate_local_entropy(num_bytes=32):
    urandom_bytes = secrets.token_bytes(num_bytes)
    ns_jitter = str(os.times()).encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(urandom_bytes)
    hasher.update(ns_jitter)
    return hasher.digest()

def calculate_raw_merkle_root(target_dir="."):
    file_hashes = []
    skip_items = {'.git', '__pycache__', 'node_modules', 'pkg_raw.py', 'raw_state.pkg.tar.gz', 'MANIFEST.seal'}
    
    for root, dirs, files in os.walk(target_dir):
        # Prune ignored directories
        dirs[:] = [d for d in dirs if d not in skip_items]
        for file in files:
            if file in skip_items or file.endswith('.pkg.tar.gz'):
                continue
            
            file_path = os.path.join(root, file)
            if not os.path.isfile(file_path):
                continue
            
            hasher = hashlib.sha256()
            try:
                with open(file_path, "rb") as f:
                    while chunk := f.read(65536):
                        hasher.update(chunk)
                
                # Bind relative file path + content hash for structural DAG integrity
                rel_path = os.path.relpath(file_path, target_dir)
                path_hasher = hashlib.sha256()
                path_hasher.update(rel_path.encode('utf-8'))
                path_hasher.update(hasher.digest())
                file_hashes.append(path_hasher.hexdigest())
            except Exception:
                continue

    file_hashes.sort()
    
    root_hasher = hashlib.sha256()
    for f_hash in file_hashes:
        root_hasher.update(f_hash.encode('utf-8'))

    return root_hasher.hexdigest(), len(file_hashes)

def package_raw_state(target_dir=".", output_archive="raw_state.pkg.tar.gz"):
    print("[+] Hashing raw directory tree into direct Merkle DAG...")
    merkle_root, file_count = calculate_raw_merkle_root(target_dir)
    print(f"    -> Scanned Files   : {file_count}")
    print(f"    -> Merkle Root     : {merkle_root}")

    print("[+] Generating 32-byte local entropy anchor...")
    entropy_bytes = generate_local_entropy(32)
    entropy_hex = entropy_bytes.hex()
    print(f"    -> Entropy Anchor  : {entropy_hex}")

    manifest_path = "MANIFEST.seal"
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    seal_hasher = hashlib.sha256()
    seal_hasher.update(merkle_root.encode('utf-8'))
    seal_hasher.update(entropy_bytes)
    state_seal = seal_hasher.hexdigest()

    manifest_content = (
        f"TIMESTAMP={timestamp}\n"
        f"FILE_COUNT={file_count}\n"
        f"MERKLE_ROOT={merkle_root}\n"
        f"ENTROPY_ANCHOR={entropy_hex}\n"
        f"STATE_SEAL={state_seal}\n"
    )

    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(manifest_content)

    print("[+] Packaging raw working tree...")
    with tarfile.open(output_archive, "w:gz") as tar:
        for item in os.listdir(target_dir):
            if item in {output_archive, manifest_path}:
                continue
            tar.add(item)
        tar.add(manifest_path, arcname="MANIFEST.seal")

    if os.path.exists(manifest_path):
        os.remove(manifest_path)

    print(f"[✔] Raw state package created : {output_archive}")
    print(f"[✔] Final State Seal Hash     : {state_seal}")

if __name__ == "__main__":
    package_raw_state()
