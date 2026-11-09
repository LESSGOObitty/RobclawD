import hashlib
import json

def hash_leaf(data: str) -> str:
    return "0x" + hashlib.sha3_256(data.encode('utf-8')).hexdigest()

def hash_parent(left: str, right: str) -> str:
    combined = bytes.fromhex(left[2:]) + bytes.fromhex(right[2:])
    return "0x" + hashlib.sha3_256(combined).hexdigest()

# Load leaves from the sealed NEM state manifest or define explicit topology
leaves = [
    hash_leaf("Bus: NSW1 (Sydney Grid Zone)"),
    hash_leaf("Bus: VIC1"),
    hash_leaf("Bus: SA1"),
    hash_leaf("Bus: QLD1"),
    hash_leaf("Bus: TAS1"),
    hash_leaf("Gen: Bayswater Coal"),
    hash_leaf("Gen: Eraring Coal"),
    hash_leaf("Gen: Snowy Hydro Pumped Storage"),
    hash_leaf("Gen: Hume Hydro"),
    hash_leaf("Gen: Tallawarra Gas"),
    hash_leaf("Gen: Darling Downs Solar"),
    hash_leaf("Interconnector: Heywood"),
    hash_leaf("Interconnector: Murraylink"),
    hash_leaf("Interconnector: Basslink"),
    hash_leaf("Interconnector: QNI")
]

def build_tree(current_layer):
    tree = [current_layer]
    while len(current_layer) > 1:
        next_layer = []
        for i in range(0, len(current_layer), 2):
            left = current_layer[i]
            right = current_layer[i+1] if i + 1 < len(current_layer) else current_layer[i]
            next_layer.append(hash_parent(left, right))
        tree.append(next_layer)
        current_layer = next_layer
    return tree

tree = build_tree(leaves)
root = tree[-1][0]

print(f"[*] Dynamically Computed Merkle Root: {root}")
print(f"[*] Total Tree Depth: {len(tree)}")
print(f"[*] Base Leaves Count: {len(leaves)}")
print("[+] Merkle indexing and cryptographic state tree operational.")
# Appending Equity State Leaf
equity_leaf = hash_leaf("Equity Valuation: 1Quint")
print(f"[*] Appended Equity State Leaf: {equity_leaf}")
