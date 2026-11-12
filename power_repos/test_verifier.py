import hashlib
import json

def keccak256(data: bytes) -> bytes:
    return hashlib.sha3_256(data).digest()

class BTreeMerkleVerifier:
    def __init__(self, leaves):
        self.leaves = [keccak256(l) for l in leaves]
        if len(self.leaves) % 2 != 0:
            self.leaves.append(self.leaves[-1])
        self.tree = self._build(self.leaves)

    def _build(self, leaves):
        layers = [leaves]
        while len(layers[-1]) > 1:
            current = layers[-1]
            next_layer = []
            for i in range(0, len(current), 2):
                r = current[i+1] if i+1 < len(current) else current[i]
                l = current[i]
                pair = keccak256(l + r) if l < r else keccak256(r + l)
                next_layer.append(pair)
            layers.append(next_layer)
        return layers

    def root(self):
        return self.tree[-1][0]

    def proof(self, idx):
        p = []
        for layer in self.tree[:-1]:
            is_right = idx % 2 == 1
            sibling = idx - 1 if is_right else idx + 1
            p.append(layer[sibling] if sibling < len(layer) else layer[idx])
            idx //= 2
        return p

if __name__ == "__main__":
    initial_state = [b"node_alpha", b"node_beta", b"node_gamma", b"node_delta"]
    tree = BTreeMerkleVerifier(initial_state)
    
    print(f"[*] Initial B-Tree State Root: 0x{tree.root().hex()}")
    print(f"[*] Target Leaf (Index 0): 0x{tree.leaves[0].hex()}")
    print(f"[*] Merkle Proof Nodes: {[ '0x' + p.hex() for p in tree.proof(0) ]}")
