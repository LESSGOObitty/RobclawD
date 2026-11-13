import os
import csv
import hashlib
import subprocess
from datetime import datetime

HOME_DIR = os.path.expanduser("~")
TARGET_DIR = os.path.expanduser("~/workspace")
OUTPUT_DIR = os.path.expanduser("~/workspace/manifests")
os.makedirs(OUTPUT_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
manifest_filename = f"termux_manifest_{timestamp}.csv"
manifest_path = os.path.join(OUTPUT_DIR, manifest_filename)

def sha256_file(filepath):
    h = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest().upper()
    except Exception:
        return "LOCKED/INACCESSIBLE"

count = 0
leaf_hashes = []

with open(manifest_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["LastWriteTime", "Length", "FullName", "SHA256"])

    for root, dirs, files in os.walk(TARGET_DIR):
        dirs[:] = [d for d in dirs if d not in (".git", "manifests", "logs")]
        for name in sorted(files):
            full_path = os.path.join(root, name)
            stat = os.stat(full_path)
            mtime = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            digest = sha256_file(full_path)
            writer.writerow([mtime, stat.st_size, full_path, digest])
            if len(digest) == 64:
                leaf_hashes.append(digest)
            count += 1

root_hash = hashlib.sha256("".join(sorted(leaf_hashes)).encode("utf-8")).hexdigest().upper()
print(f"[+] SCAN COMPLETE: {count} files cataloged.")
print(f"[+] ROOT DIGEST  : {root_hash}")
print(f"[+] MANIFEST     : {manifest_path}")

# --- Automated Git Sync ---
try:
    print("[*] Staging and pushing manifest to GitHub...")
    rel_path = os.path.relpath(manifest_path, HOME_DIR)
    
    # Stage the exact manifest file
    subprocess.run(["git", "-C", HOME_DIR, "add", rel_path], check=True)
    
    # Check if changes are actually staged
    staged_check = subprocess.run(["git", "-C", HOME_DIR, "diff", "--cached", "--quiet"])
    if staged_check.returncode != 0:
        commit_msg = f"chore(manifest): auto-seal Merkle root {root_hash[:12]}"
        subprocess.run(["git", "-C", HOME_DIR, "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "-C", HOME_DIR, "push", "origin", "main"], check=True)
        print("[+] Git sync complete: Manifest pushed to origin/main.")
    else:
        print("[!] Manifest file was already staged or ignored; no new commit needed.")
except subprocess.CalledProcessError as e:
    print(f"[!] Git auto-sync warning/error: {e}")
except Exception as ex:
    print(f"[!] Unexpected error during git sync: {ex}")
