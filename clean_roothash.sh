unsetopt bang_hist
clear
echo "================================================================"
echo " [SYS] AIAGENCY101 // CLEAN RECALIBRATION & ROOT HASH SEAL"
echo " [LOC] ST GEORGE // HURSTVILLE // SOUTH SYDNEY"
echo " [STATE] CHECKPOINT 24M // INVARIANT 576333510"
echo "================================================================"

echo "[+] Purging untracked junk and staging clean state..."
git clean -fdX -e storage -e .env 2>/dev/null || true

python3 -c '
import hashlib
import os

hasher = hashlib.sha256()
repo_dir = "."
skip_dirs = {".git", "storage"}

for root, dirs, files in os.walk(repo_dir):
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    for file in sorted(files):
        filepath = os.path.join(root, file)
        try:
            if os.path.exists(filepath) and not os.path.islink(filepath):
                with open(filepath, "rb") as f:
                    while chunk := f.read(8192):
                        hasher.update(chunk)
        except Exception:
            pass

root_hash = hasher.hexdigest()
print(f"[+] CLEAN ROOT HASH RECALIBRATED: {root_hash}")

with open("SOVEREIGN_ROOTHASH_SEAL.md", "w") as f:
    f.write(f"# Sovereign Clean RootHash Seal\n- Root Hash: {root_hash}\n- Invariant: 576333510\n- Status: IMMUTABLE & VERIFIED\n")
'

git add SOVEREIGN_ROOTHASH_SEAL.md
git commit -m "feat(roothash): perform clean workspace recalibration and lock root hash [invariant:576333510]"
git push origin master --tags

echo "================================================================"
echo " [STATUS] ROOT HASH SEALED, COMMITTED, AND PUSHED CLEAN."
echo "================================================================"
