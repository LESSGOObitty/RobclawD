#!/data/data/com.termux/files/usr/bin/env python3
import os
import json
import time
import hashlib

class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.merkle_hash = ""

class MerkleBTreeDAG:
    def __init__(self, t=3):
        self.root = BTreeNode()
        self.t = t  # Minimum degree

    def _hash_node(self, node):
        hasher = hashlib.sha256()
        for k in node.keys:
            hasher.update(str(k).encode("utf-8"))
        for child in node.children:
            hasher.update(child.merkle_hash.encode("utf-8"))
        return hasher.hexdigest()

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(leaf=False)
            self.root = temp
            temp.children.append(root)
            self._split_child(temp, 0)
            self._insert_non_full(temp, key)
        else:
            self._insert_non_full(root, key)
        self.update_merkle_roots(self.root)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i):
        t = self.t
        child = parent.children[i]
        z = BTreeNode(leaf=child.leaf)
        
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, child.keys[t - 1])
        
        z.keys = child.keys[t:(2 * t - 1)]
        child.keys = child.keys[0:(t - 1)]
        
        if not child.leaf:
            z.children = child.children[t:(2 * t)]
            child.children = child.children[0:t]

    def update_merkle_roots(self, node):
        if not node.leaf:
            for child in node.children:
                self.update_merkle_roots(child)
        node.merkle_hash = self._hash_node(node)

def execute_merkle_btree():
    print("=" * 74)
    print(" [MERKLE B-TREE DAG] CONSTRUCTING CRYPTOGRAPHIC INDEXING LATTICE")
    print("=" * 74)

    btree = MerkleBTreeDAG(t=3)
    
    # Ingest sovereign state identifiers & Collatz-Markov seeds into the B-Tree DAG
    states_to_index = [1337, 9551, 2026, 31415, 42, 8888, 512, 1024, 65536]
    for val in states_to_index:
        btree.insert(val)

    master_dag_root_hash = btree.root.merkle_hash
    
    lattice_data = {
        "system": "RobDoeAI-Core // Merkle B-Tree DAG Index",
        "operator": "root@robdoe.com",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "indexed_keys": states_to_index,
        "master_dag_merkle_root": master_dag_root_hash,
        "status": "MERKLE_BTREE_DAG_LOCKED"
    }

    output_path = "merkle_btree_state.json"
    with open(output_path, "w") as f:
        json.dump(lattice_data, f, indent=2)

    print(f" [+] Indexed Keys       : {states_to_index}")
    print(f" [+] Master DAG Root    : {master_dag_root_hash}")
    print(f" [+] State Exported To  : {output_path}")
    print("=" * 74)

if __name__ == "__main__":
    execute_merkle_btree()
