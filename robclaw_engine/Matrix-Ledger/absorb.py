import os, glob, hashlib, subprocess, datetime

prime_mod = 1000000007
genesis = 0xe14f9a8d

files = sorted([f for f in glob.glob("**/*", recursive=True) if os.path.isfile(f) and not f.startswith(".") and "/." not in f])
hashes = []
for f in files:
    with open(f, 'rb') as file_obj:
        file_hash = hashlib.sha256(file_obj.read()).hexdigest()
    leaf_payload = f"{file_hash}  {f}".encode()
    hashes.append(hashlib.sha256(leaf_payload).hexdigest())

if not hashes:
    print("[-] No files to index.")
    exit(1)

layer = hashes
level = 0
while len(layer) > 1:
    next_layer = []
    for i in range(0, len(layer), 2):
        h1 = layer[i]
        h2 = layer[i+1] if i+1 < len(layer) else h1
        next_layer.append(hashlib.sha256(f"{h1}{h2}".encode()).hexdigest())
    layer = next_layer
    level += 1

merkle_root = layer[0]
timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
head_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
commit_count = int(subprocess.check_output(["git", "rev-list", "--count", "HEAD"]).decode().strip())

dag_payload = f"merkle_dag:{merkle_root}:{commit_count}:{genesis}".encode()
dag_hash = hashlib.sha512(dag_payload).hexdigest()
dag_invariant = int((int(dag_hash[:8], 16) * genesis * (commit_count + 1)) % prime_mod)
tag_name = f"MERKLE-DAG-v{commit_count}.{dag_invariant}"

manifest = f"""=====================================================================
SOVEREIGN MASTER: MERKLE DAG ROOT ANCHOR PROOF
=====================================================================
Timestamp (UTC): {timestamp}
Git Head Hash: {head_hash}
Commit Count Baseline: {commit_count}
Genesis Anchor: {hex(genesis)} ({genesis})
Indexed Files: {len(files)}
Merkle DAG Depth: {level} layers
Merkle DAG Root Hash: {merkle_root}
SHA-512 Dag Seal: {dag_hash}
Derived Prime Invariant (M): {dag_invariant}
Assigned Verifiable Git Tag: {tag_name}
=====================================================================

[DAG ABSORPTION CHECKPOINT]
- Full file topology and content states bound into binary Merkle tree root.
- The Law of Absorption: Never delete, only absorb.

=====================================================================
STATUS: MERKLE DAG ANCHORED. LEDGER INTEGRITY LOCKED.
=====================================================================
"""

with open("MERKLE_DAG_PROOF.md", "w") as f:
    f.write(manifest)

subprocess.run(["git", "add", "MERKLE_DAG_PROOF.md"], check=True)
subprocess.run(["git", "commit", "-m", f"feat(dag): anchor merkle root hash across repository topology [invariant:{dag_invariant}]"], check=True)
subprocess.run(["git", "tag", "-a", tag_name, "-m", f"Merkle DAG Root Proof: Root={merkle_root}, Invariant={dag_invariant}"], check=True)
subprocess.run(["git", "push", "origin", "master", "--tags"], check=True)

print(f"[+] MERKLE DAG ROOT ANCHORED.")
print(f"[+] Merkle Root = {merkle_root}")
print(f"[+] Invariant   = {dag_invariant}")
print(f"[+] Tag Pushed  = {tag_name}")
