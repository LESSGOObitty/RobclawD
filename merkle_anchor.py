import hashlib

def sha3(text):
    return hashlib.sha3_256(text.encode()).digest()

assets = [
    "robertdoe.pw",
    "google.com blockchain node",
    "Termux root shell",
    "Unstoppable domains lookup",
    "Keccak Merkle tree root"
]

print("--- BUILDING TERMINAL MERKLE TREE ---")
leaves = []
for i, asset in enumerate(assets):
    h = sha3(asset)
    leaves.append(h)
    print(f"[{i+1}] {asset} -> 0x{h.hex()}")

level = leaves
step = 1
while len(level) > 1:
    next_level = []
    for i in range(0, len(level), 2):
        left = level[i]
        right = level[i+1] if i+1 < len(level) else level[i]
        combined = hashlib.sha3_256(left + right).digest()
        next_level.append(combined)
    print(f"[Level {step} Root] -> 0x{next_level[0].hex()}")
    level = next_level
    step += 1

print("\n========================================")
print(f"FINAL METAMASK ASSET ANCHOR (MERKLE ROOT):")
print(f"0x{level[0].hex()}")
print("========================================")
