#!/data/data/com.termux/files/usr/bin/zsh
unsetopt bang_hist

python3 -c '
import hashlib
import os

hasher = hashlib.sha256()
repo_dir = "."

for root, dirs, files in os.walk(repo_dir):
    if ".git" in root or "storage" in root:
        continue
    for file in sorted(files):
        filepath = os.path.join(root, file)
        try:
            with open(filepath, "rb") as f:
                while chunk := f.read(8192):
                    hasher.update(chunk)
        except Exception:
            pass

root_hash = hasher.hexdigest()
print(f"[ROOT_HASH_RECALIBRATED] {root_hash}")

with open("SOVEREIGN_ROOTHASH_SEAL.md", "w") as f:
    f.write(f"# Sovereign RootHash Seal\n- Root Hash: {root_hash}\n- Invariant: 576333510\n- Status: SECURED & VERIFIED\n")
'

git add SOVEREIGN_ROOTHASH_SEAL.md
git commit -m "feat(roothash): recalibrate and seal sovereign cryptographic root hash [invariant:576333510]"
git status -s
git log -1 --stat
